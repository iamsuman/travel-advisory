# travel-advisory v3
# Usage
```
git clone git@github.com:iamsuman/travel-advisory.git
cd travel-advisory/travelsory/v3
pip install -r requirements.txt
cd travel
python flask_api.py
 
Usage:
http://localhost:5000/health
http://localhost:5000/diag
http://localhost:5000/convert?countryCode=AD
http://localhost:5000/convert?countryCode=AD,AU,XY
```

Docker
```
cd travel-advisory/travelsory/v3
docker build -f Dockerfile -t imsuman/travel-advisory:latest .
docker container run -d -p 5000:5000 --name travel-advisory imsuman/travel-advisory:latest

Usage:
http://localhost:5000/health
http://localhost:5000/diag
http://localhost:5000/convert?countryCode=AD
http://localhost:5000/convert?countryCode=AD,AU,XY
```
Deploy on Local Kubernetes
```
for Mac: 
kubectl version 
kubectl config use-context docker-for-desktop
kubectl apply -f deployments.yaml
    service/travel-advisory-service created
    deployment.apps/travel-advisory created

http://localhost:8080/health
http://localhost:8080/diag
http://localhost:8080/convert?countryCode=AD
http://localhost:8080/convert?countryCode=AD,AU,XY

Cleanup:
kubectl delete -f deployments.yaml
```