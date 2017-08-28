import boto3

client = boto3.client('iot')
response = client.create_topic_rule(
    ruleName='IoT_boto3',
    topicRulePayload={
        'sql': 'select * from "/health/#"',
        'description': 'IoT datapipeline',
        'actions': [
            {
                'firehose': {
                    'roleArn': 'arn:aws:iam::1234567890:role/service-role/iot.firehose',
                    'deliveryStreamName': 'iot.kinesis',
                    'separator': '\n'
                }
            },
        ],
        'ruleDisabled': True,
        'awsIotSqlVersion': '2016-03-23'
    }
)
print(response)
