#SUM OF THE SQUAREROOT OF TWO NUMBERS >>>

import math
# sum=0
# num1= int(input("Enter the first number: "))
# num2= int(input("Enter the second number: "))
# num3= int(input("Enter the third number: "))

# sq1= math.sqrt(num1) 
# sq2= math.sqrt(num2)
# sq3= math.sqrt(num3)

# sum=sq1+sq2+sq3

# print("Sum of the square root of 3 numbers are: "+str(sum))

#QUADRATIC EQUATION >>>

# a=int(input("Enter a number: "))
# b=int(input("Enter a number: "))
# c=int(input("Enter a number: "))

# if(a==0):
#     print("Value should not be zero")
# else:
#     p=(b*b)-(4*a*c)
#     if(p>0):
#         r1=(-b+math.sqrt(p)/2*a)
#         r2=(-b-math.sqrt(p)/2*a)
#         print("Roots are real and unequal")
#         print("r1= ",r1,"r2= ",r2)
#     elif(p==0):
#         r1=-b/(2*a)
#         r2=-b/(2*a)
#         print("Roots are real and equal")
#         print("r1= ",r1,"r2= ",r2)
#     else:
#         print("Roots are complex and imaginary")

#Find GCD of two numbers

# n1= int(input("Enter first number: "))
# n2= int(input("Enter second number: "))

# if n1 > n2:
#     smaller= n2
# else:
#     smaller= n1
# for i in range(1,smaller+1):
#     if((n1 % i==0) and (n2 % i==0)):
#         gcd=i
# print("GCD of ",n1,"and",n2, "is", gcd)

#Compute :-
# a)5 to the power of 8  

# pow=5 ** 8
# print("5 to the power of 8= ",pow)

# # b)square root of 400
# print("Square root of 400= ",(math.sqrt(400)))

#  # c)exponent of 5
# print("The exponent of e to the power 5= ",(math.exp(5)))

# # d)Logarithm of 625 base 5
# print("Logarithm of 625 base 5= ",(math.log(625,5)))

# # Compute  :-
# # a)sin of 60 degree
# angle_degrees=60
# angle_radians= math.radians(angle_degrees)
# sin60=math.sin(angle_radians)
# print("sin of 60 degrees= ",sin60)

# #  b)cos of pi 
# cos_pi=math.cos(math.pi)
# print("Cos of pi= ",cos_pi)

# # c)sin(0.8660254037844386)
# val=0.8660254037844386
# sin_val=math.sin(val)
# print("sin of 0.8660254037844386= ",sin_val)

# #  d)tan of 90 degree
# angle_degrees_90=90
# angle_radians_90= math.radians(angle_degrees_90)
# tan_90=math.tan(angle_radians_90)
# print("Tan of 90 degrees= ",tan_90)

# Define a sum function with two parameters and call the function
# def sum(a,b):
#     return a+b

# result=sum(10,22)
# print("Sum of 10 and 22= ",result)

# #Reverse a given string
# def rev_str(s):
#     return s[::-1]

# input_str="Computer Applications"
# reversed_str= rev_str(input_str)
# print("Reversed string is ",reversed_str)

#Calculate the power of a number using recursion
# def power(base,exponent):
#     if exponent == 0:
#         return 1
#     elif exponent == 1:
#         return base
#     else:
#         return base*power(base,exponent-1)
    
# base=3
# exponent=3
# result=power(base,exponent)
# print(f"{base} to the power of {exponent} is : ",result)

# #Convert Decimal number to Binary
# def dec_to_bin(n):
#     if n==0:
#         return "0"
#     binary=""
#     while n>0:
#         binary=str(n%2)+binary
#         n//=2
#     return binary

# bin_num=dec_to_bin(10)
# print(f"Decimal 10 in binary is: ",bin_num)

#Check if a number is a Krishnamurthy number : 
#A Krishnamurthy number (Strong number) is a number where the sum of the factorials of its digits is equal to the number itself.
# num=int(input("Enter a number to check: "))
# temp=num
# sum=0

# while temp>0:
#     fact=1
#     remainder=temp%10
#     fact=math.factorial(remainder)
#     sum=sum+fact
#     temp//=10
# if(sum==num):
#     print(f"\n{num} is a Krishnamurthy number")
# else:
#     print(f"\n{num} is not a Krishnamurthy number")

#Find the sum of digits of a number
# n1=int(input("Enter a number= "))
# sum=0

# while n1>0:
#     digit=n1%10
#     sum=sum+digit
#     n1=n1//10
    
# print("Sum of digit= ",sum)

#Print the multiplication table for a number provided by the user
# n=int(input("Enter a numer: "))
# for i in range(1,11):
#  print(f"{n} * {i}=",(n*i))

 #Print the first 6 terms of a geometric sequence starting with 2 and having a common ratio of 3
# def geometric_sequence(start, ratio, terms):
#  sequence = [start * (ratio ** i) for i in range(terms)]
#  return sequence

# # Generate and print the sequence
# sequence = geometric_sequence(2, 3, 6)
# print("First 6 terms of the geometric sequence= ", sequence)

# Print the series up to N terms: 1, 2, 6, 24, 120, 720 ..
#this series represents factorial of numbers from 1 to n...
def fact_series(n):
 series=[]
 fact=1
 for i in range(1,n+1):
  fact*=i
  series.append(fact)
 return series

series=fact_series(6)
print("Series upto 6 is ",series)

#Calculate power of a base to an exponent without using the exponentiation operator or math.pow()
def pow_without_exp(base,exponent):
  result=1
  for i in range(exponent):
   result*=base
  return result

base=int(input("Enter base number= "))
exponent=int(input("Enter exponent number= "))
result=pow_without_exp(base,exponent)
print(f"{base} to the power of {exponent=}",result)