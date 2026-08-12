# ☕ Project 01: Multi-Stage Java & Maven Declarative Pipeline

This project implements a parameterized, declarative Jenkins CI/CD pipeline for a Java Maven application.

## 📌 Features
- **Parameterized Execution**:
  - `ENVIRONMENT`: Choice parameter (`dev`, `staging`, `production`).
  - `BUILD_ENV`: String parameter for build tagging.
  - `MODULES`: Comma-separated module targeting (`core`, `api`, `ui`).
- **Tooling Integration**: Configured with JDK17 and Maven 3 in Jenkins tools.
- **Cross-Platform Execution**: Supports Unix shell (`sh`) and Windows batch (`bat`) commands.
- **HTML Build Reporting**: Generates custom HTML coverage & build reports published via `publishHTML`.
- **Artifact Archiving**: Automatically archives built JAR artifacts (`target/*.jar`).

## 📁 Repository Structure
```
01-Java-Maven-Declarative-Pipeline/
├── Jenkinsfile                  # Declarative Jenkins Pipeline definition
├── pom.xml                      # Maven POM with JUnit 4 dependency
├── scripts/
│   └── deploy_job_script.sh     # Deployment helper script
└── src/
    ├── main/java/com/example/App.java
    └── test/java/com/example/AppTest.java
```

## 🚀 How to Run in Jenkins
1. Open Jenkins and create a new **Pipeline** job.
2. Select **Pipeline script from SCM**, choose **Git**, and provide the repository URL.
3. Set the Script Path to `01-Java-Maven-Declarative-Pipeline/Jenkinsfile`.
4. Click **Build with Parameters**, choose your target environment, and launch the build.
