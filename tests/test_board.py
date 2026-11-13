import pytest

from mancala.board import Board


def test_初期盤面はすべての穴に石が3個() -> None:
    board = Board()
    assert board.stones() == [3, 3, 3, 3, 3, 3, 3, 3]


@pytest.mark.skip(reason="先に move_a_stone() を作る")
def test_初期盤面から穴2を選ぶと穴3から5に1個ずつ蒔かれる() -> None:
    board = Board().move(2)
    assert board.stones() == [3, 0, 4, 4, 4, 3, 3, 3]
