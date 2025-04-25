import tldextract
import whois
import concurrent.futures
import functools
from tqdm import tqdm
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor

def extract_domain(url):
    if not url:
        raise ValueError("Invalid URL: Input cannot be None or empty.")
    
    parsed_url = urlparse(url)

    domain = parsed_url.hostname or url.split('/')[0]

    # Remove port if present (e.g., sub.example.com:8080 → sub.example.com)
    return domain.split(':')[0] if domain else domain


def extract_tld(domain):
    if not domain:  # Reject None or empty values
        raise ValueError("Invalid domain: Input cannot be None or empty.")

    extracted = tldextract.extract(domain)
    return extracted.suffix  # Gets the TLD (e.g., 'com', 'org', 'co.uk')

def get_domain_owner(domain, is_valid_url):
    if not is_valid_url:
        return "Invalid Domain"

    if not domain:
        return "Invalid Domain"
    
    print(f"Looking up WHOIS info for: {domain}")
    
    try:
        w = whois.whois(domain)
        return w.org or w.name or "Unknown Owner"
    except Exception as e:
        return f"Error: {str(e)}"
    
# Cache WHOIS lookups to avoid redundant requests
@functools.lru_cache(maxsize=1000)
def get_domain_owner(domain):
    if not domain:
        return "Invalid Domain"
    
    #print(f"Looking up: {domain}")
    
    try:
        w = whois.whois(domain)
        owner = w.org or w.name or "Unknown Owner"
        
        # Convert list to string if necessary
        return ", ".join(owner) if isinstance(owner, list) else owner
    
    except Exception as e:
        return f"WHOIS Lookup Failed"

# Function to apply parallel WHOIS lookups on a DataFrame
def get_domain_owner_parallel(df, domain_column):
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        results = list(tqdm(
            executor.map(get_domain_owner, df[domain_column]), 
            total=len(df), 
            desc="Domain Lookup Progress"
        ))
        df["domain_owner"] = results
    return df