import asyncio
import tkinter as tk

# import arcade
# import websockets

from client_objs import BaseObject


# GRAPHICS

root = tk.Tk()
canvas = tk.Canvas(root, width=200, height=200, borderwidth=0, highlightthickness=0, bg="black")
canvas.grid()
BaseObject().render(canvas)
root.mainloop()


# NETWORK

# async def hello():
#     async with websockets.connect('ws://localhost:8765') as websocket:
# 
#         name = input("What's your name? ")
#         await websocket.send(name)
#         print("> {}".format(name))
# 
#         greeting = await websocket.recv()
#         print("< {}".format(greeting))


# if __name__ == "__main__":
    # asyncio.get_event_loop().run_until_complete(hello())

