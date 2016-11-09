class NotInGameField(Exception):
    pass


class Position(object):
    """ Represent tile object position """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def serialize(self):
        return "({},{})".format(self.x, self.y)

    def __str__(self):
        return '({} {})'.format(self.x, self.y)

    def __hash__(self):
        return hash((self.x, self.y,))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return self.serialize()