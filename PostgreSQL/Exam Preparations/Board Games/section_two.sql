-- Section 2
INSERT INTO board_games(name, release_year, rating, category_id, publisher_id, players_range_id)
VALUES ('Deep Blue', 2019, 5.67, 1, 15, 7),
        ('Paris', 2016, 9.78, 7, 1, 5),
        ('Catan: Starfarers', 2021, 9.87, 7, 13, 6),
        ('Bleeding Kansas', 2020, 3.25, 3, 7, 4),
        ('One Small Step', 2019, 5.75, 5, 9, 2);

INSERT INTO publishers(name, address_id, website, phone)
VALUES
    ('Agman Games', 5, 'www.agmangames.com', '+16546135542'),
    ('Amethyst Games', 7, 'www.amethystgames.com', '+15558889992'),
    ('BattleBooks', 13, 'www.battlebooks.com', '+12345678907');

UPDATE players_ranges
SET max_players = max_players + 1
WHERE
    players_ranges.min_players = 2
    AND players_ranges.max_players = 2;

UPDATE board_games
SET name = CONCAT(name, ' ', 'V2')
WHERE board_games.release_year >= 2020;

DELETE FROM board_games AS bg
WHERE bg.publisher_id IN (SELECT p.id
                          FROM publishers AS p
                              JOIN addresses AS a ON p.address_id = a.id
                          WHERE a.town LIKE 'L%');

DELETE FROM publishers AS p
WHERE p.address_id IN (SELECT a.id 
                       FROM addresses AS a 
                       WHERE a.town LIKE 'L%');

DELETE FROM addresses
WHERE town LIKE 'L%';
