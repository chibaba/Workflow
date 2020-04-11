class Department():
    def __init__(self, name,location):
        self.name = name
        self.loc=location
    def DepartmentInfo(self):
        return "Department Name : " +str(self.name) +", Location : " +str(self.loc)