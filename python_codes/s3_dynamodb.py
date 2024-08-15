import json
import boto3 
client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    response = client.get_object(
        Bucket = 'ashutoshh-dbnomod', # name of s3 bucket 
        Key = 'DynamoDB_Samplefile.json' # file name which you will be uploading 
        )
    json_data = response['Body'].read()
    data_string = json_data.decode('UTF-8')
    print(data_string)
    print(type(data_string))
    # convert to dict
    data_dict = json.loads(data_string)
    print(data_dict)
    # insert to dynamodb table 
    table = dynamodb.Table('ashutable-s3store') # table name 
    table.put_item(Item=data_dict)
    
