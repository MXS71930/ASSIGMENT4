import boto3
import configparser

# Load configuration settings from config.ini file
config = configparser.ConfigParser()
config.read('config.ini')
topic_name = config['DEFAULT']['topic_name']
email_address1 = config['DEFAULT']['email_address1']
email_address2 = config['DEFAULT']['email_address2']

# Create an SNS client
sns_client = boto3.client('sns')

# Create a new SNS topic
response = sns_client.create_topic(Name=topic_name)
topic_arn = response['TopicArn']
print(f"Created SNS topic {topic_name} with ARN {topic_arn}")

# Subscribe email_address1 to the SNS topic
response = sns_client.subscribe(
    TopicArn=topic_arn,
    Protocol='email',
    Endpoint=email_address1
)
print(f"Subscribed {email_address1} to SNS topic {topic_name}")

# Subscribe email_address2 to the SNS topic
response = sns_client.subscribe(
    TopicArn=topic_arn,
    Protocol='email',
    Endpoint=email_address2
)
print(f"Subscribed {email_address2} to SNS topic {topic_name}")





