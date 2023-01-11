#4.Write a python script to calculate sum of first N odd natural numbers.
n=int(input("enter the number:-"))
sum=0
for i in range(1,n+1):
    sum=sum+(2*i-1)
print("sum of odd natural number is:-",sum)
