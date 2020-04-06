class Id_Generator():
    def __init__(self):
        self.id=0
    def generate(self):
        self.id=self.id+ 1
        return self.id
    
class Employee():
    def __init__(self,Name,id_gen):
        self.Id=id_gen.generate()
        self.Name=Name
        self.D_id=None
        self.Salary=None
        
    def printDetails(self):
        print("\n")
        print("Employee Details : ")
        print("ID: "+str(self.Id))
        print("Name :" +str(self.Name))
        print("Salary :"+str(self.Salary))
        print("---------------------------")
        
Id_gen=Id_Generator()
emp1=Employee("Emp1",Id_gen)
emp1.Salary= 20000
emp1.D_id=2
emp2=Employee("Emp2",Id_gen)
emp2.Salary=1000000
emp2.D_id=1
emp1.printDetails()
emp2.printDetails()