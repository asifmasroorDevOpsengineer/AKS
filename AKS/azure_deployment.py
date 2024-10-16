import os.path
from deployer import Deployer


# This script expects that the following environment vars are set:
#
# AZURE_TENANT_ID: with your Azure Active Directory tenant id or domain
# AZURE_CLIENT_ID: with your Azure Active Directory Application Client ID
# AZURE_CLIENT_SECRET: with your Azure Active Directory Application Secret

my_subscription_id = os.environ.get(
    'AZURE_SUBSCRIPTION_ID', '00912682-1091-4918-8627-598dabcc00e1')   # your Azure Subscription Id
# the resource group for deployment
my_resource_group = 'azure-aks'

msg = "\nInitializing the Deployer class with subscription id: {}, resource group: {}"
msg = msg.format(my_subscription_id, my_resource_group)
print(msg)

# Initialize the deployer class
deployer = Deployer(my_subscription_id, my_resource_group)

print("Beginning the deployment... \n\n")
# Deploy the template
my_deployment = deployer.deploy()

print("Done deploying!!")

# Destroy the resource group which contains the deployment
# deployer.destroy()