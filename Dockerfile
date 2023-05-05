FROM python:3.9.16-slim-buster

# Specify the Working Directory inside the Container
WORKDIR /usr/src/app

# Install netcat
RUN apt-get update && apt-get -y install netcat && apt-get clean

# Install Python Dependencies
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy Application files inside the Container
COPY . /usr/src/app

# Add entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# Run Application
CMD ["/usr/src/app/entrypoint.sh"]