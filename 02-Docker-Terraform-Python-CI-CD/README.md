# 🐳 Project 02: Containerized Python App with Security Scanning & Terraform IaC

This project contains an end-to-end CI/CD Jenkins Pipeline that integrates Python testing, Docker multi-stage container builds, Trivy security vulnerability scanning, Infrastructure as Code (IaC) validation via Terraform, and deployment via Docker Compose.

## 📌 Pipeline Stages
1. **Checkout Source**: Clones and initializes workspace repository.
2. **Code Analysis & Test**: Virtual environment creation, dependency installation, and `pytest` execution with coverage.
3. **Docker Build & Tag**: Multi-stage image build (`devops-assignment3:1.0.${BUILD_NUMBER}`).
4. **Security Vulnerability Scan**: Container vulnerability scan using Aqua Security Trivy for HIGH and CRITICAL severity vulnerabilities.
5. **Terraform Validation**: `terraform init -backend=false` & `terraform validate` check on IaC configurations.
6. **Local Integration Deploy**: Automatic deployment using Docker Compose followed by health check on `http://localhost:8000/health`.

## 📁 Repository Structure
```
02-Docker-Terraform-Python-CI-CD/
├── Jenkinsfile                  # Complete CI/CD Pipeline definition
├── Dockerfile                   # Multi-stage Docker build specification
├── docker-compose.yml           # Local integration service orchestrator
├── app/                         # FastAPI/Flask application (main.py, models.py, config.py)
├── tests/                       # Pytest unit & integration test suite
├── terraform/                   # Terraform IaC files (main.tf, variables.tf, outputs.tf)
└── .github/workflows/ci-cd.yml  # GitHub Actions workflow alternative
```

## 🚀 How to Run in Jenkins
1. Ensure Jenkins agent has Docker, Pytest, Terraform, and Trivy available.
2. Create a Pipeline job pointing SCM script path to `02-Docker-Terraform-Python-CI-CD/Jenkinsfile`.
3. Trigger the job build.
