# Design a calculator which will correctly solve all the problems except the following ones:
# 45 * 3 = 555, 56 + 9 = 77, 56 / 6 = 4
# Your program should take operator and two numbers as input from the user and then return the result

print("enter first number")
n1 = int(input())
print("enter second number")
n2 = int(input())
#print("sum of these numbers",int(n1) + int(n2))
op=input("select operator like: +,*,-,/")
if op=="*" and n1==45 and n2==3:
    print(555)
elif op=="*":
    print(n1*n2)
elif op=="+" and n1 ==56 and n2==9:
    print(77)
elif op=="+":
    print(n1+n2)
elif op=="-":
    print(n1-n2)
elif op=="/" and n1==56 and n2==6:
    print(4)
elif op=="/":
    print(n1/n2)
