-- Task 1
CREATE TABLE mountains(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);
CREATE TABLE peaks(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    mountain_id INT,
    CONSTRAINT fk_peaks_mountains
        FOREIGN KEY (mountain_id)
        REFERENCES mountains (id)
);

-- Task 2
SELECT
    ve.driver_id,
    ve.vehicle_type,
    CONCAT_WS(' ', cam.first_name, cam.last_name) AS driver_name
FROM vehicles AS ve
JOIN
    campers AS cam
ON
    ve.driver_id = cam.id;

-- Task 3
SELECT
    rou.start_point,
    rou.end_point,
    rou.leader_id,
    CONCAT_WS(' ', cam.first_name, cam.last_name) AS leader_name
FROM routes AS rou
JOIN
    campers AS cam
ON
    rou.leader_id = cam.id;

-- Task 4
DROP TABLE peaks;
DROP TABLE mountains;

CREATE TABLE mountains(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);
CREATE TABLE peaks(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    mountain_id INT,
    CONSTRAINT fk_mountain_id
        FOREIGN KEY (mountain_id)
        REFERENCES mountains(id)
        /*
        the next line ensures that when a mountain is
        removed from the database, all its peaks are also deleted
         */
        ON DELETE CASCADE
);

-- Task 5
CREATE DATABASE project_management_db;

CREATE TABLE clients(
    id INT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE projects(
    id INT PRIMARY KEY,
    client_id INT,
    project_lead_id INT,

    CONSTRAINT fk_client_id
        FOREIGN KEY (client_id)
            REFERENCES clients(id)
);

CREATE TABLE employees(
    id INT PRIMARY KEY,
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    project_id INT,

    CONSTRAINT fk_project_id
        FOREIGN KEY (project_id)
            REFERENCES projects(id)
);

ALTER TABLE projects
ADD CONSTRAINT fk_project_lead
FOREIGN KEY
    (project_lead_id)
    REFERENCES employees(id);
