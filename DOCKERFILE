# Use a lightweight Python image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the environment folder contents to the app directory
COPY envs/server.py .
COPY envs/models.py .
COPY envs/moderator_config.json .

# Expose the specific port used in server.py
EXPOSE 8004

# Command to run the server
CMD ["python", "server.py"]