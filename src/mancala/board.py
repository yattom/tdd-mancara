class Board:
    def __init__(self) -> None:
        self._stones = [3, 3, 3, 3, 3, 3, 3, 3]

    def stones(self) -> list[int]:
        return self._stones.copy()

    def copy(self) -> Board:
        new = Board()
        new._stones = self._stones.copy()
        return new

    def move_a_stone(self, from_pit: int, to_pit: int) -> Board:
        new = self.copy()
        new._stones[from_pit - 1] -= 1
        new._stones[to_pit - 1] += 1
        return new
