# Imagen base de Python 3.9 versión ligera
FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=demo.settings \
    PORT=8000

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Crea un usuario no-root por seguridad
RUN adduser --disabled-password --no-create-home django

# Instala dependencias del sistema necesarias
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copia el archivo de requisitos primero (mejor uso de caché)
COPY requirements.txt .

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código de la aplicación
COPY . .

# Asigna los archivos al usuario django
RUN chown -R django:django /app

# Cambia al usuario no-root
USER django

# Expone el puerto de la aplicación
EXPOSE $PORT

# Verifica la salud de la aplicación
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:$PORT/health/ || exit 1

# Comando para iniciar la aplicación
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:${PORT}"]
