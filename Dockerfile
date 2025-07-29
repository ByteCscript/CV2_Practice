# 1. Usa la imagen oficial de Python 3.10 slim
FROM python:3.10-slim

# 2. Actualiza e instala dependencias del sistema necesarias para OpenCV
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
  && rm -rf /var/lib/apt/lists/*

# 3. Crea y fija el directorio de trabajo
WORKDIR /app

# 4. Copia las dependencias y las instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copia el resto de tu código
COPY . .

# 6. Define el comando de arranque
CMD ["python", "main.py"]
