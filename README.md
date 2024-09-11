# Musbot Project
Welcome to the Musbot project! This README will guide you through setting up and running the Musbot application using Docker. This project uses multiple containers for a seamless integration of FastAPI, Rasa, Rasa SDK, and PostgreSQL.

## Overview
Musbot is a chatbot application that leverages FastAPI for backend operations, Rasa for chatbot functionalities, and PostgreSQL for data storage. Docker is used to containerize each component for easy setup and deployment.

## Prerequisites
Before you begin, ensure you have the following installed:

- Docker: Required to build and run the containers.
- Docker Compose: Manages multi-container Docker applications.
## Getting Started
### 1. Clone the Repository
First, clone the Musbot repository from GitHub:

```bash
git clone https://github.com/your-username/musbot.git
cd musbot
```
### 2. Build and Start Containers
Navigate to the project directory and use Docker Compose to build and start the containers:

```bash
docker-compose up --build
```
This command will:
- Build the Docker images for FastAPI, Rasa, and Rasa SDK.
- Start the PostgreSQL, FastAPI, Rasa, and Rasa SDK containers.

## 3. Running Individual Containers
If you only want to run a specific container, such as FastAPI or Rasa, you can do so with the following commands:

- FastAPI:

    ```bash
    docker-compose up fastapi
    ```

- Rasa:
    ```bash
    docker-compose up rasa
    ```

- Rasa SDK:
    ```bash
    docker-compose up rasa_sdk
    ```

- PostgreSQL:
    ```bash
    docker-compose up postgres
    ```

This will only start the container you secify. All the other containers will remain stopped unless started manually.

### 3. Accessing the Services
Once the containers are up and running, you can access the services as follows:

- FastAPI: http://localhost:8000
- Rasa: http://localhost:5005
- Rasa SDK: http://localhost:5055
- PostgreSQL: The database runs internally and is not exposed via a port. You can interact with it using database tools or directly from the FastAPI application.

### 4. Stopping the Containers
To stop the containers, press Ctrl + C in the terminal where Docker Compose is running. To remove the containers, use:

```bash
docker-compose down
```

## Project Structure
Here’s an overview of the project structure:

```markdown
musbot/
├── README.md
├── app/
│   ├── Dockerfile.fastapi
│   ├── __init__.py
│   ├── __pycache__/
│   │   └── main.cpython-310.pyc
│   ├── config.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── requirements.txt
│   ├── schemas.py
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   ├── images/
│   │   └── js/
│   │       └── script.js
│   ├── templates/
│   │   ├── Museum/
│   │   │   └── index.html
│   │   └── chatbot/
│   │       └── index.html
│   └── tests/
│       ├── __init__.py
│       └── test_main.py
├── docker-compose.yml
├── notes.txt
├── rasa/
│   ├── Dockerfile.rasa
│   ├── Dockerfile.rasa_sdk
│   ├── actions/
│   │   ├── __init__.py
│   │   ├── __pycache__/
│   │   │   ├── __init__.cpython-310.pyc
│   │   │   └── actions.cpython-310.pyc
│   │   └── actions.py
│   ├── config.yml
│   ├── credentials.yml
│   ├── data/
│   │   ├── nlu.yml
│   │   ├── rules.yml
│   │   └── stories.yml
│   ├── domain.yml
│   ├── endpoints.yml
│   ├── entrypoint.sh
│   ├── models/
│   │   ├── 20240908-133035-steel-tray.tar.gz
│   │   ├── 20240909-062524-quiet-static.tar.gz
│   │   ├── 20240911-022015-vicious-credits.tar.gz
│   │   └── 20240911-022258-chill-packet.tar.gz
│   ├── requirements.txt
│   └── tests/
│       └── test_stories.yml
└── tests/
    ├── __init__.py
    └── test_fastapi.py
```
- app/: Contains the FastAPI application and its Dockerfile.
- rasa/: Contains the Rasa and Rasa SDK components and their Dockerfiles.
- docker-compose.yml: Defines the services and their configurations.
- notes.txt: Additional notes or documentation.
- tests/: Contains test files for FastAPI and Rasa.
## Configuration
### Environment Variables
- FastAPI: DATABASE_URL should be set to postgresql://musebot_admin:musebot_2024@postgres/musebot_db.
### Volumes
PostgreSQL data is persisted using Docker volumes to ensure data is retained across container restarts.
## Troubleshooting
- **Containers Not Starting**: Ensure Docker and Docker Compose are correctly installed. Check logs using docker-compose logs for more information.
- **Connection Issues**: Verify the ports are correctly mapped and no other services are using the same ports.

## Additional Resources
- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Rasa Documentation](https://rasa.com/docs/)