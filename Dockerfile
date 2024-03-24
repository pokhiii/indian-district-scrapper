# Base image using Python 3.9
FROM python:3.9

# Install required libraries
WORKDIR /app
RUN pip install requests beautifulsoup4

# Copy your Python script
COPY main.py .

# Set working directory for the container (optional)
WORKDIR /app

# Entrypoint to run your script
CMD [ "python3", "main.py" ]