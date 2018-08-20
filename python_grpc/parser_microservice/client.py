import grpc

# import the generated classes
import parser_pb2
import parser_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:8000')

# create a stub (client)
stub = parser_pb2_grpc.ParserStub(channel)

# create a valid request message
number = parser_pb2.Expression(value="1+4")

# make the call
response = stub.Parse(number)

# et voilà
print(response.value)