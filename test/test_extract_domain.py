import pytest
from urllib.parse import urlparse
from src.modules.parse_urls import extract_domain  # Replace `your_module` with the actual filename

@pytest.mark.parametrize(
    "url, expected_domain",
    [
        ("http://example.com/path", "example.com"),
        ("https://www.example.com", "www.example.com"),
        ("ftp://ftp.example.com/resource", "ftp.example.com"),
        ("example.com/path", "example.com"),  # No scheme, should return the first part
        ("www.example.com", "www.example.com"),  # No scheme, should return as-is
        ("http://sub.example.com:8080", "sub.example.com"),  # Port should be removed
        ("https://user:pass@example.com", "example.com"),  # Credentials in URL
        ("http://192.168.1.1/path", "192.168.1.1"),  # IP address as domain
        ("http://localhost:5000", "localhost"),  # Localhost, port should be removed
    ],
)
def test_extract_domain(url, expected_domain):
    assert extract_domain(url) == expected_domain

@pytest.mark.parametrize("invalid_input", [None, ""])
def test_extract_domain_invalid_input(invalid_input):
    with pytest.raises(ValueError, match="Invalid URL: Input cannot be None or empty."):
        extract_domain(invalid_input)