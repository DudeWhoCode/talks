import grpc

# import the generated classes
import adder_pb2
import adder_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:8001')

# create a stub (client)
stub = adder_pb2_grpc.AdderStub(channel)

# create a valid request message
number = adder_pb2.Number(value1=5, value2=3)

# make the call
response = stub.Add(number)

# et voilà
print(response.value)