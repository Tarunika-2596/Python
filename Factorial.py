#factorial of a number
n=int(input("Enetr a  number"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print("Factorial:",fact)