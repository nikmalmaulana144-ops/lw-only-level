# -*- coding: utf-8 -*-
"""
Compatibility shim.
Semua message class sebenarnya didefinisikan di thunderFF_pb2.
"""
from thunderFF_pb2 import *  # noqa: F401,F403
from thunderFF_pb2 import (  # noqa: F401
    DESCRIPTOR,
    MajorLoginReq,
    MajorLoginGameSecurity,
    MajorLoginRes,
    GetLoginDataRes,
    StartMatch,
)