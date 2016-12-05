import asyncio
import json

import pyglet
from pyglet.window import mouse
import websockets

from messages import Message


# class Map(object):
#     def __init__(self, mp):
#         self.map = mp
#
#     def draw(self):
#         for i, row in enumerate(self.map):
#             for j, el in self.enumerate(row):
#                 if el == 1:
#                     self.draw()
#
#     def _draw_rect(self, x, y, width, height, color):
#         return
#         image_pattern = pyglet.image.SolidColorImagePattern(color=color)
#         image = image_pattern.create_image(width, height)
#         image.blit(x, y)




async def network(future):
    async with websockets.connect('ws://localhost:8765/ws') as websocket:
        print('connected')
        await websocket.send(Message.GET_MAP)
        r = await websocket.recv()
        rsp = json.loads(r)
        future.set_result(rsp)



class MainWindow(pyglet.window.Window):
    def __init__(self):
        super().__init__(width=1024, height=768)
        self.loop = asyncio.get_event_loop()
        future = asyncio.Future()
        asyncio.ensure_future(network(future))
        self.loop.run_until_complete(future)
        print(future.result())
        self.loop.close()


    def on_draw(self):
        self.clear()


    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            pass

w = MainWindow()
pyglet.app.run()