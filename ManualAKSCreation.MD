**k8-jmeter-test-engine-v1**

A first version of the Kubernetes (K8) native application able to generate up to 100000 concurrent requests directly to the ICAP server using the c-icap client.

**Requirements:**

- Azure cli installed - https://docs.microsoft.com/pl-pl/cli/azure/

**Create Azure Kubernetes Service**

- Define Variables - parameters for K8S Service in Azure
``` bash
$RESOURCEGROUPNAME="k8sk8s"
$LOCATION="eastus"
$AKS_NAME="k8s-test"
$MONITORINGNODES="1"
$MAXPODS="70"
```

- Deploy Azure Kubernetes Service
``` bash
az login
az account set --subscription subscrybtionid
az group create -l $LOCATION -n $RESOURCEGROUPNAME
az aks create --name $AKS_NAME --resource-group $RESOURCEGROUPNAME --node-count $MONITORINGNODES --network-plugin kubenet --max-pods 100 --enable-managed-identity --vm-set-type VirtualMachineScaleSets --no-ssh-key
```

**Create a secondary node pool dedicated to the JMeter workloads.**

``` bash
$JMETERNODES="1"
az aks nodepool add --resource-group $RESOURCEGROUPNAME --cluster-name $AKS_NAME --name jmeter --node-count $JMETERNODES --node-taints sku=jmeter:NoSchedule --labels purpose=jmeter 
```

**Install kubeclt and connect to the AKS instance**

- Deploy Azure Kubernetes Service
``` bash
az aks install-cli
$env:path += 'C:\Users\admin\.azure-kubectl'
az aks get-credentials --resource-group $RESOURCEGROUPNAME --name $AKS_NAME
```

**Test Deployment**

- Deploy to nodepool (default) 
``` bash
kubectl create -f akstest/phpinfomonitoring.yaml
kubectl get pods -o wide
kubectl get service
```
- Deploy to jmeter pool
``` bash
kubectl create -f akstest/phpinfojmeter.yaml
kubectl get pods
kubectl get service
```
- Destroy test deployment
``` bash
kubectl delete -f akstest/phpinfojmeter.yaml
kubectl delete -f akstest/phpinfomonitoring.yaml
kubectl get pods -o wide
kubectl get service
```
**Destroy Azure Kubernetes Service**

- Deploy to nodepool (default) 
``` bash
az group delete --name $RESOURCEGROUPNAME --yes --no-wait
```
