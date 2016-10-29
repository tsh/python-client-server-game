import random
import pyglet


class Map(object):
    def __init__(self):
        self.SIZE = 100
        self.map = [[1, 0, 1],
                    [0, 1, 0],
                    [1, 0, 1]]

    def draw(self):
        for i, row in enumerate(reversed(self.map)):
            for j, tile in enumerate(row):
                x = j * self.SIZE
                y = i * self.SIZE
                if tile == 0:
                    clr = (255, 0, 0, 0)
                elif tile == 1:
                    clr = (0, 0, 255, 0)
                self._draw_rect(x, y, self.SIZE, self.SIZE, clr)

    def _draw_rect(self, x, y, width, height, color):
        image_pattern = pyglet.image.SolidColorImagePattern(color=color)
        image = image_pattern.create_image(width, height)
        image.blit(x, y)


class Game(object):
    def __init__(self):
        self.map = Map()

    def draw(self):
        self.map.draw()


window = pyglet.window.Window(width=800, height=600)
game = Game()

@window.event
def on_draw():
    window.clear()
    game.draw()

pyglet.app.run()
