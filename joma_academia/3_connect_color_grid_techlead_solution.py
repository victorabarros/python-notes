from python_learning.joma_academia.utils import build_random_grid, print_grid


class Grid:
    def __init__(self, grid):
        self.grid = grid

    def max_connected_colors(self):
        max_n = 0

        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                max_n = max(max_n, self.dfs(x, y, {}))
        return max_n

    def dfs(self, x, y, visited):
        key = f"{x},{y}"
        if key in visited:
            return 0

        visited[key] = True
        result = 1
        for neighbor in self.neighbors(x, y):
            result += self.dfs(neighbor[0], neighbor[1], visited)
        return result

    def colorAt(self, x, y):
        if x >= 0 and x < len(self.grid[0]) and y >= 0 and y < len(grid):
            return self.grid[y][x]
        return -1

    def neighbors(self, x, y):
        POSITIONS = [[-1, 0], [0, -1], [0, 1], [1, 0]]
        n = []
        for pos in POSITIONS:
            if self.colorAt(x + pos[0], y + pos[1]) == self.colorAt(x, y):
                n.append((x + pos[0], y + pos[1]))
        return n


if __name__ == "__main__":
    grid = [[1, 0, 0, 1],
            [1, 1, 1, 0],
            [0, 1, 0, 1]]

    print(Grid(grid).max_connected_colors())
    # 5
    grid_2 = build_random_grid(4, 5, 1, 0)
    print_grid(grid_2)
