# Sudoku Solver in Python

A Sudoku solver implemented from scratch in Python.

The project started from a simple question:

> Can I design a complete Sudoku solving algorithm from first principles and implement it myself?

Rather than relying on external Sudoku libraries, the solver uses its own implementation of candidate generation, deduction rules and backtracking.

The project was created primarily as an exercise in algorithm design and logical problem solving.

---

## Features

* Solves standard 9×9 Sudoku puzzles.
* Generates candidate lists for empty cells.
* Detects naked singles.
* Detects hidden singles in rows, columns and 3×3 blocks.
* Uses heuristic ordering of unresolved positions.
* Uses backtracking only when deterministic methods are no longer sufficient.
* Includes built-in documentation accessible through Python's `help()` mechanism.

---

## Algorithm Overview

The solver works in several stages.

### 1. Candidate Generation

For every empty position, all admissible digits are determined according to Sudoku rules.

### 2. Deterministic Solving

The solver repeatedly applies deduction rules:

* Naked Singles (only one candidate remains in a cell)
* Hidden Singles (a digit can appear in only one position within a row, column or block)

### 3. Heuristic Ordering

When deterministic methods can no longer make progress, unresolved positions are ordered according to the number of available candidates.

The most constrained position is selected first.

### 4. Backtracking

If several candidates remain possible, the current state is stored and one candidate is selected.

If a contradiction is encountered later, the previous state is restored and another candidate is tried.

### 5. Completion

The process continues until all positions are filled and a valid Sudoku solution is obtained.

---

## Assumptions

The solver is intended for valid Sudoku puzzles having a unique solution.

The goal of the project is solving such puzzles efficiently rather than analysing the number of possible solutions.

---

## Project Structure

### `sudoku.py`

Main solver implementation.

Contains:

* candidate generation,
* deduction logic,
* backtracking,
* puzzle solving workflow.

### `sudoku_hlp.py`

Function documentation.

This file contains detailed descriptions of the individual functions, their parameters and return values.

### `sudoku_help_console.py`

Simple console interface for browsing the built-in documentation.

---

## Providing a Puzzle

The recommended way is to define the puzzle directly as a NumPy array in the `init` variable near the end of `sudoku.py`.

## Example

Input:

```python
import numpy as np

...

init = np.array([
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
])
```

Output:

```text
534678912
672195348
198342567
859761423
426853791
713924856
961537284
287419635
345286179
```

An interactive console input mode is also available.

---

## Motivation

My background is in physics, statistics and quantitative data analysis.

The purpose of this project was not to build a production-grade Sudoku application, but to design and implement a complete solving strategy independently.

The main focus of the project is the algorithm itself:

* modelling Sudoku constraints,
* deriving deduction rules,
* managing candidate sets,
* implementing controlled backtracking.

---

## Future Improvements

Possible future extensions include:

* puzzle validation before solving,
* graphical user interface,
* performance benchmarking,
* support for detecting multiple solutions,
* support for Sudoku variants.

These features were intentionally left outside the scope of the current project in order to keep the focus on the solving algorithm itself.

---

## How to Run

Clone the repository:

```bash
git clone https://github.com/smota-git/sudoku-python.git
cd sudoku-python
```

Running from the command line

```bash
pip install -r requirements.txt
python sudoku.py
```

Running in PyCharm

Open the project in PyCharm and run `sudoku.py`.

---

A C++ implementation of the same algorithm is also available:
https://github.com/smota-git/sudoku


