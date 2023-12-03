"""
brainstorming approach
* at each iteration, return a new board? and pass to same input function
* always find a deterministic move 

playing the game helps 
3. realization that with every move, you have to update all the conditions it impacts....
    so at every point.. how do you track changes to what determinsitic moves are there?
        consider maybe a 2nd grid map of all the possibilities for each cell???
            (one strategy u use is fill in all the ones that overlap across diff possibilities)
             so you'd need a function for overlap?

"""
import numpy as np
from nonograms import INPUT_1_5, INPUT_1_10


def solve_nonogram(nonogram: dict, size: int):
    # sanity input checks
    assert len(nonogram["across"]) == size
    assert len(nonogram["down"]) == size

    # empty game board
    board = np.zeros((size, size), dtype=np.int8)

    # determine next move
    next_move(nonogram, board, size)

    # place on board
    board = place_cell(board, (-1, -1), size)

    display(board)


def next_move(nonogram: dict, board: np.ndarray, size) -> list:
    """generate a list of deterministic moves

    Return:
        [(x_1, y_1), (x_2, y_2), ...]

    questions:
    2. how do we track all the diff possibilities
    4. determining how many combinations of possibilities?
        total = sum(conditions) + len(conditions)
        eg. (2, 2, 2) has 10 diff placements
        TODO confirm that the total determines the # of combinations?
        for 10 cells, total=11 => 1 way, total=10 => 2 ways, total=9 => 10 ways
    """
    moves = []

    # first check for any that fill entire rows or columns
    # c is a list of numbers that denote the conditions for that row/col
    for c in nonogram["across"]:
        if sum(c) + len(c) == (size + 1):
            # only one way to populate the column
            col = place_array(c, size, start=0)
            print(col)

    for c in nonogram["down"]:
        if sum(c) + len(c) == (size + 1):
            row = place_array(c, size, start=0)
            print(row)


def place_array(conditions: list, size: int, start: int = 0) -> list:
    """
    Expects a deterministic set of conditions
    i.e. only one way to fill cells in a row or column

    questions:
    1. we expect recursive? be able to handle less than n, so we need a start index

    """
    fill = np.zeros((size, 1), dtype=np.int8)

    i = start

    while i < size:
        # fill cell & update conditions
        fill[i] = 1
        conditions[0] = conditions[0] - 1

        # a condition was satisfied => skip next space
        if conditions[0] == 0:
            # pop first element as it is populated into the board
            conditions.pop(0)
            # skip a space (nonogram rules)
            i = i + 2
        else:
            i = i + 1

    return fill


# TODO double check if this is inefficient to pass boards back
def place_cell(board: np.ndarray, coord: tuple, size) -> np.ndarray:
    """"""
    x, y = coord

    # make sure within bounds of the board
    if (x >= 0) and (y >= 0) and (x < size) and (y < size):
        board[x][y] = 1

    return board


def display(board: np.ndarray):
    print("-----------------------------")
    print(board)


def main():
    solve_nonogram(INPUT_1_5, 5)

if __name__ == "__main__":
    main()
