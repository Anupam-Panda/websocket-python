import asyncio
import websockets

async def hello(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")

    #input_length = len(name)
    #reversed_name = str[input_length::-1]
    #print ("reversed name {reversed_name}")
    reversed_name = ''.join(reversed(name))
    greeting = f"Hello {name}! Your name in reverse is {reversed_name}!!"

    await websocket.send(greeting)
    print(f"> {greeting}")

start_server = websockets.serve(hello, "127.0.0.1", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
