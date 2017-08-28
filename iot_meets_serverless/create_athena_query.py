import boto3

client = boto3.client('athena')
response = client.create_named_query(
    Name='iot_boto3',
    Description='create table from heart rate data',
    Database='default',
    QueryString="""CREATE EXTERNAL TABLE heartrate_iot_data (
    heartRate int,
    userId string,
    rateType string,
    dateTime timestamp)
    ROW FORMAT  serde 'org.apache.hive.hcatalog.data.JsonSerDe'
    with serdeproperties( 'ignore.malformed.json' = 'true' )
    LOCATION 's3://pydata.iot.pipeline/heartrate_data/'""",
)
print(response)
