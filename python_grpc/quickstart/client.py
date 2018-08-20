import grpc

# import the generated classes
from quickstart import calculator_pb2_grpc, calculator_pb2

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = calculator_pb2_grpc.CalculatorStub(channel)

# create a valid request message
number = calculator_pb2.Number(value=100)

# make the call
response = stub.SquareRoot(number)

# et voilà
print(response.value)