Build Docker Image
Build the Docker image with the following commands
docker build -t wisecow:latest .
run the Docker container to test it locally.
Need to create Kubernetes manifests for  deployment.
Now deploy these manifests to  Kubernetes cluster.
Run the commands to apply.
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

