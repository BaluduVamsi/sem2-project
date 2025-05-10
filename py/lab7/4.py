class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def __add__(self,other):
        return employee(self.name+"&"+other.name,self.salary+other.salary)
    def __sub__(self,other):
        return employee(self.name+"&"+other.name,self.salary-other.salary)

e1=employee(input("enter the name of employee 1:"),int(input("enter salary:")))
e2=employee(input("enter the name of employee 2:"),int(input("enter salary:")))
print(f"combined name and salary {(e1+e2).name} and{(e1+e2).salary} \n comparison of  {(e1-e2).name} is {(e1-e2).salary}")