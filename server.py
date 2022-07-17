import asyncio
import websockets

connections = set()

async def handler(websocket, path):
  connections.add(websocket)
  print("client connected")
  try:
    while True: # keeps connection alive
      message = await websocket.recv()
      print(f"[server.py] {message}")
      for connection in connections:
        await connection.send(message)
  except websockets.exceptions.ConnectionClosed as e:
    print("client disconnected")
  finally:
    print("disconnected client")
    connections.remove(websocket)

server = websockets.serve(handler, '127.0.0.1', 8001)
asyncio.get_event_loop().run_until_complete(server)
asyncio.get_event_loop().run_forever()
