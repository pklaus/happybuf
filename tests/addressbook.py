#!/usr/bin/env python

from happybuf import Happybuf

from happybuf.capnproto import Backend as CapnBackend

hb = Happybuf(schema="schemas/addressbook.capnp", backend=CapnBackend)
with open("example_capnproto.bin", "w+b") as f:
    hb.write(f, "Person", dict(id=1, name="Roland", email="test@example.com"))
    hb.write(f, "Person", dict(id=2, name="Reinhard", email="test@example.com"))
    hb.write(f, "Person", dict(id=3, name="Rydberg", email="test@example.com"))
with open("example_capnproto.bin", "rb") as f:
    print(list(hb.read_multiple(f, "Person")))


from happybuf.flatbuffers import Backend as FlatBackend

hb = Happybuf(schema="schemas/addressbook.fbs", backend=FlatBackend)
with open("example_flatbuffers.bin", "w+b") as f:
    hb.write(f, "address_book.Person.PersonT", dict(id=1, name="Roland", email="test@example.com"))
    hb.write(f, "address_book.Person.PersonT", dict(id=2, name="Reinhard", email="test@example.com"))
    hb.write(f, "address_book.Person.PersonT", dict(id=3, name="Rydberg", email="test@example.com"))
with open("example_flatbuffers.bin", "rb") as f:
    for person in hb.read_multiple(f, "address_book.Person.Person"):
        print(f"Person: {person.Id()} {person.Name()} {person.Email()}")


from happybuf.protobuf import Backend as ProtoBackend

hb = Happybuf(schema="schemas/addressbook.proto", backend=ProtoBackend)
with open("example_protobuf.bin", "w+b") as f:
    hb.write(f, "Person", dict(id=1, name="Roland", email="test@example.com"))
    hb.write(f, "Person", dict(id=2, name="Reinhard", email="test@example.com"))
    hb.write(f, "Person", dict(id=3, name="Rydberg", email="test@example.com"))
with open("example_protobuf.bin", "rb") as f:
    for person in hb.read_multiple(f, "Person"):
        print(f"Person: {person.id=} {person.name=} {person.email=}")
