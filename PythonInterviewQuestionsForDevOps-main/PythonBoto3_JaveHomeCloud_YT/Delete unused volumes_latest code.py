import boto3
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText

# AWS credentials
aws_access_key = 'YOUR_ACCESS_KEY'
aws_secret_key = 'YOUR_SECRET_KEY'
aws_region = 'YOUR_AWS_REGION'

# Email configuration
email_sender = 'YOUR_EMAIL_SENDER'
email_recipient = 'YOUR_EMAIL_RECIPIENT'
email_subject = 'Unused EBS Volumes Report'

def get_unused_volumes(ec2_client, ec2_resource):
    unused_volumes = []

    # Step 1: List all EC2 instances
    instances = ec2_resource.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

    # Step 2: Get the IDs of attached volumes
    attached_volume_ids = [vol['Ebs']['VolumeId'] for instance in instances for vol in instance.volumes.all()]

    # Step 3: List all EBS volumes
    all_volumes = ec2_client.describe_volumes()['Volumes']

    # Step 4: Identify unused volumes
    unused_volumes = [volume for volume in all_volumes if volume['VolumeId'] not in attached_volume_ids]

    return unused_volumes

def send_email(body):
    # Step 5: Send email with details about unused volumes
    msg = MIMEText(body)
    msg['Subject'] = email_subject
    msg['From'] = email_sender
    msg['To'] = email_recipient

    # Use your email sending mechanism here
    # Example using SMTP
    with smtplib.SMTP('your_smtp_server', 587) as server:
        server.login(email_sender, 'your_email_password')
        server.sendmail(email_sender, [email_recipient], msg.as_string())

def main():
    # Set up Boto3 clients and resources
    ec2_client = boto3.client('ec2', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key, region_name=aws_region)
    ec2_resource = boto3.resource('ec2', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key, region_name=aws_region)

    # Get unused volumes
    unused_volumes = get_unused_volumes(ec2_client, ec2_resource)

    # Generate email body
    email_body = "Unused EBS Volumes:\n\n"
    for volume in unused_volumes:
        email_body += f"Volume ID: {volume['VolumeId']}\n"
        email_body += f"Size: {volume['Size']} GiB\n"
        email_body += f"Creation Time: {volume['CreateTime']}\n\n"

    # Send email
    send_email(email_body)

if __name__ == "__main__":
    main()
