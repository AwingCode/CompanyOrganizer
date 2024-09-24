#Crear boss, añadir funciones como subir sueldo y añadir empleado
employees = []

#Creating base class:
class Base():
  def __init__(self, Name, Nationality):
    self.Name = Name
    self.Nationality = Nationality
    
#Creating Employee class:
class Employee(Base):
  def __init__(self, Name, Salary, HoursOfWork, Number, Nationality):
    super().__init__(Name, Nationality)
    self.Salary = Salary
    self.HoursOfWork = HoursOfWork
    self.Number = Number
  
  def Work(self):
    print(f"The employee {self.Name} is working...")
  
  def Rest(self):
    print(f"The employee {self.Name} is resting...")
  
  def ShowInfo(self):
    print(f"""EMPLOYEE INFORMATION: \n
          -Name:{self.Name}
          -Nationality:{self.Nationality}
          -Salary:{self.Salary}
          -Hours of work:{self.HoursOfWork}
          -Number:#{self.Number}
          """)

#Creating Boss class:
class Boss(Base):
  def __init__(self, Name, Salary, HoursOfWork, Nationality):
    super().__init__(Name, Nationality)
    self.Salary = Salary
    self.HoursOfWork = HoursOfWork
  
  #Function to control the employees(Add change salary, change hours etc)
  def BossFunc(self):
    while True:
      Objective = input("""What do you want to do:
                        1.View Employees info
                        2.Control an employee 
                        3.Add Employees
                        4.Change Employee salary
                        5.Exit \n
                        NOTE: Introduce the number of your decision \n""")
      try:
        Objective = int(Objective)
      except:
        print("Introduce a valid number:")
      else:
        #Show Employee info:
        if Objective == 1:
          if len(employees) <1:
            print("\n***NO EMPLOYEES AVAILABLE***\n")
          else:
            while True:
              EmpForInfo = input("Introduce the number of the employee:")
              try:
                EmpForInfo = int(EmpForInfo)
                employees[EmpForInfo].ShowInfo()
              except:
                print("Introduce an existing employee")
              else:
                break

        #Control an Employee:
        elif Objective == 2:
          if len(employees) <1:
            print("\n***NO EMPLOYEES AVAILABLE***\n")
          else:
            while True:
              ControlEmployee = input("Introduce the number of the employee: ")
              try:
                ControlEmployee = int(ControlEmployee)
                print(f"Controlling employee number {employees[ControlEmployee].Number}")
              except:
                print("Introduce an existing employee")
              else:
                print("""Introduce:
                      [1]'work' 
                      [2]'rest'
                      [3]'break'""")
                while True:
                  activity = input()
                  if activity == "1":
                    employees[ControlEmployee].Work()
                  elif activity == "2":
                    employees[ControlEmployee].Rest()
                  elif activity == "3":
                    break
                  else:
                    print("Introduce a number between 1-3")
                break

        #Add Employees:
        elif Objective == 3: 
          while True:
            NumEmp = input("Number of employees:")
            try:
              NumEmp = int(NumEmp)
            except:
              print("Introduce a valid number:")
            else:
              if NumEmp <= 0:
                print("Introduce a valid number:")
              else:
                for Emp in range(NumEmp):
                  EmpName = input("Name:")
                  while True:
                    EmpSalary = input("Salary:")
                    try:
                      EmpSalary = float(EmpSalary)
                    except:
                      print("Introduce a valid number:")
                    else:
                      if EmpSalary <= 0:
                        print("Introduce a valid number:")
                      else:
                        break
                  while True:
                    EmpHoursOfWork = input("Hours of work a week:")
                    try:
                      EmpHoursOfWork = float(EmpHoursOfWork)
                    except:
                      print("Introduce a valid number:")
                    else:
                      if EmpHoursOfWork <= 0:
                        print("Introduce a valid number:")
                      else:
                        break
                  EmpNumber = 0
                  for employee in employees:
                    EmpNumber += 1
                  EmpNationality = input("Nationality:")
                  Employee1 = Employee(EmpName, EmpSalary, EmpHoursOfWork, EmpNumber, EmpNationality)
                  Employee1.ShowInfo()
                  employees.append(Employee1)
                break
        elif Objective == 4:
          if len(employees) <1:
            print("\n***NO EMPLOYEES AVAILABLE***\n")
          else:
            while True:
              EmployeToChangeSalary = input("Introduce the Employee number:")
              try: 
                EmployeToChangeSalary = int(EmployeToChangeSalary)
                ChangingSalaryAdvert = print(f"""You are changing the salary to employee number {employees[EmployeToChangeSalary].Number}.
\nHis actual salary is {employees[EmployeToChangeSalary].Salary}€. """)
              except:
                print("Introduce a valid number:")
              else:
                while True:
                  NewSalary = input("Introduce the Employee new salary:")
                  try:
                    NewSalary = float(NewSalary)
                  except:
                    print("Introduce a valid number:")
                  else:
                    if NewSalary <=0:
                      print("Introduce a valid number:")
                    else:
                      employees[EmployeToChangeSalary].Salary = NewSalary
                      break
                break
                  
              
        #This does nothing:
        elif Objective == 5:
          break


#Boss info:
BossName = input("Introduce your name:")
BossNationality = input("Introduce your nationallity:")
while True:  
  BossSalary = input("Introduce your earnings(€):")
  try:
    BossSalary = float(BossSalary)
  except:
    print("Introduce a valid number")
  else:
    if BossSalary <=0:
      print("Introduce a valid number")
    else:
      break
while True:  
  BossHoursOfWork = input("Introduce the hours that you work a week:")
  try:
    BossHoursOfWork = float(BossHoursOfWork)
  except:
    print("Introduce a valid number")
  else:
    if BossHoursOfWork <=0:
      print("Introduce a valid number")
    else:
      break

TheBoss = Boss(BossName, BossSalary, BossHoursOfWork, BossNationality)


TheBoss.BossFunc()
