import boto3
client = boto3.client('sns')

def lambda_handler(event, context):
    topicArn = 'arn:aws:sns:us-east-1:151408537993:ProdAlert'
    message = 'Prod Server Stopped, Please Look into it '
    client.publish(TopicArn=topicArn, Message=message)
    