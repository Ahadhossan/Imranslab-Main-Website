#!/bin/bash

# Script to set up and run a Django backend and optionally prepare a Flutter frontend.

# Step 2: Set up Django backend
# update and python3, and pip install
sudo apt update
sudo apt install python3 python-is-python3 python3-pip python3-venv -y

## Step 3: Create and activate a virtual environment
#echo "Creating a virtual environment..."
#python3 -m venv venv || {
#    echo "Error: Failed to create a virtual environment."
#    exit 1
#}
cd backend || {
    echo "Error: Backend directory not found! Exiting."
    exit 1
}
echo "Activating the virtual environment..."
source venv/bin/activate || {
    echo "Error: Failed to activate the virtual environment.Then create a virtual environment."
    echo "Creating a virtual environment..."
    python3 -m venv venv || {
        echo "Error: Failed to create a virtual environment."
        exit 1
    }
    echo "Activating the virtual environment..."
    source venv/bin/activate || {
        echo "Error: Failed to activate the virtual environment."
        exit 1
    }
}

# Step 4: Upgrade pip to the latest version
echo "Upgrading pip to the latest version..."
pip install --upgrade pip || {
    echo "Error: Failed to upgrade pip. Check your Python installation."
    exit 1
}

# Step 5: Install Python dependencies from requirements.txt
echo "Installing Python dependencies..."
pip install -r ../requirements.txt || {
    echo "Error: Failed to install Python dependencies. Ensure requirements.txt is correct."
    exit 1
}
#echo "Navigate to the backend directory..."
#cd backend || {
#    echo "Error: Backend directory not found! Exiting."
#    exit 1
#}
# Step 6: Run Django database migrations
echo "Running database migrations..."
python3 manage.py migrate || {
    echo "Error: Failed to apply database migrations."
    exit 1
}

# Step 7: Start Django server
echo "Starting Django development server..."
python3 manage.py runserver || {
    echo "Error: Failed to start the Django development server."
    exit 1
}
# Final message
echo "Setup complete! Django server is running."