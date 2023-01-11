#1.Write a python script to calculate sum of first N natural numbers.n=int(input("enter the number:-"))
n=int(input('enter the number:-'))
sum=0
for i in range(1,n+1,1):
    sum=sum+i
print("sum of digit is:-",sum)
