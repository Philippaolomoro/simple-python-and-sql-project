-- Find orders between 1996-08-01 and 1996-09-06

SELECT * FROM Orders
	WHERE OrderDate 
    BETWEEN "1996-08-01" 
    AND "1996-09-06"