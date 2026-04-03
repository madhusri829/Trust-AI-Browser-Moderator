FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY inference.py .
COPY envs/server.py .
COPY envs/models.py .
# This MUST match your README.md
EXPOSE 8004
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8004"]
