# devops_mscn

🛠️ DevOps Project: End-to-End Pipeline for Python Web App
📍 Target: Practice CI/CD, Docker, K8s, Monitoring, Secrets, Terraform
📍 Mode: Local (Docker, Minikube, GitHub)
📍 Time: ~6–8 hours (can split into weekends)


✅ [Phase 1: Setup Basic Python App]
 Install Python3 & pip

bash
Copy
Edit
sudo apt install python3 python3-pip  # or use brew on Mac
 Create Flask App

python
Copy
Edit
from flask import Flask  
app = Flask(__name__)  

@app.route("/")  
def hello():  
    return "Hello from DevOps Pipeline!"  

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
 Initialize Git repo

bash
Copy
Edit
git init  
echo "__pycache__/" > .gitignore  
git add . && git commit -m "Initial commit"
🐳 [Phase 2: Dockerize the App]
 Create Dockerfile

Dockerfile
Copy
Edit
FROM python:3.10-slim  
WORKDIR /app  
COPY . .  
RUN pip install flask  
CMD ["python", "app.py"]
 Build Docker image

bash
Copy
Edit
docker build -t flask-devops .
 Run the container

bash
Copy
Edit
docker run -p 5000:5000 flask-devops
🔁 [Phase 3: Setup CI/CD]
 Use GitHub Actions

yaml
Copy
Edit
# .github/workflows/docker.yml
name: Docker Build

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Build Docker image
        run: docker build -t flask-devops .
 Commit & push to GitHub

 ✅ Verify the build runs successfully

☸️ [Phase 4: Kubernetes with Minikube or Kind]
 Install Minikube

bash
Copy
Edit
brew install minikube  # or download from minikube website
minikube start
 Create Deployment YAML

yaml
Copy
Edit
apiVersion: apps/v1  
kind: Deployment  
metadata:
  name: flask-app  
spec:
  replicas: 1  
  selector:
    matchLabels:
      app: flask  
  template:
    metadata:
      labels:
        app: flask  
    spec:
      containers:
      - name: flask  
        image: flask-devops  
        ports:
        - containerPort: 5000
 Expose via NodePort

bash
Copy
Edit
kubectl expose deployment flask-app --type=NodePort --port=5000
minikube service flask-app
🔐 [Phase 5: Secrets Management]
 Create a K8s secret

bash
Copy
Edit
kubectl create secret generic flask-secret --from-literal=ENV=dev
 Update deployment to use secret

yaml
Copy
Edit
env:
  - name: ENV
    valueFrom:
      secretKeyRef:
        name: flask-secret
        key: ENV
📈 [Phase 6: Monitoring - Prometheus & Grafana]
 Install using Docker Compose
📦 Use existing: stefanprodan/dockprom

bash
Copy
Edit
git clone https://github.com/stefanprodan/dockprom.git  
cd dockprom  
docker-compose up -d
 Add /metrics to Flask

bash
Copy
Edit
pip install prometheus_client  
python
Copy
Edit
from prometheus_client import start_http_server, Summary  
import time  

start_http_server(8000)  # separate metrics port
☁️ [Phase 7: Terraform AWS EC2 (Optional)
 Install Terraform

bash
Copy
Edit
brew tap hashicorp/tap  
brew install hashicorp/tap/terraform  
 Simple EC2 instance

hcl
Copy
Edit
provider "aws" {
  region = "ap-south-1"
}

resource "aws_instance" "devops" {
  ami = "ami-0c55b159cbfafe1f0" # example Ubuntu
  instance_type = "t2.micro"
}
 Apply config

bash
Copy
Edit
terraform init  
terraform apply  
🎁 [Bonus: Add-ons]
 Add Slack notifications to GitHub Actions

 Canary deploy using Istio or K8s-native rollout

 Store secrets in Vault instead of K8s
👉 Docker image: vault:latest

 Use Code Scanning:
GitHub → Security → Code Scanning Alerts → Enable CodeQL

 Use Fluentd + Loki for logs
👉 Docker image: grafana/fluentd

💡 Want this in Notion?
I can send you a copy-paste ready markdown you can directly import into Notion. Or, give me your email and I can share a ready-made public Notion template. Just let me know!

Let me know if you'd like a repo template as well.
