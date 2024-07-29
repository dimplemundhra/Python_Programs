#Celsius to Fahrenheit >>>

# celsius=int(input("Enter the temperature in celsius="))
# fahreinheit= 32+(celsius * 9/5)
# print("fahreinheit= ", fahreinheit)

# #Swap two numbers >>>>

# a=int(input("Enter the first number: "))
# b=int(input("Enter the second number: "))
# temp=0

# print("Before swap=",a)
# print("Before swap=",b)

# temp=a
# a=b
# b=temp
# print("After swap=",a)
# print("After swap=",b)

#Leap Year or Not >>>>

# year= int(input("Enter the year: "))

# if(year%100==0 and year%400==0):
#     print(f"{year} is Leap year")
# else:
#     print("Not a Leap year")

#Reverse of a number >>>>

# num=int(input("Enter a number: "))
# reversed_num=0

# while num != 0:
#     digit = num % 10
#     reversed_num = (reversed_num * 10) + digit
#     num = num // 10

# print("Reversed number= ",str(reversed_num))

#Factors of a given number >>>

# num=int(input("Enter a number: "))
# for i in range(1,num+1):
#     if num % i == 0:
#         print(i)
# print(f"The factors of {num} is {i}")

#Prime number series upto nth >>>

# num=int(input("Enter a number: "))
# for num in range (1, num+1):
#  count=0
#  for i in range(2,(num//2+1)):   
#     if(num % i == 0):
#         count=count+1
#     break
#  if(count == 0 and num !=1):  
#   print(" %d" %num, end='')


#use a function to display all such numbers that are divisible by 7 and not a multiple of 5 between 1000 and 2000 >>>>


  




#Palindrome number or not >>>>>

# num= int(input("Enter a number: "))
# temp=num
# rev=0

# while (num>0):
  
#   digit= num % 10
#   rev= (rev*10)+ digit 
#   num= num//10

# if(temp == rev):
#     print("Palindrome number")
# else:
#     print("Not a Palimndrome number") 


#Perfect number or not >>>

# num=int(input("Enter a number: "))
# sum=0
# for i in range(1, num):
#    if(num %i == 0):
#       sum = sum+i
# if(sum == num):
#   print("Perfect Number !!")
# else:
#    print("Not a Perfect Number !!")
    

#Armstrong number or not >>>>

# num=int(input("Enter a number: "))
# temp=num
# sum=0

# while temp > 0:
#    digit= temp % 10
#    sum+=digit**3
#    temp= temp//10
# if(num == sum):
#    print(num,"is an Armstrong Number")
# else:
#    print(num,"is Not an Armstrong Number")

#Fibonaccii series >>>>

num=int(input("Enter a number: "))
num1=0
num2=1
new_num = num2

print("Fibonacci Series:", num1, num2, end=" ")
for i in range(2, num):
    new_num = num1 + num2
    num1 = num2
    num2 = new_num
    print(new_num, end=" ")

print()
