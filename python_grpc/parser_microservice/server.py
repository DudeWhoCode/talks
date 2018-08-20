import grpc
from concurrent import futures
import time
# import the generated classes
import parser_pb2
import parser_pb2_grpc

# import the original calculator.py
import parser

# create a class to define the server functions, derived from
# calculator_pb2_grpc.CalculatorServicer
class ParserServicer(parser_pb2_grpc.ParserServicer):

    # calculator.square_root is exposed here
    # the request and response are of the data type
    # calculator_pb2.Number
    def Parse(self, request, context):
        response = parser_pb2.Result()
        response.value = parser.parse(request.value)
        return response

    # def SquareRoot(self, request, context):
    #     response = calculator_pb2.Number()
    #     response.value = calculator.square_root(request.value)
    #     return response


# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_CalculatorServicer_to_server`
# to add the defined class to the server
parser_pb2_grpc.add_ParserServicer_to_server(
    ParserServicer(), server)

# listen on port 50051
print('Starting server. Listening on port 8000.')
server.add_insecure_port('[::]:8000')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)