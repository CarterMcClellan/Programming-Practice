use crate::{Board, BIT_MASK, C, N, NULL_BIT, NULL_CHAR, N_BITS, R};

pub fn convert_board_to_1d(board: Board) -> Vec<char> {
    let mut board_1d: Vec<char> = vec![NULL_CHAR; N as usize];
    for i in 0..R {
        for j in 0..C {
            let position = i * C + j;
            board_1d[position as usize] = board[i as usize][j as usize];
        }
    }

    board_1d
}

pub fn convert_1d_to_board(one_d_board: Vec<char>) -> Board {
    let mut board: Board = vec![vec![NULL_CHAR; C as usize]; R as usize];
    for i in 0..R {
        for j in 0..C {
            let position = i * C + j;
            board[i as usize][j as usize] = one_d_board[position as usize];
        }
    }
    board
}

pub fn convert_bits_to_1d(bits: u128) -> Vec<char> {
    let mut board_1d: Vec<char> = vec![NULL_CHAR; N as usize];
    for i in 0..N {
        let position = i;
        let c = (bits >> (N_BITS * position)) & BIT_MASK;
        board_1d[position as usize] = conver_bit_to_char(c);
    }

    board_1d
}

pub fn convert_1d_to_bits(one_d_board: Vec<char>) -> u128 {
    let mut board: u128 = 0;
    for i in 0..N {
        let position = i;
        let c = one_d_board[position as usize];
        let bit = convert_char_to_bit(c);
        board |= bit << (N_BITS * position);
    }
    board
}

pub fn print_board(board: Board) {
    for _ in 0..C {
        print!("--");
    }
    println!();
    for i in 0..R {
        print!("|");
        for j in 0..C {
            print!("{}|", board[i as usize][j as usize]);
        }
        println!();
        for _ in 0..C {
            print!("--");
        }
        println!();
    }
}

fn convert_char_to_bit(c: char) -> u128 {
    match c {
        'a' => 0,
        'b' => 1,
        'c' => 2,
        'd' => 3,
        'e' => 4,
        'f' => 5,
        'g' => 6,
        'h' => 7,
        'i' => 8,
        'j' => 9,
        'k' => 10,
        'l' => 11,
        'm' => 12,
        'n' => 13,
        'o' => 14,
        'p' => 15,
        'q' => 16,
        'r' => 17,
        's' => 18,
        't' => 19,
        'u' => 20,
        'v' => 21,
        'w' => 22,
        'x' => 23,
        'y' => 24,
        'z' => 25,
        _ => NULL_BIT,
    }
}

fn conver_bit_to_char(b: u128) -> char {
    match b {
        0 => 'a',
        1 => 'b',
        2 => 'c',
        3 => 'd',
        4 => 'e',
        5 => 'f',
        6 => 'g',
        7 => 'h',
        8 => 'i',
        9 => 'j',
        10 => 'k',
        11 => 'l',
        12 => 'm',
        13 => 'n',
        14 => 'o',
        15 => 'p',
        16 => 'q',
        17 => 'r',
        18 => 's',
        19 => 't',
        20 => 'u',
        21 => 'v',
        22 => 'w',
        23 => 'x',
        24 => 'y',
        25 => 'z',
        _ => NULL_CHAR,
    }
}

pub fn convert_word_to_bits(word: &str) -> Vec<u128> {
    let mut word_bits = Vec::new();
    for c in word.chars() {
        word_bits.push(convert_char_to_bit(c));
    }
    word_bits
}
