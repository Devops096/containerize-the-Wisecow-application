# Cow wisdom web server

## How to use?

1. Run `./wisecow.sh`
2. Point the browser to server port (default 4499)


# Problem Statement
 Wisecow on Kubernetes involves several steps, including containerizing the application, creating Kubernetes manifests, and deploying those manifests to a Kubernetes cluster. 


## Requirement
1. Create Dockerfile for the image and corresponding k8s manifest to deploy in k8s env. The wisecow service should be exposed as k8s service.
2. Github action for creating new image when changes are made to this repo
3. [Challenge goal]: Enable secure TLS communication for the wisecow app.
##  Project Structure
wisecow-app/
├── Dockerfile
├── app.py
├── docker-compose.yml
├── nginx.conf
├── requirements.txt
└── static/
    └── images/
        └── wisecow.png
## configuration for TLS communication
server {
    listen 80;
    server_name yourdomain.com;

    location / {
        return 301 https://$host$request_uri;
    }
}

server {
    listen 443 ssl;
    server_name yourdomain.com;

    ssl_certificate /etc/nginx/certs/fullchain.pem;
    ssl_certificate_key /etc/nginx/certs/privkey.pem;

    location / {
        proxy_pass http://wisecow:80;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}


## Expected Artifacts
1. Github repo containing the app with corresponding dockerfile, k8s manifest, any other artifacts needed.
   
## Deploy to Kubernetes Cluster
Deploy these manifests to  Kubernetes cluster.
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
## Verify Deployment
kubectl get deployments
kubectl get services
web browser to ensure the application is running with secure TLS communication.
## Additional Considerations
Secrets and ConfigMaps: Use Kubernetes Secrets and ConfigMaps for managing sensitive data and configuration.
Scaling: Configure Horizontal Pod Autoscalers (HPA) for automatic scaling based on metrics.
Monitoring and Logging: Implement monitoring (e.g., Prometheus) and logging (e.g., ELK stack) solutions to keep track of the application's health and performance.
Persistent Storage: needs persistent storage, consider using PersistentVolume and PersistentVolumeClaim.
