import boto3

s3 = boto3.resource('s3')
bucket = s3.Bucket('pydata.iot.serverless')
response = bucket.create(
    ACL='private',
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-southeast-1'
    },
)
print response
