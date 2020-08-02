from pathlib import Path
import tempfile, os, shutil
import importlib.util
from google.protobuf.internal import encoder
from google.protobuf.internal import decoder

class Backend:
    def __init__(self, schemafile):
        self.tmp = tempfile.TemporaryDirectory()
        tmp_schemafile = self.tmp.name + "/schema.proto"
        shutil.copy(schemafile, tmp_schemafile)
        os.system(
            f"protoc --python_out={self.tmp.name} -I {self.tmp.name} schema.proto"
        )

    def target_cls(self, target):
        spec = importlib.util.spec_from_file_location(
            target, self.tmp.name + "/schema_pb2.py"
        )
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
        data = f.read()
        pos = 0
        while pos < len(data):
            size, pos = decoder._DecodeVarint32(data, pos)
            message = message.FromString(data[pos:pos+size])
            pos += size
            yield message
