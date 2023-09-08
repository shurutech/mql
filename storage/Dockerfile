# Use the official PostgreSQL image as the base image
FROM ankane/pgvector:latest

COPY ./init.sql /docker-entrypoint-initdb.d/

# Install build dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    postgresql-server-dev-all \
    git

# Clean up
RUN apt-get remove -y build-essential postgresql-server-dev-all git && apt-get clean

# Expose the PostgreSQL port
EXPOSE 5432