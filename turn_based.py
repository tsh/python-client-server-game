import math
import pyglet
from pyglet.window import mouse


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


class Primitive(object):
    SIZE = 48

    def _draw_rect(self, x, y, width, height, color):
        image_pattern = pyglet.image.SolidColorImagePattern(color=color)
        image = image_pattern.create_image(width, height)
        image.blit(x, y)

    def get_clicked_tile_position(self, x, y):
        tx = math.floor(x / self.SIZE)
        ty = math.floor(y / self.SIZE)
        return tx, ty



class Map(Primitive):
    def __init__(self):
        super().__init__()
        self.map = {
            Position(0, 12): 0,     Position(1, 12): 1,         Position(2, 12): 0,     Position(3, 12): 0,     Position(4, 12): 0,     Position(5, 12): 0,     Position(6, 12): 0,     Position(7, 12): 0,     Position(8, 12): 0,     Position(9, 12): 0,     Position(10, 12): 0,        Position(11, 12): 0,
            Position(0, 11): 1,     Position(1, 11): 0,         Position(2, 11): 1,     Position(3, 11): 0,     Position(4, 11): 0,     Position(5, 11): 0,     Position(6, 11): 0,     Position(7, 11): 0,     Position(8, 11): 0,     Position(9, 11): 0,     Position(10, 11): 0,        Position(11, 11): 0,
            Position(0, 10): 0,     Position(1, 10): 1,         Position(2, 10): 0,     Position(3, 10): 0,     Position(4, 10): 0,     Position(5, 10): 0,     Position(6, 10): 0,     Position(7, 10): 0,     Position(8, 10): 0,     Position(9, 10): 0,     Position(10, 10): 0,        Position(11, 10): 0,
            Position(0, 9): 0,      Position(1, 9): 0,          Position(2, 9): 0,      Position(3, 9): 0,      Position(4, 9): 0,      Position(5, 9): 0,      Position(6, 9): 0,      Position(7, 9): 0,      Position(8, 9): 0,      Position(9, 9): 0,      Position(10, 9): 0,         Position(11, 9): 0,
            Position(0, 8): 0,      Position(1, 8): 0,          Position(2, 8): 0,      Position(3, 8): 0,      Position(4, 8): 0,      Position(5, 8): 0,      Position(6, 8): 0,      Position(7, 8): 0,      Position(8, 8): 0,      Position(9, 8): 0,      Position(10, 8): 0,         Position(11, 8): 0,
            Position(0, 7): 0,      Position(1, 7): 0,          Position(2, 7): 0,      Position(3, 7): 0,      Position(4, 7): 0,      Position(5, 7): 0,      Position(6, 7): 0,      Position(7, 7): 0,      Position(8, 7): 0,      Position(9, 7): 0,      Position(10, 7): 0,         Position(11, 7): 0,
            Position(0, 6): 0,      Position(1, 6): 0,          Position(2, 6): 0,      Position(3, 6): 0,      Position(4, 6): 0,      Position(5, 6): 0,      Position(6, 6): 0,      Position(7, 6): 0,      Position(8, 6): 0,      Position(9, 6): 0,      Position(10, 6): 0,         Position(11, 6): 0,
            Position(0, 5): 0,      Position(1, 5): 0,          Position(2, 5): 0,      Position(3, 5): 0,      Position(4, 5): 0,      Position(5, 5): 0,      Position(6, 5): 0,      Position(7, 5): 0,      Position(8, 5): 0,      Position(9, 5): 0,      Position(10, 5): 0,         Position(11, 5): 0,
            Position(0, 4): 0,      Position(1, 4): 0,          Position(2, 4): 0,      Position(3, 4): 0,      Position(4, 4): 0,      Position(5, 4): 0,      Position(6, 4): 0,      Position(7, 4): 0,      Position(8, 4): 0,      Position(9, 4): 0,      Position(10, 4): 0,         Position(11, 4): 0,
            Position(0, 3): 0,      Position(1, 3): 0,          Position(2, 3): 0,      Position(3, 3): 0,      Position(4, 3): 0,      Position(5, 3): 0,      Position(6, 3): 0,      Position(7, 3): 0,      Position(8, 3): 0,      Position(9, 3): 0,      Position(10, 3): 0,         Position(11, 3): 0,
            Position(0, 2): 1,      Position(1, 2): 1,          Position(2, 2): 1,      Position(3, 2): 0,      Position(4, 2): 0,      Position(5, 2): 0,      Position(6, 2): 0,      Position(7, 2): 0,      Position(8, 2): 0,      Position(9, 2): 0,      Position(10, 2): 0,         Position(11, 2): 0,
            Position(0, 1): 1,      Position(1, 1): 0,          Position(2, 1): 1,      Position(3, 1): 0,      Position(4, 1): 0,      Position(5, 1): 0,      Position(6, 1): 0,      Position(7, 1): 0,      Position(8, 1): 0,      Position(9, 1): 0,      Position(10, 1): 0,         Position(11, 1): 0,
            Position(0, 0): 1,      Position(1, 0): 1,          Position(2, 0): 1,      Position(3, 0): 0,      Position(4, 0): 0,      Position(5, 0): 0,      Position(6, 0): 0,      Position(7, 0): 0,      Position(8, 0): 0,      Position(9, 0): 0,      Position(10, 0): 0,         Position(11, 0): 1
        }

    def draw(self):
        for pos, tile in self.map.items():
                x = pos.x * self.SIZE
                y = pos.y * self.SIZE
                if tile == 0:
                    clr = (211, 211, 211, 0)
                elif tile == 1:
                    clr = (0, 0, 255, 0)
                self._draw_rect(x, y, self.SIZE, self.SIZE, clr)

    def clicked(self, x, y):
        pass


class Character(Primitive):
    def __init__(self):
        super().__init__()
        self.is_selected = False
        self.color = (0, 255, 0, 0)
        self.selection_color = (128, 0, 128, 0)

    def toggle_selection(self):
        self.is_selected = not self.is_selected

    def draw(self, x, y, size, shrink_factor):
        if self.is_selected:
            self._draw_rect(x + shrink_factor , y + shrink_factor , size, size, self.color)
            self._draw_rect(x + shrink_factor + int(Primitive.SIZE*0.2) , y + shrink_factor + int(Primitive.SIZE*0.2) ,
                            size - int(Primitive.SIZE*0.4) , size - int(Primitive.SIZE*0.4),
                            self.selection_color)
        else:
            self._draw_rect(x + shrink_factor , y + shrink_factor , size, size, (0, 255, 0, 0))


class Enemy(Primitive):
    def __init__(self):
        self.color = (255, 0, 0, 0)

    def toggle_selection(self):
        pass

    def draw(self, x, y, size, shrink_factor):
        self._draw_rect(x + shrink_factor , y + shrink_factor , size, size, self.color)


class Objects(Primitive):
    def __init__(self):
        super().__init__()
        self.shrink_factor = 5
        self.default_value = 0
        self.map = {
            Position(0, 12): 0,     Position(1, 12): 0,         Position(2, 12): 0,     Position(3, 12): 0,     Position(4, 12): 0,     Position(5, 12): 0,     Position(6, 12): 0,     Position(7, 12): 0,     Position(8, 12): 0,     Position(9, 12): 0,     Position(10, 12): 0,        Position(11, 12): 0,
            Position(0, 11): 0,     Position(1, 11): 0,         Position(2, 11): 0,     Position(3, 11): 0,     Position(4, 11): 0,     Position(5, 11): 0,     Position(6, 11): 0,     Position(7, 11): 0,     Position(8, 11): 0,     Position(9, 11): 0,     Position(10, 11): 0,        Position(11, 11): 0,
            Position(0, 10): 0,     Position(1, 10): 0,         Position(2, 10): 0,     Position(3, 10): 0,     Position(4, 10): 0,     Position(5, 10): 0,     Position(6, 10): 0,     Position(7, 10): 0,     Position(8, 10): 0,     Position(9, 10): 0,     Position(10, 10): 0,        Position(11, 10): 0,
            Position(0, 9): 0,      Position(1, 9): 0,          Position(2, 9): 0,      Position(3, 9): 0,      Position(4, 9): 0,      Position(5, 9): 0,      Position(6, 9): Enemy(),      Position(7, 9): 0,      Position(8, 9): 0,      Position(9, 9): 0,      Position(10, 9): 0,         Position(11, 9): 0,
            Position(0, 8): 0,      Position(1, 8): 0,          Position(2, 8): 0,      Position(3, 8): 0,      Position(4, 8): 0,      Position(5, 8): 0,      Position(6, 8): 0,      Position(7, 8): 0,      Position(8, 8): 0,      Position(9, 8): 0,      Position(10, 8): 0,         Position(11, 8): 0,
            Position(0, 7): 0,      Position(1, 7): 0,          Position(2, 7): 0,      Position(3, 7): 0,      Position(4, 7): 0,      Position(5, 7): 0,      Position(6, 7): 0,      Position(7, 7): 0,      Position(8, 7): 0,      Position(9, 7): 0,      Position(10, 7): 0,         Position(11, 7): 0,
            Position(0, 6): 0,      Position(1, 6): 0,          Position(2, 6): 0,      Position(3, 6): 0,      Position(4, 6): 0,      Position(5, 6): 0,      Position(6, 6): 0,      Position(7, 6): 0,      Position(8, 6): 0,      Position(9, 6): 0,      Position(10, 6): 0,         Position(11, 6): 0,
            Position(0, 5): 0,      Position(1, 5): 0,          Position(2, 5): 0,      Position(3, 5): 0,      Position(4, 5): 0,      Position(5, 5): 0,      Position(6, 5): 0,      Position(7, 5): 0,      Position(8, 5): 0,      Position(9, 5): 0,      Position(10, 5): 0,         Position(11, 5): 0,
            Position(0, 4): 0,      Position(1, 4): 0,          Position(2, 4): 0,      Position(3, 4): 0,      Position(4, 4): 0,      Position(5, 4): 0,      Position(6, 4): 0,      Position(7, 4): 0,      Position(8, 4): 0,      Position(9, 4): 0,      Position(10, 4): 0,         Position(11, 4): 0,
            Position(0, 3): 0,      Position(1, 3): 0,          Position(2, 3): 0,      Position(3, 3): 0,      Position(4, 3): 0,      Position(5, 3): 0,      Position(6, 3): 0,      Position(7, 3): 0,      Position(8, 3): 0,      Position(9, 3): 0,      Position(10, 3): 0,         Position(11, 3): 0,
            Position(0, 2): 0,      Position(1, 2): 0,          Position(2, 2): 0,      Position(3, 2): 0,      Position(4, 2): 0,      Position(5, 2): 0,      Position(6, 2): 0,      Position(7, 2): 0,      Position(8, 2): 0,      Position(9, 2): 0,      Position(10, 2): 0,         Position(11, 2): 0,
            Position(0, 1): 0,      Position(1, 1): Character(),Position(2, 1): 0,      Position(3, 1): 0,      Position(4, 1): 0,      Position(5, 1): 0,      Position(6, 1): 0,      Position(7, 1): 0,      Position(8, 1): 0,      Position(9, 1): 0,      Position(10, 1): 0,         Position(11, 1): 0,
            Position(0, 0): 0,      Position(1, 0): 0,          Position(2, 0): 0,      Position(3, 0): 0,      Position(4, 0): 0,      Position(5, 0): 0,      Position(6, 0): 0,      Position(7, 0): 0,      Position(8, 0): 0,      Position(9, 0): 0,      Position(10, 0): 0,         Position(11, 0): 1
        }
        self.FIELD_SIZE = math.sqrt(len(self.map)) - 1

    def draw(self):
        for pos, tile in self.map.items():
            x = pos.x * self.SIZE
            y = pos.y * self.SIZE
            size = self.SIZE - self.shrink_factor * 2
            if not isinstance(tile, int):
                tile.draw(x, y, size, self.shrink_factor)

    def move(self, frm: Position, to: Position):
        tmp = self.map[frm]
        self.map[frm] = self.default_value
        self.map[to] = tmp

    def _get_selected_object_position(self):
        for pos, tile in self.map.items():
            try:
                if tile.is_selected:
                    return pos
            except AttributeError:
                pass
        return None

    def clicked(self, x, y):
        if not (x <= self.FIELD_SIZE and y <= self.FIELD_SIZE):
            print('Out of boundaries: ', x, y)
            return
        pos = Position(x, y)
        clicked = self.map[pos]
        if not isinstance(clicked, int):
            # select clicked object
            clicked.toggle_selection()
        else:
            # if we have selected object, move him
            frm = self._get_selected_object_position()
            if frm:
                self.move(frm, pos)


class Game(object):
    def __init__(self):
        self.map = Map()
        self.objects = Objects()

    def draw(self):
        self.map.draw()
        self.objects.draw()

    def on_left_click(self, x, y):
        # Transform screen coordinates into tile
        tx, ty = self.objects.get_clicked_tile_position(x, y)
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

# TODO: fix boundary bag, movement action through proxy object, wall, cant stand on wall.
# MAP: either put map as global object, or create 3rd map object in Objects that holds Logic data.
