-- Section 3
SELECT
    a.username,
    a.gender,
    a.age
FROM accounts AS a
WHERE a.age >= 18 AND LENGTH(a.username) > 9
ORDER BY a.age DESC, a.username;

SELECT
    p.id AS photo_id,
    p.capture_date,
    p.description,
    COUNT(*) AS comments_count
FROM comments AS c
JOIN photos AS p ON c.photo_id = p.id
WHERE description IS NOT NULL
GROUP BY p.id, p.capture_date, p.description
ORDER BY comments_count DESC , p.id
LIMIT 3;

SELECT
    CONCAT(p.id, ' ', a.username),
    a.email
FROM accounts AS a
JOIN accounts_photos AS ap ON a.id = ap.account_id
JOIN photos as p ON ap.photo_id = p.id
WHERE a.id = p.id
ORDER BY a.id;

SELECT
    p.id AS photo_id,
    COUNT(DISTINCT l.id) AS likes_count,
    COUNT(DISTINCT c.id) AS comments_count
FROM photos AS p
LEFT JOIN likes AS l ON p.id = l.photo_id
LEFT JOIN comments AS c ON p.id = c.photo_id
GROUP BY p.id
ORDER BY likes_count DESC, comments_count DESC, photo_id;

SELECT
    CONCAT(SUBSTRING(p.description FOR 10), '...') AS summary,
    TO_CHAR(p.capture_date, 'DD.MM HH24:MI') AS date
FROM photos AS p
WHERE EXTRACT(day FROM p.capture_date) = 10
ORDER BY p.capture_date DESC;
