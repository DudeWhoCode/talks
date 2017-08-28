import boto3

client = boto3.client('firehose')
response = client.create_delivery_stream(
    DeliveryStreamName='iot_boto3',
    S3DestinationConfiguration={
        'RoleARN': 'arn:aws:iam::1234567890:role/firehose_delivery_role',
        'BucketARN': 'arn:aws:s3:::pydata.iot.pipeline',
        'Prefix': 'string',
        'BufferingHints': {
            'SizeInMBs': 5,
            'IntervalInSeconds': 300
        },
        'CompressionFormat': 'UNCOMPRESSED',
        'EncryptionConfiguration': {
            'NoEncryptionConfig': 'NoEncryption',
        },
    },
)
print(response)
