import asyncio
import json
import websockets

from messages import Message

async def start():
    async with websockets.connect('ws://localhost:8765/ws') as websocket:
        await websocket.send(Message.GET_MAP)

        r = await websocket.recv()
        rsp = json.loads(r)
        print(rsp, type(rsp))

asyncio.get_event_loop().run_until_complete(start())