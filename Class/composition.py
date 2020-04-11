class car():
    def __init__(self, cat,mil,cap):
        self.category=cat
        self.milage=mil
        self.capacity=cap
class ferrari(car):
    def __init__(self, cat,mil,cap,HP,TS,ACC):
        super().__init__(cat,mil,cap)
        self.HorsePower=HP
        self.TopSpeed=TS
        self.Accelerator=ACC
        
        