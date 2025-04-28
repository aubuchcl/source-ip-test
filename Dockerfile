FROM python:3.11-alpine

# Install any necessary system dependencies (if needed)
RUN apk add --no-cache bash

# Set working directory
WORKDIR /app

# Copy server code
COPY server.py .

# Expose port 8080
EXPOSE 8080

# Set environment variables (optional for better behavior)
ENV PYTHONUNBUFFERED=1

# Start the server
CMD ["python", "server.py"]
