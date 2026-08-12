# DevOps Course - Assignment 3 Report

**Course**: DevOps (Semester 7)  
**Topic**: End-to-End DevOps Pipeline: Containerization, Infrastructure as Code, and CI/CD Automation  
**Date**: August 12, 2026  

---

## 1. Executive Summary

This report documents the implementation of **Assignment 3** for the DevOps course. The objective was to design and deploy a complete, production-ready DevOps workflow including an application layer, containerization, Infrastructure as Code (IaC), and automated CI/CD pipelines.

The project incorporates:
- A Python FastAPI RESTful microservice with automated test suites.
- Multi-stage Docker containerization following container security standards.
- Terraform scripts to provision cloud infrastructure (AWS VPC, Subnets, Security Groups, and EC2).
- CI/CD automation via both GitHub Actions workflows and a Jenkins Declarative Pipeline.

---

## 2. Architecture & Components

### 2.1 Application Layer
The web application is built using **FastAPI** and **Pydantic**. It features structured logging, CORS handling, health checks (`/health`), system metrics (`/api/v1/metrics`), and RESTful item management endpoints (`/api/v1/items`).

### 2.2 Containerization Strategy
A 2-stage `Dockerfile` was built:
1. **Builder Stage**: Compiles and installs dependencies.
2. **Runtime Stage**: Copies only installed libraries into a `python:3.11-slim` base image, runs under a unprivileged non-root user (`appuser`), and exposes port `8000` with an active healthcheck rule.

Multi-container setup using `docker-compose.yml` integrates the FastAPI application with a PostgreSQL database container and an Adminer database administration container.

### 2.3 Infrastructure as Code (Terraform)
Terraform was selected to ensure reproducible, version-controlled cloud infrastructure:
- **VPC & Networking**: Dedicated 10.0.0.0/16 VPC with a public subnet (10.0.1.0/24) and Internet Gateway.
- **Security Group**: Restricts inbound access exclusively to port 8000 (FastAPI) and port 22 (SSH).
- **Compute Instance**: EC2 instance with user data script to automatically start the containerized service upon launching.

### 2.4 CI/CD Automation
The repository includes two independent pipeline definitions:
1. **GitHub Actions (`.github/workflows/ci-cd.yml`)**:
   - `lint-and-test`: Executes `pytest` with code coverage reports.
   - `docker-build-and-scan`: Builds Docker image and scans for vulnerabilities using Trivy.
   - `terraform-validate`: Validates syntax and formatting of Terraform configuration files.
2. **Jenkins Pipeline (`Jenkinsfile`)**:
   - Covers stages: Checkout, Code Analysis & Test, Docker Build & Tag, Security Scan, Terraform Validation, and Local Deployment.

---

## 3. Verification & Execution Results

| Component | Test Executed | Command | Result |
| :--- | :--- | :--- | :--- |
| **App Unit Tests** | Pytest Test Suite | `pytest` | **PASSED** (100% route coverage) |
| **Container Build** | Docker Multi-stage Build | `docker build -t app:latest .` | **SUCCESS** (Small footprint, non-root user) |
| **Orchestration** | Multi-container bring-up | `docker compose up -d` | **SUCCESS** (All services healthy) |
| **Terraform IaC** | Syntax & Structure Check | `terraform validate` | **SUCCESS** (Configuration valid) |
| **Pipeline** | CI/CD Trigger | Automated on Push/PR | **PASSED** |

---

## 4. Conclusion & DevOps Learnings

By completing this assignment:
1. Continuous Integration guarantees that code regressions are identified immediately through automated testing.
2. Multi-stage Docker builds reduce container image vulnerability surface and image sizes.
3. Declarative IaC with Terraform eliminates manual cloud setup errors and enables infrastructure versioning.
4. Automated pipelines streamline deployment to staging and production environments.
