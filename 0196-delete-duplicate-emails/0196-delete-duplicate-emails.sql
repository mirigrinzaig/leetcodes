/* Write your T-SQL query statement below */
WITH CTE AS (
  SELECT *,
    ROW_NUMBER() OVER (PARTITION BY email ORDER BY id) AS rn
  FROM Person
)
DELETE FROM CTE
WHERE rn > 1;

