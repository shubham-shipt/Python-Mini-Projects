import tkinter as tk
from tkinter import messagebox
import time

class SudokuGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Game - By Shubham")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        self.root.configure(bg='#0F0F0F')  # Dark hacker theme

        self.board = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        
        self.start_time = time.time()
        self.score = 0
        self.create_widgets()

    def create_widgets(self):
        self.cells = {}
        for row in range(9):
            for col in range(9):
                if self.board[row][col] != 0:
                    label = tk.Label(self.root, text=str(self.board[row][col]), font=('Arial', 18), bg='#0F0F0F', fg='#33FF33')
                    label.grid(row=row, column=col, sticky="nsew", padx=1, pady=1, ipadx=10, ipady=10)
                else:
                    entry = tk.Entry(self.root, width=2, font=('Arial', 18), justify='center', bg='#000000', fg='#33FF33')
                    entry.grid(row=row, column=col, sticky="nsew", padx=1, pady=1, ipadx=10, ipady=10)
                    entry.insert(0, '')
                    entry.bind('<KeyRelease>', lambda event, r=row, c=col: self.validate_entry(event, r, c))
                    self.cells[(row, col)] = entry
        
        self.score_label = tk.Label(self.root, text=f"Score: {self.score}", bg='#0F0F0F', fg='#33FF33', font=('Arial', 14))
        self.score_label.grid(row=9, column=0, columnspan=9, sticky="nsew", padx=10, pady=5)

        check_button = tk.Button(self.root, text="Check", command=self.check_solution, bg='#33FF33', fg='#000000', font=('Arial', 14))
        check_button.grid(row=10, column=0, columnspan=9, sticky="nsew", padx=10, pady=10)

        rules_label = tk.Label(self.root, text="Rules: Har row, column, aur 3x3 box me 1-9 ke unique digits hone chaiye.", bg='#0F0F0F', fg='#33FF33', font=('Arial', 12), wraplength=400)
        rules_label.grid(row=11, column=0, columnspan=9, sticky="nsew", padx=10, pady=10)

    def validate_entry(self, event, row, col):
        entry = self.cells[(row, col)]
        value = entry.get()
        
        if value.isdigit() and 1 <= int(value) <= 9:
            self.board[row][col] = int(value)
            if self.is_valid(row, col):
                entry.config(fg='#33FF33')  # Green if valid
                self.score += 10
            else:
                entry.config(fg='#FF3333')  # Red if invalid
                self.score -= 5
        else:
            entry.config(fg='#FF3333')
            self.score -= 5
        
        self.score_label.config(text=f"Score: {self.score}")

    def check_solution(self):
        if self.is_solved():
            elapsed_time = time.time() - self.start_time
            messagebox.showinfo("Congratulations!", f"You solved the puzzle in {int(elapsed_time)} seconds! Your score: {self.score}")
        else:
            messagebox.showwarning("Incorrect Solution", "The solution is incorrect. Please try again.")

    def is_solved(self):
        for row in range(9):
            for col in range(9):
                if not self.is_valid(row, col):
                    return False
        return True

    def is_valid(self, row, col):
        value = self.board[row][col]
        for i in range(9):
            if i != col and self.board[row][i] == value:
                return False
            if i != row and self.board[i][col] == value:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if (start_row + i != row or start_col + j != col) and self.board[start_row + i][start_col + j] == value:
                    return False
        return True

if __name__ == "__main__":
    root = tk.Tk()
    game = SudokuGame(root)
    root.mainloop()

