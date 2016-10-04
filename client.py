import asyncio
import tkinter as tk

import arcade
import websockets


# GRAPHICS
root = tk.Tk()
canvas = tk.Canvas(root, width=200, height=200, borderwidth=0, highlightthickness=0, bg="black")
canvas.grid()

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle = _create_circle

canvas.create_circle(100, 120, 50, fill="blue", outline="#DDD", width=4)
root.mainloop()


# NETWORK

async def hello():
    async with websockets.connect('ws://localhost:8765') as websocket:

        name = input("What's your name? ")
        await websocket.send(name)
        print("> {}".format(name))

        greeting = await websocket.recv()
        print("< {}".format(greeting))


# if __name__ == "__main__":
    # asyncio.get_event_loop().run_until_complete(hello())

