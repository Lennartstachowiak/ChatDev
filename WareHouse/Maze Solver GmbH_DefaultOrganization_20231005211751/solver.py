'''
File containing the Solver class for maze solving.
'''
class Solver:
    def __init__(self, maze):
        self.maze = maze
        self.solution = []
    def solve(self):
        # Maze solving algorithm implementation
        start = self.maze.get_start_position()
        end = self.maze.get_end_position()
        visited = set()
        return self.dfs(start, end, visited)
    def dfs(self, current, end, visited):
        if current == end:
            return True
        visited.add(current)
        neighbors = self.maze.get_neighbors(current)
        for neighbor in neighbors:
            if neighbor not in visited:
                if self.dfs(neighbor, end, visited):
                    self.solution.append(neighbor)
                    return True
        return False
    def draw_solution(self, canvas):
        # Solution drawing implementation using tkinter canvas
        for position in self.solution:
            x, y = position
            canvas.create_rectangle(x * 30, y * 30, (x + 1) * 30, (y + 1) * 30, fill="green")