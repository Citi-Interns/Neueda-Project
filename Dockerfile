# Use an official Python runtime as a parent image.
FROM python:3.8.5 

# Allow the name of the Python program to be passed as a parameter into the Docker build command.
ARG PYTHON_MAIN_FILE

# Create an /app folder inside the container.
RUN mkdir /neueda-project

# Set the working directory inside the container to /app.
WORKDIR /neueda-project
# Port issues
# Copy files from the current directory into the container's /app directory.
COPY routes ./routes
COPY requirements.txt .
#COPY app.py .
COPY ${PYTHON_MAIN_FILE} .

# Install any needed packages specified in requirements.txt.
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 5000 available to the world outside this container.
EXPOSE 5000

# Run main.py when the container launches.
ENTRYPOINT ["python3", "app.py"]
