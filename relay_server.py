from fastapi import FastAPI, WebSocket
import uvicorn

app = FastAPI()
clients = []

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    print("Client connecté !")
    try:
        while True:
            data = await websocket.receive_text()
            print("Reçu :", data)
            for client in clients:
                if client != websocket:
                    await client.send_text(data)
    except:
        print("Client déconnecté")
        clients.remove(websocket)

if __name__ == "__main__":
    uvicorn.run("relay_server:app", host="0.0.0.0", port=10000)
