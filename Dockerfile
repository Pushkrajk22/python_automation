# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install required Python libraries from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Define environment variable to avoid output buffering in Python
ENV PYTHONUNBUFFERED=1

# Run your Python script
CMD ["python", "resolve_sandbox_access.py"]
