list = {'abd' :'as','hf':'er'}
print(list)

#Dictionary Creation with different column names

students = {
    1: {"name": "google", "age": 20},
    2: {"name": "deloite", "age": 22},
    3: {"name": "pwc", "age": 19},
    4: {"name": "aaa", "age": 21},
    5: {"name": "Eee", "age": 23},
}

# Example of accessing the data
for student_id, details in students.items():
    print(f"Student ID: {student_id}, Name: {details['name']}, Age: {details['age']}")

import pandas as pd
data =[20,30,40,50,2,3,6,8,10,18,19,20,24,2,4,5,6]

No_of_studied = data[4:8]
print("No.Of hours_studied",No_of_studied)
Age = data[9:13]
print("Student_age",Age)
screen_time = data[12:18]
print("screen_time",screen_time)
Data_Frame = pd.DataFrame(data)
print(Data_Frame)

#  creating dataframe with dictionary and lists

import pandas as pd

# Creating lists
No_of_studied = [2, 3, 6, 8]
Age = [10, 18, 19, 20]
screen_time = [24, 2, 4, 5]

# Creating a DataFrame
df = pd.DataFrame({
    "No_of_studied": No_of_studied,
    "Age": Age,
    "screen_time": screen_time
})

# Display the DataFrame
print(df)



#List Mutability

#Python mutable lists may involve various data types such as objects, integers and strings.


numbers = [1, 2, 3, 4, 5]
print(numbers)

numbers[0] = 99         #changing the value of index 0
numbers[2] = 'python'   #changing the value of index 2
numbers[4] = -46        #changing the value of index 4

print(numbers)

#Taking a string input and converting it into a list of elements

#Note: use split() function


# Python program to take space
# separated input as a string
# split and store it to a list
# and print the string list

# input the list as string
string = input("Enter elements (space-separated)): ")

# split the strings and store it to a list
lst = string.split()
print('The list is:', lst)   # printing the list

#Concatenating Lists 1

# concatenate means to join two things together. You can use the + operator to concatenate two lists.


list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list3 = list1 + list2

print(list3)

#Concatenating Lists 2


favorite_fruits = ["Apple", "Banana", "Cherry"]
favorite_vegetables = ["Carrot", "Broccoli", "Cucumber"]

# Now let's concatenate them
favorite_foods = favorite_fruits + favorite_vegetables

print("Favorite Fruits:", favorite_fruits)
print("Favorite Vegetables:", favorite_vegetables)
print("Favorite Foods:", favorite_foods)

#Tuple with only one item

#To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.


thistuple1 = ("apple",)
print(type(thistuple1))

#NOT a tuple
thistuple2 = ("apple")
print(type(thistuple2))

#Tuples can store various data types


tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)

#Example 7: len() Function


my_list = [10, 20, 30, 40]
size = len(my_list)
print(size)

d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(d)

