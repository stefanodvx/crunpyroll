# Client

[Crunpyroll Index](../README.md#crunpyroll-index) / [Crunpyroll](./index.md#crunpyroll) / Client

> Auto-generated documentation for [crunpyroll.client](https://github.com/stefanodvx/crunpyroll/blob/main/crunpyroll/client.py) module.

- [Client](#client)
  - [Client](#client-1)
    - [Client().api_request](#client()api_request)
    - [Client().manifest_request](#client()manifest_request)
    - [Client.parse_response](#clientparse_response)
    - [Client().start](#client()start)

## Client

[Show source in client.py:14](https://github.com/stefanodvx/crunpyroll/blob/main/crunpyroll/client.py#L14)

Initialize Crunchyroll Client

#### Arguments

email (``str``):
    Email or username of the account
password (``str``):
    Password of the account
locale (``str``, optional):
    The language to use in Crunchyroll
    - `E.g.` - en-US, it-IT...
    Default to en-US
proxies (``dict | str``, optional):
    Proxies for Crunchyroll
    - `E.g.` - https://0.0.0.0:8080 or {"https://": "0.0.0.0:8080"}

#### Signature

```python
class Client(Object, Methods):
    def __init__(
        self,
        email: str,
        password: str,
        locale: str = "en-US",
        proxies: dict | str = None,
    ) -> None: ...
```

### Client().api_request

[Show source in client.py:68](https://github.com/stefanodvx/crunpyroll/blob/main/crunpyroll/client.py#L68)

#### Signature

```python
async def api_request(
    self,
    method: str,
    endpoint: str,
    host: APIHost = APIHost.BETA,
    url: str = None,
    params: dict = None,
    headers: dict = None,
    payload: dict = None,
) -> dict | None: ...
```

### Client().manifest_request

[Show source in client.py:94](https://github.com/stefanodvx/crunpyroll/blob/main/crunpyroll/client.py#L94)

#### Signature

```python
async def manifest_request(self, url: str, headers: dict = None) -> str: ...
```

### Client.parse_response

[Show source in client.py:55](https://github.com/stefanodvx/crunpyroll/blob/main/crunpyroll/client.py#L55)

#### Signature

```python
@staticmethod
def parse_response(response: httpx.Response) -> dict | str | None: ...
```

### Client().start

[Show source in client.py:45](https://github.com/stefanodvx/crunpyroll/blob/main/crunpyroll/client.py#L45)

Start Crunchyroll Client and login.

#### Returns

- ```bool``` - On success, True is returned.

#### Signature

```python
async def start(self): ...
```