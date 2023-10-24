# We Use an official Python runtime as a parent image
FROM python:3.10

# The environment variable ensures that the python output is set straight
# to the terminal without buffering it first
ENV PYTHONUNBUFFERED 1

# Install system dependencies for GDAL
RUN apt-get update && apt-get install -y binutils libproj-dev gdal-bin libgdal-dev && apt-get clean && rm -rf /var/lib/apt/lists/*

# Clone the app repository
RUN git clone https://github.com/RioSakao/BudgetTravel.git

# Set the working directory
WORKDIR /nearbyshops

# Install Python dependencies
COPY requirements.txt /nearbyshops/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Ensure the Docker container can persist data
VOLUME /nearbyshops

# You commented out static file collection; uncomment if necessary in future
# RUN python manage.py collectstatic --no-input

# Expose the port the app runs on
EXPOSE 8080

# The command to run the app when the docker container starts
CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000

