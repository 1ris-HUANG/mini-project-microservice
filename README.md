Projet Kubernetes - Architecture Microservices Python
📝 Description
Ce projet implémente et déploie une architecture microservices composée de deux services Python sur un cluster Kubernetes (Minikube). L'accès est orchestré par un contrôleur Ingress via un nom de domaine local personnalisé.

🏗️ Architecture du Projet
Service Principal (app.py) : Gère les requêtes utilisateurs sur le port 5000.

Service d'Information (service-info.py) : Microservice secondaire fournissant des données complémentaires sur le port 5001.

Ingress Controller : Route le trafic du nom de domaine http://my-python-app.local vers le service principal.

📂 Contenu du dépôt
app.py & service-info.py : Codes sources des services Flask.

Dockerfile & Dockerfile.info : Instructions de conteneurisation.

k8s-deploy.yaml : Configuration des Deployments (3 réplicas), des Services et de l'Ingress.

🚀 Instructions de Déploiement
Lancer l'environnement :

Bash
minikube start
minikube addons enable ingress
Préparer le domaine local :
Ajouter 127.0.0.1 my-python-app.local dans votre fichier /etc/hosts (ou C:\Windows\System32\drivers\etc\hosts).

Déployer sur Kubernetes :

Bash
kubectl apply -f k8s-deploy.yaml
Activer l'accès :

Bash
minikube tunnel
Accédez ensuite à : http://my-python-app.local
