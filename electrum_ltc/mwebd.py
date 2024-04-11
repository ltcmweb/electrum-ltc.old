import grpc

from .bitcoin import is_mweb_address
from .transaction import PartialTransaction, Transaction
from .mwebd_pb2 import CreateRequest
from .mwebd_pb2_grpc import RpcStub

def stub():
    return RpcStub(grpc.insecure_channel('127.0.0.1:12345'))

def stub_async():
    return RpcStub(grpc.aio.insecure_channel('127.0.0.1:12345'))

def create(tx, scan_secret, spend_secret, fee_estimator, *, dry_run = False):
    raw_tx = bytes.fromhex(tx.serialize_to_network(include_sigs=False))
    resp = stub().Create(CreateRequest(raw_tx=raw_tx,
        scan_secret=scan_secret, spend_secret=spend_secret,
        fee_rate_per_kb=fee_estimator(1000), dry_run=dry_run))
    if resp.raw_tx == raw_tx: return tx, 0
    tx2 = PartialTransaction.from_tx(Transaction(resp.raw_tx))
    for i, txin in enumerate(tx2.inputs()):
        tx2.inputs()[i] = next(x for x in tx.inputs() if str(x.prevout) == str(txin.prevout))
    mweb_input = tx.input_value() - tx2.input_value()
    expected_pegin = max(0, tx.output_value() - mweb_input)
    fee_increase = tx2.output_value() - expected_pegin
    if expected_pegin: fee_increase += fee_estimator(41)
    for txout in tx.outputs():
        if is_mweb_address(txout.address) and not dry_run:
            tx2._mweb_output_ids[resp.output_id.pop(0)] = txout
    if dry_run: tx2._extra_bytes = b''
    return tx2, fee_increase
