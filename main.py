class PicrossGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [[None] * width for _ in range(height)]  # None = unknown, True = filled, False = empty

# Functional approach for rule checking
def check_line_valid(line, rule):
    # Example: line [True, True, False, True]
    # rule [2, 1] means "2 blocks then 1 block"
    groups = get_groups(line)
    return groups == rule

    # Example representation
row_clues = [
    [4],      # Row 0: "4 consecutive filled squares"
    [1, 1],   # Row 1: "1 filled square, space, 1 filled square"
    [1, 2]    # Row 2: "1 filled square, space, 2 consecutive filled"
]

from enum import Enum

class CellState(Enum):
    UNKNOWN = 0
    FILLED = 1
    UNFILLED = 2  # represented by 'X' in visual display

class PicrossGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[CellState.UNKNOWN] * width for _ in range(height)]

def find_obvious_lines(row_clues, col_clues, grid_size):
    obvious_rows = []
    # Check for fully filled rows
    for row_num, clues in enumerate(row_clues):
        if sum(clues) == grid_size:
            obvious_rows.append((row_num, CellState.FILLED))
        elif sum(clues) == 0:
            obvious_rows.append((row_num, CellState.UNFILLED))