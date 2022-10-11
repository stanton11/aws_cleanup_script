import boto3
from sys import argv

ACCESS_KEY = argv[1]
SECRET_KEY = argv[2]

# create etc3 client
ec2 = boto3.client('ec2', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY, region_name='us-east-2')

# retrieve all ec2 
response = ec2.describe_addresses()

# list of dictionaries relating to each address
addresses = response['Addresses']

# release any addresses with no association ID
for address in addresses:
    if 'AssociationId' not in address:
        response = ec2.release_address(AllocationId=address['AllocationId'])

# retrieve all ec2 network interfaces
response = ec2.describe_network_interfaces()

# list of dictionaries relating to each interface
interfaces = response['NetworkInterfaces']

# release any interfaces that are not in use
for interface in interfaces:
    if interface.get('Status') == 'available':
        response = ec2.delete_network_interface(NetworkInterfaceId=interface['NetworkInterfaceId'])
