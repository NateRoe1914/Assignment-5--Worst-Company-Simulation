"""
Student information for this assignment:

Replace <FULL NAME> with your name.
On my/our honor, Nathaniel Roe, this
programming assignment is my own work and I have not provided this code to
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: nr25328
"""

from abc import ABC, abstractmethod
import random

DAILY_EXPENSE = 60
HAPPINESS_THRESHOLD = 50
MANAGER_BONUS = 1000
TEMP_EMPLOYEE_PERFORMANCE_THRESHOLD = 50
PERM_EMPLOYEE_PERFORMANCE_THRESHOLD = 25
RELATIONSHIP_THRESHOLD = 10
INITIAL_PERFORMANCE = 75
INITIAL_HAPPINESS = 50
PERCENTAGE_MAX = 100
PERCENTAGE_MIN = 0
SALARY_ERROR_MESSAGE = "Salary must be non-negative."


class Employee(ABC):
    """
    Abstract base class representing a generic employee in the system.
    """

    def __init__(self, name, manager, salary, savings):
        self.relationships = {}
        self.savings = savings
        self.is_employed = True
        self.__name = name
        self.__manager = manager
        self.performance = INITIAL_PERFORMANCE
        self.happiness = INITIAL_HAPPINESS
        self.salary = salary

class Manager(Employee):
    """
    A subclass of Employee representing a manager.
    """
    def work(self):
        change_value = random.randint(-5, 5)
        performance = self.performance + change_value
        if change_value < 0:
            for person in self.relationships:
                self.relationships[person] -= change_value
            self.happiness -= 1
        else:
            self.happiness += 1


class TemporaryEmployee(Employee):
    """
    A subclass of Employee representing a temporary employee.
    """
    def work(self):
        change_value = random.randint(-15, 15)
        performance = self.performance + change_value
        if change_value < 0:
            for person in self.relationships:
                self.relationships[person] -= change_value
            self.happiness -= 2
        else:
            self.happiness += 1

    def interact(self, other):
        if other == Manager:
            if Manager.happiness > 50 and self.performance >= 50:
                self.savings += 1000
            else:
                self.salary // 0
                if self.salary == 0:
                    self.is_employed = False
        


class PermanentEmployee(Employee):
    """
    A subclass of Employee representing a permanent employee.
    """
    def work(self):
        change_value = random.randint(-10, 10)
        performance = self.performance + change_value
        if change_value > 0:
            self.happiness += 1
    def interact(self, other):
        if other == Manager:
            if Manager.happiness > 50 and self.performance >= 25:
                self.savings += 1000
            else:
                self.happiness -= 1
                
                
