class Car:
    # def __init__(self): #we need this method(function) to create an object
    def __init__(self,model,year,color,for_sale):
        self.model=model
        self.year=year
        self.color=color
        self.for_sale=for_sale
        
    def drive(self):
        print(f"you can drive {self.color} {self.model}")
    
    def stop(self):
        print(f"Yoou stop the car{self.color}{self.model}")
    
    def describe(self):
        print(f"{self.year} {self.color} {self.for_sale}")