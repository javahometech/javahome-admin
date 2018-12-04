import boto3
dynamodb = boto3.resource('dynamodb')
table= dynamodb.Table('javahome_batch')

def lambda_handler(event, context):
    table.put_item(Item=event)
    return {
        'message': 'Batch Student Added Succussfully'

    }
