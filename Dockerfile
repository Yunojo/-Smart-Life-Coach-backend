FROM python:3.13.5

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# Cambia "main:app" si tu archivo principal no se llama main.py
# o si tu instancia de FastAPI no se llama "app"
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]