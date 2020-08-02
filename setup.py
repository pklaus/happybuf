from setuptools import setup

setup(
    name='happybuf',
    version='0.1.dev0',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'flatbuffers',
        'protobuf',
        'pycapnp',
    ],
    packages=[
        'happybuf',
        'happybuf.capnproto',
        'happybuf.flatbuffers',
        'happybuf.protobuf',
    ],
)
