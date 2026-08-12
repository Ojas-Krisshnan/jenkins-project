# ⚙️ Project 04: Jenkins Job Configurations (XML Exports)

This directory contains exported XML job configuration files from the local Jenkins instance.

## 📄 Included Job Configurations
| Job XML File | Job Type | Description |
| :--- | :--- | :--- |
| `build-job.xml` | Freestyle / Parameterized | Compiles Java app, generates build reports, and archives artifacts. |
| `deploy-job.xml` | Freestyle / Downstream | Uses Copy Artifact plugin to deploy output from `build-job`. |
| `sample-java-pipeline.xml` | Pipeline | Declarative Jenkinsfile pipeline execution job. |
| `Build-Maven-Project.xml` | Freestyle (SCM) | Maven build triggered from Git SCM repository. |
| `Build-From-GitHub.xml` | Freestyle (SCM) | Automated SCM polling build job. |
| `Freestyle-Simple-Commands.xml` | Freestyle | Command line environment testing job. |
| `hello-world-job.xml` | Freestyle | Basic verification job printing build info. |

## 📥 How to Import into Jenkins
1. Open your Jenkins Home directory (e.g., `C:\Users\<User>\.jenkins\jobs\`).
2. Create a new directory for the job (e.g., `my-imported-job`).
3. Copy the desired `.xml` file into that folder and rename it to `config.xml`.
4. Go to **Jenkins Dashboard** -> **Manage Jenkins** -> **Reload Configuration from Disk**.
