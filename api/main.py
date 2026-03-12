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
    mensajes= cuerpo.get("mensajes",[])
    if mensajes:
        ultimo_mensaje=mensajes[-1]["content"]
        print(f"Mensaje recibido: {ultimo_mensaje}")

        return "Mensaje recibido en FastApi"
