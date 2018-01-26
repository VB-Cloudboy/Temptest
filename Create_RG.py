import os
import traceback

from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.compute.models import DiskCreateOption

from msrestazure.azure_exceptions import CloudError
from haikunator import Haikunator


haikunator = Haikunator()



AZURE_TENANT_ID="701615f7-e8af-48a8-a6cb-94252db8b385"
AZURE_CLIENT_ID="a688424c-f847-4f0e-9a56-5e0a15dff805"
AZURE_CLIENT_SECRET="BpR1CBewAuRRjJpQD3z8STyrPhtGXlhDTmU2PfEjiyU="
AZURE_SUBSCRIPTION_ID="1b3c60d3-efc5-44d7-bb87-0a0d7f1b7be2"

# Resource Group
GROUP_NAME = 'Temp-RG02'

# Azure Datacenter
LOCATION = 'west india'



def get_credentials():
    subscription_id = os.environ['AZURE_SUBSCRIPTION_ID']
    credentials = ServicePrincipalCredentials(
        client_id=os.environ['AZURE_CLIENT_ID'],
        secret=os.environ['AZURE_CLIENT_SECRET'],
        tenant=os.environ['AZURE_TENANT_ID']
    )
    return credentials, subscription_id


def run_example():
    """Virtual Machine management example."""
    #
    # Create all clients with an Application (service principal) token provider
    #
    credentials, subscription_id = get_credentials()
    resource_client = ResourceManagementClient(credentials, subscription_id)
    compute_client = ComputeManagementClient(credentials, subscription_id)
    network_client = NetworkManagementClient(credentials, subscription_id)

# Create Resource group
    print('\nCreate Resource Group')
    resource_client.resource_groups.create_or_update(GROUP_NAME, {'location': LOCATION})