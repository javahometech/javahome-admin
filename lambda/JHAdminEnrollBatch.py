import boto3
import json
from boto3.dynamodb.conditions import Attr
from boto3.dynamodb.conditions import Key
import botocore

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('javahome_students')


def lambda_handler(event, context):
    try:
        try:

         resp = table.update_item(
            Key={
                'year': event['year'],
                'time_stamp': event['time_stamp']
            },
            UpdateExpression="set batch_details = list_append(batch_details, :b)",
            ExpressionAttributeValues={
                ':b': [event['batches']]
            },
            ConditionExpression='attribute_exists(batch_details)'
         )
         return {
            'message': 'Batch_details added succussfully'
         }
        except botocore.exceptions.ClientError as e:
         resp = table.update_item(
            Key={
                'year': event['year'],
                'time_stamp': event['time_stamp']
            },
            UpdateExpression="set batch_details = :b",
            ExpressionAttributeValues={
                ':b': event['batches']
            },
        )
        return {
            'message': 'Batch_details added succussfully'
        }
    except Exception:
        return {
            'responseCode': 500,
            'message': 'Error adding batch details '
        }
