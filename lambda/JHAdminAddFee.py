import boto3
import json
from boto3.dynamodb.conditions import Attr
from boto3.dynamodb.conditions import Key
import botocore
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('javahome_students')

def lambda_handler(event,context):
    year  = event['year']
    time_stamp=event['time_stamp']
    del event['year']
    del event['time_stamp']

    try:

        resp = table.update_item(
            Key={
                'year': year,
                'time_stamp': time_stamp
            },
            UpdateExpression="set fee.payments = list_append(fee.payments, :payments)",
            ExpressionAttributeValues={
                ':payments': event['payments']
            },
            ConditionExpression='attribute_exists(fee)'
        )
        return {
            'statusCode': 200,
            'message': 'Fee updated succussfully'
        }
    except botocore.exceptions.ClientError as e:
        try:
            resp = table.update_item(
            Key={
                'year': year,
                'time_stamp': time_stamp
            },
            UpdateExpression="set fee = :fee",
            ExpressionAttributeValues={
                ':fee': event
            },
            ConditionExpression='attribute_exists(time_stamp)'

            )
            return {
                'statusCode': 200,
                'message': 'Fee updated succussfully'
             }
        except Exception as e:
            response={
            'statusCode': 500,
            'message': 'Student not found'

        }
            raise Exception(json.dumps(response))

            
