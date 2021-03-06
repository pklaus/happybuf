# happybuf - **H**appy **Ap**pendable **Py**thon **Buf**fers

*An abstraction layer for multiple popular serialization formats:*

* [Protocol Buffers][]
* [Cap'n Proto][]
* [FlatBuffers][]

This package is an exploration of different serialization formats/libraries
regarding their support of appending (chaining) multiple messages.
This can be useful when storing serialized data in a binary file that is
supposed to grow over time.

Further libs: [MessagePack][], [Arrow][], ...

------

While developing, those general resources for using the different backend libs with Python are useful:

* Protocol Buffers:
    * <https://googleapis.dev/python/protobuf/latest/>
    * <https://developers.google.com/protocol-buffers/docs/reference/python-generated>
    * <https://github.com/protocolbuffers/protobuf/tree/master/python>
    * <https://developers.google.com/protocol-buffers/docs/pythontutorial>
* Cap'n Proto:
    * <https://github.com/capnproto/pycapnp>
    * <https://capnproto.github.io/pycapnp/>
* FlatBuffers:
    * <https://google.github.io/flatbuffers/flatbuffers_guide_tutorial.html> -> select *Python*
    * <https://google.github.io/flatbuffers/flatbuffers_guide_use_python.html>
    * <https://google.github.io/flatbuffers/flatbuffers_support.html>
    * <https://github.com/google/flatbuffers/blob/master/samples/sample_binary.py>

[Protocol Buffers]: https://developers.google.com/protocol-buffers/
[Cap'n Proto]: https://capnproto.org/
[FlatBuffers]: https://google.github.io/flatbuffers/
[MessagePack]: https://msgpack.org/
[arrow]: https://arrow.apache.org/docs/python/data.html#schemas

------

If your project doesn't depend on minimal binary storage (in terms of file size),
or on one of those big cross-platform serialization libraries from above,
serializing to **JSON** and appending to a [JSON Lines](http://jsonlines.org/) file
might be an option, too.
It's human readable, many serialization libs exist like [serpy](https://github.com/clarkduvall/serpy).
And you can still compress the output stream using lz4 if you need to save storage space.

------

Some more Python libs I found interesting while doing research
(not necessarily related to this project):

* [protobuf-serialization](https://github.com/alvinchow86/protobuf-serialization-py)
