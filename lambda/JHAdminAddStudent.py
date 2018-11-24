import boto3
import json
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table= dynamodb.Table('javahome_students')


def lambda_handler(event, context):
    try:
        timestamp=datetime.now()
        timestamp=(timestamp.strftime("%d-%b-%Y %H:%M:%S:%f "))
        now=datetime.now()
        year=(now.strftime("%Y"))
        record = event
        record['year'] = year
        record['time_stamp'] = timestamp
        table.put_item(
            Item=record
        )
        return {
            'message': 'Student added succussfully'
        }
    except Exception as e:
        response = {
            'responseCode': 500,
            'message': 'Error adding Student'
        }
        raise Exception(json.dumps(response))
