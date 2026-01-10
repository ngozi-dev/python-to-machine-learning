#!/usr/bin/python3
# a module that creates a base class

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = None  # Internal attribute
        self.salary = salary # Uses the setter for validation

    @property
    def salary(self):
        """Getter for salary (Encapsulation)"""
        return self._salary

    @salary.setter
    def salary(self, value):
        """Setter with validation (Encapsulation)"""
        if value > 0:
            self._salary = value
        else:
            raise ValueError("Salary must be a positive number.")

    def get_details(self):
        """Base method for Polymorphism"""
        return f"Name: {self.name}, Salary: ${self.salary:,.2f}"


class Manager(Employee):
    """Derived class demonstrating Inheritance"""
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def get_details(self):
        """Overriding method for Polymorphism"""
        return f"Manager: {self.name}, Dept: {self.department}, Salary: ${self.salary:,.2f}"


class Intern(Employee):
    """Derived class demonstrating Inheritance"""
    def __init__(self, name, salary, duration):
        super().__init__(name, salary)
        self.duration = duration

    def get_details(self):
        """Overriding method for Polymorphism"""
        return f"Intern: {self.name}, Duration: {self.duration} months, Stipend: ${self.salary:,.2f}"


# --- Demonstration ---

# Create objects of each type
emp = Employee("Alice Smith", 50000)
mgr = Manager("Bob Jones", 95000, "Operations")
itn = Intern("Charlie Day", 2000, 6)

# List of different employee objects
staff = [emp, mgr, itn]

print("--- Employee Records ---")
for person in staff:
    # Demonstrates Polymorphism: the same method call behaves differently
    # based on the object's actual class.
    print(person.get_details())

# Demonstrating Encapsulation validation
try:
    emp.salary = -1000
except ValueError as e:
    print(f"\nValidation Error: {e}")