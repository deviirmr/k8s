1. Test Django
''''
python manage.py test
''''


2. Build a container
'''
docker build -t registry.digitalocean.com/cfe-k8s-deb/django-k8s:latest -f Dockerfile .
'''


3. Push container
'''
docker push registry.digitalocean.com/cfe-k8s-deb/django-k8s --all-tags 
'''

4. Update secrets
'''
kubectl get secrets
kubectl delete secret <secret name>
kubectl create secret generic django-k8s-web-prod-env --from-env-file=web/.env.prod
'''

5. Update deployment
'''
kubectl apply -f deployment.yaml
'''

6. Wait for Rollout to Finish
'''
kubectl rollout status deployment/django-k8s-web-deployment
'''

7.Migrate database
'''
Get a single pod (either method works)

kubectl get pods

export SINGLE_POD_NAME=$(kubectl get pod -l app=django-k8s-web-deployment -o jsonpath="{.items[0].metadata.name}")
or

export SINGLE_POD_NAME=$(kubectl get pod -l=app=django-k8s-web-deployment -o NAME | tail -n 1)
Then run migrate.sh

kubectl exec -it $SINGLE_POD_NAME -- bash /app/migrate.sh
'''