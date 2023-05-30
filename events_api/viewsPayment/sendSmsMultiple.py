import boto3

# Create an SNS client
client = boto3.client(
    "sns",
    aws_access_key_id="AKIAJX7MQLBOPMRNKC6A",
    aws_secret_access_key="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",
    region_name="ap-southeast-1",
)

# Create the topic if it doesn't exist (this is idempotent)
topic = client.create_topic(Name="notifications")
topic_arn = topic['TopicArn']  # get its Amazon Resource Name
some_list_of_contacts=["919947267251","919496337251"]
# Add SMS Subscribers
for number in some_list_of_contacts:
    client.subscribe(
        TopicArn=topic_arn,
        Protocol='sms',
        Endpoint=number  # <-- number who'll receive an SMS message.
    )

# Publish a message.
client.publish(Message="Saloon test!", TopicArn=topic_arn)
