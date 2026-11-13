from mancala.pit import Pit


class Board:
    def __init__(self) -> None:
        self._stones = [3, 3, 3, 3, 3, 3, 3, 3]

    def stones(self) -> list[int]:
        return self._stones.copy()

    def pit(self, pit_no: int) -> Pit:
        return Pit(pit_no)

    def copy(self) -> Board:
        new = Board()
        new._stones = self._stones.copy()
        return new

    def move_a_stone(self, from_pit: Pit, to_pit: Pit) -> Board:
        new = self.copy()
        new._stones[self._index(from_pit)] -= 1
        new._stones[self._index(to_pit)] += 1
        return new

    def move(self, from_pit: Pit) -> Board:
        board = self
        to_pit = from_pit
        for _ in range(self._stones[self._index(from_pit)]):
            to_pit = Pit(to_pit.value + 1)
            board = board.move_a_stone(from_pit, to_pit)
        return board

    def _index(self, pit: Pit) -> int:
        return pit.value - 1
