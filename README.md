# mlops-major-assignment

mlops-major-assignment/

├── .github/workflows/ci.yml   # GitHub Actions CI/CD pipeline

├── templates/index.html        # Flask web app UI

├── train.py                    # Model training script

├── test.py                     # Model evaluation script

├── app.py                      # Flask web application

├── Dockerfile                  # Docker image definition

├── deployment.yaml             # Kubernetes deployment (3 replicas)

├── service.yaml                # Kubernetes NodePort service

├── requirements.txt            # Python dependencies

└── README.md                   # This file



## Branches
- `main` — Initial repository setup
- `dev` — Model development + CI pipeline
- `docker_cicd` — Flask app + Docker + Kubernetes deployment

## Dataset & Model
- **Dataset:** Olivetti Faces (400 samples, 40 classes) from sklearn
- **Model:** DecisionTreeClassifier
- **Split:** 70% train, 30% test

## CI/CD Pipeline (GitHub Actions)
On every push to `dev` or `docker_cicd`:
1. Sets up Python 3.10 environment
2. Installs dependencies from requirements.txt
3. Runs train.py to train and save the model
4. Runs test.py to display test accuracy

On push to `docker_cicd` only:
5. Builds Docker image
6. Pushes image to Docker Hub automatically

## How to Run Locally

### Without Docker
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python train.py
python app.py
```
Open http://localhost:5000

### With Docker
```bash
docker pull rparna/olivetti-classifier:latest
docker run -p 5000:5000 rparna/olivetti-classifier:latest
```
Open http://localhost:5000

## Kubernetes Deployment

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl get pods
```

3 replicas are always maintained. To demonstrate resilience:
```bash
kubectl delete pod <pod-name>
kubectl get pods  # Kubernetes auto-restores to 3 pods
```

### Note on Windows
NodePort (port 30007) is not directly accessible on Windows Docker Desktop
due to Kubernetes running inside a VM. Use port-forward instead:
```bash
kubectl port-forward deployment/olivetti-deployment 5000:5000
```

## Docker Hub
Image: `rparna/olivetti-classifier:latest`

## Links
- GitHub: https://github.com/Rituparna770/mlops-major-assignment
- Docker Hub: https://hub.docker.com/r/rparna/olivetti-classifier
