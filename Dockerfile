FROM python:3.10.5

ARG PYTHON_MAIN_FILE

RUN mkdir /Application
WORKDIR /Application

COPY ./requirements.txt /Application
COPY ${PYTHON_MAIN_FILE} /Application/app.py

# Install any needed packages specified in requirements.txt.
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 5000 available to the world outside this container.
EXPOSE 5000

# Run app.py when the container launches.
ENTRYPOINT ["python", "app.py"]