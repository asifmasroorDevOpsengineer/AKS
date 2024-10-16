# Manage Azure Kubernetes Cluster for running jmeter scripts

## Create 

1. If you don't already have it [install Python](https://www.python.org/downloads/), please remember to install python package manager - pip (Python and pip 3.6+).

1. We recommend to use a [virtual environnement](https://docs.python.org/3/tutorial/venv.html), but it's not mandatory. You can initialize a virtualenv this way:

    ```
    pip install virtualenv
    virtualenv mytestenv
    cd mytestenv
    source bin/activate #.\Scripts\activate for Windows
    ```

1. Clone the repository.

    ```
    git clone https://github.com/k8-proxy/p-k8-jmeter-test-engine.git
	cd .\p-k8-jmeter-test-engine\AKS\
    ```

1. Install the dependencies using pip.

    ```
    pip3 install -r python-requirements.txt
    ```

1. Create an Azure service principal either through
[Azure CLI](https://azure.microsoft.com/documentation/articles/resource-group-authenticate-service-principal-cli/),
[PowerShell](https://azure.microsoft.com/documentation/articles/resource-group-authenticate-service-principal/)
or [the portal](https://azure.microsoft.com/documentation/articles/resource-group-create-service-principal-portal/).

1. Export these environment variables into your current shell. 

    ```
    export AZURE_TENANT_ID={your tenant id}
    export AZURE_CLIENT_ID={your client id}
    export AZURE_CLIENT_SECRET={your client secret}
    export AZURE_SUBSCRIPTION_ID={your subscription id}
    ```

1. Create Azure Kubernetes Service with two node pools - inspect the code for Resource Group Names and parameters.

    ```
    python3 azure_deployment.py
    ```

