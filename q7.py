#7.Write a python script to count digits in a given number.
x=int(input("Enter the number:-"))
count=0
while(x>0):
    count=count+1
    x=x//10
print('total no.of digit is:-',count)
