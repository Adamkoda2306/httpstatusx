# httpstatusx – Usage Documentation

This document provides detailed examples and best practices for using **httpstatusx**,
a semantic, bidirectional, and framework-agnostic HTTP status utility for Python developers.

---

## Installation

```bash
pip install httpstatusx
```

For local development:

```bash
pip install -e .
```

---

## Basic Lookup (Name → Code)

```python
from httpstatusx import HTTP

HTTP["ok"]          # 200
HTTP["created"]     # 201
HTTP["not_found"]   # 404
HTTP["forbidden"]   # 403
```

---

## Reverse Lookup (Code → Name)

```python
HTTP.name(200)   # "ok"
HTTP.name(404)   # "not_found"
HTTP.name(503)   # "service_unavailable"
```

---

## Category Detection

```python
HTTP.category(100)  # informational
HTTP.category(201)  # success
HTTP.category(302)  # redirection
HTTP.category(404)  # client_error
HTTP.category(503)  # server_error
```

---

## Error Detection

```python
HTTP.is_error(200)  # False
HTTP.is_error(404)  # True
HTTP.is_error(503)  # True
```

---

## Fuzzy Matching

```python
HTTP["unauth"]      # 401
HTTP["timeout"]     # 408
HTTP["server"]      # 500
HTTP["gateway"]     # 502
```

> ⚠️ Note:
> Fuzzy matching is substring-based.  
> In ambiguous cases, the first semantic match is returned.
> Avoid fuzzy matching in critical production logic.

---

## FastAPI Integration

```python
from fastapi import FastAPI
from httpstatusx import fastapi

app = FastAPI()

@app.get("/user")
def get_user():
    raise fastapi("not_found", "User not found")
```

---

## Flask Integration

```python
from flask import Flask
from httpstatusx import flask

app = Flask(__name__)

@app.route("/admin")
def admin():
    flask("unauthorized")
```

---

## CLI Usage

### Basic CLI Lookup

```bash
httpstatusx ok
httpstatusx not_found
httpstatusx 404
httpstatusx 503
```

---

### List HTTP Status Categories

```bash
httpstatusx --list
```

---

### List All Codes in a Category

```bash
httpstatusx --list 200
httpstatusx --list 400
```

---

### Show CLI Examples

```bash
httpstatusx --examples
```

---

## Best Practices

- Prefer semantic names over numeric HTTP codes
- Avoid fuzzy matching for business-critical logic
- Use framework helpers for cleaner APIs
- Write explicit tests when integrating into production systems
- Use the CLI for quick reference while developing APIs

---

Happy coding 🚀
