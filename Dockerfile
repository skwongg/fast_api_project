# Use the official Python image from Docker Hub
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the application code
COPY app app

# Expose the port Flask will run on
EXPOSE 5001

# Command to run the app
CMD ["python", "app/main.py"]
