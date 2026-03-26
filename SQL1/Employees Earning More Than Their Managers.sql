-- Write a solution to find the employees who earn more than their managers.
-- Return the result table in any order.

SELECT e.name as Employee
FROM Employee e
JOIN Employee m
ON e.ManagerID = m.id
WHERE e.salary > m.salary;
