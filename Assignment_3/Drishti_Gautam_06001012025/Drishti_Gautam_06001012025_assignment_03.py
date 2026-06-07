"""Assignment-03
Student name-Drishti gautam
Enrollment number-06001012025
College-IGDTUW 
QUESTIONS:
1.Create a function to print first 10 natural numbers.
2.Create a function to calculate sum of first N natural numbers.
3.Create a function to reverse a number.
4.Create a function to count digits in a number.#done
5.Create a function to check palindrome number.
6.Create a function to generate Fibonacci series.
7.Calculator Using Functions that contains the following features:
User selects operation
Program performs calculation
Display result
8.Create a text file and store student details.
9.Read data from a file.
10.Handle division by zero using exception handling.
11,Create a Student class with name and marks.
"""
#1.
def natural_no():#print natural number upto n
    for i in range(1,11):
        print(i)

#2
def sum(n):#by use of parameter
    sum=0
    for i in range(1,n+1):
        sum+=i
    print(sum)
#3
"""def reverse():
    number=int(input("enter number u want to reverse(if single digit add 0 before writing number) "))
    a=number%10
    b=number/10"""
def count(n):
    a=len(str(n))
    print(a)
def palindrome_number(n):
    a = str(n)
    b = len(a)

    for i in range(b):
        if a[i] != a[b-i-1]:
            print("not a palindrome number")
            return

    print("palindrome number")

#6
def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

fibonacci(10)
#7
def user_choice():
    ch=input("enter your choice(+,-,*,/)")
    sum=0
    numbers=int(input("on how many numbers u want to perform operation"))
    for i in range(numbers):
        number=int(input(f"enter your {i+1} number"))
        if ch=="+":
            sum+=number
            print(sum)





