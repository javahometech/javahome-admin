import boto3
import json
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table= dynamodb.Table('javahome_students')
sns_client =  boto3.client('sns', 'us-east-1')
jh_sns_arn = 'arn:aws:sns:us-east-1:353848682332:javahome'

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
        validate_number(event['mobile'])
        subscribe_to_sns(event['mobile'])
        return {
            'message': 'Student added succussfully'
        }
    except Exception as e:
        print(" ", e)
        response = {
            'responseCode': 500,
            'message': e
        }
        raise Exception(json.dumps(response))

def subscribe_to_sns(mobile):


    response = sns_client.subscribe(
        TopicArn=jh_sns_arn,
        Protocol="sms",
        Endpoint=mobile
    )


def validate_number(mobile):
        print(mobile)
        if len(mobile)==10:
            if mobile.startswith(' '):
                mobile = '+91' + mobile
        valid_length = [13,12]
        if mobile.startswith('+') and len(mobile) not in valid_length :
            raise Exception("Invalid Mobile Number,Enter Valid Mobile Number")

        if (len(mobile) < 10):
            print("Enter 10 digits mobile number\n")
            raise Exception("Invalid Mobile Number,Enter Valid Mobile Number")

