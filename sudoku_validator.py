

from typing import List, Tuple

def is_valid_unit(unit: List[int]) -> bool:
    """
    Helper function to validate a group of 9 cells (row, column, box, or zone).
    """
    unit = [num for num in unit if num != 0]
    return len(unit) == len(set(unit)) and all(1 <= num <= 9 for num in unit)

def validate_sudoku(board: List[List[int]], zones: List[List[Tuple[int, int]]]) -> bool:
    """
    Validates a 9x9 Sudoku board with custom zones.
    
    Args:
        board: 2D list representing the Sudoku board.
        zones: List of 9 custom zones, each with 9 (row, col) tuples.
    
    Returns:
        True if board is valid, False otherwise.
    """

    # Validate rows and columns
    for i in range(9):
        row = board[i]
        col = [board[r][i] for r in range(9)]
        if not is_valid_unit(row) or not is_valid_unit(col):
            return False

    # Validate 3x3 standard subgrids
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            box = [board[r][c] for r in range(box_row, box_row+3)
                                for c in range(box_col, box_col+3)]
            if not is_valid_unit(box):
                return False

    # Validate custom zones
    for zone in zones:
        custom = [board[r][c] for r, c in zone]
        if not is_valid_unit(custom):
            return False

    return True

def run_tests():
    """Runs sample test cases."""
    print("=== Sudoku Validator with Custom Zones ===\n")

    # Sample valid board
    valid_board = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9],
    ]

    # Custom zones (for example: 9 diagonal zones, each crossing the board)
    custom_zones = [
        [(i, i) for i in range(9)],
        [(i, 8 - i) for i in range(9)],
        [(i, (i + 1) % 9) for i in range(9)],
        [(i, (i + 2) % 9) for i in range(9)],
        [(i, (i + 3) % 9) for i in range(9)],
        [(i, (i + 4) % 9) for i in range(9)],
        [(i, (i + 5) % 9) for i in range(9)],
        [(i, (i + 6) % 9) for i in range(9)],
        [(i, (i + 7) % 9) for i in range(9)],
    ]

    # Test 1: Valid board and custom zones
    result1 = validate_sudoku(valid_board, custom_zones)
    print("Test Case 1 - Valid Board with Custom Zones: ", "✅ Passed\n" if result1 else "❌ Failed\n")

    # Test 2: Modify a cell to break a row rule
    invalid_board = [row[:] for row in valid_board]
    invalid_board[0][0] = 6
    result2 = validate_sudoku(invalid_board, custom_zones)
    print("Test Case 2 - Invalid Row: ", "✅ Passed\n" if not result2 else "❌ Failed\n")

    # Test 3: Modify a cell to break a custom zone rule
    invalid_board2 = [row[:] for row in valid_board]
    invalid_board2[1][1] = 5  # (1,1) is part of first custom zone
    result3 = validate_sudoku(invalid_board2, custom_zones)
    print("Test Case 3 - Invalid Custom Zone: ", "✅ Passed\n" if not result3 else "❌ Failed\n")

if __name__ == "__main__":
    run_tests()
