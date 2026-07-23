-- Problem 4: Show patients whose weight is between 100 and 120.

-- Question:
-- Show first name and last name of patients whose weight is within the range of 100 to 120 (inclusive).

SELECT first_name,
       last_name
FROM patients
WHERE weight BETWEEN 100 AND 120;
