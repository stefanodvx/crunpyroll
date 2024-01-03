# Seasons

[Crunpyroll Index](../../README.md#crunpyroll-index) / [Crunpyroll](../index.md#crunpyroll) / [Types](./index.md#types) / Seasons

> Auto-generated documentation for [crunpyroll.types.seasons](https://github.com/stefanodvx/crunpyroll/blob/main/crunpyroll/types/seasons.py) module.

- [Seasons](#seasons)
  - [Season](#season)
    - [Season.parse](#seasonparse)
  - [SeasonsQuery](#seasonsquery)
    - [SeasonsQuery.parse](#seasonsqueryparse)

## Season

[Show source in seasons.py:20](https://github.com/stefanodvx/crunpyroll/blob/main/crunpyroll/types/seasons.py#L20)

#### Signature

```python
class Season(Content):
    def __init__(self, data: dict): ...
```

### Season.parse

[Show source in seasons.py:40](https://github.com/stefanodvx/crunpyroll/blob/main/crunpyroll/types/seasons.py#L40)

#### Signature

```python
@classmethod
def parse(cls, obj: dict): ...
```



## SeasonsQuery

[Show source in seasons.py:5](https://github.com/stefanodvx/crunpyroll/blob/main/crunpyroll/types/seasons.py#L5)

#### Signature

```python
class SeasonsQuery(Object):
    def __init__(self, data: dict): ...
```

### SeasonsQuery.parse

[Show source in seasons.py:10](https://github.com/stefanodvx/crunpyroll/blob/main/crunpyroll/types/seasons.py#L10)

#### Signature

```python
@classmethod
def parse(cls, obj: dict): ...
```