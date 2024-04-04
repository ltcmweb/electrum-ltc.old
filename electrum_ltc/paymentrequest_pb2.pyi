from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Output(_message.Message):
    __slots__ = ("amount", "script")
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    amount: int
    script: bytes
    def __init__(self, amount: _Optional[int] = ..., script: _Optional[bytes] = ...) -> None: ...

class PaymentDetails(_message.Message):
    __slots__ = ("network", "outputs", "time", "expires", "memo", "payment_url", "merchant_data")
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_FIELD_NUMBER: _ClassVar[int]
    MEMO_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_URL_FIELD_NUMBER: _ClassVar[int]
    MERCHANT_DATA_FIELD_NUMBER: _ClassVar[int]
    network: str
    outputs: _containers.RepeatedCompositeFieldContainer[Output]
    time: int
    expires: int
    memo: str
    payment_url: str
    merchant_data: bytes
    def __init__(self, network: _Optional[str] = ..., outputs: _Optional[_Iterable[_Union[Output, _Mapping]]] = ..., time: _Optional[int] = ..., expires: _Optional[int] = ..., memo: _Optional[str] = ..., payment_url: _Optional[str] = ..., merchant_data: _Optional[bytes] = ...) -> None: ...

class PaymentRequest(_message.Message):
    __slots__ = ("payment_details_version", "pki_type", "pki_data", "serialized_payment_details", "signature")
    PAYMENT_DETAILS_VERSION_FIELD_NUMBER: _ClassVar[int]
    PKI_TYPE_FIELD_NUMBER: _ClassVar[int]
    PKI_DATA_FIELD_NUMBER: _ClassVar[int]
    SERIALIZED_PAYMENT_DETAILS_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    payment_details_version: int
    pki_type: str
    pki_data: bytes
    serialized_payment_details: bytes
    signature: bytes
    def __init__(self, payment_details_version: _Optional[int] = ..., pki_type: _Optional[str] = ..., pki_data: _Optional[bytes] = ..., serialized_payment_details: _Optional[bytes] = ..., signature: _Optional[bytes] = ...) -> None: ...

class X509Certificates(_message.Message):
    __slots__ = ("certificate",)
    CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    certificate: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, certificate: _Optional[_Iterable[bytes]] = ...) -> None: ...

class Payment(_message.Message):
    __slots__ = ("merchant_data", "transactions", "refund_to", "memo")
    MERCHANT_DATA_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    REFUND_TO_FIELD_NUMBER: _ClassVar[int]
    MEMO_FIELD_NUMBER: _ClassVar[int]
    merchant_data: bytes
    transactions: _containers.RepeatedScalarFieldContainer[bytes]
    refund_to: _containers.RepeatedCompositeFieldContainer[Output]
    memo: str
    def __init__(self, merchant_data: _Optional[bytes] = ..., transactions: _Optional[_Iterable[bytes]] = ..., refund_to: _Optional[_Iterable[_Union[Output, _Mapping]]] = ..., memo: _Optional[str] = ...) -> None: ...

class PaymentACK(_message.Message):
    __slots__ = ("payment", "memo")
    PAYMENT_FIELD_NUMBER: _ClassVar[int]
    MEMO_FIELD_NUMBER: _ClassVar[int]
    payment: Payment
    memo: str
    def __init__(self, payment: _Optional[_Union[Payment, _Mapping]] = ..., memo: _Optional[str] = ...) -> None: ...
