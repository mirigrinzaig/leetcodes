-- SELECT name AS Customers
-- FROM Customers
-- WHERE id IN (
--     SELECT id
--     FROM Customers
--     EXCEPT
--     SELECT customerId
--     FROM Orders
-- );
SELECT c.name AS Customers
FROM Customers c
LEFT JOIN Orders o
    ON c.id = o.customerId
WHERE o.customerId IS NULL;
