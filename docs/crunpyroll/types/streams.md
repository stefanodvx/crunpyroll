# Streams

[Crunpyroll Index](../../README.md#crunpyroll-index) / [Crunpyroll](../index.md#crunpyroll) / [Types](./index.md#types) / Streams

> Auto-generated documentation for [crunpyroll.types.streams](https://github.com/stefanodvx/crunpyroll/blob/main/crunpyroll/types/streams.py) module.

- [Streams](#streams)
  - [MediaStreams](#mediastreams)
    - [MediaStreams.parse](#mediastreamsparse)

## MediaStreams

[Show source in streams.py:5](https://github.com/stefanodvx/crunpyroll/blob/main/crunpyroll/types/streams.py#L5)

#### Signature

```python
class MediaStreams(Object):
    def __init__(self, data: dict): ...
```

### MediaStreams.parse

[Show source in streams.py:14](https://github.com/stefanodvx/crunpyroll/blob/main/crunpyroll/types/streams.py#L14)

#### Signature

```python
@classmethod
def parse(cls, obj: dict, media_id: str): ...
```