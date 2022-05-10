def max_function(a):
    i=0
    max=0
    while i<len(a):
        print(a[i])
        if a[i]> max:
            max = a[i]
        i=i+1
    return(max) 


import sys

'''
#print("max value is: ",max)
print("hello world")
x = [20,8,90,8,2,1]
y = [56,999,12,2]
z= [232,8,90,1]
mx= max_function(x)
print("max vaklue is ",mx)
a = max_function(y)
print("max value is",a)
b = max_function(z)
print("max value is ",b)

a = sys.argv[1]
i = int(sys.argv[2])
j = int(sys.argv[3])
'''
a = input("enter the value of a:")
print (a)
i = input("enter the value of i : ")
i = int(i)
j = input(" enetr the value of j: ")
j = int(j)
if a == '+':
    x= i+j
    print("addition",x)
if a == '*':
    x = i*j
    print("subtraction",x)
if a == '-':
    x = i-j
    print("multiplication",x)






