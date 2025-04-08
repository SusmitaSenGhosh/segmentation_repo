# Use the official Python base image
FROM python:3.11.11-slim
#FROM ultralytics/ultralytics:latest

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install -r fastapi
RUN pip install -r opencv-python
RUN pip install -r ultralytics

# Copy the application code to the working directory
COPY . .

# Expose the port on which the application will run
EXPOSE 8080

# Run the FastAPI application using uvicorn server
CMD ["uvicorn", "fastapi:app", "--host", "0.0.0.0", "--port", "8080"]
