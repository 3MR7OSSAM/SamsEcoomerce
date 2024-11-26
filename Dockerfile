# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the application port
EXPOSE 5001

# Define the command to run the app
CMD ["python", "run.py"]