'''6:festival budget for 2000 is anounced inr 10000/- and every year it will increade by 10%.
write a recursuve function to calculate total expense till 2020'''

def fes(year,budget):

        if year == 2000 :
            return budget
        
        else:
            year-=1
            return fes(year, budget+1000)    
       

print(fes(2020, 10000))


        
# class Employee:
#     salar = 1000
#     increment = 1.5
#     @property
#     def salaryAfterIncrement(self):
#         return self.salar * self.increment
        
#     @salaryAfterIncrement.setter
#     def salaryAfterIncrement(self,sai):
#          self.increment = sai / self.salar
         
# e = Employee()
# print(e.salar)
# print(e.salaryAfterIncrement)



        



