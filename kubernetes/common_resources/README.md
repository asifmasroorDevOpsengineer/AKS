# Deploy applications to K8s cluster

Set below environment variables with the values you like, in the terminal before following the next deployment steps:

1. GF_USERNAME
2. GF_PASSWORD
3. MINIO_ACCESS_KEY
4. MINIO_SECRET_KEY

### Deploy grafana

    kubectl create ns grafana
    kubectl -n grafana create secret generic grafana-creds --from-literal=username=$GF_USERNAME --from-literal=password=$GF_PASSWORD
    kubectl apply -n grafana -f grafana.yaml

### Deploy ELK

    kubectl create ns elk
    kubectl apply -n elk -f elk/tenant_multipod.yaml
    kubectl apply -n elk -f elk/tenant.yaml

### Deploy Minio

    kubectl create ns minio
    kubectl -n minio create secret generic minio-creds --from-literal=MINIO_ACCESS_KEY=$MINIO_ACCESS_KEY --from-literal=MINIO_SECRET_KEY=$MINIO_SECRET_KEY
    kubectl apply -n minio -f minio.yaml

### Deploy InfluxDB

    kubectl create ns influxdb
    kubectl create secret generic init-script -n influxdb --from-file=influxdb/init-influxdb.iql
    kubectl apply -n influxdb -f influxdb/influxdb.yaml

### Deploy Prometheus

    kubectl create ns prometheus
    helm repo add stable https://kubernetes-charts.storage.googleapis.com
    helm repo update
    helm upgrade --install -n prometheus prometheus stable/prometheus

### Deploy Loki

    kubectl create ns loki-stack
    helm repo add loki https://grafana.github.io/loki/charts
    helm repo update
    helm upgrade --install loki --namespace=loki-stack loki/loki-stack


## Setup connection to k8s cluster in Github repo to deploy using Github Actions

1. Create a service account with cluster-admin clusterrole which will be used in Github Actions

    kubectl create serviceaccount -n default cd-pipeline
    kubectl create clusterrolebinding cd-pipeline-admin-binding --clusterrole=cluster-admin --serviceaccount=default:cd-pipeline

2. Create below secrets in github repo.

* K8S_URL - Get kubernetes API URL using `kubectl config view --minify -o jsonpath={.clusters[0].cluster.server}`
* K8S_SECRET - Get service account's secret in json format using `kubectl get secret cd-pipeline-token-bjmml -n default -o json`


### Grafana
Set below secrets in Github project before running Github workflow to deploy Grafana

1. GF_USERNAME
2. GF_PASSWORD

Connect to Grafana on http://localhost:3000 by running below commands

    kubectl port-forward -n grafana service/grafana-service 3000

Connect to Grafana on http://grafana.grafana.svc.cluster.local:3000 from within the cluster

### ELK
Connect to Elastic and Kibana using below commands

#### Check the credentials
Username: elastic Password: see command below

    kubectl get secret quickstart-es-elastic-user -o go-template='{{.data.elastic | base64decode}}'

Connect to Kibana on https://localhost:5601 by running below command

    kubectl port-forward -n elk service/quickstart-kb-http 5601

Connect to Kibana on https://quickstart-kb-http.elk.svc.cluster.local:5601 from within the cluster

### Minio
Set below secrets in Github project before running Github workflow to deploy Minio

1. MINIO_ACCESS_KEY
2. MINIO_SECRET_KEY

Connect to Minio on http://localhost:9000 by running below commands

    kubectl port-forward -n minio service/minio 9000

Connect to Minio on http://minio.minio.svc.cluster.local:9000 from within the cluster

### InfluxDB

Connect to InfluxDB on http://localhost:8086 by running below commands

    kubectl port-forward -n influxdb service/influxdb 8086

Connect to InfluxDB on http://influxdb.influxdb.svc.cluster.local:8086 from within the cluster

### Prometheus

Connect to Prometheus server on http://localhost:9090 URL by running these commands:
    
    kubectl --namespace prometheus port-forward service/prometheus-server 9090:80

### Loki

Connect to loki server on http://localhost:3100 URL by running below command:

    kubectl --namespace loki-stack port-forward service/loki 3100:3100

Connect to Loki on http://loki.loki-stack.svc.cluster.local:3100 from grafana and anywhere from the cluster.


## Integrate these applications with jmeter-icap

Create a kubernetes secret with key-value pairs required by the jmeter-icap in the namespace where jmeter-icap k8s jobs will run. 
For example, we need Minio access key and secret key as environment variables inside the jmeter-icap container.

Create a secret by running below command

    `kubectl -n default create secret generic minio-creds-secret --from-literal=MINIO_ACCESS_KEY=$MINIO_ACCESS_KEY --from-literal=MINIO_SECRET_KEY=$MINIO_SECRET_KEY`    

Use this secret in the k8s job/pod to set the required environment variables.

## Port forwarding

To start port forwarding for minio, grafana and influxdb on Windows OS run the following in Windwos PowerShell

```
    PowerShell -ExecutionPolicy ByPass -File .\port-forwarding.ps1
```
