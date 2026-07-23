-- Problem 9: Count Patients by Province

-- Question:
-- Display the total number of patients for each province.
-- Order the results in descending order.

SELECT
    pr.province_name,
    COUNT(*) AS patient_count
FROM patients pa
JOIN province_names pr
ON pa.province_id = pr.province_id
GROUP BY pr.province_name
ORDER BY patient_count DESC;
