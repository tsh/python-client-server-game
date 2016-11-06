import math
import pyglet
from pyglet.window import mouse


class NotInGameField(Exception):
    pass


class Position(object):
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
        return tx, ty

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

    def draw(self):
        for pos, tile in self.map.items():
            tile.draw(pos)

    def clicked(self, x, y):
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


class Objects(object):
    def __init__(self):
        super().__init__()
        self.default_value = 0
        self.objs = {
            Position(0, 12): 0,     Position(1, 12): 0,         Position(2, 12): 0,     Position(3, 12): 0,     Position(4, 12): 0,     Position(5, 12): 0,     Position(6, 12): 0,     Position(7, 12): 0,     Position(8, 12): 0,     Position(9, 12): 0,     Position(10, 12): 0,        Position(11, 12): 0,    Position(12, 12): 0,
            Position(0, 11): 0,     Position(1, 11): 0,         Position(2, 11): 0,     Position(3, 11): 0,     Position(4, 11): 0,     Position(5, 11): 0,     Position(6, 11): 0,     Position(7, 11): 0,     Position(8, 11): 0,     Position(9, 11): 0,     Position(10, 11): 0,        Position(11, 11): 0,    Position(12, 11): 0,
            Position(0, 10): 0,     Position(1, 10): 0,         Position(2, 10): 0,     Position(3, 10): 0,     Position(4, 10): 0,     Position(5, 10): 0,     Position(6, 10): 0,     Position(7, 10): 0,     Position(8, 10): 0,     Position(9, 10): 0,     Position(10, 10): 0,        Position(11, 10): 0,    Position(12, 10): 0,
            Position(0, 9): 0,      Position(1, 9): 0,          Position(2, 9): 0,      Position(3, 9): 0,      Position(4, 9): 0,      Position(5, 9): 0,      Position(6, 9): Enemy(),      Position(7, 9): 0,      Position(8, 9): 0,      Position(9, 9): 0,      Position(10, 9): 0,   Position(11, 9): 0,     Position(12, 9): 0,
            Position(0, 8): 0,      Position(1, 8): 0,          Position(2, 8): 0,      Position(3, 8): 0,      Position(4, 8): 0,      Position(5, 8): 0,      Position(6, 8): 0,      Position(7, 8): 0,      Position(8, 8): 0,      Position(9, 8): 0,      Position(10, 8): 0,         Position(11, 8): 0,     Position(12, 8): 0,
            Position(0, 7): 0,      Position(1, 7): 0,          Position(2, 7): 0,      Position(3, 7): 0,      Position(4, 7): 0,      Position(5, 7): 0,      Position(6, 7): 0,      Position(7, 7): 0,      Position(8, 7): 0,      Position(9, 7): 0,      Position(10, 7): 0,         Position(11, 7): 0,     Position(12, 7): 0,
            Position(0, 6): 0,      Position(1, 6): 0,          Position(2, 6): 0,      Position(3, 6): 0,      Position(4, 6): 0,      Position(5, 6): 0,      Position(6, 6): 0,      Position(7, 6): 0,      Position(8, 6): 0,      Position(9, 6): 0,      Position(10, 6): 0,         Position(11, 6): 0,     Position(12, 6): 0,
            Position(0, 5): 0,      Position(1, 5): 0,          Position(2, 5): 0,      Position(3, 5): 0,      Position(4, 5): 0,      Position(5, 5): 0,      Position(6, 5): 0,      Position(7, 5): 0,      Position(8, 5): 0,      Position(9, 5): 0,      Position(10, 5): 0,         Position(11, 5): 0,     Position(12, 5): 0,
            Position(0, 4): 0,      Position(1, 4): 0,          Position(2, 4): 0,      Position(3, 4): 0,      Position(4, 4): 0,      Position(5, 4): 0,      Position(6, 4): 0,      Position(7, 4): 0,      Position(8, 4): 0,      Position(9, 4): 0,      Position(10, 4): 0,         Position(11, 4): 0,     Position(12, 4): 0,
            Position(0, 3): 0,      Position(1, 3): 0,          Position(2, 3): 0,      Position(3, 3): 0,      Position(4, 3): 0,      Position(5, 3): 0,      Position(6, 3): 0,      Position(7, 3): 0,      Position(8, 3): 0,      Position(9, 3): 0,      Position(10, 3): 0,         Position(11, 3): 0,     Position(12, 3): 0,
            Position(0, 2): 0,      Position(1, 2): 0,          Position(2, 2): 0,      Position(3, 2): 0,      Position(4, 2): 0,      Position(5, 2): 0,      Position(6, 2): 0,      Position(7, 2): 0,      Position(8, 2): 0,      Position(9, 2): 0,      Position(10, 2): 0,         Position(11, 2): 0,     Position(12, 2): 0,
            Position(0, 1): 0,      Position(1, 1): Character(),Position(2, 1): 0,      Position(3, 1): 0,      Position(4, 1): 0,      Position(5, 1): 0,      Position(6, 1): 0,      Position(7, 1): 0,      Position(8, 1): 0,      Position(9, 1): 0,      Position(10, 1): 0,         Position(11, 1): 0,     Position(12, 1): 0,
            Position(0, 0): 0,      Position(1, 0): 0,          Position(2, 0): 0,      Position(3, 0): 0,      Position(4, 0): 0,      Position(5, 0): 0,      Position(6, 0): 0,      Position(7, 0): 0,      Position(8, 0): 0,      Position(9, 0): 0,      Position(10, 0): 0,         Position(11, 0): 1,     Position(12, 0): 0,
        }
        self.FIELD_SIZE = math.sqrt(len(self.objs)) - 1

    def draw(self):
        for pos, tile in self.objs.items():
            if not isinstance(tile, int):
                tile.draw(pos)

    def move(self, frm: Position, to: Position):
        tmp = self.objs[frm]
        self.objs[frm] = self.default_value
        self.objs[to] = tmp

    def _get_selected_object_position(self):
        for pos, tile in self.objs.items():
            try:
                if tile.is_selected:
                    return pos
            except AttributeError:
                pass
        return None

    def clicked(self, x, y):
        pos = Position(x, y)
        try:
            self.check_boundaries(pos)
        except NotInGameField:
            return
        clicked = self.objs[pos]
        if not isinstance(clicked, int):
            # select clicked object
            clicked.toggle_selection()
        else:
            # if we have selected object, move him
            frm = self._get_selected_object_position()
            if frm:
                self.move(frm, pos)

    def check_boundaries(self, pos: Position):
        if not (pos.x <= self.FIELD_SIZE and pos.y <= self.FIELD_SIZE):
            print('Out of boundaries: ', pos.x, pos.y)
            raise NotInGameField

class Game(object):
    def __init__(self):
        self.map = Map()
        self.objects = Objects()

    def draw(self):
        self.map.draw()
        self.objects.draw()

    def on_left_click(self, x, y):
        # Transform screen coordinates into tile
        tx, ty = Drawable.get_clicked_tile_position(x, y)
        self.map.clicked(tx, ty)
        self.objects.clicked(tx, ty)


window = pyglet.window.Window(width=1024, height=768)
game = Game()

@window.event
def on_draw():
    window.clear()
    game.draw()

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        game.on_left_click(x, y)

pyglet.app.run()

# TODO: all action through proxy object, wall, cant stand on wall.
# MAP: either put map as global object, or create 3rd map object in Objects that holds Logic data.
