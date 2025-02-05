#!/bin/bash

# Set up the backend
mkdir -p backend/app
touch backend/app/__init__.py backend/app/models.py backend/app/routes.py backend/app/config.py backend/app/utils.py

# Create the migrations directory
mkdir backend/migrations

# Set up a virtual environment
python3 -m venv backend/venv

# Create the requirements file
touch backend/requirements.txt

# Create the run script
touch backend/run.py

# Set up the frontend
mkdir -p frontend/public frontend/src/components frontend/src/styles
touch frontend/public/index.html frontend/public/favicon.ico
touch frontend/src/components/App.js frontend/src/components/index.js
touch frontend/src/styles/App.css
touch frontend/src/App.test.js frontend/src/index.js frontend/src/serviceWorker.js frontend/src/setupTests.js

# Initialize a new Node.js project
cd frontend || exit
npm init -y

# Create package-lock.json (this will be generated when you install packages)
touch package-lock.json

cd ..

# Create the README
touch README.md

# Install Backend Dependencies
cd backend || exit
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install Flask SQLAlchemy Flask-Migrate
pip freeze > requirements.txt
deactivate
cd ..

# Initialize React App
cd frontend || exit
npx create-react-app .  # This will set up a basic React app and overwrite some files
cd ..

echo "Project setup complete!"