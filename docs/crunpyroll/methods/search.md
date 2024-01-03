# Search

[Crunpyroll Index](../../README.md#crunpyroll-index) / [Crunpyroll](../index.md#crunpyroll) / [Methods](./index.md#methods) / Search

> Auto-generated documentation for [crunpyroll.methods.search](https://github.com/stefanodvx/crunpyroll/blob/main/crunpyroll/methods/search.py) module.

- [Search](#search)
  - [Search](#search-1)
    - [Search().search](#search()search)

## Search

[Show source in search.py:6](https://github.com/stefanodvx/crunpyroll/blob/main/crunpyroll/methods/search.py#L6)

#### Signature

```python
class Search: ...
```

### Search().search

[Show source in search.py:7](https://github.com/stefanodvx/crunpyroll/blob/main/crunpyroll/methods/search.py#L7)

#### Signature

```python
async def search(
    self: "crunpyroll.Client",
    query: str,
    max_results: int = 6,
    locale: str = None,
    filters: list["enums.ContentType"] = [
        enums.ContentType.SERIES,
        enums.ContentType.MOVIE_LISTING,
        enums.ContentType.EPISODE,
        enums.ContentType.MUSIC,
    ],
) -> "types.SearchQuery": ...
```