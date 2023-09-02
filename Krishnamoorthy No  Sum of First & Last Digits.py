import math
n= int(input("enetr a value - "))
t=n
s=0
while n>0:
    d=n%10
    s=s+math.factorial(d)
    n=n//10
if t==s:
    print('Krshnamoorti')
else:
    print("not krishnamoorti")
  