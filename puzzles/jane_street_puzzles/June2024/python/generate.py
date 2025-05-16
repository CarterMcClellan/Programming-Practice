# We want to try and generate a 5x5 board which will score well
# guessing that will mean trying to put popular 2 letter combinations
# adjacent to each other
from typing import List 

from utils import convert_board_to_string, convert_string_to_board, get_king_moves, get_king_moves_1d, print_board
from data import state_population
from tqdm import tqdm

NULL_CHAR = "#"

def can_arrange(words: List[str], R: int, C: int) -> bool:
    return False

def generate_arrangement(starting_board: List[List[str]], word: str):
    """
    rough first draft idea is to arrange the first word in K different ways
    then to iterate through K, and for each arrangement, try to place the next word
    without removing any of the previous word's letters
    
    if we can't place the next word, then elinimate that arrangement from the set
    of possible arrangements
    """
    R = len(starting_board)
    C = len(starting_board[0])
    N = R * C
    arrangements = []
    precomputed_king_moves = {}

    for position in range(N):
        precomputed_king_moves[position] = get_king_moves_1d(position, R, C)

    def generate_arrangement_helper(current_board: List[str], word: str, position: int, index: int):
        """
        we are sorta limited by python here by the representation for the current board,
        each "current board" which we pass into the recursive substack needs to be added to a
        list of arrangements.

        random thought, but is there a way in which we can represent the current board
        as an integer, and then use bitwise operations to update the board, then we
        could store the arrangements as a list of integers which would be must faster
        and the update operation would be faster (O(1) but the bit mask is probably faster
        than indexing into an array)
        """
        if index == len(word):
            arrangements.append([s for s in current_board])
            return

        if not (0 <= position < N):
            return

        original_char = current_board[position]
        if original_char != NULL_CHAR and original_char != word[index]:
            return

        current_board[position] = word[index]

        next_index = index + 1

        for new_position in precomputed_king_moves[position]:
            generate_arrangement_helper(current_board, word, new_position, next_index)

        # Backtrack 
        current_board[position] = original_char

    starting_board_1d = convert_board_to_string(starting_board)
    for position in tqdm(range(R * C), desc="Generating arrangements"):
        generate_arrangement_helper(starting_board_1d, word, position, 0)

    return arrangements

if __name__ == "__main__":
    R = 5
    C = 5
    null_board = [[NULL_CHAR for _ in range(R)] for _ in range(C)]

    states = list(state_population.keys())
    state = states[0]

    print("Generating arrangements for", state)
    arrangements = generate_arrangement(null_board, state)
    print("Found", len(arrangements), "arrangements")
    dedupe = set()
    for val in arrangements:
        dedupe.add(tuple(val))
    print("Deduped to", len(dedupe), "arrangements")

    if len(dedupe) > 0:
        print_board(convert_string_to_board(list(dedupe)[0], R, C), R, C)