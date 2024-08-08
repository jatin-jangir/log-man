# log-man
inspired by ant man




# installation

```
git clone https://github.com/jatin-jangir/log-man
cd log-man

helm repo add fluent https://fluent.github.io/helm-charts
helm install fluent-bit fluent/fluent-bit -f fluent-bit-values.yaml

helm repo add minio https://charts.min.io/
helm install minio --namespace minio minio/minio --set mode=standalone --set rootUser=rootuser,rootPassword=rootpass123 -f minio-values.yaml


```


## minio 
```
MinIO can be accessed via port 9000 on the following DNS name from within your cluster:
minio.minio.svc.cluster.local

To access MinIO from localhost, run the below commands:

  1. export POD_NAME=$(kubectl get pods --namespace minio -l "release=minio" -o jsonpath="{.items[0].metadata.name}")

  2. kubectl port-forward $POD_NAME 9000 --namespace minio

Read more about port forwarding here: http://kubernetes.io/docs/user-guide/kubectl/kubectl_port-forward/

You can now access MinIO server on http://localhost:9000. Follow the below steps to connect to MinIO server with mc client:

  1. Download the MinIO mc client - https://min.io/docs/minio/linux/reference/minio-mc.html#quickstart

  2. export MC_HOST_minio-local=http://$(kubectl get secret --namespace minio minio -o jsonpath="{.data.rootUser}" | base64 --decode):$(kubectl get secret --namespace minio minio -o jsonpath="{.data.rootPassword}" | base64 --decode)@localhost:9000

  3. mc ls minio-local
```


## creds
```
minio bucket 
name - logs
access - ZK1KrWTumiVmPcHvs35e
secret - Uw5mbs2oJKnsMTsWtsnyutRXQT1FiCR80IcBN8xZ
```

## minio connection 
```
python3.12 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install minio
```

to get back form venv of python 
```
deactivate
```

refer minio-connection.py