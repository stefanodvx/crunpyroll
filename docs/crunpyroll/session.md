# Session

[Crunpyroll Index](../README.md#crunpyroll-index) / [Crunpyroll](./index.md#crunpyroll) / Session

> Auto-generated documentation for [crunpyroll.session](https://github.com/stefanodvx/crunpyroll/blob/main/crunpyroll/session.py) module.

- [Session](#session)
  - [Session](#session-1)
    - [Session().authorization_header](#session()authorization_header)
    - [Session().authorize](#session()authorize)
    - [Session().is_authorized](#session()is_authorized)
    - [Session().refresh](#session()refresh)
    - [Session().retrieve](#session()retrieve)

## Session

[Show source in session.py:15](https://github.com/stefanodvx/crunpyroll/blob/main/crunpyroll/session.py#L15)

#### Signature

```python
class Session:
    def __init__(self, client: "crunpyroll.Client"): ...
```

### Session().authorization_header

[Show source in session.py:30](https://github.com/stefanodvx/crunpyroll/blob/main/crunpyroll/session.py#L30)

#### Signature

```python
@property
def authorization_header(self): ...
```

### Session().authorize

[Show source in session.py:41](https://github.com/stefanodvx/crunpyroll/blob/main/crunpyroll/session.py#L41)

#### Signature

```python
async def authorize(self) -> bool | None: ...
```

### Session().is_authorized

[Show source in session.py:26](https://github.com/stefanodvx/crunpyroll/blob/main/crunpyroll/session.py#L26)

#### Signature

```python
@property
def is_authorized(self): ...
```

### Session().refresh

[Show source in session.py:65](https://github.com/stefanodvx/crunpyroll/blob/main/crunpyroll/session.py#L65)

#### Signature

```python
async def refresh(self) -> bool | None: ...
```

### Session().retrieve

[Show source in session.py:34](https://github.com/stefanodvx/crunpyroll/blob/main/crunpyroll/session.py#L34)

#### Signature

```python
async def retrieve(self) -> None: ...
```