# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /opt/

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install mysql-connector-python
RUN pip install cryptography

# Run the Python script when the container launches
CMD ["python", "./main.py"]
