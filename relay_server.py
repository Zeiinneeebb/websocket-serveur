import asyncio
import websockets

PORT = 7890

clients = set()

async def echo(websocket):
    clients.add(websocket)
    print("Client connected")
    try:
        async for message in websocket:
            print("Received:", message)
            for client in clients:
                if client != websocket:
                    await client.send(message)
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")
    finally:
        clients.remove(websocket)

async def main():
    async with websockets.serve(echo, "0.0.0.0", PORT):
        print(f"WebSocket server started on port {PORT}")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
