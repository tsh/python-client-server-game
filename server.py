import math
from common import Position, NotInGameField


class Floor(object):
    pass


class Water(object):
    pass


class Map(object):
    def __init__(self):
        super().__init__()
        self.map = {
            Position(0, 12): Floor(),     Position(1, 12): Water(),         Position(2, 12): Floor(),     Position(3, 12): Floor(),     Position(4, 12): Floor(),     Position(5, 12): Floor(),     Position(6, 12): Floor(),     Position(7, 12): Floor(),     Position(8, 12): Floor(),     Position(9, 12): Floor(),     Position(10, 12): Floor(),        Position(11, 12): Floor(),    Position(12, 12): Floor(),
            Position(0, 11): Water(),     Position(1, 11): Floor(),         Position(2, 11): Water(),     Position(3, 11): Floor(),     Position(4, 11): Floor(),     Position(5, 11): Floor(),     Position(6, 11): Floor(),     Position(7, 11): Floor(),     Position(8, 11): Floor(),     Position(9, 11): Floor(),     Position(10, 11): Floor(),        Position(11, 11): Floor(),    Position(12, 11): Floor(),
            Position(0, 10): Floor(),     Position(1, 10): Water(),         Position(2, 10): Floor(),     Position(3, 10): Floor(),     Position(4, 10): Floor(),     Position(5, 10): Floor(),     Position(6, 10): Floor(),     Position(7, 10): Floor(),     Position(8, 10): Floor(),     Position(9, 10): Floor(),     Position(10, 10): Floor(),        Position(11, 10): Floor(),    Position(12, 10): Floor(),
            Position(0, 9): Floor(),      Position(1, 9): Floor(),          Position(2, 9): Floor(),      Position(3, 9): Floor(),      Position(4, 9): Floor(),      Position(5, 9): Floor(),      Position(6, 9): Floor(),      Position(7, 9): Floor(),      Position(8, 9): Floor(),      Position(9, 9): Floor(),      Position(10, 9): Floor(),         Position(11, 9): Floor(),     Position(12, 9): Floor(),
            Position(0, 8): Floor(),      Position(1, 8): Floor(),          Position(2, 8): Floor(),      Position(3, 8): Floor(),      Position(4, 8): Floor(),      Position(5, 8): Floor(),      Position(6, 8): Floor(),      Position(7, 8): Floor(),      Position(8, 8): Floor(),      Position(9, 8): Floor(),      Position(10, 8): Floor(),         Position(11, 8): Floor(),     Position(12, 8): Floor(),
            Position(0, 7): Floor(),      Position(1, 7): Floor(),          Position(2, 7): Floor(),      Position(3, 7): Floor(),      Position(4, 7): Floor(),      Position(5, 7): Floor(),      Position(6, 7): Floor(),      Position(7, 7): Floor(),      Position(8, 7): Floor(),      Position(9, 7): Floor(),      Position(10, 7): Floor(),         Position(11, 7): Floor(),     Position(12, 7): Floor(),
            Position(0, 6): Floor(),      Position(1, 6): Floor(),          Position(2, 6): Floor(),      Position(3, 6): Floor(),      Position(4, 6): Floor(),      Position(5, 6): Floor(),      Position(6, 6): Floor(),      Position(7, 6): Floor(),      Position(8, 6): Floor(),      Position(9, 6): Floor(),      Position(10, 6): Floor(),         Position(11, 6): Floor(),     Position(12, 6): Floor(),
            Position(0, 5): Floor(),      Position(1, 5): Floor(),          Position(2, 5): Floor(),      Position(3, 5): Floor(),      Position(4, 5): Floor(),      Position(5, 5): Floor(),      Position(6, 5): Floor(),      Position(7, 5): Floor(),      Position(8, 5): Floor(),      Position(9, 5): Floor(),      Position(10, 5): Floor(),         Position(11, 5): Floor(),     Position(12, 5): Floor(),
            Position(0, 4): Floor(),      Position(1, 4): Floor(),          Position(2, 4): Floor(),      Position(3, 4): Floor(),      Position(4, 4): Floor(),      Position(5, 4): Floor(),      Position(6, 4): Floor(),      Position(7, 4): Floor(),      Position(8, 4): Floor(),      Position(9, 4): Floor(),      Position(10, 4): Floor(),         Position(11, 4): Floor(),     Position(12, 4): Floor(),
            Position(0, 3): Floor(),      Position(1, 3): Floor(),          Position(2, 3): Floor(),      Position(3, 3): Floor(),      Position(4, 3): Floor(),      Position(5, 3): Floor(),      Position(6, 3): Floor(),      Position(7, 3): Floor(),      Position(8, 3): Floor(),      Position(9, 3): Floor(),      Position(10, 3): Floor(),         Position(11, 3): Floor(),     Position(12, 3): Floor(),
            Position(0, 2): Water(),      Position(1, 2): Water(),          Position(2, 2): Water(),      Position(3, 2): Floor(),      Position(4, 2): Floor(),      Position(5, 2): Floor(),      Position(6, 2): Floor(),      Position(7, 2): Floor(),      Position(8, 2): Floor(),      Position(9, 2): Floor(),      Position(10, 2): Floor(),         Position(11, 2): Floor(),     Position(12, 2): Floor(),
            Position(0, 1): Water(),      Position(1, 1): Floor(),          Position(2, 1): Water(),      Position(3, 1): Floor(),      Position(4, 1): Floor(),      Position(5, 1): Floor(),      Position(6, 1): Floor(),      Position(7, 1): Floor(),      Position(8, 1): Floor(),      Position(9, 1): Floor(),      Position(10, 1): Floor(),         Position(11, 1): Floor(),     Position(12, 1): Floor(),
            Position(0, 0): Water(),      Position(1, 0): Water(),          Position(2, 0): Water(),      Position(3, 0): Floor(),      Position(4, 0): Floor(),      Position(5, 0): Floor(),      Position(6, 0): Floor(),      Position(7, 0): Floor(),      Position(8, 0): Floor(),      Position(9, 0): Floor(),      Position(10, 0): Floor(),         Position(11, 0): Water(),     Position(12, 0): Floor(),
        }
        self.FIELD_SIZE = math.sqrt(len(self.map)) - 1


    def check_boundaries(self, pos: Position):
        if not (pos.x <= self.FIELD_SIZE and pos.y <= self.FIELD_SIZE):
            print('Out of boundaries: ', pos.x, pos.y)
            raise NotInGameField


    def clicked(self, pos: Position):
        pass
