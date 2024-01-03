# Episodes

[Crunpyroll Index](../../README.md#crunpyroll-index) / [Crunpyroll](../index.md#crunpyroll) / [Types](./index.md#types) / Episodes

> Auto-generated documentation for [crunpyroll.types.episodes](https://github.com/stefanodvx/crunpyroll/blob/main/crunpyroll/types/episodes.py) module.

- [Episodes](#episodes)
  - [Episode](#episode)
    - [Episode.parse](#episodeparse)
  - [EpisodesQuery](#episodesquery)
    - [EpisodesQuery.parse](#episodesqueryparse)

## Episode

[Show source in episodes.py:24](https://github.com/stefanodvx/crunpyroll/blob/main/crunpyroll/types/episodes.py#L24)

#### Signature

```python
class Episode(Content):
    def __init__(self, data: dict): ...
```

### Episode.parse

[Show source in episodes.py:59](https://github.com/stefanodvx/crunpyroll/blob/main/crunpyroll/types/episodes.py#L59)

#### Signature

```python
@classmethod
def parse(cls, obj: dict): ...
```



## EpisodesQuery

[Show source in episodes.py:9](https://github.com/stefanodvx/crunpyroll/blob/main/crunpyroll/types/episodes.py#L9)

#### Signature

```python
class EpisodesQuery(Object):
    def __init__(self, data: dict): ...
```

### EpisodesQuery.parse

[Show source in episodes.py:14](https://github.com/stefanodvx/crunpyroll/blob/main/crunpyroll/types/episodes.py#L14)

#### Signature

```python
@classmethod
def parse(cls, obj: dict): ...
```