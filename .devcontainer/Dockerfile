FROM python:3.11-slim

WORKDIR /app

# Install Tkinter dependencies
RUN apt-get update && apt-get install -y python3-tk tk && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]