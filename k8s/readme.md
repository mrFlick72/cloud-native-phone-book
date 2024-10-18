# Cloud Native Phone Book

## How to install on K8s (Kind)

### set up the basic infrastructure

```shell

helm install postgresql oci://registry-1.docker.io/bitnamicharts/postgresql  --create-namespace --namespace phonebook --values postgresql.yml

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