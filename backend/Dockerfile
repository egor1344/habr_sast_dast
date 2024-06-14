FROM python:3.12-alpine

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONWARNINGS ignore
ENV CURL_CA_BUNDLE ""
ENV POETRY_VIRTUALENVS_CREATE true
ENV PATH "${PATH}:/root/.local/bin"

# Expose port 8000
EXPOSE 8000/tcp

# Set the working directory for the application
WORKDIR /app

# Copy just the dependencies installation from the current directory to the Docker image
COPY pyproject.toml poetry.lock /app/

# Install necessary dependencies
RUN set -ex; \
    apk update; \
    apk add --no-cache --virtual build-deps \
        curl \
        git \
        gcc \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir --user poetry==1.6 \
    && poetry install --no-interaction --no-ansi \
    && pip install  --no-cache-dir --user requests \
    && apk del --no-cache build-deps

# Create link python interpritator
RUN ln -sf $(poetry env info -e) /python

# Copy wait-for script and give it necessary permissions
COPY wait-for /usr/bin/
RUN chmod +x /usr/bin/wait-for

# Copy the current directory contents into the container
COPY . /app/

# Give necessary permissions to entrypoint
RUN chmod +x entrypoint.*
