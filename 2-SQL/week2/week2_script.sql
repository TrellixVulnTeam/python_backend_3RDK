CREATE TABLE divisions (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    city TEXT NOT NULL,
    name TEXT NOT NULL UNIQUE,
    home_color TEXT NOT NULL,
    away_color TEXT,
    division_id INT
);

ALTER TABLE teams
    ADD CONSTRAINT fk_teams_divisions
    FOREIGN KEY (division_id)
    REFERENCES divisions (id)
    ON DELETE SET NULL;

-- Insert Data into Division Table
INSERT INTO divisions (name) VALUES ('Atlantic'), ('Metropolitan'), ('Pacific'), ('Central');

-- Insert Data into Team Table
INSERT INTO teams (city, name, home_color, away_color, division_id) VALUES ('New York', 'Islanders', 'Royal blue', 'White', 2);
INSERT INTO teams (city, name, home_color, away_color, division_id) VALUES ('Seattle', 'Kraken', 'Deep sea blue', 'White', 3);

-- Update City Name
UPDATE divisions SET name = 'Cosmopolitan' WHERE name = 'Metropolitan';

-- Delete Cosmopolitan from Division Table
DELETE FROM divisions WHERE name = 'Cosmopolitan';