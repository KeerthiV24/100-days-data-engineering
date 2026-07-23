# SQL Problem 10 – Show the Tallest Patient

## 📝 Problem Statement
Show the first name, last name, and height of the patient with the greatest height.

## 💡 SQL Solution

```sql
SELECT
    first_name,
    last_name,
    height
FROM patients
WHERE height = (
    SELECT MAX(height)
    FROM patients
);
```

## 📖 Explanation
- `MAX(height)` finds the greatest height in the `patients` table.
- The subquery returns the maximum height.
- The outer query retrieves the first name, last name, and height of the patient(s) whose height matches that maximum value.

### 🔑 SQL Concepts Practiced
- Subqueries
- Aggregate Functions (`MAX`)
- WHERE Clause
