from abc import abstractmethod, ABC


# Component class
class Employee(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def rest(self):
        pass


# Leaf class
class Lawyer(Employee):
    def __repr__(self):
        return self.__class__.__name__

    def work(self):
        return f'{self.__repr__()} is working now'

    def rest(self):
        return f'{self.__repr__()} is on vacation'


# Leaf class
class Developer(Employee):
    def __repr__(self):
        return self.__class__.__name__

    def work(self):
        return f'{self.__repr__()} is working now'

    def rest(self):
        return f'{self.__repr__()} is on vacation'


# Composite class
class EmployeeSystem(Employee):
    def __init__(self):
        self.employees = []

    def add(self, employee: Employee):
        return self.employees.append(employee.__repr__())

    def remove(self, employee: Employee, number: int):
        return self.employees.remove(f'{employee} + str(number')

    def work(self):
        for emp in self.employees:
            print(f'{emp},', end=' ')
        print('are working now')

    def rest(self):
        print(f'{self.employees} will go to vacation')


if __name__ == '__main__':
    worker1 = Lawyer()
    worker2 = Developer()

    employee_sys = EmployeeSystem()
    employee_sys.add(worker1)
    employee_sys.add(worker1)
    employee_sys.add(worker2)

    employee_sys.work()
    employee_sys.rest()



