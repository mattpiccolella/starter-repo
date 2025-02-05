#!/bin/bash

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

PORT=$1

if [ -z "$PORT" ]; then
    echo -e "${RED}Please provide a port number${NC}"
    echo "Usage: ./kill_port.sh <port_number>"
    exit 1
fi

echo -e "${YELLOW}Checking for processes on port $PORT...${NC}"

# Get PIDs using the port
pids=$(lsof -ti :$PORT)

if [ -z "$pids" ]; then
    echo -e "${GREEN}No processes found using port $PORT${NC}"
    exit 0
fi

echo -e "${YELLOW}Found processes using port $PORT: $pids${NC}"
echo -e "${RED}Killing processes...${NC}"

# Kill each process
for pid in $pids; do
    echo -e "Killing process $pid..."
    kill -9 $pid 2>/dev/null
done

# Verify port is free
sleep 1
if [ -z "$(lsof -ti :$PORT)" ]; then
    echo -e "${GREEN}Successfully killed all processes on port $PORT${NC}"
else
    echo -e "${RED}Failed to kill all processes. Please try again or kill processes manually.${NC}"
    exit 1
fi 