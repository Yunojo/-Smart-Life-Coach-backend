# -Smart-Life-Coach-backend

Backend for the repository Smart-Life-Coach

## Intrucciones para obtener las variables de .env

Entrar en el repositorio Smart-Life-Coach-DB y con el comando:

```bash
npx supabase status
```

Obtener la SUPABASE_JWT_SECRET y ponerla en el .env

## .env

1. Copiar el archivo .env.template en un .env
2. Las variables de entorno requeridas en .env son generadas con npx supabase start (o status si ya hiciste la DB):
   SUPABASE*URL=http://127.0.0.1:54321 # Suele ser esta direccion
   SUPABASE_SERVICE_ROLE_KEY=sb_secret*...
   SUPABASE_JWT_SECRET=super-secret-jwt-token-with-at-least-32-characters-long

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

Para montar la imagen de Docker estando en la carpeta backend/ vamos a ejecutar estos dos comandos (obviamente debes tener Docker instalado y corriendo):

```Bash
docker docker build -t fast-backend .
```

```Bash
docker run -p 8000:8000\
  --name mi-server-fastapi \
  --add-host host.docker.internal:host-gateway \
  -e SUPABASE_URL=http://host.docker.internal:54321\
  fast-backend
```

Abrir http://localhost:8000/docs en tu navegador para ver el status de tu api
