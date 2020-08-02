
from typing import List, Union

#from .protobuf import Backend as ProtoBackend
#from .flatbuffers import Backend as FlatBackend
#from .capnproto import Backend as CapnBackend

class Happybuf:
    def __init__(self, schema, backend=None):
        self.b = backend(schema)

    def write(self, f, target, data):
        self.b.write(f, target, data)

    def write_multiple(self, f, target, data: List):
        self.b.write_multiple(f, target, data)

    def read_multiple(self, f, target):
        return self.b.read_multiple(f, target)
