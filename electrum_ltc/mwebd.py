import grpc
from .mwebd_pb2_grpc import RpcStub

def stub():
    return RpcStub(grpc.insecure_channel('localhost:12345'))

def stub_async():
    return RpcStub(grpc.aio.insecure_channel('localhost:12345'))
