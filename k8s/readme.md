# Cloud Native Phone Book

## How to install on K8s (Kind)

### set up the basic infrastructure

#### install istio

````shell
curl -L https://istio.io/downloadIstio | sh -
cd istio-1.23.2
export PATH=$PWD/bin:$PATH
istioctl install

kubectl apply -f samples/addons
kubectl rollout status deployment/kiali -n istio-system
istioctl dashboard kiali
istioctl dashboard grafana

````

#### install basic application infrastructure

```shell
kubectl apply -f namespace.yml

helm install postgresql oci://registry-1.docker.io/bitnamicharts/postgresql  --namespace phonebook --values postgresql.yml
helm upgrade postgresql oci://registry-1.docker.io/bitnamicharts/postgresql  --namespace phonebook --values postgresql.yml

```
in order to connect from host issue this command:

kubectl port-forward svc/postgresql -n phonebook  5432:5432

### set up the specific services

> account service
```shell

helm install account-service account-service --namespace phonebook
helm upgrade account-service account-service --namespace phonebook

kubectl port-forward svc/account-service -n phonebook 3000:3000



```
> phone book service
```shell

helm install phone-book-service phone-book-service --namespace phonebook
helm upgrade phone-book-service phone-book-service --namespace phonebook


```

### change kubectl default namespace

```shell
kubectl config set-context $(kubectl config current-context) --namespace=phonebook

```
