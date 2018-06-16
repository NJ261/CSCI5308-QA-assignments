# CSCI 5308: Quality Assurance - Assignment 2


### Question 1
##### Principle violated: Depedency Inversion Principle
##### Explanation:
The high level employee class Employer depends on 2 other classes directly HourlyWorker and SalaryWorker. We can't change the data further.

### Question 2
##### Principle violated: Interface Segregation Principle
##### Explanation:
Here, common interface ILibraryItem is there for both the classes which indicates repetition in methods for both the classes.

### Question 3
##### Principle violated: Single Responsibility Principle
##### Explanation:
Here, class named 'ProfitReport' has more than 1 responsibility (sending data to printer and email) rather than creating report.

### Question 4
##### Principle violated: Liskov Substitution Principle
##### Explanation:
In this question, class USDollarAccount is depending on other class BankAccount, which indicates that interface is required as a substitution for both the classes.

### Question 5
##### Principle violated: Open/Closed Principle
##### Explanation:
Here, the methods in class 'CountryGDPReport' can be modified which ultimately change the application.

### Question 6
##### Principle violated: Single Responsibility Principle
##### Explanation:
The 'PiggyBank' class has more than 1 responsibility (save and load). so it violates single responsibility principle.

### Question 7
##### Principle violated: Interface Segregation Principle
##### Explanation:
Here, methods in both classes are dependent on single interface 'IInsect'. Hence, interface segregation is applied.

### References
[1] "SOLID Design Principles Explained – Dependency Inversion Principle with Code Examples", stackify.com. [Online]. Available: https://stackify.com/dependency-inversion-principle/. [Accessed: 13- June- 2018]

[2] Lectures Slides and Notes [Accessed: 14- June- 2018]

##### By: Mr. Niravsinh Jadeja | B00789139 | nirav.jadeja@dal.ca
