# ICAP+JMeter Dockerfile

## Access Minio
Run below command to do port forwarding in order to access minio locally
```
kubectl port-forward -n minio svc/minio 9000
```
you can access minio using http://localhost:9000/
## Access Grafana Dashboard
Run below command to do port forwarding in order to access Grafana locally 
```
kubectl port-forward -n grafana service/grafana-service 3000
```
you can access grafana using http://localhost:3000/

Create a Minio bucket called `input` and upload your test files there

Create an influx DB database called `JMeter` on the influx DB POD

## JMeter Jobs
### Run
On Windows 10 run the following from within the PowerShell
```
    powershell -ExecutionPolicy ByPass -File run.ps1 <jmeter-conf> <file_list> <number_of_pods>
```
Where
`jmeter-conf` is the JMeter file to be utilized in the test
`file_list` is a text file containing the list of files to be handled during the test
The files are to be uploaded to the Minio `input` bucket prior to the test start

The following example will start 10 parallel JMeter jobs:
```
    PowerShell -ExecutionPolicy ByPass -File run.ps1 ICAP-POC_s3.jmx files.txt 10
```
### Stop and remove 
```
    powershell -ExecutionPolicy ByPass -File stop.ps1
```