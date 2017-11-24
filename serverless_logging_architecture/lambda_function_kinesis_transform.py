from __future__ import print_function

import base64

print('Loading function')


def lambda_handler(event, context):
    output = []

    for record in event['records']:
        payload = base64.b64decode(record['data'])
        
        # manipulate the log payload
        service = payload.get('service')
        if service == 'batman':
        	# modify the payload
        # You should stick with the following kinesis transform output format for kinesis to pickup the data
        output_record = {
            'recordId': record['recordId'],
            'result': 'Ok',
            'data': base64.b64encode(payload)
        }
        output.append(output_record)

    print('Successfully processed {} records.'.format(len(event['records'])))

    return {'records': output}