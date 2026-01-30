# 🌤️ Weather Dashboard: An End-to-End Automation Journey

This repository documents my progression from a beginner to a practitioner of **Infrastructure-as-Code (IaC)**. I built a real-time weather application and automated its entire lifecycle using **Docker** and **Terraform**.

## 🏗️ Project Architecture
The project follows a modern delivery pipeline, ensuring that code is packaged safely and deployed predictably.

* **Application Layer**: Python Flask app fetching real-time weather data via API.
* **Packaging Layer**: Dockerized environment for consistent runtime across any machine.
* **Orchestration Layer**: Terraform for automated provisioning and state management.

---

## 🛤️ The Build Process

### 1. Development & Version Control 🐍
I started by developing the core application logic in **Python** using the **Flask** framework. 
* **Skills**: Used **Git Bash** for terminal navigation and **Git** for version control.
* **Key Learning**: Every automated system starts with a well-structured, version-controlled codebase.

### 2. Containerization (CI/CD Foundations) 🐳
To solve the "it works on my machine" problem, I packaged the app into a **Docker Image**.
* **The Blueprint**: Wrote a `Dockerfile` to install dependencies and configure the environment.
* **Delivery**: Pushed the image to **Docker Hub** (`waseem1216/weather-app`) to make it available for any environment.

### 3. Infrastructure-as-Code with Terraform 🏗️
Instead of manual deployments, I wrote a `main.tf` configuration to define my infrastructure as code.
* **Automation**: Used Terraform to pull the image and launch the container with specific port mappings (`8080:5000`).
* **Lifecycle**: Mastered the full `init` -> `plan` -> `apply` -> `destroy` workflow.

---

## 🛠️ The "Engineer's Log": Overcoming Real-World Hurdles
Hiring managers look for problem-solving skills. Here are the technical blockers I successfully navigated:

* **Docker API Mismatch** 🧱: Resolved a `1.41 vs 1.44` version conflict by upgrading Terraform providers and explicitly defining the API version in the provider block.
* **Environment Sanitization** 🧹: Identified hidden `DOCKER_API_VERSION` variables in the shell that were interfering with the deployment; cleared them using the `unset` command.
* **Provider Caching** 🔄: Learned to manage the `.terraform` directory to resolve persistent configuration errors and force provider updates.

---

## 📊 Skills & Competencies Acquired

| Skill | Accomplishment |
| :--- | :--- |
| **Python & Flask** | Developed a dynamic web app with API integration and HTML rendering. |
| **Docker** | Mastered image creation, container management, and registry (Docker Hub) usage. |
| **Terraform** | Managed resource lifecycles and state-aware deployments through code. |
| **DevOps Logic** | Applied CI/CD principles to bridge the gap between development and operations. |

---

## 🚀 How to Replicate
1.  `git clone <your-repo-link>`
2.  `terraform init`
3.  `terraform apply` (Visit `http://localhost:8080`)
4.  `terraform destroy` (To clean up)
