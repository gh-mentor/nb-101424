Create a Python 3.14 package 'CompanyLibrary' that models a company. The project should include the following classes:

1. `Company` class:
   - Properties:
     - `name` (String)
     - `departments` (Array)
   - Methods:
     - `constructor(name)`
     - `addDepartment(department)`
     - `getDetails()`
     - `getDepartments()`

2. `Department` class:
   - Properties:
     - `id` (Number)
     - `name` (String)
     - `employees` (Array)
   - Methods:
     - `constructor(id, name)`
     - `getId()`
     - `getName()`
     - `addEmployee(employee)`
     - `removeEmployee(employee)`
     - `getDetails()`
     - `getEmployees()`

3. `Employee` class:
   - Properties:
     - `id` (Number)
     - `name` (String)
     - `salary` (Number)
   - Methods:
     - `constructor(id, name, salary)`
     - `getId()`
     - `getName()`
     - `getSalary()`
     - `getDetails()`

4. `Developer` class (extends `Employee`):
   - Properties:
     - `programmingLanguage` (String)
   - Methods:
     - `constructor(id, name, salary, programmingLanguage)`
     - `getDetails()`

5. `Manager` class (extends `Employee`):
   - Properties:
     - `department` (String)
   - Methods:
     - `constructor(id, name, salary, department)`
     - `getDetails()`

