import grpc
from concurrent import futures
import time
# import the generated classes
import adder_pb2
import adder_pb2_grpc

# import the original calculator.py
import adder

# create a class to define the server functions, derived from
# calculator_pb2_grpc.CalculatorServicer
class AdderServicer(adder_pb2_grpc.AdderServicer):

    # calculator.square_root is exposed here
    # the request and response are of the data type
    # calculator_pb2.Number
    def Add(self, request, context):
        response = adder_pb2.AddedResult()
        response.value = adder.add(request.value1, request.value2)
        return response

    # def SquareRoot(self, request, context):
    #     response = calculator_pb2.Number()
    #     response.value = calculator.square_root(request.value)
    #     return response


# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_CalculatorServicer_to_server`
# to add the defined class to the server
adder_pb2_grpc.add_AdderServicer_to_server(
    AdderServicer(), server)

# listen on port 50051
print('Starting server. Listening on port 8001.')
server.add_insecure_port('[::]:8001')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)