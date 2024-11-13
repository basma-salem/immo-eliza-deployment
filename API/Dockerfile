# Use the Python 3.10 base image
FROM python:3.10

# Create a directory for the app
RUN mkdir /app

# Set the working directory
WORKDIR /app

# Copy requirements.txt from the root folder
COPY ../requirements.txt /app/

# Copy the entire API folder contents into /app
COPY . /app/

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port FastAPI will run on
EXPOSE 8000

# Run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
