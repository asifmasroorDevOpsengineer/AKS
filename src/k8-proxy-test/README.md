*** Run Proxy site test ***
- In order to run proxy site test clone the repo - https://github.com/k8-proxy/p-k8-jmeter-test-engine.git
- Navigate to /src/k8-proxy-test
- run docker build command 
```
docker build -t k8-proxysite-image .
```
- execute docker run command to run the image
``` 
docker run -it k8-proxysite-image
```
the current setup in image is for single user for test. 

will add more steps to update those details in script