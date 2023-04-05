#!/usr/bin/python3
"""
N queens
"""
import sys


def is_safe(board, row, col, n):
    """
    Checks if it is safe to place a queen at board[row][col]
    """
    # Check this row on left side
    for i in range(col):
        if board[row][i]:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j]:
            return False

    # It is safe to place a queen at board[row][col]
    return True


def solve(board, col, n):
    """
    Recursive function to solve the N queens problem
    """
    # Base case: If all queens are placed, return True
    if col == n:
        print([[i, j] for i in range(n) for j in range(n) if board[i][j]], end="")
        print()
        return True

    # Consider this column and try placing a queen in all rows one by one
    res = False
    for row in range(n):
        if is_safe(board, row, col, n):
            # Place this queen in board[row][col]
            board[row][col] = 1

            # Make the recursive call to place the rest of the queens
            res = solve(board, col + 1, n) or res

            # If placing the queen at board[row][col] does not lead
            # to a solution, remove the queen from board[row][col]
            board[row][col] = 0

    # Return False if no queen can be placed in this column
    return res


if __name__ == "__main__":
    # Check if the number of arguments is correct
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Get the value of N from the command line argument
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize an empty board
    board = [[0 for j in range(n)] for i in range(n)]

    # Call the solve function to find all solutions
    solve(board, 0, n)
