-- Problem 3: Show first names starting with 'C'

-- Question:
-- Show the first name of patients that start with the letter 'C'.

SELECT first_name
FROM patients
WHERE first_name LIKE 'C%';
