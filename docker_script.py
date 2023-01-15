import os
import subprocess
import git

# specify the GitHub repository URL
repo_url = "https://github.com/username/myrepo.git"

# specify the local directory where you want to download the folder
local_directory = "/cinema"

# clone the repository to the local directory
repo = git.Repo.clone_from(repo_url, local_directory)

# Navigate to the project directory
os.chdir('cinema')

# Create a new file for the Dockerfile
with open('Dockerfile', 'w') as f:
    f.write("""
    # Use an official Python runtime as the base image
    FROM python:3.8

    # Set the working directory
    WORKDIR /app

    # Copy the requirements file
    COPY requirements.txt /app

    # Install the required packages
    RUN pip install --no-cache-dir -r requirements.txt

    # Copy the application files
    COPY . /app

    # Expose the port
    EXPOSE 8000

    # Start the application
    CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
    """)

# Build the Docker image
subprocess.call(['docker', 'build', '-t', 'myproject', '.'])

# Run the Docker container
subprocess.call(['docker', 'run', '-p', '8000:8000', 'myproject'])
