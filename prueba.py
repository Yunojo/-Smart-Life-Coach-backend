from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI,HTTPException, Request
from Esquemas import ChatPayload, CoachResponse
import asyncio
from datetime import datetime, timezone
import uuid
from fastapi.responses import StreamingResponse
import httpx
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

async def generar_respuesta(texto: str):
    # 1. En la v5, necesitamos generar un ID único para el mensaje
    msg_id = f"msg_{uuid.uuid4().hex}"
    
    # 2. Evento de inicio (Server-Sent Event format)
    yield f'data: {{"type":"text-start","id":"{msg_id}"}}\n\n'
    
    # 3. Eventos de escritura (delta) letra por letra o palabra por palabra
    palabras = texto.split(" ")
    for palabra in palabras:
        yield f'data: {{"type":"text-delta","id":"{msg_id}","delta":"{palabra} "}}\n\n'
        await asyncio.sleep(0.1)
        
    # 4. Evento de fin
    yield f'data: {{"type":"text-end","id":"{msg_id}"}}\n\n'

           
    

@app.post("/Chat")
async def recibir_mensaje(text:str):
            print(f"Mensaje recibido: {text}")
            url = "http://localhost:8001/chat"
            payload = ChatPayload(
                        id="123",
                        messages=[
                            {
                                "id": str(uuid.uuid4()),
                                "role": "user",
                                "parts": [
                                    {
                                        "type": "text",
                                        "text": text
                                    }
                                ]
                            }
                        ],
                        trigger="chat",
                        user_name="Jose",
                        age=22
                    )
            async with httpx.AsyncClient() as client:
                response = await client.post(url, json=payload.model_dump())
            if response.status_code != 200:
                raise HTTPException(status_code=500, detail="Error en API 2")
            coach = CoachResponse(**response.json())
            print(coach)


ahora = datetime.now(timezone.utc).isoformat()

# Generamos un ID maestro que actuará como el Padre
plan_maestro_id = str(uuid.uuid4()) 

mock_db = [
{
    "id": plan_maestro_id,
    "user_id": "usuario_demo",
    "parent_id": None,
    "title": "🏆 Dominar el Stack de IA",
    "description": "Aprender a conectar Next.js con FastAPI y Gemini",
    "status": "pending",
    "due_date": ahora,
    "created_at": ahora,
    "updated_at": ahora
},
{
    "id": str(uuid.uuid4()),
    "user_id": "usuario_demo",
    "parent_id": plan_maestro_id,
    "title": "Revisar arquitectura BFF",
    "description": "Comprender cómo Next.js protege las peticiones",
    "status": "completed", 
    "due_date": ahora,
    "created_at": ahora,
    "updated_at": ahora
},
{
    "id": str(uuid.uuid4()),
    "user_id": "usuario_demo",
    "parent_id": plan_maestro_id,
    "title": "Implementar filtrado de jerarquías",
    "description": "Verificar que el array.filter funcione en el Server Component",
    "status": "pending", 
    "due_date": ahora,
    "created_at": ahora,
    "updated_at": ahora
}
]

@app.get("/api/planes")
async def obtener_planes_mock(user_id: str = "usuario_demo"):
    # 2. Ahora el GET simplemente devuelve la variable global actual
    return mock_db

@app.patch("/api/planes/{item_id}")
async def actualizar_estado_tarea(item_id: str, request: Request):
    body = await request.json()
    nuevo_estado = body.get("status")
    
    # 3. Buscamos el item en nuestra "base de datos" global y lo modificamos
    for item in mock_db:
        if item["id"] == item_id:
            item["status"] = nuevo_estado
            print(f"✅ Python actualizó en memoria el item {item_id} a: {nuevo_estado}")
            return {"status": "success", "item_id": item_id, "new_status": nuevo_estado}
            
    # Si no lo encuentra
    return {"status": "error", "message": "Item no encontrado"}
