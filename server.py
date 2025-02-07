import asyncio
import websockets

PORT = 8080
HOST = "0.0.0.0"  # Listen on all network interfaces

connected_clients = set()

async def handle_client(websocket, path):
    addr = websocket.remote_address
    print(f"New connection from {addr}")
    
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            print(f"Received: {message} from {addr}")
            response = "Message received"
            await websocket.send(response)
    except websockets.exceptions.ConnectionClosed:
        print(f"Client {addr} disconnected")
    finally:
        connected_clients.remove(websocket)

async def start_server():
    print("WebSocket server is starting...")
    server = await websockets.serve(handle_client, HOST, PORT)
    await server.wait_closed()

print("WebSocket server is running...")
asyncio.run(start_server())

