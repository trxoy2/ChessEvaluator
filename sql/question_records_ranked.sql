-- Add the rank column if it doesn't already exist
ALTER TABLE url_transform ADD COLUMN rank INTEGER;

-- Update rank based on type values
UPDATE url_transform
SET rank = CASE 
    WHEN type = 'malware' THEN 4  -- High
    WHEN type = 'defacement' THEN 3  -- Medium High
    WHEN type = 'phishing' THEN 2  -- Medium
    WHEN type = 'benign' THEN 1  -- Low
    ELSE 0  -- Default for unknown types
END;

SELECT 
    domain,
    type,
    CASE 
        WHEN rank = 4 THEN 'High'  
        WHEN rank = 3 THEN 'Medium High'  
        WHEN rank = 2 THEN 'Medium'  
        WHEN rank = 1 THEN 'Low'  
        ELSE 'Unknown'  
    END AS Severity
FROM url_transform
ORDER BY rank DESC, domain ASC
LIMIT 10;