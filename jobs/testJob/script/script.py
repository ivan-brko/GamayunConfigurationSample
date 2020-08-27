import GamayunResult_pb2_grpc
import GamayunResult_pb2
import grpc


channel = grpc.insecure_channel('localhost:16656')
stub = GamayunResult_pb2_grpc.ResultStub(channel)

valid_json = """
{
   "value":"balbalba"
}
"""

res = GamayunResult_pb2.TaskResult(jobId = "Test", results = ["test", "AnotherTest", valid_json])

result = stub.ReportResult(res)