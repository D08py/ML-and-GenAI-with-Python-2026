"""1.find sum of first 10 natural numbers 
2.find factorial of number
3.print fibonacci series
4.create student result system with input student details input marks calculate percentage display grade(use id-elif-else,loops)"""
print("Assignment 2")
#1.
sum=0
for i in range(1,11):
    sum+=i
print(sum)
def factorial(n):
    if n== 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
def fibonacci_generator(n):
    a, b = 0, 1
    result = []#created  a list to store
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

print(fibonacci_generator(10))
def student_result():
    sum=0
    name=input("enter your name")
    college=input("enter your college name")
    branch=input("enter your branch")
    subjects=int(input("how many subjects"))
    total=int(input("enter total marks"))
    for i in range(subjects):
        marks=int(input(f"enter your marks of subject {i+1}"))
        sum+=marks
        percentage=(sum/total)*100
    print("your percentage is",(sum/total)*100)
    if percentage>=90:
        print(name,"from",college,"and",branch,"scored",percentage,"and CONGRATULATIONS GRADE A")
    elif percentage>=80 and percentage<90:
        print(name,"from",college,"and",branch,"scored",percentage,"Could have been better Grade B")
    elif percentage>=70 and percentage<80:
        print(name,"from",college,"and",branch,"scored",percentage,"better luck next time Grade C")
    elif percentage>=60 and percentage<70:
        print(name,"from",college,"and",branch,"scored",percentage,"POOR RESULT GRade D")
    else:
        print(name,"from",college,"and",branch,"scored",percentage,"FAIL:")
    
student_result()