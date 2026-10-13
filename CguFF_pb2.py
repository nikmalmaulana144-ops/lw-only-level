# -*- coding: utf-8 -*-
"""
Compatibility shim.
Semua message class sebenarnya didefinisikan di thunderFF_pb2.
File ini hanya me-re-export agar `import CguFF_pb2` tetap bekerja tanpa
bentrok descriptor pool protobuf.
"""
from thunderFF_pb2 import *  # noqa: F401,F403
from thunderFF_pb2 import (  # noqa: F401  (eksplisit, agar editor/IDE happy)
    DESCRIPTOR,
    MajorLoginReq,
    MajorLoginGameSecurity,
    MajorLoginRes,
    GetLoginDataRes,
    StartMatch,
)