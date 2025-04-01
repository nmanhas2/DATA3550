class Employee:
    def __init__(self, name):
        self._name = name
    
    def getName(self):
        return self._name
    
    def weeklyPlay(self, hoursWorked):
        return 100

class HourlyEmployee(Employee):
    def __init__(self, name, wage):
        super().__init__(name)
        self._wage = wage
    
    def weeklyPay(self, hoursWorked):
        pay = self._wage * hoursWorked
        return pay

class SalariedEmployee(Employee):
  def __init__(self, name, salary):
   super().__init__(name)
   self._annualsalary = salary

  def weeklyPay(self, hoursWorked) :
    WEEKS_PER_YEAR = 52
    pay = self._annualsalary / WEEKS_PER_YEAR
    return pay

class Manager(SalariedEmployee):
  def __init__(self, name, salary, bonus):
   super().__init__(name, salary)
   self._weeklybonus = bonus

  def weeklyPay(self, hoursWorked) :
    return super().weeklyPay(hoursWorked) + self._weeklybonus

def main():
    e1 = Employee("Mary")
    print(e1.weeklyPlay(30))

    e2 = HourlyEmployee("Tom", 30)
    print(e2.weeklyPay(35))

    e3 = SalariedEmployee("Mark", 100000)
    print(e3.weeklyPay(60))

    e4 = Manager("Alice", 100000, 60)
    print(e4.weeklyPay(40))

    staff = []
    staff.append(HourlyEmployee("Morgan, Harry", 30.0))
    staff.append(SalariedEmployee("Lin, Sally", 52000.0))
    staff.append(Manager("Smith, Mary", 104000.0, 50.0))

    for employee in staff :
        hours = int(input("Hours worked by  " + employee.getName() + ": "))
        income = employee.weeklyPay(hours)
        print(income)


if __name__ == "__main__":
    main()