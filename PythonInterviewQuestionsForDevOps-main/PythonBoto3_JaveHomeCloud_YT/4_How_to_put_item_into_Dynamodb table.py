import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('employees') # name of table created in dynamodb--> employees

# from documentation, to insert item in table--> put_item () --> json format dictionary
table.put_item(
    Item={
        'employee_id':'1',
        'Name':'Kashvi',
        'Age':2
    }
)