-- select the second highest vale from the table. should return null if not exist.
SELECT MAX(Salary) AS SecondHighestSalary FROM Employee
WHERE Salary<(SELECT MAX(Salary) FROM Employee)
