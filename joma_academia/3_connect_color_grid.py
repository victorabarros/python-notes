# https://www.techseries.dev/coderpro-episode3
import random
CELL_COLORED = "X"
CELL_EMPTY = " "
CELLS_VISITED = list()


def build_random_grid(rows_len=random.randint(1, 5),
                      col_len=random.randint(1, 5)):
    grid = list()
    for row in range(rows_len):
        new_row = list()
        for cell in range(col_len):
            new_row.append(random.choice([CELL_COLORED, CELL_EMPTY]))
        grid.append(new_row)
    return grid


def print_grid(grid):
    print("\n".join(
        ["\t".join([str(cell) for cell in row]) for row in grid]))


# def find_neighbor_colored(grid, element):
#     colored_neighbors = 0
#     e_ii, e_jj = element

#     neighbors = []
#     neighbors.append((e_ii, e_jj - 1))  # left_neighbor
#     neighbors.append((e_ii, e_jj + 1))  # right_neighbor
#     neighbors.append((e_ii + 1, e_jj))  # up_neighbor
#     neighbors.append((e_ii - 1, e_jj))  # down_neighbor

#     for neighbor in neighbors:
#         n_ii, n_jj = neighbor
#         try:
#             if grid[n_ii][n_jj] is True:
#                 colored_neighbors += 1
#         except IndexError:
#             pass
#     return colored_neighbors


# def map_colored_elements(grid):
#     colored_elements = list()
#     heat_map = list()
#     ii, jj = 0, 0

#     for row in grid:
#         heat_map_line = list()
#         for element in row:
#             colored_neighbors = 0
#             if element is True:
#                 # colored_elements.append((ii, jj))
#                 colored_neighbors = find_neighbor_colored(grid, (ii, jj))
#             heat_map_line.append(colored_neighbors)
#             jj += 1
#         heat_map.append(heat_map_line)
#         ii += 1
#         jj = 0
#     print('\n')
#     print_grid(heat_map)
#     return colored_elements


def colored_cells_search(grid):
    max_colored_result = 0
    ii = 0
    jj = 0

    for row in grid:
        for cell in row:
            if cell == CELL_COLORED:
                n = dfs((ii, jj), grid)
                max_colored_result = max(max_colored_result, n)
            jj += 1
        ii += 1
        jj = 0

    return max_colored_result


def dfs(cell_coordinate, grid):
    colored_neighbors = 1
    c_ii, c_jj = cell_coordinate

    neighbors = [
        (c_ii, c_jj - 1),  # left_neighbor
        (c_ii, c_jj + 1),  # right_neighbor
        (c_ii + 1, c_jj),  # up_neighbor
        (c_ii - 1, c_jj),  # bottom_neighbor
    ]

    for neighbor in neighbors:
        print(cell_coordinate, neighbor)
        n_ii, n_jj = neighbor
        try:
            neighbor_value = grid[n_ii][n_jj]
        except IndexError:
            continue
        if neighbor_value == CELL_COLORED and\
           neighbor_value not in CELLS_VISITED:
            colored_neighbors += dfs(neighbor, grid)
    return colored_neighbors


if __name__ == "__main__":
    grid = build_random_grid(2, 3)
    print_grid(grid)
    result = colored_cells_search(grid)
    print(result)
    # map_colored_elements(grid)
