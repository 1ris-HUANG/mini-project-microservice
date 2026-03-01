# mini-project-microservice
ProgWeb
Ce projet implémente un microservice Python déployé sur Kubernetes.
## Contenu du dépôt
- `app.py` : Code source du service Flask.
- `Dockerfile` : Instructions de conteneurisation.
- `k8s-deploy.yaml` : Configuration Deployment (3 réplicas) et Service.
## Comment déployer
1. Build & Push image: `docker build -t <user>/<image>:v2 .`
2. Deploy on K8s: `kubectl apply -f k8s-deploy.yaml`
3. Access service: `minikube service python-app-service`
