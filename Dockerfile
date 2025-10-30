# Dockerfile for production deployment
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY alioop-microservice-prototype/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY alioop-microservice-prototype/ .

# Create necessary directories
RUN mkdir -p storage/deliveries

# Expose port (Railway/Render will set PORT env var)
ENV PORT=8000
EXPOSE 8000

# Run the application
CMD uvicorn app.main:app --host 0.0.0.0 --port $PORT
