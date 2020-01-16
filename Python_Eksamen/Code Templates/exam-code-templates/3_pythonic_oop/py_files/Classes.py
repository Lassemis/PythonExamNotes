class Employee:
    def __init__(self, name, x, *args):
         
        self.__name = name
        self.x = x
        
        if len(args) > 0:
            self.salary = args[0]
            company = args[1]
    
    def __repr__(self):
        return f'{self.__dict__}'
    
    def __str__(self):
        return f'{self.__name},  {self.salary}' 
    
    
    @property
    def x(self):
        return self.__x 
    
    @x.setter
    def x(self, x):     
        if x > 1000:
            self.__x = 1000
        elif x < 0:
            self.__x = 0
        else:
            self.__x = x
    
        
class Secretary(Employee):
    
    def __init__(self, name, x ,salary, company, vacation):
        super().__init__(name, x, salary, company)
        self.vacation = vacation