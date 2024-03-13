# Use the official PostgreSQL image as the base image
FROM ankane/pgvector:latest

# Install necessary packages and generate locale
RUN apt-get update && apt-get upgrade -y && apt-get install -y locales locales-all && \
    locale-gen en_US.UTF-8 && \
    update-locale LANG=en_US.UTF-8

# Debug: List generated locales
RUN locale -a

# Set environment variables for locale
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8

COPY ./init.sql /docker-entrypoint-initdb.d/

# Install build dependencies and cleanup in a single RUN to reduce image layers and size
RUN apt-get install -y \
    build-essential \
    postgresql-server-dev-all \
    git && \
    apt-get remove -y build-essential postgresql-server-dev-all git && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Expose the PostgreSQL port
EXPOSE 5432
