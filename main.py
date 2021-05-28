from typing import Dict
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from json.decoder import JSONDecodeError

app = FastAPI()

class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[WebSocket] = {}

    async def connect(self, websocket: WebSocket, username: str = None):
        await websocket.accept()
        if username and username.lower() in self.active_connections:
            await websocket.send_text(f"Username {username} already in use. Use a different one")
            raise WebSocketDisconnect
        if username:
            self.active_connections[username.lower()] = websocket

    def disconnect(self, websocket: WebSocket, username: str = None):
        if username:
            del self.active_connections[username.lower()]

    async def send_personal_message(self, sender_websocket: WebSocket, message: str, partner: str):
        partner_name = partner.lower()
        if partner_name in self.active_connections:
            websocket = self.active_connections[partner_name]
            await websocket.send_text(message)
        else:
            await sender_websocket.send_text(f"Server: {partner} is not connected")

manager = ConnectionManager()

@app.websocket("/ws/{username}")
async def websocket_dm(websocket: WebSocket, username: str):
    try:
        await manager.connect(websocket, username)
        data = None
        try:
            while True:
                try:
                    data = await websocket.receive_json()
                except JSONDecodeError as jde:
                    await manager.send_personal_message(websocket, 'Error ocurred: Please define a partner(p) and message(m) in JSON format. Syntax: {"p": "partner_username", "m": "your message"}', username)
                    continue

                if "p" not in data or "m" not in data:
                    await manager.send_personal_message(websocket, 'Error ocurred: Please define a partner(p) and message(m) in JSON format. Syntax: {"p": "partner_username", "m": "your message"}', username)
                    continue
                message = data["m"]
                partner_name = data["p"]
                await manager.send_personal_message(websocket, f"{username}: {message}", partner_name)
        except WebSocketDisconnect:
            if data:
                partner_name = data.pop("p")
                manager.disconnect(websocket, username)
                await manager.send_personal_message(websocket, f"{username} left the chat and is no longer available", partner_name)
    except WebSocketDisconnect:
        pass
