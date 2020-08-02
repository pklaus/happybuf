"""
Contains code from https://stackoverflow.com/a/34539706/183995
and https://stackoverflow.com/a/59073600/183995
"""

from pathlib import Path
import tempfile, os, shutil
import importlib.util
from google.protobuf.internal import encoder
from google.protobuf.internal import decoder


def getSize(raw_varint32):
    result, shift = 0, 0
    b = raw_varint32[0]
    result |= (b & 0x7f) << shift
    return result

def readRawVarint32(stream):
    mask = 0x80 # (1 << 7)
    raw_varint32 = b""
    while 1:
        b = stream.read(1)
        if len(b) == 0:
            break
        raw_varint32 += b
        if not (ord(b) & mask):
            #we found a byte starting with a 0, which means it's the last byte of this varint
            break
    return raw_varint32

class Backend:
    def __init__(self, schemafile):
        self.tmp = tempfile.TemporaryDirectory()
        tmp_schemafile = self.tmp.name + "/schema.proto"
        shutil.copy(schemafile, tmp_schemafile)
        os.system(f"protoc --python_out={self.tmp.name} -I {self.tmp.name} schema.proto")

    def target_cls(self, target):
        spec = importlib.util.spec_from_file_location(target, self.tmp.name + "/schema_pb2.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        Cls = getattr(module, target)
        return Cls

    def write(self, f, target, data):
        message = self.target_cls(target)()
        for key, value in data.items():
            setattr(message, key, value)
            # HERE, we would have to treat the nested stuff properly...
            # (list of phone numbers, to be added as list of address_book.Phone.PhoneT))
        message_str = message.SerializeToString()
        delimiter = encoder._VarintBytes(len(message_str))
        f.write(delimiter + message_str)

    def read_multiple(self, f, target):
        message = self.target_cls(target)()
        while raw_varint32 := readRawVarint32(f):
            if raw_varint32:
                size = getSize(raw_varint32)
                data = f.read(size)
                if len(data) < size:
                    raise Exception("Unexpected end of file")
                message = message.FromString(data)
            yield message


