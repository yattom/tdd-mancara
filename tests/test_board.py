from mancala.board import Board


def test_初期盤面はすべての穴に石が3個() -> None:
    board = Board()
    assert board.stones() == [3, 3, 3, 3, 3, 3, 3, 3]


def test_初期盤面から穴2を選ぶと穴3から5に1個ずつ蒔かれる() -> None:
    board = Board().move(2)
    assert board.stones() == [3, 0, 4, 4, 4, 3, 3, 3]


def test_初期盤面で穴2から穴3に石を1つ移す() -> None:
    board = Board().move_a_stone(2, 3)
    assert board.stones() == [3, 2, 4, 3, 3, 3, 3, 3]
