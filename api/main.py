from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI,HTTPException
from Esquemas import ChatPayload
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

@app.post("/api/chat")
async def process_chat(payload: ChatPayload):
    session_id = payload.id
    trigger_action = payload.trigger
    user_messages = [msg for msg in payload.messages if msg.role == 'user']
    if not user_messages:
        raise HTTPException(status_code=400, detail="No hay mensajes del usuario para procesar.")

    ultimo_mensaje = user_messages[-1].parts[0].text

    # ---
    # tomar este historial estructurado y enviarlo aVictor 
    # ---

    print(f"Procesando sesión {session_id}. Acción: {trigger_action}")
    print(f"Último mensaje del usuario: {ultimo_mensaje}")

    return {
        "status": "success",
        "session_id": session_id,
        "processed_messages": len(payload.messages),
        "reply": "Mensaje recibido y validado correctamente por el backend."
    }