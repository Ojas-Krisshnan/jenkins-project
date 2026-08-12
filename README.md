# 🚀 Jenkins CI/CD Projects & Pipelines Repository

Welcome to the comprehensive **Jenkins CI/CD Projects** repository by **[Ojas Krisshnan](https://github.com/Ojas-Krisshnan)**.

This repository consolidates all Jenkins CI/CD automation projects, declarative pipelines, containerized build workflows, Terraform IaC validations, Maven starter applications, exported Jenkins job configurations, and automated reporting tools developed during the DevOps coursework.

---

## 📌 Repository Overview

```
jenkins-projects/
├── 📁 01-Java-Maven-Declarative-Pipeline/    # Multi-stage Jenkins Declarative Pipeline for Java/Maven
├── 📁 02-Docker-Terraform-Python-CI-CD/       # Full CI/CD: Pytest -> Docker -> Trivy Scan -> Terraform -> Deploy
├── 📁 03-Maven-Jenkins-Apps/                  # Starter Java Maven applications for Jenkins builds
├── 📁 04-Jenkins-Job-Configurations/          # Exported XML job configurations (Freestyle, Pipeline, SCM)
├── 📁 05-Reports-and-Automation/              # Jenkins execution documentation & Python report generator
├── 📄 .gitignore                              # Git exclusion rules for build outputs & transient files
└── 📄 README.md                               # Primary repository documentation
```

---

## 🛠️ Project Summaries

### 1. [01-Java-Maven-Declarative-Pipeline](./01-Java-Maven-Declarative-Pipeline)
- **Description**: Parameterized Jenkins Declarative Pipeline designed for building Java applications with Apache Maven.
- **Key Features**:
  - Environment selection (`dev`, `staging`, `production`) and module targeting (`core`, `api`, `ui`).
  - Automated JDK 17 & Maven 3 tool management.
  - Custom HTML test coverage report generation (`publishHTML` plugin).
  - Archiving of target JAR artifacts (`archiveArtifacts`).

### 2. [02-Docker-Terraform-Python-CI-CD](./02-Docker-Terraform-Python-CI-CD)
- **Description**: Enterprise-grade CI/CD pipeline demonstrating modern containerized application lifecycle.
- **Key Stages**:
  - **Code Analysis**: Virtual environment creation, dependency management, and `pytest` execution with coverage.
  - **Docker Build**: Multi-stage image compilation and tagging.
  - **Security Scan**: Image vulnerability assessment via Aqua Security Trivy (HIGH/CRITICAL checks).
  - **Terraform Validation**: IaC syntax and configuration validation (`terraform validate`).
  - **Deployment**: Local container deployment via Docker Compose with automated `/health` check verification.

### 3. [03-Maven-Jenkins-Apps](./03-Maven-Jenkins-Apps)
- **Description**: Lightweight Java Maven starter applications configured for testing Jenkins Freestyle builds, SCM polling triggers, and Maven lifecycle plugins.
- **Includes**:
  - `java-maven-junit-helloworld`: JUnit 4/5 integration testing application.
  - `maven-demo-app`: Standard Maven starter project for artifact build tests.
  - `java-hello-world-with-maven`: SCM repository integration app.

### 4. [04-Jenkins-Job-Configurations](./04-Jenkins-Job-Configurations)
- **Description**: Full collection of XML job configurations exported directly from the active Jenkins server.
- **Includes**:
  - `build-job.xml` (Parameterized Freestyle build job)
  - `deploy-job.xml` (Artifact copy & deployment job)
  - `sample-java-pipeline.xml` (Jenkinsfile SCM pipeline job)
  - `Build-Maven-Project.xml` & `Build-From-GitHub.xml` (SCM build jobs)
  - `Freestyle-Simple-Commands.xml` & `hello-world-job.xml` (Freestyle execution jobs)

### 5. [05-Reports-and-Automation](./05-Reports-and-Automation)
- **Description**: Detailed execution reports (`Jenkins_Execution_Report.docx`) along with `generate_report.py`, a Python utility for automated report formatting.

---

## 🧰 Prerequisites & Requirements

- **Jenkins**: Version 2.400+ (with Pipeline, Git, HTML Publisher, Copy Artifact plugins installed).
- **Java Development Kit (JDK)**: JDK 17 or JDK 21.
- **Build & DevOps Tools**: Apache Maven 3.9+, Docker Desktop / Docker Engine, Terraform 1.5+, Python 3.10+, Trivy.

---

## 👨‍💻 Author

**S Ojaskrisshnan**  
- **GitHub**: [@Ojas-Krisshnan](https://github.com/Ojas-Krisshnan) / [@ojaskrisshnan](https://github.com/ojaskrisshnan)  
- **Email**: ojaskrisshnan@gmail.com  
