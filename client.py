import asyncio
import tkinter as tk

# import arcade
# import websockets

from client_objs import BaseObject


# GRAPHICS

root = tk.Tk()
canvas = tk.Canvas(root, width=800, height=600, borderwidth=0, highlightthickness=0, bg="black")
canvas.grid()
BaseObject().render(canvas)

@asyncio.coroutine
def run_tk(root, interval=0.05):
    '''
    Run a tkinter app in an asyncio event loop.
    '''
    try:
        while True:
            root.update()
            yield from asyncio.sleep(interval)
    except tk.TclError as e:
        if "application has been destroyed" not in e.args[0]:
            raise


def main():
    yield from run_tk(root)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())

