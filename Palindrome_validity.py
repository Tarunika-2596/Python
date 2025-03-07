#palindrome validity
n=int(input("Enter value of a"))
p=0
t=n
while(n!=0):
    rem=n%10
    p=p*10+rem
    n=n//10
if(t==p):
    print(t,"is a palindrome")
else:
    print(t,"is not a palindrome")