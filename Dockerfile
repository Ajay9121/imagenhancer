FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu22.04

WORKDIR /app

RUN apt update && apt install -y \
    git ffmpeg python3 python3-pip

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:create_app", "--host", "0.0.0.0", "--port", "8000"]
