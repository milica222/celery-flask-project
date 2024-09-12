# Flask Celery Redis Docker Project

This project demonstrates how to build a web application using Flask as the web framework, Celery for background task processing, and Redis as a message broker. The application is containerized using Docker, with separate containers for the web app, Celery worker, and Redis.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Running the Application](#running-the-application)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Build and Start the Containers](#2-build-and-start-the-containers)
  - [3. Running and Monitoring Tasks](#3-running-and-monitoring-tasks)


## Prerequisites

Make sure you have the following installed:
- [Docker](https://docs.docker.com/get-docker/) (to run the containers)
- [Docker Compose](https://docs.docker.com/compose/install/) (to orchestrate the containers)
- Python 3.9 (if running the application locally without Docker)

## Project Structure

```bash
.
├── images/                    # Directory for image files of code results
├── project/                   
│   ├── Dockerfile             # Dockerfile for the web app and Celery worker
│   ├── app.py                 # Flask application defining routes and logic
│   ├── celery_worker.py       # Celery tasks definition for background jobs
│   ├── docker-compose.yml     # Docker Compose configuration file
│   └── requirements.txt       # Dependencies for the Flask app and Celery worker
└── README.md                  # Project documentation (this file)
```

## Getting started

**1. Clone the Repository**
To start, clone the repository to your local machine using the following command:

```bash
git clone https://github.com/milica222/celery-flask-project.git
cd flask-celery-redis-docker
```

**2. Build and Start the Containers**
To build the Docker images and start the containers, use the following command from the root of the project directory:

```bash
docker-compose up --build
```

Docker will pull the necessary base images, install dependencies, and start the Flask web app, Celery worker, and Redis containers.

**3.Running and Monitoring Tasks**
To run a task and monitor its status, follow these steps:

 - Running a Task: You can initiate a task by sending a POST request to the /run-task endpoint. The request should include the number of samples in the task payload. For example:

```bash
curl -X POST http://localhost:5000/run-task -H "Content-Type: application/json" -d '{"num_samples": 100000}'
```
This request runs a task that generates 100,000 samples.

 - Checking Task Status: To check the status of the task after initiating it, use the task ID returned in the response of the POST request. Replace <task_id> with the actual ID of your task:

```bash
curl http://localhost:5000/task-status/<task_id>
```
This will return the current status of the task, allowing you to monitor its progress.
