-- As a solution to HW, create a file named: task2.sql with all SQL queries:

-- write a query to display the names (first_name, last_name) using alias name "First Name", "Last Name" from the table of employees;
SELECT first_name as "First name", last_name as "Last name"
FROM employees
-- write a query to get the unique department ID from the employee table
SELECT DISTINCT department_id as unique_id
FROM employees
-- write a query to get all employee details from the employee table ordered by first name, descending
SELECT * FROM employees
ORDER BY first_name DESC
-- write a query to get the names (first_name, last_name), salary, PF of all the employees (PF is calculated as 12% of salary)
SELECT first_name, last_name, salary, salary*0.12 as PF
FROM employees
-- write a query to get the maximum and minimum salary from the employees table
SELECT MAX(salary) as "Max salary", MIN(salary) as "Min salary"
FROM employees
-- write a query to get a monthly salary (round 2 decimal places) of each and every employee
SELECT *, ROUND(salary/12, 2) as "Month salary"
FROM employees