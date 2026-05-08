# -Smart-Life-Coach-backend
Backend for the repository Smart-Life-Coach

## Correr en entorno virtual con uv y uvicorn
```bash
uv venv .venv --python 3.13.5
```

```bash
source .venv/bin/activate
```

```bash
uv pip install -r requirements.txt
```

```bash
uvicorn main:app --port 8000 --reload
```

## Docker
Para montar la imagen de Docker estando en la carpeta frontend vamos a ejecutar estos dos comandos (obviamente debes tener Docker instalado y corriendo):

```bash
docker build -t fastapi-backend .
```

```bash
docker run -p 8000:8000 \
  --add-host host.docker.internal:host-gateway \
  -e SUPABASE_URL=http://host.docker.internal:54321 \
  fastbackend
```