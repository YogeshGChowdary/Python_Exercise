import boto3
client = boto3.client('ec2')

# we will use describe instances -> from that we get all instances -> to get AMI ids

instances = client.describe_instances()
used_amis =[]

# check syntax in documentation for describe instances (check syntax of response syntax) -> from that get the loop logic

for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        used_amis.append(instance['ImageId'])

print(used_amis)

# to remove duplicate amis we will create function and loop through the amis and add to list unique_amis only unique ids
        
def remove_duplicates(amis):
    unique_amis=[]
    for ami in amis:
        if ami not in unique_amis:
            unique_amis.append(ami)

    return unique_amis

unique_amis = remove_duplicates(used_amis)
print(unique_amis)

# get custom amis form the account
# use boto3 documentation -> ec2 -> describe images

custom_images = client.describe_images(
    Filters=[
        {
            'Name':'state',
            'Values': ['available']
        }
    ],
    Owners=['self']
)

custom_amis_list =[]

for image in custom_images['Images']:
    custom_amis_list.append(image['ImageId'])

# Delete unused amis
# use boto3 documentation -> to delete unused amis -> deregister_image   

for custom_ami in custom_amis_list:
    if custom_ami not in used_amis:    
        print("deregistering ami {}".format(custom_ami))
        client.deregister_image(ImageId=image['ImageId']) 
