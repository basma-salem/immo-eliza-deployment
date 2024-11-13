# Use the Python 3.10 base image
FROM python:3.10

# Create a directory for the app
RUN mkdir /app

# Set the working directory
WORKDIR /app

COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copy application's code into the container at /app
COPY api/ /app/


# Expose the port FastAPI will run 
EXPOSE 8000

# Run the application
CMD ["uvicorn", "API.app:app", "--host", "0.0.0.0", "--port", "8000"]

