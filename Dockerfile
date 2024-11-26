FROM python:3.9-slim

# Install necessary system dependencies for ODBC
RUN apt-get update && apt-get install -y \
    unixodbc-dev \
    gcc \
    g++ \
    make \
    && rm -rf /var/lib/apt/lists/*

# Install the Microsoft ODBC Driver for SQL Server
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/9/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && apt-get install -y msodbcsql17

# Install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Install pyodbc
RUN pip install pyodbc

# Set the working directory
WORKDIR /app

# Copy the app files
COPY . .

# Expose the port for your application
EXPOSE 5001

# Command to run the app
CMD ["python", "app.py"]
