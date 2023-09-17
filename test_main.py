# Test main.py

import main


def test_calculate_stat():
    calculate_stat()


def test_count_row():
    num_row = main.count_row()
    assert num_row == 15723


if __name__ == "__main__":
    test_count_col()
    test_count_row()
