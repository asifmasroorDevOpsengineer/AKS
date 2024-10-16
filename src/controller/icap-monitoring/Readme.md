# Health check monitoring of the icap-server

## Prerequisites
	Install c-icap
	```
    apt-get update && \
    apt-get -y install c-icap
	```
## Usage
  Open FetchICAP_Server_metrics.jmx file
  In Thread Group -> Get ICAP server status-> HTTP request -> change IP of localhost to IP address(host) of influxDB server
  
## License
MIT License
See: LICENSE
