# happybuf - **H**appy **Ap**pendable **Py**thon **Buf**fers

*An abstraction layer for multiple popular serialization formats:*

* [Protocol Buffers][]
* [Cap'n Proto][]
* [FlatBuffers][]

This package is an exploration of different serialization formats/libraries
regarding their support of appending (chaining) multiple messages.
This can be useful when storing serialized data in a binary file that is
supposed to grow over time.

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

------

Some more Python libs I found interesting while doing research
(not necessarily related to this project):

* [protobuf-serialization](https://github.com/alvinchow86/protobuf-serialization-py)
* [serpy](https://github.com/clarkduvall/serpy)
