"""ASSIGNMENT 1
STUDENT NAME:DRISHTI GAUTAM
ROLL NO-06001012025
ML AND GEN AI INTERNSHIP"""
#Questions
"""Assignment 1

1 Find area of rectangle.
2 Find simple interest.
3 Convert temperature from Celsius to Fahrenheit.
4 Calculate average of 3 numbers.
5 Find square and cube of a number.
6 Swap two numbers without third variable.
7 Create a Student Report Program that take student details using input(), Store marks in variables, Calculate total 
and percentage , Use comments, Use proper indentation"""
#1
def area():
    length=int(input("enter length of rectangle"))
    breadth=int(input("enter the breadth of rectangle"))
    area=length*breadth
    print("Area of the rectangle is",area)
def simple_interest():
    principal_amount=int(input("enter the principal amount"))
    Rate_of_interest_per_year=int(input("enter Rate of interest per year"))
    time=int(input("Time the money is borrowed or invested (in years)"))
    simple_interest=(principal_amount*Rate_of_interest_per_year*time)/100
    print("simple interest is",simple_interest)
def conversion():
    celsius=int(input("enter celsius temperature"))
    converted=(celsius*(9/5))+32
    print("after conversion",converted)
def average():
    a=int(input("enter first number"))
    b=int(input("enter second number"))
    c=int(input("enter third number"))
    average=(a+b+c)/3
    print("average of ",a,b,c,"is",average)
def square_or_cube():
    no=int(input("enter the number"))
    ch=int(input("for square enter 1 for cube enter 2"))
    if ch==1:
        print("square of ",no,"is",no**2)
    elif ch==2:
        print("cube of ",no,"is",no**3)
    else:
        print("wrong choice")
def swap():
    a=int(input("enter first number"))
    b=int(input("enter xecond number"))
    a,b=b,a
    print("afte the swap a=",a,"b=",b)
def student_input():
    sum=0
    name=input("enter your name")
    college=input("enter your college name")
    branch=input("enter your branch")
    subjects=int(input("how many subjects"))
    total=int(input("enter total marks"))
    sum = 0
    for i in range(subjects):
        marks = int(input(f"Enter marks of subject {i+1}: "))
        sum += marks
        percentage = (sum / total) * 100
    print("your percentage is",(sum/total)*100)
def menu():
        while True:
            ch=int(input("enter your choice"))
            if ch==1:
                area()
                
            elif ch==2:
                simple_interest()
                
            elif ch==3:
                conversion()
                
            elif ch==4:
                average()
                
            elif ch==5:
                square_or_cube()
                
            elif ch==6:
                swap()
                
            elif ch==7:
                student_input()
            
            else:
                print("no such option available please try again later")
                break
menu()


        
