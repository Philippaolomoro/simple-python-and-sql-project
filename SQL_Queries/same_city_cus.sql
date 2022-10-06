-- Find all customers that are from the same city

SELECT * FROM Customers 
   WHERE City IN (SELECT City FROM Customers GROUP BY City HAVING COUNT(*) > 1)