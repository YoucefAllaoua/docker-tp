# Use python:3.9-slim as your base image
FROM python:3.9-slim

# Create a working directory /app in the container
WORKDIR /app

# Copy the api source code to /app in the container
COPY . /app  
# Install the requirements.txt in the container
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 in the container
EXPOSE 5000

# Execute the following command when the container starts
CMD ["python", "app.py"]
