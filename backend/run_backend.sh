#!/bin/bash

# Exit on error
set -e

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}Starting backend setup...${NC}"

# Check if port 5001 is in use
if lsof -ti :5001 >/dev/null; then
    echo -e "${YELLOW}Port 5000 is in use. Attempting to free it...${NC}"
    ./kill_port.sh 5001
    if [ $? -ne 0 ]; then
        echo -e "${RED}Failed to free port 5001. Please free it manually and try again.${NC}"
        exit 1
    fi
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo -e "${YELLOW}Creating virtual environment...${NC}"
    python3 -m venv venv
fi

# Activate virtual environment
echo -e "${GREEN}Activating virtual environment...${NC}"
source venv/bin/activate

# Install requirements
echo -e "${GREEN}Installing dependencies...${NC}"
pip install -r requirements.txt

# Export environment variables
export FLASK_APP=run.py
export FLASK_ENV=development
export FLASK_DEBUG=1

# Initialize database and run migrations
echo -e "${GREEN}Initializing database...${NC}"
flask db init || true
flask db migrate -m "Initial migration"
flask db upgrade

# Seed the database with sample data
echo -e "${GREEN}Seeding database with sample data...${NC}"
flask seed-db

echo -e "${GREEN}Starting Flask application...${NC}"
python run.py 