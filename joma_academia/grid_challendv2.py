# https://www.techseries.dev/coderpro-episode3
import random
CELL_COLORED = "X"
CELL_EMPTY = " "

# Validation cell type
if type(CELL_COLORED) is not str or type(CELL_EMPTY) is not str:
    raise Exception("Cells must be string types")


def _build_grid(rows_len=random.randint(2, 4),
                cols_len=random.randint(2, 4)):
    grid = list()
    for row in range(rows_len):
        new_row = list()
        for cell in range(cols_len):
            new_row.append(random.choice([CELL_COLORED, CELL_EMPTY]))
        grid.append(new_row)
    return grid


class Grid:
    def __init__(self, grid=_build_grid()):
        self.grid = grid

    def __str__(self):
        return "\n".join(["\t".join(row) for row in self.grid])

    def max_connected(self):
        _max = 0
        ii, jj = 0, 0

        for row in self.grid:
            for element in row:
                if element == CELL_COLORED:
                    n = self.dfs(ii, jj)
                    _max = max(_max, n)
                jj += 1
            ii += 1
            jj = 0

        return _max

    def dfs(self, ii, jj, visited=None):
        visited = visited if visited else dict()

        key = f"{ii},{jj}"
        if key in visited.keys():
            return 0

        visited[key] = True
        result = 1
        for neighbor_ii, neighbor_jj, neighbor_fill in self.neighbors(ii, jj):
            if neighbor_fill != CELL_COLORED:
                continue
            result += self.dfs(neighbor_ii, neighbor_jj, visited)
        return result

    def neighbors(self, ii, jj):
        responde = list()
        positions = [
            (ii, jj - 1),  # left
            (ii, jj + 1),  # right
            (ii - 1, jj),  # up
            (ii + 1, jj),  # bottom
        ]

        for position_ii, position_jj in positions:
            if position_ii < 0 or position_ii >= len(self.grid):
                continue
            if position_jj < 0 or position_jj >= len(self.grid[0]):
                continue

            responde.append((position_ii,
                             position_jj,
                             self.grid[position_ii][position_jj]))

        return responde


if __name__ == "__main__":
    grid = Grid()
    print(grid)
    print(grid.max_connected())
