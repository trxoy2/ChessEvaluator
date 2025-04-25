SELECT 
    type, 
    COUNT(*) AS domain_count,
    ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM url_transform), 2) AS percentage
FROM url_transform
WHERE type IS NOT NULL
GROUP BY type
ORDER BY domain_count DESC;