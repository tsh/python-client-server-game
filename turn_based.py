import random
import pyglet


class Primitive(object):
    def __init__(self):
        self.SIZE = 100

    def _draw_rect(self, x, y, width, height, color):
        image_pattern = pyglet.image.SolidColorImagePattern(color=color)
        image = image_pattern.create_image(width, height)
        image.blit(x, y)


class Map(Primitive):
    def __init__(self):
        super().__init__()
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


class Objects(Primitive):
    def __init__(self):
        super().__init__()
        self.map = [[0, 0, 0],
                    [0, 1, 0],
                    [0, 0, 0]]

    def draw(self):
        for i, row in enumerate(reversed(self.map)):
            for j, tile in enumerate(row):
                x = j * self.SIZE
                y = i * self.SIZE
                self.shrink_factor = 15
                size = self.SIZE - self.shrink_factor * 2
                if tile == 1:
                    self._draw_rect(x + self.shrink_factor , y + self.shrink_factor , size, size, (0, 255, 0, 0))



class Game(object):
    def __init__(self):
        self.map = Map()
        self.objects = Objects()

    def draw(self):
        self.map.draw()
        self.objects.draw()


window = pyglet.window.Window(width=800, height=600)
game = Game()

@window.event
def on_draw():
    window.clear()
    game.draw()

pyglet.app.run()
