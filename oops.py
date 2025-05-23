'''
class bank():
    def __init__(self):
        self.balance=0
    def deposit(self,amt):
        self.balance+=amt
    def withrdraw(self,amt):
        if amt < self.balance:
            self.balance -= amt
        else:
            print("Insufficient balance")
    def display(self):
        print("Balance:",self.balance)
b=bank()
b.deposit(1000)
b.withrdraw(500)
b.display()   '''

from matplotlib import pyplot as plt
x=[1,2,3,4,5]
y=[6,7,8,9,10]
plt.plot(x,y)
plt.show()