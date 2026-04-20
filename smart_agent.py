from collections import deque

class SmartAgent:
    def __init__(self, start):
        self.start = start
        self.path = []

    def bfs(self, grid):
        queue = deque()
        queue.append((self.start, [self.start]))

        visited = set()
        visited.add(self.start)

        while queue:
            current, path = queue.popleft()

            if current == grid.goal:
                self.path = path
                return True

            x, y = current
            moves = [
                (x-1, y),
                (x+1, y),
                (x, y-1),
                (x, y+1)
            ]

            for move in moves:
                if grid.is_valid(move) and move not in visited:
                    visited.add(move)
                    queue.append((move, path + [move]))

        return False