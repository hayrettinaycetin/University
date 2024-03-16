class Employee:
    def __init__(self,emp_id,emp_name,emp_salary,emp_department) :
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = int(emp_salary)
        self.emp_department = emp_department

    def assing_department(self,emp_department):
        self.emp_department = emp_department
        return emp_department
    def calculate_salary(self,emp_salary,hours_worked):
        if hours_worked > 50:
            overtime = hours_worked - 50
            overtime_amount = (overtime*(emp_salary/50))
            emp_salary = emp_salary + overtime_amount
            return emp_salary
        else:
            emp_salary = emp_salary
            return emp_salary
    
    def display(self):
        print("Employee Name" , self.emp_name)
        print("Employee ID: ",self.emp_id)
        print("Employee Department: ", self.emp_department)
        print("Employee Salary: ",self.emp_salary)
        
emp1 = Employee("E7876","ADAMS",50000,"ACCOUNTING")
emp2 = Employee("E7499","JONES",45000,"RESEARCH")
emp3 = Employee("E7900","MARTIN",50000,"SALES")
emp4 = Employee("E7698","SMITH",55000,"OPERATIONS")

emp1.assing_department("SALES")
emp1.display()
print(f"{emp1.emp_name} over time salary: ",emp1.calculate_salary(50000,60))


        