-- Use the sample SQLite database hr.db (same database you used in the previous lesson for homework tasks)

-- As a solution to HW, create a file named: task1.sql with all SQL queries:

-- write a query in SQL to display the first name, last name, department number, and department name for each employee
SELECT first_name, last_name, depart_name, department_id
FROM employees
JOIN departments
ON employees.department_id = departments.department_id
-- write a query in SQL to display the first and last name, department, city, and state province for each employee
SELECT first_name, last_name, depart_name, department_id, city, state_province
FROM employees
JOIN departments
ON employees.department_id = departments.department_id
JOIN locations
ON departments.location_id = locations.location_id
-- write a query in SQL to display the first name, last name, department number, and department name, for all employees for departments 80 or 40
SELECT first_name, last_name, depart_name, department_id
FROM employees
JOIN departments
ON employees.department_id = departments.department_id AND (departments.department_id = 80 OR departments.department_id = 40)
-- write a query in SQL to display all departments including those where does not have any employee
SELECT department_id, depart_name, employee_id
FROM departments
LEFT JOIN employees
ON departments.department_id = employees.department_id
-- write a query in SQL to display the first name of all employees including the first name of their manager
SELECT e.first_name AS employee_first_name, m.first_name AS manager_first_name
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.employee_id
-- write a query in SQL to display the job title, full name (first and last name ) of the employee, and the difference between the maximum salary for the job and the salary of the employee
SELECT e.first_name, e.last_name, j.job_title, (j.max_salary - e.salary)AS Diff
FROM employees e
JOIN jobs j ON e.job_id = j.job_id
-- write a query in SQL to display the job title and the average salary of employees
SELECT j.job_title,  AVG(e.salary) as "AVG salary"
FROM employees e
JOIN jobs j ON e.job_id = j.job_id
GROUP BY job_title
-- write a query in SQL to display the full name (first and last name), and salary of those employees who work in any department located in London
SELECT first_name, last_name, salary
FROM employees
WHERE department_id 
IN (SELECT department_id FROM departments JOIN locations ON departments.location_id=locations.location_id WHERE city ="London")
-- write a query in SQL to display the department name and the number of employees in each department
SELECT d.depart_name, COUNT(e.employee_id) AS num_employees
FROM departments d
LEFT JOIN employees e ON d.department_id = e.department_id
GROUP BY d.depart_name