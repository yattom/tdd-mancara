from mancala.board import Board


def test_初期盤面はすべての穴に石が3個() -> None:
    board = Board()
    assert board.stones() == [3, 3, 3, 3, 3, 3, 3, 3]


def test_初期盤面から穴2を選ぶと穴3から5に1個ずつ蒔かれる() -> None:
    board = Board()
    pit = board.pit(2)
    board = board.move(pit)
    assert board.stones() == [3, 0, 4, 4, 4, 3, 3, 3]


def test_初期盤面で穴2から穴3に石を1つ移す() -> None:
    board = Board()
    from_pit = board.pit(2)
    to_pit = board.pit(3)
    board = board.move_a_stone(from_pit, to_pit)
    assert board.stones() == [3, 2, 4, 3, 3, 3, 3, 3]
