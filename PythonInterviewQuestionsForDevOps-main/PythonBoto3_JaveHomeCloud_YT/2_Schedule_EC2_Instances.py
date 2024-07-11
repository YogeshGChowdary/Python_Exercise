import boto3
ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
    # declaring variable 'filter' which is array of json of objects
    filter = [
        {
            'Name': 'tag:Type',
            'Values': ['Scheduled']
        }
    ]
    instances = ec2.instances.filter(Filters=filter) # this function returns all ec2 instances whose tag key is 'Type' and value is 'Scheduled'

    for instance in instances:
        instance.start()

    # # this lambda fuction code to start instances at particular time, and to stop instances at particular time, create new function mention instead of start in code, change to stop and rest all code remains same
        
    #     for instance in instances:
    #     instance.stop()
        
    # # create new rule with reqd corn job to stop instances, select target as newly created stop lambda function

    return 'success'
    
