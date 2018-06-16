# CSCI 5308: Quality Assurance - Assignment 2


### Question 1
##### Principle violated: Depedency Inversion Principle
##### Explanation:
The high level employee class Employer depends on 2 other classes directly HourlyWorker and SalaryWorker. We can't change the data further.

**Solution:** Here, an interface is defined 'IEmployerInterface' with the method 'float calculate(int hours);' and in the Employer class only one array objects is made and all 3 classes Employer, HourlyWorker, SalaryWorker are have been known with the interface and HourlyWorker and SalaryWorker are implemented with the interface.

### Question 2
##### Principle violated: Interface Segregation Principle
##### Explanation:
Here, common interface ILibraryItem is there for both the classes which indicates repetition in methods for both the classes.

**Solution:** Here, 3 interfaces are defined named IBookSwitch (for Book class), ILibraryItem (for DVD class) and one common interface name 'ICommonDetails' is extended with common menthods with other 2 interfaces and in other 2 classes methods which are not part relevant has been removed respectively.

### Question 3
##### Principle violated: Single Responsibility Principle
##### Explanation:
Here, class named 'ProfitReport' has more than 1 responsibility (sending data to printer and email) rather than creating report.

**Solution:** For the solution, ProfitReport class is divided in other 2 classes named EmailInformation and Printer which contains methods that were part of ProfitReport. Hence, each class have the single responsibility.

### Question 4
##### Principle violated: Liskov Substitution Principle
##### Explanation:
In this question, class USDollarAccount is depending on other class BankAccount, which indicates that interface is required as a substitution for both the classes.

**Solution:** For the solution, 2 interfaces have been introduced name IBank and IUSDollar. they contains methods for BankAccount and USDollarAccount classes respectively. 

### Question 5
##### Principle violated: Open/Closed Principle
##### Explanation:
Here, the methods in class 'CountryGDPReport' can be modified which ultimately change the application.

**Solution:** Here, interfaces are defined for Canada (ICanada interface)and Mexico (IMexico interface) classes. in addition it has one more interface (ICommonDetails) which contains common method for other 2 interfaces and then ICanada and IMexico interfaces have been extended with the ICommonDetails interface which makes it application closed for the modification (specially CountryGRPReport class). 

### Question 6
##### Principle violated: Single Responsibility Principle
##### Explanation:
The 'PiggyBank' class has more than 1 responsibility (save and load). so it violates single responsibility principle.

**Solution:** Here PiggyBank class is divided and its method has been separated in other 2 classes LoadOperation (Load method)and SaveOperation (Save method). this action gives single responsibility to all the classes.

### Question 7
##### Principle violated: Interface Segregation Principle
##### Explanation:
Here, methods in both classes are dependent on single interface 'IInsect'. Hence, interface segregation is applied.

**Solution:** Here, two interfaces (IInsectFly, IInsectSwim) are provided for 2 classes for the connection. The purpose for the same is to remove dependency on the earlier single interface. One common interfaces is added (IInsectWithAntennae) with has common method for 2 classes and this interface is extended in other 2 interfaces.

### References
[1] "SOLID Design Principles Explained – Dependency Inversion Principle with Code Examples", stackify.com. [Online]. Available: https://stackify.com/dependency-inversion-principle/. [Accessed: 13- June- 2018]

[2] Lectures Slides and Notes [Accessed: 14- June- 2018]

##### By: Mr. Niravsinh Jadeja | B00789139 | nirav.jadeja@dal.ca
