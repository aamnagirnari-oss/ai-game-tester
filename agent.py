class Agent:
    def __init__(self, start):
        self.position = start
        self.path = [start]
        self.steps = 0

    def move(self, grid):
        import random

        x, y = self.position

        moves = [
            (x-1, y),
            (x+1, y),
            (x, y-1),
            (x, y+1)
        ]

        valid_moves = [m for m in moves if grid.is_valid(m)]

        if valid_moves:
            self.position = random.choice(valid_moves)
            self.path.append(self.position)
            self.steps += 1

    def reached_goal(self, goal):
        return self.position == goal