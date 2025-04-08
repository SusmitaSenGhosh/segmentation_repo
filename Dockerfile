# Use the official Python base image
FROM python:3.11.11-slim
#FROM ultralytics/ultralytics:latest

# Set the working directory inside the container
WORKDIR /

# Install the Python dependencies
RUN pip install fastapi uvicorn opencv-python
RUN pip install ultralytics --extra-index-url https://download.pytorch.org/whl/cpu --no-cache-dir
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

# Copy the application code to the working directory
COPY . .

# Expose the port on which the application will run
EXPOSE 8000

# Run the FastAPI application using uvicorn server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


