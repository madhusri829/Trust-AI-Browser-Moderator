FROM python:3.10-slim
WORKDIR /app

# Copy requirements from root
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy inference.py from root
COPY inference.py .

# Copy server files from the envs folder
COPY envs/server.py .
COPY envs/models.py .

EXPOSE 8004
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8004"]
