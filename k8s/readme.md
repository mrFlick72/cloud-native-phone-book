# Cloud Native Phone Book

## How to install on K8s (Kind)

### set up the basic infrastructure

```shell

helm install postgresql oci://registry-1.docker.io/bitnamicharts/postgresql  --create-namespace --namespace phonebook --values postgresql.yml

```
in order to connect from host issue this command:

> kubectl port-forward svc/postgresql -n phonebook  5432:5432
 