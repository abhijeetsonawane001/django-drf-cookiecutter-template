import os
import subprocess

import random
import string

def generate_secret_key(length=50):
    """Generate a random secret key for Django."""
    # Use a mix of letters, digits, and specific characters for a more valid key
    characters = (
        string.ascii_letters + string.digits + 
        string.punctuation.replace("'", "").replace('"', "").replace("\\", "")
    )
    return ''.join(random.choice(characters) for _ in range(length))

def copy_and_update_env_file():
    """Copy .env.example to .env and update SECRET_KEY."""
    env_example_path = '.env.example'
    env_path = '.env'

    # Check if .env.example exists
    if os.path.exists(env_example_path):
        # Generate a new SECRET_KEY
        secret_key = generate_secret_key()

        # Read the .env.example file
        with open(env_example_path, 'r') as env_example_file:
            lines = env_example_file.readlines()

        # Replace the SECRET_KEY line
        updated_lines = []
        for line in lines:
            if line.startswith('SECRET_KEY='):
                updated_lines.append(f'SECRET_KEY={secret_key}\n')
            else:
                updated_lines.append(line)

        # Write the updated lines to .env
        with open(env_path, 'w') as env_file:
            env_file.writelines(updated_lines)
            print(f"Copied {env_example_path} to {env_path} and updated SECRET_KEY.")

def run_command(command):
    """Helper function to run shell commands."""
    try:
        subprocess.check_call(command, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {command}")
        exit(1)

def add_dependencies(dependencies, dev=False):
    """Add dependencies using Poetry's add command."""
    command_prefix = 'poetry add'
    if dev:
        command_prefix += ' --group dev'

    # Join dependencies into a single command
    command = f"{command_prefix} " + " ".join(dependencies)
    run_command(command)

if __name__ == "__main__":
    # Change to the project directory
    os.chdir(os.path.realpath(os.path.curdir))

    # Initialize a new Poetry project if pyproject.toml does not exist
    if not os.path.exists('pyproject.toml'):
        print("Initializing new Poetry project...")
        run_command('poetry init --no-interaction')

    # Install dependencies by creating a virtual environment
    print("Installing virtual environment...")
    run_command('poetry install --no-root')

    # Define main dependencies
    dependencies = [
        "django",
        "djangorestframework",
        "django-split-settings",
        "psycopg2-binary",
        "django-environ",
        "django-cors-headers",
        "gunicorn",
        "celery",
        "redis",
        "pytz",
        "nanoid",
        "django-filter"
    ]

    # Define development dependencies
    dev_dependencies = [
        "flake8",
        "black",
        "isort"
    ]

    # Add main dependencies
    if dependencies:
        print("Installing main dependencies...")
        add_dependencies(dependencies)

    # Add development dependencies
    if dev_dependencies:
        print("Installing development dependencies...")
        add_dependencies(dev_dependencies, dev=True)
    

    copy_and_update_env_file()

    print("Project setup complete!")
    project_slug = "{{ cookiecutter.project_slug }}"  # Assuming you have this variable set
    print(f"To start the project, navigate to the project directory and run:")
    print(f"cd {project_slug} && docker-compose up --build")
    print("This will build and start your services.")

