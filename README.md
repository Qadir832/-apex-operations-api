Apex Operations API

A containerized FastAPI application built as a Junior DevOps Engineer assessment project. The project demonstrates Docker packaging, local multi-container orchestration, CI validation, application health checks, structured logging, metrics exposure, and incident troubleshooting.

Repository: "Qadir832/-apex-operations-api" (https://github.com/Qadir832/-apex-operations-api)
Branch: "main"

Project Overview

The API provides health, readiness, and metrics endpoints. Docker Compose runs the API alongside a PostgreSQL database, while GitHub Actions runs code-quality checks, automated tests, and a Docker image build on pushes to "main".

Key Features

- FastAPI application with "/health", "/ready", and "/metrics" endpoints.
- Docker packaging using Python 3.11 slim and a non-root application user.
- Docker Compose for the API and PostgreSQL services.
- Persistent database storage using a named Docker volume.
- Health checks for the API and PostgreSQL services.
- GitHub Actions CI for Ruff linting, pytest, and Docker image building.
- Structured JSON logs for operational visibility.
- Evidence screenshots stored in the "Images/" directory.

Architecture

flowchart TD
Dev[Developer pushes to main]
CI[GitHub Actions CI]
Lint[Ruff lint checks]
Tests[Pytest tests]
Build[Docker image build]
User[Client or browser]
API[FastAPI container]
DB[(PostgreSQL container)]
Vol[(Persistent database volume)]
Logs[Structured JSON logs]
Metrics[Prometheus-format metrics]

Dev --> CI  
CI --> Lint --> Tests --> Build  
User --> API  
API --> DB  
DB --> Vol  
API --> Logs  
API --> Metrics

The CI pipeline validates code and builds the image. The current workflow does not define an automated deployment or rollback stage.

Technology Stack

Component| Technology
API framework| FastAPI
Language| Python 3.11
Application server| Uvicorn
Database| PostgreSQL 15 Alpine
Containerization| Docker
Local orchestration| Docker Compose
Testing| pytest
Linting| Ruff
CI| GitHub Actions
Metrics format| Prometheus client exposition format

Repository Structure

-apex-operations-api/
├── .github/
│   └── workflows/
│       └── ci.yml
├── Images/
│   └── Evidence screenshots
├── Dockerfile
├── docker-compose.yml
├── main.py
├── requirements.txt
└── test_main.py

API Endpoints

Endpoint| Purpose
"GET /health"| Returns the application's health status.
"GET /ready"| Checks whether PostgreSQL is reachable and returns a readiness response. Returns HTTP 503 if the database connection fails.
"GET /metrics"| Exposes metrics in Prometheus-compatible format.

When the application is running locally, these endpoints are available at:

- "http://localhost:8000/health"
- "http://localhost:8000/ready"
- "http://localhost:8000/metrics"

Interactive API documentation is available at "http://localhost:8000/docs".

Prerequisites

Install the following tools before running the project:

- Git
- Docker
- Docker Compose
- Python 3.11 or a compatible Python environment for local testing

Run the Project Locally

1. Clone the repository

git clone https://github.com/Qadir832/-apex-operations-api.git
cd -apex-operations-api

2. Build the Docker image

The current Compose file references the image tag "apex-api:v2". Build that exact tag before starting the services:

docker build -t apex-api:v2 .

3. Start the API and database

docker compose up -d

4. Check running services

docker compose ps

5. Test the endpoints

curl http://localhost:8000/health
curl http://localhost:8000/ready
curl http://localhost:8000/metrics

Expected health response:

{
"status": "healthy"
}

The readiness endpoint requires a reachable PostgreSQL database. The metrics endpoint returns Prometheus-format output.

6. View logs

docker compose logs -f api
docker compose logs -f db

7. Stop the services

docker compose down

The named "postgres_data" volume is retained when the services are stopped this way. To remove the database volume and its stored data as well, use the following command only when you are sure the data is disposable:

docker compose down -v

Automated Testing

The repository contains "test_main.py" with six test functions covering:

- Health endpoint response
- Invalid route handling
- Readiness endpoint response
- A basic arithmetic assertion
- A basic string assertion
- A test labelled as an intentional-failure demonstration

Run the tests locally:

python -m pip install -r requirements.txt
python -m pip install httpx pytest ruff
pytest -v

Run the linter:

ruff check .

Testing note: The current version of the test labelled as an intentional failure asserts a true condition, so it passes as written. Do not describe it as a currently failing test unless you deliberately change the assertion, run the CI pipeline, and capture the failure and recovery evidence.

Continuous Integration

The workflow is located at ".github/workflows/ci.yml".

It runs on pushes to the "main" branch and performs these steps:

1. Checks out the repository.
2. Sets up Python 3.11.
3. Installs application and testing dependencies.
4. Runs Ruff lint checks.
5. Runs pytest.
6. Builds the Docker image tagged "apex-api:latest".

A failed lint or test step prevents later steps in the same job from running. The current workflow builds the image but does not publish it to a registry or deploy it to a server.

Check the Actions tab in GitHub for the actual run status and logs.

Observability and Incident Troubleshooting

The application supports basic operational checks through health, readiness, metrics, and structured JSON logs.

Suggested troubleshooting sequence:

1. Check service status using "docker compose ps".
2. Inspect application logs with "docker compose logs --tail=100 api".
3. Inspect database logs with "docker compose logs --tail=100 db".
4. Request "/health" to check whether the API responds.
5. Request "/ready" to check database connectivity.
6. Review "/metrics" for exposed metrics.

If readiness returns HTTP 503, investigate database availability, service networking, and the configured "DATABASE_URL" before restarting services.

The "Images/" directory contains project evidence screenshots. Use those screenshots and actual GitHub Actions run records to demonstrate the incident, failure, recovery, and successful validation sequence.

Security Considerations

- The Dockerfile runs the application as a non-root user.
- The application uses environment-based configuration for the database URL.
- The current Compose file contains demonstration database credentials directly in its configuration.
- Do not reuse the example credentials in production.
- For a production deployment, move credentials to a protected environment or secrets manager, use least-privilege access, and scan application dependencies and container images.
- Do not commit real credentials, access tokens, or private keys.
- Restrict network access and expose only required services.

This project is an assessment/demo implementation and should not be considered production-hardened without further security review.

Deployment and Rollback Scope

The current repository workflow performs CI validation and Docker image building. It does not implement automated deployment or rollback.

For a future deployment workflow, use versioned image tags, retain the previously working image, validate readiness after deployment, and document the exact rollback procedure. A rollback should be tested before claiming it is automated or production-ready.

Evidence

Project screenshots are stored in the "Images/" directory. They are intended to support review of the project structure, container health, readiness behavior, incident troubleshooting, code changes, CI outcomes, and structured logs.

Refer to the actual screenshot files and GitHub Actions run history when reviewing the evidence. Screenshots alone should not be used to claim a current deployment or a passing test run without matching verification.

AI Assistance Disclosure

AI assistance was used to review the repository structure and help prepare this documentation. Implementation details and claims about test results, CI runs, deployment, and rollback should be verified against the actual code and execution evidence before submission.

Current Limitations

- The CI workflow does not currently deploy the application.
- The workflow does not implement an automated rollback process.
- The Compose file uses demonstration credentials that should be externalized before production use.
- The test suite includes basic placeholder assertions; meaningful service and failure-path coverage can be expanded.
- Production readiness requires further security hardening, dependency and image scanning, and a defined monitoring and alerting strategy.

Isko rako wahan
