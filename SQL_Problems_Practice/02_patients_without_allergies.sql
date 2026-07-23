-- Problem 2: Show first name and last name of patients who do not have allergies.

-- Question:
-- Show first name and last name of patients who do not have allergies. (NULL)

SELECT first_name, last_name
FROM patients
WHERE allergies IS NULL;
