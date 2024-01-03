# Search

[Crunpyroll Index](../../README.md#crunpyroll-index) / [Crunpyroll](../index.md#crunpyroll) / [Types](./index.md#types) / Search

> Auto-generated documentation for [crunpyroll.types.search](https://github.com/stefanodvx/crunpyroll/blob/main/crunpyroll/types/search.py) module.

- [Search](#search)
  - [SearchQuery](#searchquery)
    - [SearchQuery.parse](#searchqueryparse)

## SearchQuery

[Show source in search.py:8](https://github.com/stefanodvx/crunpyroll/blob/main/crunpyroll/types/search.py#L8)

#### Signature

```python
class SearchQuery(Object):
    def __init__(self, total: int, items: list): ...
```

### SearchQuery.parse

[Show source in search.py:17](https://github.com/stefanodvx/crunpyroll/blob/main/crunpyroll/types/search.py#L17)

#### Signature

```python
@classmethod
def parse(cls, response: dict): ...
```