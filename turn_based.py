import pyglet


class Map(object):
    def __init__(self):
        self.SIZE = 100
        self.map = [[1, 0, 1],
                    [0, 1, 0],
                    [1, 0, 1]]

    def draw(self):
        for i, row in enumerate(self.map):
            for j, tile in enumerate(row):
                x = j * self.SIZE
                y = i * self.SIZE
                if tile == 1:
                    color = (255, 0, 0, 0)
                else:
                    color = (0, 0, 255, 0)
                self.draw_rect(x, y, x+self.SIZE, y+self.SIZE, color)

    def draw_rect(self, x, y, width, height, color):
        width = int(round(width))
        height = int(round(height))
        image_pattern = pyglet.image.SolidColorImagePattern(color=color)
        image = image_pattern.create_image(width, height)
        image.blit(x, y)



window = pyglet.window.Window()
map = Map()

@window.event
def on_draw():
    window.clear()
    map.draw()

pyglet.app.run()
