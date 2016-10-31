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
    def __init__(self):
        self.SIZE = 100

    def _draw_rect(self, x, y, width, height, color):
        image_pattern = pyglet.image.SolidColorImagePattern(color=color)
        image = image_pattern.create_image(width, height)
        image.blit(x, y)

    def get_clicked_tile_position(self, x, y):
        tx = math.floor(x / 100)
        ty = math.floor(y / 100)
        return tx, ty



class Map(Primitive):
    def __init__(self):
        # TODO: 64x64
        super().__init__()
        self.map = {Position(0, 0): 0, Position(1, 0): 1, Position(2, 0): 0,
                    Position(0, 1): 1, Position(1, 1): 0, Position(2, 1): 1,
                    Position(0, 2): 0, Position(1, 2): 1, Position(2, 2): 0}

    def draw(self):
        for pos, tile in self.map.items():
                x = pos.x * self.SIZE
                y = pos.y * self.SIZE
                if tile == 0:
                    clr = (255, 0, 0, 0)
                elif tile == 1:
                    clr = (0, 0, 255, 0)
                self._draw_rect(x, y, self.SIZE, self.SIZE, clr)

    def clicked(self, x, y):
        pass


class Character(Primitive):
    def __init__(self):
        super().__init__()
        self.is_selected = False

    def toggle_selection(self):
        self.is_selected = not self.is_selected

    def draw(self, x, y, size, shrink_factor):
        if self.is_selected:
            self._draw_rect(x + shrink_factor , y + shrink_factor , size, size, (0, 255, 0, 0))
            self._draw_rect(x + shrink_factor + 20 , y + shrink_factor + 20 , size - 40 , size - 40, (128, 0, 128, 0))
        else:
            self._draw_rect(x + shrink_factor , y + shrink_factor , size, size, (0, 255, 0, 0))


class Objects(Primitive):
    def __init__(self):
        super().__init__()
        self.shrink_factor = 15
        self.default_value = 0
        self.map = {Position(0, 0): 0, Position(1, 0): 1,           Position(2, 0): 0,
                    Position(0, 1): 1, Position(1, 1): Character(), Position(2, 1): 1,
                    Position(0, 2): 0, Position(1, 2): 1,           Position(2, 2): 0}

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
            if not isinstance(tile, int) and tile.is_selected:
                return pos
        return None

    def clicked(self, x, y):
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


window = pyglet.window.Window(width=800, height=600)
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

# TODO: movement, game field boundries, map size, player object, enemy object, wall, cant move on wall.
