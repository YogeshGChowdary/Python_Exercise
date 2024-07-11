import boto3
import json
s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

# refer notes for code explanation.

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    json_file_name = event['Records'][0]['s3']['bucket']['key']

    # code from documentation --> boto3 s3 --> get object

    json_object = s3_client.get_object(Bucket=bucket, Key=json_file_name)
    jsonFileReader = json_object['Body'].read()
    jsonDict = json.loads(jsonFileReader)
    table=dynamodb.Table('employees')
    table.put_item(Item=jsonDict)

    return 'success'
    