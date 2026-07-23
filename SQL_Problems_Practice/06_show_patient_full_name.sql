-- Problem 6: Show patient's full name

-- Question:
-- Show first name and last name concatenated into one column as full_name.

-- MySQL
SELECT CONCAT(first_name, ' ', last_name) AS full_name
FROM patients;

-- PostgreSQL / Oracle / SQLite
SELECT first_name || ' ' || last_name AS full_name
FROM patients;
