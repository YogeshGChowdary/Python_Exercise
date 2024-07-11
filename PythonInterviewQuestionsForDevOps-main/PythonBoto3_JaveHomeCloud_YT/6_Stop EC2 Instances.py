import boto3
client = boto3.client('ec2')

ec2_filter = [{'Name': 'instance-state-name', 'Values': ['running']}]

# Describe instances based on the filter
instances = client.describe_instances(Filters=ec2_filter)

# Stop each running instance
for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        client.stop_instances(InstanceIds=[instance_id])