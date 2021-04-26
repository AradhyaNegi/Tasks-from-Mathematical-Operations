# -*- coding: utf-8 -*-
"""
TASKS of WORKING WITH DATA
"""
#TASK 1
name = input (" Enter your name : " )
Grade= input (" Enter your Section : " )
S1=float (input("Enter your marks of Subject 1 :"))
S2=float (input("Enter your marks of Subject 2 :"))
S3=float (input("Enter your marks of Subject 3 :"))
S4=float (input("Enter your marks of Subject 4 :"))
S5=float (input("Enter your marks of Subject 5 :"))
om=float (input("Enter the out of marks.."))
tm= S1 + S2 + S3 + S4 + S5
otm = om * 5
per=((S1 + S2 + S3 + S4 + S5)/otm)*100

print("Students Name : " + (name))

print("Your Total Marks are : " + str(tm) +  " out of " + str(otm))

print("Your percentage is :  " + str(per) + "% ")





