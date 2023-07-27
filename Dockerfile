# Use the official Python image as the base image
FROM python:3.8-slim-buster

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the required packages from the requirements.txt file
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port that Flask is running on
EXPOSE 5000

# Define the command to run your Flask app using gunicorn (or you can use any other server of your choice)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "run:app"]