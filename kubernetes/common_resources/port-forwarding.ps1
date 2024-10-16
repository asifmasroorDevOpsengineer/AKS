Start-Process -FilePath "kubectl" -ArgumentList "port-forward -n minio --address 0.0.0.0 service/minio 9000:9000"
Start-Process -FilePath "kubectl" -ArgumentList "port-forward -n influxdb --address 0.0.0.0 service/influxdb 8086"
Start-Process -FilePath "kubectl" -ArgumentList "port-forward -n grafana --address 0.0.0.0 service/grafana-service 3000"
