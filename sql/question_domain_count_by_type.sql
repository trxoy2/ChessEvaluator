SELECT 
    type, 
    COUNT(*) AS domain_count
FROM url_transform
WHERE type IS NOT NULL
GROUP BY type
ORDER BY domain_count DESC;