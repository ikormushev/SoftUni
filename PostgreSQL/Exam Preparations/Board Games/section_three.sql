-- Section 3
SELECT
    bg.name,
    bg.rating
FROM board_games AS bg
ORDER BY bg.release_year, bg.name DESC;

SELECT
    bg.id,
    bg.name,
    bg.release_year,
    c.name
FROM board_games AS bg
JOIN categories AS c ON bg.category_id = c.id
WHERE c.name in ('Strategy Games', 'Wargames')
ORDER BY bg.release_year DESC;

SELECT
    c.id,
    CONCAT(c.first_name, ' ', c.last_name) AS creator_name,
    c.email
FROM creators AS c
LEFT JOIN creators_board_games AS cbg ON c.id = cbg.creator_id
WHERE cbg.creator_id IS NULL
ORDER BY creator_name;

SELECT
    bg.name,
    bg.rating,
    c.name
FROM board_games AS bg
JOIN categories AS c ON bg.category_id = c.id
JOIN players_ranges AS pr ON bg.players_range_id = pr.id
WHERE (bg.rating > 7.00 AND bg.name ILIKE '%a%')
   OR (bg.rating > 7.50 AND (pr.min_players = 2 AND pr.max_players = 5))
ORDER BY bg.name, bg.rating DESC
LIMIT 5;

SELECT
    CONCAT(c.first_name, ' ', c.last_name) AS full_name,
    c.email,
    MAX(bg.rating)
FROM creators AS c
JOIN creators_board_games AS cbg ON c.id = cbg.creator_id
JOIN board_games AS bg ON cbg.board_game_id = bg.id
WHERE c.email LIKE '%.com'
GROUP BY c.first_name, c.last_name, c.email
ORDER BY full_name;

SELECT
    *
FROM (SELECT
    c.last_name,
    CEIL(AVG(bg.rating)) AS average_rating,
    p.name AS publisher_name
FROM creators AS c
JOIN creators_board_games AS cbg ON c.id = cbg.creator_id
JOIN board_games AS bg ON cbg.board_game_id = bg.id
JOIN publishers AS p ON bg.publisher_id = p.id
GROUP BY c.last_name, p.name
ORDER BY average_rating DESC) AS s
WHERE s.publisher_name = 'Stonemaier Games';
