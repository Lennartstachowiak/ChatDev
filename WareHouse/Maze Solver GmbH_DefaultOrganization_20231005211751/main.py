'''
Main file for the maze generation and solving program.
'''
import tkinter as tk
from maze import Maze
from solver import Solver
class MazeSolverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Maze Solver")
        self.maze = Maze()
        self.solver = Solver(self.maze)
        self.canvas = tk.Canvas(self.root, width=600, height=600, bg="white")
        self.canvas.pack()
        self.generate_button = tk.Button(self.root, text="Generate Maze", command=self.generate_maze)
        self.generate_button.pack()
        self.solve_button = tk.Button(self.root, text="Solve Maze", command=self.solve_maze)
        self.solve_button.pack()
    def generate_maze(self):
        self.maze.generate()
        self.maze.draw(self.canvas)
    def solve_maze(self):
        solution = self.solver.solve()
        if solution:
            self.solver.draw_solution(self.canvas)
        else:
            print("No solution found for the maze.")
if __name__ == "__main__":
    root = tk.Tk()
    app = MazeSolverApp(root)
    root.mainloop()