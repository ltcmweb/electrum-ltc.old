from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class StatusRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StatusResponse(_message.Message):
    __slots__ = ("block_header_height", "mweb_header_height", "mweb_utxos_height", "block_time")
    BLOCK_HEADER_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    MWEB_HEADER_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    MWEB_UTXOS_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    BLOCK_TIME_FIELD_NUMBER: _ClassVar[int]
    block_header_height: int
    mweb_header_height: int
    mweb_utxos_height: int
    block_time: int
    def __init__(self, block_header_height: _Optional[int] = ..., mweb_header_height: _Optional[int] = ..., mweb_utxos_height: _Optional[int] = ..., block_time: _Optional[int] = ...) -> None: ...

class UtxosRequest(_message.Message):
    __slots__ = ("from_height", "scan_secret")
    FROM_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    SCAN_SECRET_FIELD_NUMBER: _ClassVar[int]
    from_height: int
    scan_secret: bytes
    def __init__(self, from_height: _Optional[int] = ..., scan_secret: _Optional[bytes] = ...) -> None: ...

class Utxo(_message.Message):
    __slots__ = ("height", "value", "address", "output_id", "block_time")
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_ID_FIELD_NUMBER: _ClassVar[int]
    BLOCK_TIME_FIELD_NUMBER: _ClassVar[int]
    height: int
    value: int
    address: str
    output_id: str
    block_time: int
    def __init__(self, height: _Optional[int] = ..., value: _Optional[int] = ..., address: _Optional[str] = ..., output_id: _Optional[str] = ..., block_time: _Optional[int] = ...) -> None: ...

class AddressRequest(_message.Message):
    __slots__ = ("from_index", "to_index", "scan_secret", "spend_pubkey")
    FROM_INDEX_FIELD_NUMBER: _ClassVar[int]
    TO_INDEX_FIELD_NUMBER: _ClassVar[int]
    SCAN_SECRET_FIELD_NUMBER: _ClassVar[int]
    SPEND_PUBKEY_FIELD_NUMBER: _ClassVar[int]
    from_index: int
    to_index: int
    scan_secret: bytes
    spend_pubkey: bytes
    def __init__(self, from_index: _Optional[int] = ..., to_index: _Optional[int] = ..., scan_secret: _Optional[bytes] = ..., spend_pubkey: _Optional[bytes] = ...) -> None: ...

class AddressResponse(_message.Message):
    __slots__ = ("address",)
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    address: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, address: _Optional[_Iterable[str]] = ...) -> None: ...

class LedgerApdu(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    def __init__(self, data: _Optional[bytes] = ...) -> None: ...

class SpentRequest(_message.Message):
    __slots__ = ("output_id",)
    OUTPUT_ID_FIELD_NUMBER: _ClassVar[int]
    output_id: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, output_id: _Optional[_Iterable[str]] = ...) -> None: ...

class SpentResponse(_message.Message):
    __slots__ = ("output_id",)
    OUTPUT_ID_FIELD_NUMBER: _ClassVar[int]
    output_id: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, output_id: _Optional[_Iterable[str]] = ...) -> None: ...

class CreateRequest(_message.Message):
    __slots__ = ("raw_tx", "scan_secret", "spend_secret", "fee_rate_per_kb", "dry_run")
    RAW_TX_FIELD_NUMBER: _ClassVar[int]
    SCAN_SECRET_FIELD_NUMBER: _ClassVar[int]
    SPEND_SECRET_FIELD_NUMBER: _ClassVar[int]
    FEE_RATE_PER_KB_FIELD_NUMBER: _ClassVar[int]
    DRY_RUN_FIELD_NUMBER: _ClassVar[int]
    raw_tx: bytes
    scan_secret: bytes
    spend_secret: bytes
    fee_rate_per_kb: int
    dry_run: bool
    def __init__(self, raw_tx: _Optional[bytes] = ..., scan_secret: _Optional[bytes] = ..., spend_secret: _Optional[bytes] = ..., fee_rate_per_kb: _Optional[int] = ..., dry_run: bool = ...) -> None: ...

class CreateResponse(_message.Message):
    __slots__ = ("raw_tx", "output_id")
    RAW_TX_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_ID_FIELD_NUMBER: _ClassVar[int]
    raw_tx: bytes
    output_id: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, raw_tx: _Optional[bytes] = ..., output_id: _Optional[_Iterable[str]] = ...) -> None: ...

class BroadcastRequest(_message.Message):
    __slots__ = ("raw_tx",)
    RAW_TX_FIELD_NUMBER: _ClassVar[int]
    raw_tx: bytes
    def __init__(self, raw_tx: _Optional[bytes] = ...) -> None: ...

class BroadcastResponse(_message.Message):
    __slots__ = ("txid",)
    TXID_FIELD_NUMBER: _ClassVar[int]
    txid: str
    def __init__(self, txid: _Optional[str] = ...) -> None: ...

class CoinswapRequest(_message.Message):
    __slots__ = ("scan_secret", "spend_secret", "output_id", "addr_index")
    SCAN_SECRET_FIELD_NUMBER: _ClassVar[int]
    SPEND_SECRET_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_ID_FIELD_NUMBER: _ClassVar[int]
    ADDR_INDEX_FIELD_NUMBER: _ClassVar[int]
    scan_secret: bytes
    spend_secret: bytes
    output_id: str
    addr_index: int
    def __init__(self, scan_secret: _Optional[bytes] = ..., spend_secret: _Optional[bytes] = ..., output_id: _Optional[str] = ..., addr_index: _Optional[int] = ...) -> None: ...

class CoinswapResponse(_message.Message):
    __slots__ = ("output_id",)
    OUTPUT_ID_FIELD_NUMBER: _ClassVar[int]
    output_id: str
    def __init__(self, output_id: _Optional[str] = ...) -> None: ...
