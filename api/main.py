from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI, Request

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.post("/Chat")
async def recibir_mensaje(request:Request):
    cuerpo = await request.json()
    mensajes= cuerpo.get("menssages",[])
    if mensajes:
        ultimo_mensaje=mensajes[-1]
        part=ultimo_mensaje.get("parts",[])
        if part:
            cont=part[0].get("text","")
            print(f"Mensaje recibido: {cont}")
            return "Mensaje recibido en FastApi"

