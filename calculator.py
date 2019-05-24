print("\nSIMPLE CALCULATOR")
print("\nENTER TWO NUMBERS")
a=float(input("\nENTER FIRST NUMBER:"))
b=float(input("ENTER SECOND NUMBER:"))
c=input("\nSELECT OPERATION: +,-,*,/ = ")
print("\n===========================")
if c =="+":
    print("SUM IS =",a+b)
elif c =="-":
    print("DIFFERENCE IS =",a-b)
elif c =="*":
    print("MULTIPLE IS =",a*b)
elif c =="/":
    print("DIVISION IS =",a/b)
else :
    print("INVALID OPERATION")
print("===========================")