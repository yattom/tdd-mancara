class Board:
    def __init__(self) -> None:
        self._stones = [3, 3, 3, 3, 3, 3, 3, 3]

    def stones(self) -> list[int]:
        return self._stones.copy()

    def copy(self) -> Board:
        new = Board()
        new._stones = self._stones.copy()
        return new

    def move_a_stone(self, from_pit_no: int, to_pit_no: int) -> Board:
        new = self.copy()
        new._stones[from_pit_no - 1] -= 1
        new._stones[to_pit_no - 1] += 1
        return new

    def move(self, from_pit_no: int) -> Board:
        board = self
        to_pit_no = from_pit_no
        for _ in range(self.stones()[from_pit_no - 1]):
            to_pit_no = to_pit_no + 1
            board = board.move_a_stone(from_pit_no, to_pit_no)
        return board
