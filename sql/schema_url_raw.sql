CREATE TABLE IF NOT EXISTS url_raw (
    url TEXT NOT NULL, --The URL being classified
    type TEXT NOT NULL --The classification type of the URL, possible values include malware, phishing, benign, or defacement
);