import boto3

# Create an EC2 client
ec2 = boto3.client('ec2')

# Specify the parameters for the instance
instance_params = {
    'ImageId': 'ami-xxxxxxxxxxxxxxxxx',  # Specify the AMI ID of the desired Amazon Machine Image
    'InstanceType': 't2.micro',          # Specify the instance type
    'KeyName': 'your-key-pair-name',     # Specify the key pair name
    'MinCount': 1,                        # Minimum number of instances to launch
    'MaxCount': 1                         # Maximum number of instances to launch
}

# Launch the instance
response = ec2.run_instances(**instance_params)

# Extract the instance ID from the response
instance_id = response['Instances'][0]['InstanceId']

print(f'Launched EC2 instance with ID: {instance_id}')
