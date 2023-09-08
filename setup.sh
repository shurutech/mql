#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
RESET='\033[0m'

# Prerequisites
echo -e "${GREEN}Checking prerequisites...${RESET}"

# Check for Node.js
if ! command -v node &> /dev/null; then
    echo -e "${RED}Node.js is not installed. Please install it before running this script.${RESET}"
    exit 1
fi

# Check for Python
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Python is not installed. Please install it before running this script.${RESET}"
    exit 1
fi

# Check for PostgreSQL
if ! command -v psql &> /dev/null; then
    echo -e "${RED}PostgreSQL is not installed. Please install it before running this script.${RESET}"
    exit 1
fi

# Check for pgvector extension
if ! psql -d analytics -c "SELECT 'pgvector is installed';" &> /dev/null; then
    echo -e "${RED}pgvector extension is not installed. Please install it by following the instructions at [https://github.com/ankane/pgvector](https://github.com/ankane/pgvector).${RESET}"
    exit 1
fi

# Install backend dependencies
echo -e "${GREEN}Installing backend dependencies...${RESET}"
cd server
pip3 install -r requirements.txt
cd ..

# Install frontend dependencies
echo -e "${GREEN}Installing frontend dependencies...${RESET}"
cd client
npm install
cd ..

# Configure and start the application
echo -e "${GREEN}Configuring and starting the application...${RESET}"

cd server
alembic upgrade head
uvicorn app.main:app --reload &
backend_pid=$!
cd ..

cd client
npm run dev &
frontend_pid=$!
cd ..

echo -e "${GREEN}Setup complete! You can now access your application on http://localhost:3000.${RESET}"

wait $frontend_pid
wait $backend_pid


