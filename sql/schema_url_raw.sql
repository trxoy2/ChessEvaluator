CREATE TABLE IF NOT EXISTS url_raw (
    url TEXT, --The URL being classified
    type TEXT --The classification type of the URL, possible values include malware, phishing, benign, or defacement
);