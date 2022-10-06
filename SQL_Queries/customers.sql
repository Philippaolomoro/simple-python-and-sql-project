-- Find customers with more than 3 orders

SELECT Customers.CustomerID, Customers.CustomerName FROM Customers 
	INNER JOIN Orders
		ON Orders.CustomerID = Customers.CustomerID
	GROUP BY Customers.CustomerID, Customers.CustomerName
    HAVING COUNT(Orders.CustomerID) > 3
    