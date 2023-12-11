import pytest
from src.app.utils.string_helpers import str_to_float, sanitize_text

@pytest.mark.parametrize("text, expected", [
    ("1000", 10.0),
    ("5", 0.5),
    ("12", 0.12),
    ("abc", 0)
])
def test_str_to_float(text, expected):
    assert str_to_float(text) == expected

@pytest.mark.parametrize("text, expected", [
    ("Hello\nWorld", "Hello World"),
    ("", None),
    ("   Trim spaces   ", "Trim spaces")
])
def test_sanitize_text(text, expected):
    assert sanitize_text(text) == expected
