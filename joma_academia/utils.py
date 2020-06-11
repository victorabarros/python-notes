# https://www.techseries.dev/coderpro-episode3
import random
CELL_COLORED = "X"
CELL_EMPTY = " "
CELLS_VISITED = list()


def build_random_grid(rows_len, col_len, cell_colored=CELL_COLORED, cell_empty=CELL_EMPTY):
    grid = list()
    for row in range(rows_len):
        new_row = list()
        for cell in range(col_len):
            new_row.append(random.choice([cell_colored, cell_empty]))
        grid.append(new_row)
    return grid


def print_grid(grid):
    print("\n".join(
        ["\t".join([str(cell) for cell in row]) for row in grid]))
