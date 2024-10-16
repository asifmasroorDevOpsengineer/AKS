**k8-jmeter-test-engine**

**Project brief**

**k8-jmeter-test-engine-v1**

A first version of the Kubernetes (K8) native application able to generate up to 100000 concurrent requests directly to the ICAP server using the c-icap client.

**Requirements:**

- A JMeter test plan configured for concurrency test to use Icap client to send traffic directly to the ICAP server
- Configured K8 cluster with a traffic generator and Docker image to generate the number of pods based on the scenario &amp; load scripts in the JMeter test plan.
- Implemented input mechanism to retrieve required file for processing from MinIO
- Implemented assertion mechanism that validates the response code returned
- Implemented Elasticsearch or InfluxDB logging solution to visualize the performance metrics
- Implemented monitoring feature using Grafana or Kibana for result dashboard display


**K8s V1 Infrastructure**

- The traffic generator will pick up a scenario &amp; files, generate pods to execute all the instructions in the scenario file
- The JMeter results are sent to MinIO for storage
- The logs, response times, throughput and error metrics etc. are sent to the Elastic logging pod
- The metrics are sent to &amp; displayed on Kibana dashboard

**Metrics to monitor:**

- **Running Servers Statistics**

- Children number:
- Free Servers:
- Used Servers:
- Started Processes:
- Closed Processes:
- Crashed Processes:
- Closing Processes:

- **Service gw\_rebuild Statistics**

- Service gw\_rebuild REQMODS:
- Service gw\_rebuild RESPMODS:
- Service gw\_rebuild REQUESTS SCANNED:
- Service gw\_rebuild REBUILD FAILURES:
- Service gw\_rebuild REBUILD ERRORS:
- Service gw\_rebuild SCAN REBUILT:
- Service gw\_rebuild UNPROCESSED:
- Service gw\_rebuild UNPROCESSABLE:
- Service gw\_rebuild BYTES IN:
- Service gw\_rebuild BYTES OUT:
- Service gw\_rebuild HTTP BYTES IN:
- Service gw\_rebuild HTTP BYTES OUT:
- Service gw\_rebuild BODY BYTES IN:
- Service gw\_rebuild BODY BYTES OUT:
- Service gw\_rebuild BODY BYTES SCANNED:

**Other metrics:**

- CPU &amp; Memory utilisation of the running pods
- Number of files processed
- Number of concurrent requests processed

**Success Criteria:**

- The solution setup details are clearly documented with required step by step information and scripts to run
- The solution contains both versions and satisfies all the above defined requirements
- Use of GitHub Actions CI/CD
- The test engine can be started with minimal configuration and run tests with 1 command based on test requirement
- The test engine can run up to 4 million requests to generate up to 100k concurrent requests with use of few files
- Ability to run a continuous heartbeat test successfully with a continuous view of the performance dashboard
