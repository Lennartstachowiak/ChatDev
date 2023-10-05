'''
File containing the Maze class for maze generation.
'''
import random
class Maze:
    def __init__(self):
        self.width = 20
        self.height = 20
        self.grid = [[1] * self.width for _ in range(self.height)]
    def generate(self):
        # Maze generation algorithm implementation
        stack = [(0, 0)]
        while stack:
            current = stack[-1]
            x, y = current
            self.grid[y][x] = 0
            neighbors = self.get_unvisited_neighbors(current)
            if neighbors:
                next_cell = random.choice(neighbors)
                nx, ny = next_cell
                self.grid[ny][nx] = 0
                stack.append(next_cell)
            else:
                stack.pop()
    def draw(self, canvas):
        # Maze drawing implementation using tkinter canvas
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == 1:
                    canvas.create_rectangle(x * 30, y * 30, (x + 1) * 30, (y + 1) * 30, fill="black")
    def get_unvisited_neighbors(self, current):
        x, y = current
        neighbors = []
        if x > 0 and self.grid[y][x - 1] == 1:
            neighbors.append((x - 1, y))
        if x < self.width - 1 and self.grid[y][x + 1] == 1:
            neighbors.append((x + 1, y))
        if y > 0 and self.grid[y - 1][x] == 1:
            neighbors.append((x, y - 1))
        if y < self.height - 1 and self.grid[y + 1][x] == 1:
            neighbors.append((x, y + 1))
        return neighbors
    def get_start_position(self):
        return (0, 0)
    def get_end_position(self):
        return (self.width - 1, self.height - 1)
    def get_neighbors(self, current):
        x, y = current
        neighbors = []
        if x > 0 and self.grid[y][x - 1] == 0:
            neighbors.append((x - 1, y))
        if x < self.width - 1 and self.grid[y][x + 1] == 0:
            neighbors.append((x + 1, y))
        if y > 0 and self.grid[y - 1][x] == 0:
            neighbors.append((x, y - 1))
        if y < self.height - 1 and self.grid[y + 1][x] == 0:
            neighbors.append((x, y + 1))
        return neighbors