FROM python:3.9-slim

# Create working folder and install dependencies
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip wheel && \
    pip install --no-cache-dir -r requirements.txt

# Copy the application contents
COPY service/ ./service/

# Create a non-root user and switch to it for security
RUN useradd --uid 1000 theia && chown -R theia /app
USER theia

# Expose the service port and run it with Gunicorn
EXPOSE 8080
ENV PORT=8080
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:8080", "--log-level=info", "service:app"]
