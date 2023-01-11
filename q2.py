# 2.Write a python script to calculate sum of squares of first N natural numbers.
n=int(input("enter the value of n:-"))
sum=0
for i in range(1,n+1,1):
    sum=sum+i*i
print("sum of square of digit is:-",sum)
