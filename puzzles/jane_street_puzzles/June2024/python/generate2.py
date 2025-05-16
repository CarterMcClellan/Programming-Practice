# We want to try and generate a 5x5 board which will score well
# guessing that will mean trying to put popular 2 letter combinations
# adjacent to each other

from functools import cache
from typing import List, Tuple

from utils import calc_nbits_from_codec, convert_board_to_string, convert_int_to_string, convert_string_to_board, convert_string_to_int, gen_random_board, get_king_moves, get_king_moves_1d, get_king_moves_bitmask, get_value_at, print_board
from data import state_population
from tqdm import tqdm

NULL_CHAR = "#"
encoding_alphabet = f"abcdefghijklmnopqrstuvwxyz{NULL_CHAR}"
MAX_VAL = len(encoding_alphabet) - 1
CHAR_ENCODING = {
    val: idx for idx, val in enumerate(encoding_alphabet)
}
REVERSE_CHAR_ENCODING = {
    idx: val for idx, val in enumerate(encoding_alphabet)
}

# other small optimizations
# - ref word, dont copy in recursive calls
# - compute len word at the beginning
# def generate_arrangement(starting_board: List[List[str]], word: str):
#     R = len(starting_board)
#     C = len(starting_board[0])
#     N = R * C
#     arrangements = []

#     precomputed_king_moves = {}
#     position_bit_masks = {}
#     n_bits_per_position = calc_nbits_from_codec(len(CHAR_ENCODING))

#     for position in range(R * C):
#         king_moves = get_king_moves_1d(position, R, C)
#         king_moves_bit_mask = get_king_moves_bitmask(position, R, C, n_bits_per_position)
#         precomputed_king_moves[position] = king_moves
#         position_bit_masks[position] = king_moves_bit_mask 

#     def generate_arrangement_helper(current_board: int, word: str, position: int, index: int):
#         if index == len(word):
#             arrangements.append(int)
#             return

#         if not (0 <= position < N):
#             return

#         mask = position_bit_masks[position]
#         bit_offset = position * n_bits_per_position
#         original_char = 
#         if original_char != NULL_CHAR and original_char != word[index]:
#             return

#         current_board[position] = word[index]

#         next_index = index + 1

#         for new_position in precomputed_king_moves[position]:
#             generate_arrangement_helper(current_board, word, new_position, next_index)

#         # Backtrack 
#         current_board[position] = original_char

#     starting_board_1d = convert_board_to_string(starting_board)
#     for position in tqdm(range(R * C), desc="Generating arrangements"):
#         generate_arrangement_helper(starting_board_1d, word, position, 0)

#     return arrangements

if __name__ == "__main__":
    R = 5
    C = 5
    null_board = [[NULL_CHAR for _ in range(R)] for _ in range(C)]

    # Verifying that the basic encoding/decoding functions work
    # null_board = gen_random_board(R, C)
    null_board = [['a' for _ in range(R)] for _ in range(C)]

    as_string = convert_board_to_string(null_board)
    as_string[5] = 'b'
    as_int = convert_string_to_int(as_string, CHAR_ENCODING)
    int_val = get_value_at(as_int, 5, 5)
    string_val = REVERSE_CHAR_ENCODING[int_val]
    print("Value at position 5", int_val, string_val)

    # back_to_string = convert_int_to_string(as_int, REVERSE_CHAR_ENCODING, R * C)
    # as_board = convert_string_to_board(back_to_string, R, C)

    # Verifying that the bit manipulations work