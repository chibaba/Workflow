class car():
    def __init__(self, cat,mil,cap):
        self.category=cat
        self.milage=mil
        self.capacity=cap
class Ferarri(car):
    def __init__(self, cat,mil,cap,HP,TS,ACC):
        super().__init__(cat,mil,cap)
        self.HorsePower=HP
        self.TopSpeed=TS
        self.Accelerator=ACC
    def printCarDetails(self):
        engine=Engine()
        print("Category : "+str(self.category))
        print("mileage :"+str(self.mileage))
        print("Capacity: "+str(self.capacity))
        print("Horse Power : "+str(self.HorsePower))
        print("TopSpeed : "+str(self.TopSpeed))
        print("Acceleration: "+str(self.Accelerator))
        print("Engine : ")
        print("\t"+str(engine.Details()))
class Engine():
    def __init__(self):
        self.details=None
    def Details(self):
        self.details="""
    The 458 is powered by a 4,499 cc (274.5 cu in; 4.5 L) V8 engine of the
    "Ferari/Maserati" F136 engine family, producing 570 PS (419 kw; 560 hp) AT 9000
    rpm (redline) and 540 N.m (398 lb.ft) at 6, 000 rpm with 86% torque available at 3,250 rpm """
        return self.details
    obj=Ferarri("Sports", "4kpmh", "4 seater", "660 horsepower", "349km/h", "2.9sec")
    obj.printCarDetails()
        
        