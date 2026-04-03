# 1. Use a lightweight Python image
FROM python:3.10-slim

# 2. Set the working directory
WORKDIR /app

# 3. Copy and install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. CRITICAL: Copy inference.py to the root (The grader needs this!)
COPY inference.py .

# 5. Copy your server files from the envs folder to the app root
COPY envs/server.py .
COPY envs/models.py .
COPY envs/moderator_config.json .

# 6. Expose the port (must match your README and server.py)
EXPOSE 8004

# 7. Start the server using Uvicorn (Better for FastAPI)
# Make sure server.py has an 'app' object inside it
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8004"]
