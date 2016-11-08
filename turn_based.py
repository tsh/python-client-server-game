import math
import pyglet
from pyglet.window import mouse


class NotInGameField(Exception):
    pass


class Position(object):
    """ Represent tile object position """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y,))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return '({} {})'.format(self.x, self.y)


class Drawable(object):
    SIZE = 48

    def draw(self, pos: Position):
        x, y = self.get_screen_coord(pos)
        self._draw_rect(x, y, self.SIZE, self.SIZE, self.color)

    def _draw_rect(self, x, y, width, height, color):
        image_pattern = pyglet.image.SolidColorImagePattern(color=color)
        image = image_pattern.create_image(width, height)
        image.blit(x, y)

    @classmethod
    def get_clicked_tile_position(cls, x, y):
        """ Transforms screen coordinate `x` and `y` to tile clicked tile """
        tx = math.floor(x / cls.SIZE)
        ty = math.floor(y / cls.SIZE)
        return Position(tx, ty)

    @classmethod
    def get_screen_coord(cls, pos: Position):
        """ Transforms tile position to screen coordinates """
        x = pos.x * cls.SIZE
        y = pos.y * cls.SIZE
        return x, y


class Floor(Drawable):
    def __init__(self):
        self.color = (211, 211, 211, 0)


class Water(Drawable):
    def __init__(self):
        self.color = (0, 0, 250, 0)


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

    def draw(self):
        for pos, tile in self.map.items():
            tile.draw(pos)

    def check_boundaries(self, pos: Position):
        if not (pos.x <= self.FIELD_SIZE and pos.y <= self.FIELD_SIZE):
            print('Out of boundaries: ', pos.x, pos.y)
            raise NotInGameField

    def clicked(self, pos: Position):
        pass


class Character(Drawable):
    def __init__(self):
        super().__init__()
        self.is_selected = False
        self.color = (0, 255, 0, 0)
        self.selection_color = (128, 0, 128, 0)
        self.shrink_factor = 5

    def toggle_selection(self):
        self.is_selected = not self.is_selected

    def draw(self, pos: Position):
        x, y = self.get_screen_coord(pos)
        size = self.SIZE - self.shrink_factor * 2
        if self.is_selected:
            self._draw_rect(x + self.shrink_factor , y + self.shrink_factor , size, size, self.color)
            self._draw_rect(x + self.shrink_factor + int(Drawable.SIZE * 0.2), y + self.shrink_factor + int(Drawable.SIZE * 0.2),
                            size - int(Drawable.SIZE * 0.4), size - int(Drawable.SIZE * 0.4),
                            self.selection_color)
        else:
            self._draw_rect(x + self.shrink_factor , y + self.shrink_factor , size, size, (0, 255, 0, 0))


class Enemy(Drawable):
    def __init__(self):
        self.color = (255, 0, 0, 0)
        self.shrink_factor = 5

    def toggle_selection(self):
        pass

    def draw(self, pos: Position):
        x, y = self.get_screen_coord(pos)
        size = self.SIZE - self.shrink_factor * 2
        self._draw_rect(x + self.shrink_factor, y + self.shrink_factor, size, size, self.color)


class GameFieldManager(object):
    def __init__(self, mp: Map):
        self.default_value = 0
        self.objs = {
            Position(6, 9): Enemy(),    Position(1, 1): Character(),
        }
        self.map = mp

    def draw(self):
        self.map.draw()
        for pos, tile in self.objs.items():
            if not isinstance(tile, int):
                tile.draw(pos)

    def move(self, frm: Position, to: Position):
        tmp = self.objs[frm]
        self.objs[frm] = self.default_value
        self.objs[to] = tmp

    def get_selected_object_position(self):
        for pos, tile in self.objs.items():
            try:
                if tile.is_selected:
                    return pos
            except AttributeError:
                pass
        return None

    def clicked(self, clicked_pos: Position):
        try:
            self.map.check_boundaries(clicked_pos)
        except NotInGameField:
            return
        try:
            clicked = self.objs[clicked_pos]
        except KeyError:
            # click on empty field.
            # if we have selected object, move selected
            selected_obj_pos = self.get_selected_object_position()
            if selected_obj_pos:
                self.move(selected_obj_pos, clicked_pos)
        else:
            # select clicked object
            clicked.toggle_selection()


class Game(object):
    def __init__(self):
        map = Map()
        self.gfm = GameFieldManager(map)

    def draw(self):
        self.gfm.draw()

    def on_left_click(self, x, y):
        # Transform screen coordinates into tile
        pos = Drawable.get_clicked_tile_position(x, y)
        self.gfm.clicked(pos)


class MainWindow(pyglet.window.Window):
    """ Handle all low level implementation detail. Register events and pass them to game handlers. """
    def __init__(self, game):
        super().__init__(width=1024, height=768)
        self.game = game

    def on_draw(self):
        self.clear()
        self.game.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            self.game.on_left_click(x, y)


if __name__ == '__main__':
    game = Game()
    w = MainWindow(game)
    pyglet.app.run()

# TODO: all action through proxy object, wall, cant stand on wall.
