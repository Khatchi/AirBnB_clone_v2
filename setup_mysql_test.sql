-- This is a script that prepared a MySQL server for AiBnB_clone_v2 project.

-- Creates project developt database named : hbnb_test_db
CREATE DATABASE
IF NOT EXISTS hbnb_test_db;

-- Creates a new user name: hbnb_test with all privileges on the above database,
--	 with password: hbnb_test_pwd if not exists.
CREATE USER
IF NOT EXISTS 'hbnb_test'@'localhost'
IDENTIFIED BY 'hbnb_test_pwd';

-- Grants all privileges to the new user:
GRANT ALL PRIVILEGES
ON hbnb_test_db.*
TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;

--grants the SELECT privilege for the user in the db performance_schema
GRANT SELECT
ON performance_schema.*
TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
