class Backend:
    def __init__(self, schema):
        import capnp

        capnp.remove_import_hook()
        self.schema = capnp.load(schema)

    def create(self, target, data):
        target = getattr(self.schema, target)
        return target.new_message(**data)

    def write(self, f, target, data):
        target = getattr(self.schema, target)
        dat = target.new_message(**data)
        dat.write(f)

    def read_multiple(self, f, target):
        target = getattr(self.schema, target)
        for el in target.read_multiple(f):
            yield el
