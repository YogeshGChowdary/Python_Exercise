import boto3
from datetime import datetime, timedelta

def delete_old_snapshots():
    # Create an EC2 client
    ec2 = boto3.client('ec2')

    # Get all EBS snapshots
    snapshots = ec2.describe_snapshots(OwnerIds=['self'])['Snapshots']

    # Get the current date
    current_date = datetime.now()

    # Specify the retention period in days
    retention_days = 15

    for snapshot in snapshots:
        # Get the snapshot creation date
        snapshot_date = snapshot['StartTime'].replace(tzinfo=None)

        # Calculate the age of the snapshot
        age = current_date - snapshot_date

        # If the snapshot is older than the retention period, delete it
        if age.days > retention_days:
            snapshot_id = snapshot['SnapshotId']
            print(f"Deleting snapshot: {snapshot_id}")
            
            # Uncomment the next line to actually delete the snapshot
            # ec2.delete_snapshot(SnapshotId=snapshot_id)

# Uncomment the next line to execute the function
# delete_old_snapshots()
