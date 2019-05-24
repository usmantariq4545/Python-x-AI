a=input("ENTER STUDENT NAME:")
b=input("ENTER ROLL NO:")
c=input("ENTER CLASS:")
d=input("ENTER SECTION:")
print("\nPLEASE ENTER MARKS OUT OF 100")
phy=int(input("\nENTER MARKS OF PHYSICS:"))
chem=int(input("ENTER MARKS OF CHEMISTRY:"))
math=int(input("ENTER MARKS OF MATHS:"))
comp=int(input("ENTER MARKS OF COMPUTER:"))
eng=int(input("ENTER MARKS OF ENGLISH:"))
isl=int(input("ENTER MARKS OF ISLAMIAT:"))
pst=int(input("ENTER MARKS OF P.S.T:"))
urdu=int(input("ENTER MARKS OF URDU:"))
totalmarks = phy+chem+math+comp+eng+isl+pst+urdu
percentage = ((totalmarks/800)*100)
if (percentage >= 80):
    grade ="A+"
elif (percentage > 70 & percentage <= 80 ):
    grade = "A"
elif (percentage > 60 & percentage <= 70):
    grade = "B"
elif (percentage > 50 & percentage <= 60 ):
    grade = "C"
elif (percentage > 40 & percentage <=50):
    grade = "D"
else:
    grade = "F"
print("\n\t       ***MARKSHEET***")
print("\nStudent's Name:",a +"      "+ "Roll No:",b)
print("Class:",c +"      "+ "Section",d)
print("\n════════════════════════════════════════════════════════")
print("SUBJECTS         TOATAL MARKS           MARKS OBTAINED")
print("\nPHYSICS               100                   ",phy  )
print("CHEMISTRY             100                   ",chem )
print("MATHS                 100                   ",math )
print("COMPUTER              100                   ",comp )
print("ENGLISH               100                   ",eng )
print("ISLAMIAT              100                   ",isl )
print("P.S.T                 100                   ",pst  )
print("URDU                  100                   ",urdu  ) 
print("\n════════════════════════════════════════════════════════")
print("TOTAL MARKS           800                   ",totalmarks)
print("════════════════════════════════════════════════════════")
print("\n|PERCENTAGE|                              ",percentage )
print("|GRADE|                                   ",grade )
print("\n════════════════════════════════════════════════════════")