import asyncio

import arcade
import websockets

# Size of the screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

def on_draw(delta_time):
    arcade.start_render()
    arcade.draw_rectangle_filled(0, 0,      # position
                                 50, 50,    # size
                                 arcade.color.ALIZARIN_CRIMSON)

async def hello():
    async with websockets.connect('ws://localhost:8765') as websocket:

        name = input("What's your name? ")
        await websocket.send(name)
        print("> {}".format(name))

        greeting = await websocket.recv()
        print("< {}".format(greeting))


def main():
    arcade.open_window("Rectangle", SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_background_color(arcade.color.WHITE)

    # Tell the computer to call the draw command at the specified interval.
    arcade.schedule(on_draw, 1 / 80)

    # Run the program
    arcade.run()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(hello())
    main()
