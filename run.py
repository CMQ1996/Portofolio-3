import random

GRID_SIZE = 5
NUM_SHIPS = 3
MAX_TURNS = 10

def print_board(board):
    print("  " + " ".join(str(i) for i in range(GRID_SIZE)))
    for idx, row in enumerate(board):