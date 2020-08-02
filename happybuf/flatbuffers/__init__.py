from pathlib import Path
import tempfile, os
import importlib.util
import flatbuffers
from flatbuffers.packer import int32


class Backend:
    def __init__(self, schema):
        self.tmp = tempfile.TemporaryDirectory()
        os.system(f"flatc --python --gen-object-api -o {self.tmp.name} {schema}")

    def target_cls(self, target):
        module, _, cls = target.rpartition(".")
        module_file = module.replace(".", "/") + ".py"
        spec = importlib.util.spec_from_file_location(
            target, Path(self.tmp.name) / Path(module_file)
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        Cls = getattr(module, cls)
        return Cls

    def write(self, f, target, data):
        target = self.target_cls(target)()
        builder = flatbuffers.Builder(1024)

        for key, value in data.items():
            setattr(target, key, value)
            # HERE, we would have to treat the nested stuff properly...
            # (list of phone numbers, to be added as list of address_book.Phone.PhoneT))

        builder.FinishSizePrefixed(target.Pack(builder))
        buf = builder.Output()
        f.write(buf)

    def read_multiple(self, f, target):
        buf = f.read()
        offset = 0
        target = self.target_cls(target)()
        while len(buf[offset:]) > 4:
            bufsize = int32.unpack(buf[offset : offset + int32.size])[0]
            target = getattr(target, f"GetRootAs{target.__class__.__name__}")(
                buf, offset + int32.size
            )
            offset += int32.size + bufsize
            yield target
