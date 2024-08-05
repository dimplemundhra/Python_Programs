import math

# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
# def check_season(month):
#     month=month.lower()
#     if month in ['december','january','February']:
#         return 'Winter'
#     elif month in ['march','april','may']:
#         return 'Spring'
#     elif month in ['June','July','August']:
#         return 'Summer'
#     elif month in ['September','October','November']:
#         return 'Autumn'
#     else:
#         return 'Invalid Month'
# print(check_season('December'))


# # Write a function called calculate_slope which return the slope of a linear equation
# def calc_slope(x1,y1,x2,y2):
#     if x2==x1:
#         raise ValueError("Cannot calculate slope for vertical line (x1 == x2)")
#     return (y2-y1)/(x2-x1)

# print(calc_slope(1,3,4,6))

# #Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, _solve_quadratic_eqn_.
# def quad_eqn(a,b,c):
#     discriminant=b**2 - 4*a*c
#     if discriminant>0:
#         root1=(-b + math.sqrt(discriminant))/(2*a)
#         root2=(-b - math.sqrt(discriminant))/(2*a)
#         return(root1,root2)
#     elif(discriminant==0):
#         root=-b/(2*a)
#         return (root)
#     else:
#         return(0)
    
# print(quad_eqn(1,-3 ,2))

# # Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
# def print_list(l1):
#     for item in l1:
#         print(item)
# print([24,7,8,12,10])

# # Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
# def reversed_list(ar):
#     rev_ar=[]
#     for i in range(len(ar)-1,-1,-1):
#         rev_ar.append(ar[i])
#     return rev_ar
# print(reversed_list([2,5,6,8,19]))

# # Compute the sum up to n terms in the series 1 - 1/2 + 1/3 - 1/4 + 1/5 -... 1/n where n is a positive integer and input by user.
# def series_sum(n):
#     sum_series=0
#     for i in range(1,n+1):
#         if(i % 2 == 0):
#             sum_series-=1/i
#         else:
#             sum_series+=1/i
#     return sum_series

# n=int(input("Enter the value of n: "))
# print(series_sum(n))

# Write a program to compute sin x for given x. The user should supply x and a positive integer n. We compute the sine of x using the series and the computation should use all terms in the
# series up through the term involving xn sin x = x - x3/3! + x5/5! - x7/7! + x9/9! ........
# def sin_series(x,n):
#     sin_x=0
#     sign=1
#     for i in range(n):
#         term=sign * (x ** (2*i+1)) / math.factorial(2*i+1)
#         sin_x+=term
#         sign=-sign
#     return sin_x

# x=float(input("Enter the value of x= "))
# n=int(input("Enter the number of terms n= "))

# result=sin_series(x,n)
# print(f"sin({x}) ussing {n} terms is approximately {result}")

# Write a program to compute cosine of x. The user should supply x and a positive integer n.We compute the cosine of x using the series and the computation should use all terms in the
# series up through the term involving xn cos x = 1 - x2/2! + x4/4! - x6/6! ....
# def cos_series(x,n):
#     cos_x=0
#     sign=1
#     for i in range(n):
#         term=sign * (x ** (2*i)) / math.factorial(2*i)
#         cos_x+=term
#         sign=-sign
#     return cos_x

# x=float(input("Enter the value of x= "))
# n=int(input("Enter the number of terms n= "))

# result=cos_series(x,n)
# print(f"cos({x}) using {n} terms is approximately {result}")

#Print the pattern upto N Lines:  \ /WRONG
#  .                              / \
# /_\  .
#     / \
#    /___\
#            .
#           / \
#           / \
#         /_____\
# N=2  N=3   N=4
# def print_pattern(n):
#     for i in range(1, n+1):
#         print(" " * (n - i) + "/" + " " * (2 * (i - 1)) + "\\")
#         print(" " * (n - i) + "/" + "_" * (2 * (i - 1)) + "\\")

# # Input from user
# N = int(input("Enter the number of lines N: "))
# print_pattern(N)

#  Write a python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27 
# 4 1 4 16 64
# 5 1 5 25 125
def print_table():
    #print(f"{'N':>2} {'1':>2} {'2':>2} {'N^2':>3} {'N^3':>3}")
    for n in range(1, 6):
        print(f"{n:>2} {1:>2} {n:>2} {n**2:>3} {n**3:>3}")

print_table()


