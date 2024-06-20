-- Install mySQL
-- Start a mySQL server
-- In order to do utilize the commands below, run the following command: source main.sql

-- Create the database:

CREATE DATABASE movie_metadata;

-- Use the movie_metadata db:

USE movie_metadata;

-- Create a table to store the movie metadata w/ the following SQL command:

CREATE TABLE movies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    year VARCHAR(255),
    genre VARCHAR(255),
    director VARCHAR(255),
    enriched BOOLEAN,
    custom_field VARCHAR(255),
    actors TEXT,
    plot TEXT,
    language VARCHAR(255),
    country VARCHAR(255)
);