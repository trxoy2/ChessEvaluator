CREATE TABLE IF NOT EXISTS url_transform (
    url TEXT NOT NULL, --The URL being classified
    type TEXT CHECK (type IN ('malware', 'phishing', 'benign', 'defacement') OR type IS NULL), --The classification type of the URL, possible values include malware, phishing, benign, or defacement
    conflicting_url BOOLEAN NOT NULL --Indicates if the url is duplicated with different types, which could be conflicting.
);