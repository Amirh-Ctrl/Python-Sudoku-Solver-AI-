# 🧩 Python Sudoku Solver (AI)

This project is a Python script designed to solve 9x9 Sudoku puzzles. It utilizes a **Backtracking** algorithm combined with **Constraint Satisfaction Problem (CSP)** techniques to efficiently find a solution.

## 📜 Description

This solver models the Sudoku puzzle as a Constraint Satisfaction Problem (CSP). Each empty cell is treated as a variable, its domain consists of the numbers 1 through 9, and the constraints are the standard Sudoku rules (no repeated numbers in any row, column, or 3x3 block).

To optimize the search process, the **Minimum Remaining Values (MRV)** heuristic is implemented.

### ⚙️ How It Works

1.  **`Table` Class:** This class holds the current state of the Sudoku board.
2.  **`CreateCSP()`:** This method calculates the "domain" (the list of possible numbers) for each empty cell by checking its corresponding row, column, and 3x3 block.
3.  **`MRVFind()` (Minimum Remaining Values):** This heuristic finds the empty cell with the **fewest possible valid numbers** (the smallest domain). This strategy prioritizes the most constrained variables first, leading to faster pruning of the search tree.
4.  **`Solve()` (Backtracking):** This is the main recursive function:
    * It first checks if the board is already solved.
    * It uses `MRVFind()` to select the best cell to fill.
    * It iterates through the possible numbers (domain) for that cell.
    * For each number, it places it on the board and recursively calls `Solve()` for the new state.
    * If the recursive call returns `True` (a solution is found), it propagates `True` up the call stack.
    * If it leads to a dead end (`False`), it **backtracks** by resetting the cell to `0` and tries the next possible number.
    * If all numbers for the cell have been tried without success, it returns `False`.

---

## 🚀 How to Use

### 1. Prerequisites
* Python 3.x

### 2. Running the Solver

1.  Save the code as a Python file (e.g., `sudoku.py`).
2.  Open your terminal or command prompt.
3.  Run the script using the following command:

    ```bash
    python sudoku.py
    ```

### 3. Input Format

After running the script, it will wait for 9 lines of input. Each line must represent a row of the Sudoku puzzle.

* Separate the numbers in each row with a **space**.
* Use the number **0** to represent empty cells.

#### 📝 Example Input

You can copy and paste the following hard puzzle directly into your terminal:

0 0 3 0 2 0 6 0 0

9 0 0 3 0 5 0 0 1

0 0 1 8 0 6 4 0 0

0 0 8 1 0 2 9 0 0

7 0 0 0 0 0 0 0 8

0 0 6 7 0 8 2 0 0

0 0 2 6 0 9 5 0 0

8 0 0 2 0 3 0 0 9

0 0 5 0 1 0 3 0 0



### 4. Output



If a solution exists, the solved board will be printed:

4 8 3 9 2 1 6 5 7

9 6 7 3 4 5 8 2 1

2 5 1 8 7 6 4 9 3

5 4 8 1 3 2 9 7 6

7 2 9 5 6 4 1 3 8

1 3 6 7 9 8 2 4 5

3 7 2 6 8 9 5 1 4

8 1 4 2 5 3 7 6 9

6 9 5 4 1 7 3 8 2



If the puzzle is unsolvable, it will print:

This Sudoku puzzle has no solution.

#### 📝 Example Input

You can copy and paste the following hard puzzle directly into your terminal:
