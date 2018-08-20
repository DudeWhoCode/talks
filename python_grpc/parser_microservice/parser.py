import grpc

# import the generated classes
import adder_pb2
import adder_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:8001')

# create a stub (client)
stub = adder_pb2_grpc.AdderStub(channel)


def parse(e):
    print("Parsing expression: ", e)
    if '+' in e:
        inputs = e.split('+')
        a = inputs[0].strip()
        b = inputs[1].strip()
        a = int(a)
        b = int(b)
        # create a valid request message
        number = adder_pb2.Number(value1=a, value2=b)

        # make the call
        response = stub.Add(number)

        return response.value
