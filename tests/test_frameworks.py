import pytest
from httpstatusx.frameworks import fastapi, flask

def test_fastapi_exception():
    try:
        exc = fastapi("not_found", "User missing")
        assert exc.status_code == 404
        assert exc.detail == "User missing"
    except ImportError:
        pytest.skip("FastAPI not installed")

def test_flask_abort():
    try:
        with pytest.raises(Exception):
            flask("unauthorized")
    except ImportError:
        pytest.skip("Flask not installed")
