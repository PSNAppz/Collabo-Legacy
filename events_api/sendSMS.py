import boto3
from django.conf import settings
# Create an SNS client

def SendMessage(number,message):
    try:
        print(number)
        client = boto3.client(
            "sns",
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID_SAL[0],
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY_SAL[0],
            region_name=settings.REGION_NAME[0]

        )


        message_attributes = {'AWS.SNS.SMS.SMSType': {'DataType': 'String', 'StringValue': 'Transactional'},
                              }

        # Send your sms message.
        some_list_of_contacts = [number,]

        for number in some_list_of_contacts:
            print(number)
            client.publish(
                PhoneNumber=str(number),
                Message=str(message),
                MessageAttributes=message_attributes

            )
            sms={"sms":"message sent succsfully"}
        return (sms)
    except Exception as e:

        e={"error":"error in sending sms"}
        return (e)

# `message_attributes = {'AWS.SNS.SMS.SMSType': {'DataType': 'String', 'StringValue': 'Transactional'}}` (edited)

# `MessageAttributes=message_attributes`