CREATE TABLE IF NOT EXISTS url_clean (
    url TEXT NOT NULL, --The URL being classified
    type TEXT CHECK (type IN ('malware', 'phishing', 'benign', 'defacement') OR type IS NULL) --The classification type of the URL, possible values include malware, phishing, benign, or defacement
);