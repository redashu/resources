import json
import boto3

print('Loading function')

s3 = boto3.client('s3')

def lambda_handler(event, context):
    try:
        # List all buckets
        response = s3.list_buckets()
        buckets = response['Buckets']
        
        # Print bucket names
        bucket_names = [bucket['Name'] for bucket in buckets]
        print("Buckets:")
        for name in bucket_names:
            print(name)
        
        # Return the bucket names as a JSON response
        return {
            'statusCode': 200,
            'body': json.dumps({
                'buckets': bucket_names
            }),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
        
    except Exception as e:
        print(e)
        print('Error listing buckets.')
        raise e
