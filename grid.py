from game.maze_generator import generate_maze

class Grid:
    def __init__(self, rows=5, cols=5):
        # generate random maze
        self.grid = generate_maze(rows, cols)

        self.rows = len(self.grid)
        self.cols = len(self.grid[0])

        self.start = (0, 0)
        self.goal = (self.rows - 1, self.cols - 1)

    def is_valid(self, position):
        x, y = position

        # boundary check
        if x < 0 or y < 0 or x >= self.rows or y >= self.cols:
            return False

        # obstacle check
        if self.grid[x][y] == 1:
            return False

        return True