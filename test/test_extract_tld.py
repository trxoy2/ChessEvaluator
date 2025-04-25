import pytest
from src.modules.parse_urls import extract_tld

@pytest.mark.parametrize("domain, expected_tld", [
    ("example.com", "com"),             # Standard TLD
    ("sub.example.co.uk", "co.uk"),     # Multi-level TLD
    ("ftp.example.org", "org"),         # Standard organization TLD
    ("mywebsite.net", "net"),           # Generic TLD
    ("university.edu", "edu"),          # Educational TLD
    ("government.gov", "gov"),          # Government TLD
    ("custom.store", "store"),          # New gTLD
    ("sub.custom.tech", "tech"),        # New gTLD with subdomain
    ("localhost", ""),                  # Localhost should have no TLD
    ("192.168.1.1", ""),                # IP address should have no TLD
])

def test_extract_tld(domain, expected_tld):
    assert extract_tld(domain) == expected_tld

@pytest.mark.parametrize("invalid_input", [None, ""])
def test_extract_tld_invalid_input(invalid_input):
    with pytest.raises(ValueError, match="Invalid domain: Input cannot be None or empty."):
        extract_tld(invalid_input)