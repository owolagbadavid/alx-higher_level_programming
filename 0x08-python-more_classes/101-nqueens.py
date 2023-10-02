#!/usr/bin/python3
import sys


def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(n):
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_util(board, 0, n, solutions)
    
    for solution in solutions:
        print(solution)

def solve_util(board, col, n, solutions):
    if col == n:
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve_util(board, col + 1, n, solutions)
            board[i][col] = 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    N = 0
    try:
        N = int(sys.argv[1])
        if N < 4:
            raise TypeError()
        solve_nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    except TypeError:
        print("N must be at least 4")
        sys.exit(1)
