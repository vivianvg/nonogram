""" Standardize input into the nonogram solver

input : {
    across: list of n lists, where the nth list contains nonogram inputs ordered top to bottom
    down: list of n lists,  where the nth list contains nonogram inputs ordered left to right
}

output : [n x n] matrix


"""


# EXAMPLES
INPUT_1_5 = {
    "across": [[1], [2, 1], [5], [2, 1], [1]],
    "down": [[3], [3], [1, 1, 1], [3], [1]],
}

OUTPUT_1_5 = [
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0],
]


INPUT_1_10 = {
    "across": [[2], [4, 1], [7, 2], [7], [10], [9], [6], [2, 3, 2], [1, 5], [3]],
    "down": [[1, 1], [1, 2, 1], [1, 2, 2], [5], [8], [9], [9], [4, 2], [8], [8]],
}

OUTPUT_1_10 = [
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 1, 0, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 1, 1, 1, 0, 1, 1],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
]

INPUT_2_10 = {
    "across": [
        [1, 1, 3, 1],
        [1, 4, 1, 1],
        [2, 1, 1],
        [1, 2, 4],
        [2, 1, 2, 1],
        [2, 2, 1],
        [2, 4, 1],
        [1, 3, 3],
        [1, 1, 4],
        [1, 1, 4],
    ],
    "rows": [
        [2, 3, 1],
        [5],
        [3, 1, 1],
        [5, 1],
        [1, 3],
        [2, 5],
        [1, 4, 2],
        [4, 4],
        [3, 3],
        [3, 4],
    ],
}

OUTPUT_2_10 = [
    [1, 1, 0, 1, 1, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 1, 1, 0],
    [1, 1, 0, 1, 1, 1, 1, 1, 0, 0],
    [1, 0, 0, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
]
