kubectl delete --ignore-not-found jobs -l jobgroup=jmeter
kubectl delete --ignore-not-found secret jmeterconf
kubectl delete --ignore-not-found secret filesconf
