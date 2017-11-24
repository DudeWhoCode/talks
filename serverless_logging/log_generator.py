import json
import boto3
import calendar
import random
from random import randrange
from datetime import timedelta, datetime

my_stream_name = 'serverlessLog-test'
kinesis_client = boto3.client('kinesis', region_name='us-east-1')
micro_services = ['robin', 'watchtower', 'batman', 'nightwing', 'gordon', 'joker', 'gcpd']
responses = [200, 403, 404, 500]
clients = ['amazon', 'flipkart', 'jabong', 'myntra', 'levis', 'ebay', 'aliexpress', 'alibaba']

class Randomizer(object):
	def __init__(self, start, end):
		self.start = start
		self.end = end

	def get_randlog(self):
	    """
	    This function will return a random datetime between two datetime 
	    objects.
	    """
	    delta = self.end - self.start
	    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
	    random_second = randrange(int_delta)
	    time_obj = self.start + timedelta(seconds=random_second)
	    dt = datetime.strftime(time_obj, "%Y-%m-%d %H:%M:%S")
	    log_obj = dict()
	    log_obj['service'] = random.sample(micro_services, 1)[0]
	    log_obj['response'] = random.sample(responses, 1)[0]
	    log_obj['created_at'] = dt
	    log_obj['client'] = random.sample(clients, 1)[0]
	    log_obj['latency'] = random.uniform(10.2, 200.5)
	    return log_obj

def put_to_stream(thing_id, property_value):
    put_response = kinesis_client.put_record(
                        StreamName=my_stream_name,
                        Data=json.dumps(property_value),
                        PartitionKey=thing_id)
    print(put_response)

d1 = datetime.strptime('7/1/2017 1:30 PM', '%m/%d/%Y %I:%M %p')
d2 = datetime.strptime('11/18/2017 4:50 AM', '%m/%d/%Y %I:%M %p')
generator = Randomizer(d1, d2)

while True:
	log = generator.get_randlog()
	property_value = log
	thing_id = '1234'
	put_to_stream(thing_id, property_value)