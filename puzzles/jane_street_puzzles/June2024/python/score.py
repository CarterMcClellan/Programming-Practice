from typing import List, Tuple
from utils import convert_string_to_board, get_king_moves, print_board, print_board_with_positions
from data import state_population

class BoardScorer:
    def __init__(self, board: list[list[str]]):
        self.state_scores = state_population
        self.states = list(self.state_scores.keys())

        self.board = board

        self.R = len(self.board)
        self.C = len(self.board[0])

    def word_search_helper(self, word: str, current_x: int, current_y: int, mulligan: int, positions: List[Tuple[int, int]]) -> Tuple[bool, List[Tuple[int, int]]]:
        if word == "":
            return True, positions

        curr_moves = get_king_moves(current_x, current_y, self.R, self.C)
        for (x, y) in curr_moves:
            new_positions = positions + [(x, y)]
            if self.board[x][y] == word[0] or (self.board[x][y] != word[0] and mulligan > 0):
                used_mulligan = 1 if self.board[x][y] != word[0] else 0
                found, path = self.word_search_helper(word[1:], x, y, mulligan - used_mulligan, new_positions)
                if found:
                    return True, path

        return False, []


    def word_search(self, word: str) -> Tuple[bool, List[Tuple[int, int]]]:
        for x in range(self.R):
            for y in range(self.C):
                result, positions = self.word_search_helper(word, x, y, 1, [])
                if result:
                    return True, positions
        return False, []


    def score_states(self, states: List[str]) -> int:
        final_score = 0
        for state in states :
            final_score += self.state_scores[state]

        return final_score

    def main(self):
        states_found = []
        state_positions = {}
        for state in self.states:
            state_found, positions = self.word_search(state)
            if state_found:
                states_found.append(state)
                state_positions[state] = positions

        final_score = 0
        for state in states_found:
            final_score += self.state_scores[state]

        print("-"*50)
        print("States Found:")
        for state in sorted(states_found):
            print("\t", state)
        print("Final Score:", f"{final_score:,}")  # This will format the score with commas
        print("-"*50)

        for state, positions in state_positions.items():
            print("positions", positions)
            print("-"*50)
            print("State:", state)
            print_board_with_positions(self.board, self.R, self.C, positions)
            print("-"*50)


if __name__ == "__main__":
    # one_d_board = list("thoainesl")
    # one_d_board = list("goltarinepsainwhclrsufoyk")
    one_d_board = list("chndsariactnolvpeyihgwmsc")
    # as_lower = "CODHCLUTANIORKSSNABODIETL".lower()
    # one_d_board = list(as_lower)
    board = convert_string_to_board(one_d_board, 5, 5)
    print_board(board, 3, 3)
    # board = [
    #     [ "t", "h", "o" ],
    #     [ "a", "i", "n" ],
    #     [ "e", "s", "l" ],
    # ]


    bs = BoardScorer(board)
    bs.main()

    # states_to_try = [
    #     "california", "texas", "florida", "newyork",  "pennsylvania", "illinois",
    #     "northcarolina", "ohio", "georgia", "utah", "iowa", "idaho",  "arizona", "michigan"
    # ]
    # print("For states", states_to_try, "we got a score of:", bs.score_states(states_to_try))

    # Basic Question: how can we tell if a set of words will even fit on a board
    # there are 26 possible tiles and a 5x5 board so by list of unique characters we are always
    # going to be fine