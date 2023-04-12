import boto3

sns = boto3.client('sns')

# Create a new SNS topic
response = sns.create_topic(Name='reyaantopic-assigment2')

# Get the ARN of the topic that was created
topic_arn = response['TopicArn']




