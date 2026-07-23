-- Problem 5: Replace NULL allergies with 'NKA'

-- Question:
-- Update the patients table for the allergies column.
-- If the patient's allergies is NULL, replace it with 'NKA'.

UPDATE patients
SET allergies = 'NKA'
WHERE allergies IS NULL;
