import asyncio
import tkinter as tk

# import arcade
# import websockets

from old.client_objs import BaseObject

LOOP_DELAY = 0.05  # ms

# GRAPHICS

root = tk.Tk()
canvas = tk.Canvas(root, width=800, height=600, borderwidth=0, highlightthickness=0, bg="black")
canvas.grid()
circle = BaseObject()

@asyncio.coroutine
def run_tk(root):
    '''
    Run a tkinter app in an asyncio event loop.
    '''
    try:
        while True:
            root.update()
            canvas.delete("all")
            circle.render(canvas)
            yield from asyncio.sleep(LOOP_DELAY)
    except tk.TclError as e:
        if "application has been destroyed" not in e.args[0]:
            raise


@asyncio.coroutine
def logic():
    while True:
        print('test')
        circle.update()
        yield from asyncio.sleep(LOOP_DELAY)

def main():
    asyncio.ensure_future(logic())
    yield from run_tk(root)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())

