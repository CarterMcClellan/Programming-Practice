import math
from typing import Dict, List
import random

def get_king_moves(x: int, y: int, R: int, C: int) -> list[tuple[int, int]]:
    x_moves = []
    if x == 0:
        x_moves.append(x+1)
    elif x == C-1:
        x_moves.append(x-1)
    else:
        x_moves.append(x+1)
        x_moves.append(x-1)

    x_moves.append(x)

    y_moves = []
    if y == 0:
        y_moves.append(y+1)
    elif y == R-1:
        y_moves.append(y-1)
    else:
        y_moves.append(y+1)
        y_moves.append(y-1)

    y_moves.append(y)

    king_moves = []
    for n_x in x_moves:
        for n_y in y_moves:
            if n_x == x and n_y == y:
                continue
            king_moves.append((n_x, n_y))

    return king_moves

def get_king_moves_1d(position: int, R: int, C: int) -> List[int]:
    x = position // R
    y = position % R

    king_moves = get_king_moves(x, y, R, C)
    return [x*R + y for (x, y) in king_moves]

def get_king_moves_bitmask(position: int, R: int, C: int, n_bits: int) -> List[int]:
    """
    Generate bitmasks for possible king moves from a given position on a RxC board
    where each board position's state is represented by `n_bits` in a single integer.
    
    Args:
    - position (int): Current position index based on a flat list representation.
    - R (int): Number of rows in the board.
    - C (int): Number of columns.
    - n_bits (int): Number of bits used to represent each position on the board.

    Returns:
    - List[int]: List of bit masks representing each valid king move.
    """
    # Function to calculate a bitmask for setting or clearing bits at a given position
    def bitmask_for_position(pos: int) -> int:
        return (1 << (n_bits * pos)) - 1

    # Get potential king moves using a utility function that accounts for board edges
    king_moves = get_king_moves_1d(position, R, C)

    # Calculate bitmasks for each valid move
    king_moves_bit_mask = []
    for km in king_moves:
        # Bit mask for the specific position km
        mask = bitmask_for_position(km)
        king_moves_bit_mask.append(mask)

    return king_moves_bit_mask

def convert_board_to_string(board: List[List[str]]) -> List[str]:
    return list("".join(["".join(row) for row in board]))

def convert_string_to_board(board_str: List[str], R: int, C: int) -> List[List[str]]:
    board = []
    for i in range(0, len(board_str), R):
        board.append(list(board_str[i:i+R]))

    return board

def convert_string_to_int(board_str: List[str], codec: Dict[str, int]) -> int:
    """
    convert the board string to a packed integer
    
    n bits in final int = log2(len(codec)) * len(board_str)
    """
    packed_value = 0
    bits_per_integer = calc_nbits_from_codec(len(codec))
    for char in board_str:
        int_val = codec[char]
        packed_value = (packed_value << bits_per_integer) | int_val 
 
    return packed_value

def convert_int_to_string(packed_value: int, codec: Dict[int, str], length: int) -> List[str]:
    """
    convert the packed integer back to a board string
    """
    bits_per_integer = calc_nbits_from_codec(len(codec))
    mask = (1 << bits_per_integer) - 1
    board_str = []
    for _ in range(length):
        int_val = packed_value & mask
        board_str.append(codec[int_val])
        packed_value >>= bits_per_integer

    return board_str[::-1]

def calc_nbits_from_codec(codec_len: int) -> int:
    bits_per_integer = math.ceil(math.log2(codec_len))
    return bits_per_integer

def get_value_at(board: int, position: int, n_bits: int) -> int:
    mask = (1 << n_bits) - 1
    return (board >> (position * n_bits)) & mask

def update_value_at(board: int, position: int, n_bits: int, value: int) -> int:
    mask = (1 << n_bits) - 1
    mask = mask << (position * n_bits)
    board = (board & ~mask) | (value << (position * n_bits))
    return board

def print_board(board, R, C):
    print("-"*(R*2 + 1))
    for row in board:
        print(end="|")
        for item in row:
            print(item, end="|")

        print()
        print("-"*(R*2 + 1))

def print_board_with_positions(board: List[List[str]], R: int, C: int, positions: List[tuple[int, int]]):
    # Define ANSI escape codes for colors and effects
    green_bold = "\033[1;32m"  # Bold Green
    reset = "\033[0m"  # Reset to default terminal color
    
    print("-" * (R * 2 + 1))
    for i, row in enumerate(board):
        print(end="|")
        for j, item in enumerate(row):
            # Check if the current position is in the list of positions to highlight
            if (i, j) in positions:
                # Print in bold green if the position is in the list
                print(f"{green_bold}{item}{reset}", end="|")
            else:
                # Print in default color
                print(item, end="|")
        print()
        print("-" * (R * 2 + 1))


def draw_king_moves(king_moves, R, C):
    board = [[" " for _ in range(R)] for _ in range(C)]

    for (x, y) in king_moves:
        board[x][y] = "#"

    print_board(board, R, C)

def gen_random_board(R, C):
    return [[random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(R)] for _ in range(C)]