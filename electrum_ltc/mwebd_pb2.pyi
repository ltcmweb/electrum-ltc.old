from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class StatusRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StatusResponse(_message.Message):
    __slots__ = ("block_header_height", "mweb_header_height", "mweb_utxos_height")
    BLOCK_HEADER_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    MWEB_HEADER_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    MWEB_UTXOS_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    block_header_height: int
    mweb_header_height: int
    mweb_utxos_height: int
    def __init__(self, block_header_height: _Optional[int] = ..., mweb_header_height: _Optional[int] = ..., mweb_utxos_height: _Optional[int] = ...) -> None: ...

class UtxosRequest(_message.Message):
    __slots__ = ("from_height", "scan_secret")
    FROM_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    SCAN_SECRET_FIELD_NUMBER: _ClassVar[int]
    from_height: int
    scan_secret: bytes
    def __init__(self, from_height: _Optional[int] = ..., scan_secret: _Optional[bytes] = ...) -> None: ...

class Utxo(_message.Message):
    __slots__ = ("height", "value", "address", "output_id")
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_ID_FIELD_NUMBER: _ClassVar[int]
    height: int
    value: int
    address: str
    output_id: str
    def __init__(self, height: _Optional[int] = ..., value: _Optional[int] = ..., address: _Optional[str] = ..., output_id: _Optional[str] = ...) -> None: ...

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
    __slots__ = ("raw_tx", "scan_secret", "spend_secret", "fee_rate_per_kb")
    RAW_TX_FIELD_NUMBER: _ClassVar[int]
    SCAN_SECRET_FIELD_NUMBER: _ClassVar[int]
    SPEND_SECRET_FIELD_NUMBER: _ClassVar[int]
    FEE_RATE_PER_KB_FIELD_NUMBER: _ClassVar[int]
    raw_tx: bytes
    scan_secret: bytes
    spend_secret: bytes
    fee_rate_per_kb: int
    def __init__(self, raw_tx: _Optional[bytes] = ..., scan_secret: _Optional[bytes] = ..., spend_secret: _Optional[bytes] = ..., fee_rate_per_kb: _Optional[int] = ...) -> None: ...

class CreateResponse(_message.Message):
    __slots__ = ("raw_tx", "output_id")
    RAW_TX_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_ID_FIELD_NUMBER: _ClassVar[int]
    raw_tx: bytes
    output_id: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, raw_tx: _Optional[bytes] = ..., output_id: _Optional[_Iterable[str]] = ...) -> None: ...
