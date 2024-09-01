# 1. The following is a list of 10 students ages:
#   ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#   I. Sort the list and find the min and max age

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min_age = min(ages)
max_age = max(ages)
print(f"Sorted ages: {ages}")
print(f"Min age: {min_age}, Max age: {max_age}")

#   II. Add the min age and the max age again to the list

ages.extend([min_age, max_age])
print(f"Ages after adding min and max: {ages}")

#   III. Find the median age (one middle item or two middle items divided by two)

if len(ages) % 2 == 0:
    med_age = (ages[len(ages)//2 - 1] + ages[len(ages)//2]) / 2
else:
    med_age = ages[len(ages)//2]
print(f"Median age: {med_age}")

#   IV. Find the average age (sum of all items divided by their number )

avg_age = sum(ages) / len(ages)
print(f"Average age: {avg_age}")

#   V. Find the range of the ages (max minus min)

age_range = max_age - min_age
print(f"Age range: {age_range}")

#   VI. Compare the value of (min - average) and (max - average), use _abs()_ method

min_diff = abs(min_age - avg_age)
max_diff = abs(max_age - avg_age)
print(f"Min-Average Difference: {min_diff}, Max-Average Difference: {max_diff}")




#2.Iterate through the list,
#['Python','Numpy','Pandas','Django','Flask'] using a for loop and print out the items.

items = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for item in items:
    print(item)


# 3.Create fruits, vegetables and animal products tuples.

fruits = ("apple", "banana", "cherry")
vegetables = ("carrot", "broccoli", "spinach")
animal_products = ("milk", "cheese", "yogurt")

# I. Join the three tuples and assign it to a variable called food_stuff_tp.

food_stuff_tp = fruits + vegetables + animal_products
print(f"Food stuff (tuple): {food_stuff_tp}")

# II. Change the about food_stuff_tp tuple to a food_stuff_lt list4

food_stuff_lt = list(food_stuff_tp)
print(f"Food stuff (list): {food_stuff_lt}")

# III. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.

middle_index = len(food_stuff_lt) // 2
if len(food_stuff_lt) % 2 == 0:
    middle_items = food_stuff_lt[middle_index-1:middle_index+1]
else:
    middle_items = food_stuff_lt[middle_index]
print(f"Middle item(s): {middle_items}")

# IV. Slice out the first three items and the last three items from food_staff_lt list

first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print(f"First three items: {first_three}, Last three items: {last_three}")

# V. Delete the food_staff_tp tuple completely

del food_stuff_tp


# 4. Create a set given below
# it_companies = {&#39;Facebook&#39;, &#39;Google&#39;, &#39;Microsoft&#39;, &#39;Apple&#39;, &#39;IBM&#39;, &#39;Oracle&#39;, &#39;Amazon&#39;}
# A = {19, 22, 24, 20, 25, 26}
# B = {19, 22, 20, 25, 26, 24, 28, 27}
# age = [22, 19, 24, 25, 26, 24, 25, 24]

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# I. Find the length of the set it_companies

print(f"Length of IT companies: {len(it_companies)}")

# II. Add &#39;Twitter&#39; to it_companies

it_companies.add('Twitter')
print(f"IT companies after adding Twitter: {it_companies}")

# III. Insert multiple IT companies at once to the set it_companies

it_companies.update(['TCS', 'Infosys', 'Wipro'])
print(f"IT companies after adding multiple companies: {it_companies}")

# IV. Remove one of the companies from the set it_companies

it_companies.discard('Oracle')
print(f"IT companies after removing Oracle: {it_companies}")

# V. What is the difference between remove and discard

#ANSWER: `remove()` raises an error if the item doesn't exist, `discard()` does not.
  # Set operations with A and B


# 5. From the above sets A and B
# I. Join A and B

A_B_union = A.union(B)
print(f"A union B: {A_B_union}")

# II. Find A intersection B

A_B_intersection = A.intersection(B)
print(f"A intersection B: {A_B_intersection}")

# III. Is A subset of B

is_A_subset_B = A.issubset(B)
print(f"Is A a subset of B? {is_A_subset_B}")

# IV. Are A and B disjoint sets

are_disjoint = A.isdisjoint(B)
print(f"Are A and B disjoint sets? {are_disjoint}")

# V. Join A with B and B with A

A_B_join = A.union(B)
B_A_join = B.union(A)
print(f"A join B: {A_B_join}")
print(f"B join A: {B_A_join}")

# VI. What is the symmetric difference between A and B

sym_diff = A.symmetric_difference(B)
print(f"Symmetric difference between A and B: {sym_diff}")

# VII. Delete the sets completely

del it_companies, A, B

# 6. Create an empty dictionary called dog.Add name, color, breed, legs, age to the dog dictionary

dog = {
    "name": "Buddy",
    "color": "Brown",
    "breed": "Golden Retriever",
    "legs": 4,
    "age": 5
}
print(dog)


# 7. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills,
# country, city and address as keys for the dictionary

student = {
    "first_name": "John",
    "last_name": "Doe",
    "gender": "Male",
    "age": 21,
    "marital_status": "Single",
    "skills": ["Python", "Java"],
    "country": "USA",
    "city": "New York",
    "address": "123, 4th Street, NY"
}

# I. Get the length of the student dictionary

print(f"Length of the student dictionary: {len(student)}")

# II. Get the value of skills and check the data type, it should be a list

skills = student["skills"]
print(f"Skills: {skills}, Type: {type(skills)}")

# III. Modify the skills values by adding one or two skills

student["skills"].extend(["SQL", "C++"])
print(f"Updated skills: {student['skills']}")

# IV. Get the dictionary keys as a list
keys = list(student.keys())
print(f"Keys: {keys}")

# V. Get the dictionary values as a list
values = list(student.values())
print(f"Values: {values}")

# VI. Change the dictionary to a list of tuples using items() method
items = list(student.items())
print(f"Items: {items}")

# VII. Delete one of the items in the dictionary
del student["city"]
print(f"Dictionary after deleting city: {student}")

# VIII. Delete the student dictionary completely
del student


# 8.Create a person dictionary.
#  person = {
#     'first_name': 'Asabeneh',
#     'last_name': 'Yetayeh',
#     'age': 250,
#     'country': 'Finland',
#     'is_married': True,
#     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#     }
# }

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# I. Check if the person dictionary has skills key, if so print out the middle skill in the skills list.

if 'skills' in person:
    skills_list = person['skills']
    middle_skill = skills_list[len(skills_list) // 2]
    print(f"Middle skill: {middle_skill}")

# II. Check if the person dictionary has skills key, if so check if the person has &#39;Python&#39; skill and print out the result.

if 'skills' in person:
    has_python = 'Python' in person['skills']
    print(f"Has Python skill: {has_python}")

# III. If a person skills has only JavaScript and React, print(&#39;He is a front end developer&#39;), if the
# person skills has Node, Python, MongoDB, print(&#39;He is a backend developer&#39;), if the person
# skills has React, Node and MongoDB, Print(&#39;He is a fullstack developer&#39;), else print(&#39;unknown
# title&#39;) - for more accurate results more conditions can be nested!

if set(['JavaScript', 'React']).issubset(person['skills']):
    print("He is a front-end developer.")
elif set(['Node', 'Python', 'MongoDB']).issubset(person['skills']):
    print("He is a backend developer.")
elif set(['React', 'Node', 'MongoDB']).issubset(person['skills']):
    print("He is a fullstack developer.")
else:
    print("Unknown title.")

# IV. If the person is married and if he lives in Finland, print the information in the following
# format:
# py
# Asabeneh Yetayeh lives in Finland. He is married.

if person['is_married'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in Finland. He is married.")

# 9. Print the season name of the year based on the month number using a dictionary.

month_season = {
    1: "Winter",
    2: "Winter",
    3: "Spring",
    4: "Spring",
    5: "Spring",
    6: "Summer",
    7: "Summer",
    8: "Summer",
    9: "Autumn",
    10: "Autumn",
    11: "Autumn",
    12: "Winter"
}

month = int(input("Enter month number (1-12): "))
season = month_season.get(month, "Invalid month")
print(f"The season is: {season}")
