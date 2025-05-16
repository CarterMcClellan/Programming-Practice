use std::collections::BinaryHeap;
use std::collections::HashMap;
use std::collections::HashSet;
use std::time::Duration;

use itertools::Itertools;

use lazy_static::lazy_static;

mod utils;

use utils::{
    convert_1d_to_bits, convert_1d_to_board, convert_bits_to_1d, convert_board_to_1d,
    convert_word_to_bits, print_board,
};

static NULL_CHAR: char = '#';
const NULL_BIT: u128 = 26;
const R: u128 = 5;
const C: u128 = 5;
const N: u128 = R * C;
const N_BITS: u128 = 5;
const BIT_MASK: u128 = (1 << N_BITS) - 1;

lazy_static! {
    static ref PRECOMPUTED_KING_MOVES: HashMap<u128, Vec<u128>> = {
        let mut map = HashMap::new();
        for position in 0..N {
            let king_moves = get_king_moves_1d(position, R, C);
            map.insert(position, king_moves);
        }
        map
    };
}

type Board = Vec<Vec<char>>;

fn get_king_moves_1d(position: u128, r: u128, c: u128) -> Vec<u128> {
    let mut moves = Vec::new();
    let row = position / c;
    let col = position % c;

    for i in (row as isize - 1)..=(row as isize + 1) {
        for j in (col as isize - 1)..=(col as isize + 1) {
            if i >= 0 && i < r as isize && j >= 0 && j < c as isize {
                let new_pos = (i as u128) * c + (j as u128);
                if new_pos != position {
                    moves.push(new_pos);
                }
            }
        }
    }
    moves
}

fn generate_arrangement(bit_board: u128, word_as_bits: &Vec<u128>) -> HashSet<u128> {
    fn generate_arrangement_helper(
        current_board: &mut u128,
        word: &Vec<u128>,
        position: u128,
        index: usize,
        arrangements: &mut HashSet<u128>,
        mulligan: bool,
    ) {
        // current_board: the current board state
        // word: the word we are trying to fit
        // position: the position we are trying to fit the word into 
        // index: the current character of the word we are trying to fit
        // arrangements: the set of arrangements we are trying to build
        if index == word.len() {
            arrangements.insert(*current_board);
            return;
        }

        if position >= N {
            return;
        }

        // To get the original value we simply shift the board to the correct position
        // then we apply a mask
        let original_char = (*current_board >> (N_BITS * position)) & BIT_MASK;
        let requires_mulligan = original_char != NULL_BIT && original_char != word[index] ;

        if requires_mulligan && !mulligan{
            return;
        }

        // if a mulligan is required (meaning we need to replace a non-null character)
        // then we can skip the current position, and set mulligan to false, and move in
        // any of the valid directions
        else if requires_mulligan && mulligan {
            for new_position in &PRECOMPUTED_KING_MOVES[&position] {
                generate_arrangement_helper(
                    current_board,
                    word,
                    *new_position,
                    index + 1,
                    arrangements,
                    false
                );
            }
        }

        else {
            // To mutate the board at a given position, we want to clear the bits at the position
            // then we shift the new value to the correct position and apply an OR operation
            let offset = N_BITS * position;
            let zero_mask = !(BIT_MASK << (offset)); // compute the mask to clear the bits at the position
            *current_board &= zero_mask; // clear the bits at the position
            *current_board |= word[index] << (offset); // set the new value at the position

            for new_position in &PRECOMPUTED_KING_MOVES[&position] {
                generate_arrangement_helper(
                    current_board,
                    word,
                    *new_position,
                    index + 1,
                    arrangements,
                    mulligan
                );
            }

            // Backtrack (by inplace updating what we had done before)
            *current_board &= zero_mask;
            *current_board |= original_char << (offset);
        }

    }

    let mut bit_board = bit_board;
    let mut arrangements = HashSet::new();
    for position in 0..N {
        generate_arrangement_helper(
            &mut bit_board,
            &word_as_bits,
            position,
            0,
            &mut arrangements,
            true
        );
    }

    arrangements
}

fn fitness_heuristic(bit_board: u128) -> i32 {
    // basic idea: there are way too many arrangements for us to consider all
    // so we want a fitness heuristic which helps us select the subset which 
    // might be considered "good"

    // we can start with the most basic heuristic which is counting the number of
    // NULL_CHARs, more being better
    let mut null_count = 0;
    for i in 0..N {
        let position = i;
        let c = (bit_board >> (N_BITS * position)) & BIT_MASK;

        if c == NULL_BIT {
            null_count += 1;
        }
    }

    null_count
}

struct Arrangement {
    board: u128,
    fitness: i32,
}

impl PartialEq for Arrangement {
    fn eq(&self, other: &Self) -> bool {
        self.fitness == other.fitness
    }
}

impl Eq for Arrangement {}

impl PartialOrd for Arrangement {
    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        Some(self.cmp(other))
    }
}

impl Ord for Arrangement {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        self.fitness.cmp(&other.fitness)
    }
}

fn top_k_arrangements(arrangements: HashSet<u128>, k: usize) -> HashSet<u128> {
    let mut heap = BinaryHeap::with_capacity(k);
    for arrangement in arrangements.iter() {
        let fitness = fitness_heuristic(*arrangement);
        heap.push(Arrangement {
            board: *arrangement,
            fitness,
        });
    }

    let mut top_k = HashSet::new();
    for _ in 0..k {
        if let Some(arrangement) = heap.pop() {
            top_k.insert(arrangement.board);
        }
    }

    top_k
}

fn update_set_with_state(state: &str, viable_set: &mut HashSet<u128>) -> HashSet<u128> {
    println!("{}", "-".repeat(50));
    println!("Processing state: {}", state);
    let start_time = std::time::Instant::now();
    let mut new_set = HashSet::new();
    let word_as_bits = convert_word_to_bits(state);

    let mut total_time = Duration::new(0, 0);
    let n_ele = viable_set.len();
    for (idx, arrangement ) in viable_set.iter().enumerate() {
        let start_time = std::time::Instant::now();
        let new_arrangements = generate_arrangement(*arrangement, &word_as_bits);
        let last_loop = start_time.elapsed();
        total_time += last_loop;
        if idx % 1 == 0 && idx > 0 {
            let avg_time = total_time / idx as u32;
            // if last_loop > avg_time * 10 {
            //     println!("Time taken: {:?}", last_loop);
            // }

            println!("Prog: {}/{} | [last loop: {:?} | [avg time: {:?}] | [total time {:?}]", idx, n_ele, start_time.elapsed(), avg_time, total_time);
        }


        new_set.extend(new_arrangements);
    }

    println!("Found {} arrangements [before fitness]", new_set.len());
    let resp = top_k_arrangements(new_set, 100);
    println!("Found {} arrangements [after fitness]", resp.len());
    let end_time = start_time.elapsed();
    println!("Time taken: {:?}", end_time);
    println!("{}", "-".repeat(50));
    // new_set
    resp
}

// There are roughly 3 sets
//
// 1. The "complete" set: where all the tiles are taken
// 2. The "viable" set: where some tiles are taken
// 3. the "incomplete" set: where some tiles are taken, but we will not be able
// to make any more state names with the tiles remaining
//
// for the time being lets consider 2+3 one set
fn premute_and_try(states: Vec<&str>) {
    let null_board: Board = vec![vec![NULL_CHAR; C as usize]; R as usize];
    let one_d_board = convert_board_to_1d(null_board.clone());
    let bit_board = convert_1d_to_bits(one_d_board.clone());

    let mut best_idx = 0;
    let mut best_soln: u128 = 0;

    for state_perm in states.iter().permutations(states.len()).unique() {
        let mut curr_set = HashSet::new();
        curr_set.insert(bit_board);
        for (idx, state ) in state_perm.iter().enumerate() {
            curr_set = update_set_with_state(state, &mut curr_set);

            if curr_set.len() > 0 && idx > best_idx {
                best_idx = idx;
                best_soln = curr_set.iter().next().unwrap().clone();
            }

            if curr_set.len() == 0 {
                break;
            }
        }

        if curr_set.len() > 0 {
            println!("Found a solution");
            let sample = curr_set.iter().next().unwrap();
            let one_d = convert_bits_to_1d(*sample);
            let sample_board = convert_1d_to_board(one_d.clone());
            println!("{}", "-".repeat(50));
            print_board(sample_board);
            println!("Board Str: {}", one_d.iter().collect::<String>());
            println!("{}", "-".repeat(50));
            return
        } else {
            println!("No solution found. Best Solution");
            let sample = best_soln;
            let one_d = convert_bits_to_1d(sample);
            let sample_board = convert_1d_to_board(one_d.clone());
            println!("{}", "-".repeat(50));
            print_board(sample_board);
            println!("Board Str: {}", one_d.iter().collect::<String>());
            println!("{}", "-".repeat(50));
        }
    }

}

fn main() {
    // let states = vec!["california", "texas", "florida"];
    // let states = vec!["illinois", "ohio", "utah", "iowa", "idaho"];
    // let states = vec!["ohio", "utah", "iowa", "idaho", "illinois"];
    let states = vec![
        "california", "texas", "florida", "newyork",  "pennsylvania", "illinois",
        "northcarolina", "ohio", "georgia", "utah", "iowa", "idaho",  "arizona", "michigan" 
    ];
    premute_and_try(states);

    // println!("Printing a sample arrangement");
    // let sample = curr_set.iter().next().unwrap();
    // let sample_board = convert_1d_to_board(convert_bits_to_1d(*sample));
    // print_board(sample_board);
    // println!("{}", "-".repeat(50));
}

#[cfg(test)]
fn test() {
    let null_board: Board = vec![vec![NULL_CHAR; C as usize]; R as usize];
    let one_d_board = convert_board_to_1d(null_board.clone());
    let bit_board = convert_1d_to_bits(one_d_board.clone());
    let tmp_one_d = convert_bits_to_1d(bit_board.clone());
    let tmp_board = convert_1d_to_board(tmp_one_d.clone());

    println!("1d board");
    println!("{:?}", one_d_board);

    println!("Bits board");
    println!("{:?}", bit_board);

    println!("Reconstructed 1d board");
    println!("{:?}", tmp_one_d);

    println!("Original board");
    print_board(null_board);
    println!("Reconstructed board");
    print_board(tmp_board);
}
