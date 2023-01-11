#6.Write a python script to calculate factorial of a given number.
n=int(input("enter the number:-"))
fact=1
for i in range(1,n+1,1):
    fact=fact*i
print("factorial is:-",fact)
