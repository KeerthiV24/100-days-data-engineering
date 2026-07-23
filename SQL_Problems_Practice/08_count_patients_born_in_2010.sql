-- Problem 8: Count patients born in 2010

-- Question:
-- Show how many patients have a birth_date with 2010 as the birth year.

-- Solution 1 (Using YEAR function)
SELECT COUNT(*) AS total_patients
FROM patients
WHERE YEAR(birth_date) = 2010;

-- Solution 2 (Using BETWEEN)
SELECT COUNT(*) AS total_patients
FROM patients
WHERE birth_date BETWEEN '2010-01-01' AND '2010-12-31';
