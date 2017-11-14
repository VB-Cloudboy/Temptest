"""Start virtual machines.
This script expects that the following environment vars are set:
AZURE_CLIENT_ID: your Azure Active Directory Application Client ID
AZURE_CLIENT_SECRET: your Azure Active Directory Application Secret
AZURE_SUBSCRIPTION_ID: your Azure Subscription Id
"""

import os
import traceback

from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.compute import ComputeManagementClient

## DEFINING CREDENTIALS ##
AZURE_TENANT_ID: "701615f7-e8af-48a8-a6cb-94252db8b385"
# Object ID in AppRegistration of AAD is Client ID #
AZURE_CLIENT_ID: "a688424c-f847-4f0e-9a56-5e0a15dff805"
# Keys in Object ID in AppRegistration of AAD is Client secret #
AZURE_CLIENT_SECRET: "BpR1CBewAuRRjJpQD3z8STyrPhtGXlhDTmU2PfEjiyU="
AZURE_SUBSCRIPTION_ID: "1b3c60d3-efc5-44d7-bb87-0a0d7f1b7be2"

## LOGIN ATTEMPT ##

def get_credentials():
    subscription_id = os.environ['AZURE_SUBSCRIPTION_ID']
    credentials = ServicePrincipalCredentials(
        client_id = os.environ['AZURE_CLIENT_ID']
        secret = os.environ['AZURE_CLIENT_SECRET']
        tenant = os.environ['AZURE_TENANT_ID']
        )
            return credentials, subscription_id
    
def run_example():
    credentials, subscription_id = get_credentials()
    resource_client = ResourceManagementClient (credentials, subscription_id) 
    compute_client = ComputeManagementClient(credentials, subscription_id)

#List VMs in subscription
        print('\nList VMs in subscription')
        for vm in compute_client.virtual_machines.list_all():
            print("\tVM: {}".format(vm.name))


# Resource Group & VM Name
GROUP_NAME = 'Temp-RG01'
VM_NAME = 'TestVM'

 # Start the VM
        print('\nStart VM')
        async_vm_start = compute_client.virtual_machines.start(GROUP_NAME, VM_NAME)
        async_vm_start.wait()

  


