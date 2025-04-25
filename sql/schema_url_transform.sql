CREATE TABLE IF NOT EXISTS url_transform (
    url TEXT NOT NULL, --The URL being classified
    type TEXT CHECK (type IN ('malware', 'phishing', 'benign', 'defacement') OR type IS NULL), --The classification type of the URL, possible values include malware, phishing, benign, or defacement
    conflicting_url BOOLEAN NOT NULL, --Indicates if the url is duplicated with different types, which could be conflicting.
    is_valid_url BOOLEAN NOT NULL, --Indicates if the url is in a valid format defined in the code. Helps to identify bad data.
    domain TEXT NOT NULL, --The domain extracted from the URL.
    tld TEXT, --The top level domain extracted from the domain.
    domain_owner TEXT NOT NULL, --The owner of the domain, gathered from WHOIS.
    e_count INTEGER NOT NULL --The count of the letter E in each domain.
);