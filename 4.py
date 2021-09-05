''' 4 :a company has 20 employee with salaray rs 20000/- for 15% of them,25000/- for 3 and 50000/- for the remaining 2.wirte a java program to find what % of these to be announced
uniformly when the available fund id rs 70000/- on account of bonus'''
employee =20
emp15=employee*.15

class Company:
    
    def __init__(self,salary):
        self.salary=salary
        
        print("employee is created")
    def getSalary(self):
        print(self.salary)
    def avgfund(self):
        fund=70000
        a=(fund/self.salary)*100
        print(f"anounced fund is: {fund} and you get : {a}")
   



emp15=Company(20000)
emp15.avgfund()
emp15.getSalary()

emp2=Company(25000)
emp2.avgfund()
emp2.getSalary()

emp3=Company(50000)
emp3.avgfund()
emp3.getSalary()

