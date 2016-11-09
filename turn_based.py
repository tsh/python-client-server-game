import math
import pyglet
from pyglet.window import mouse

from client_objs import GameFieldManager, Map, Drawable


class Nexus(object):
    """ Implements connection local or through network """

    def get_map(self):
        return Map()


class Game(object):
    def __init__(self):
        self.nexus = Nexus()
        map = self.nexus.get_map()
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
