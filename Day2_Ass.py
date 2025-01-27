'''Create a List, tuple and Dictionary with 5 elements in it and how to access few elements based on the index. Try  with different examples '''

# Creating a List with 5 elements
my_list = [10, 3.14, "apple", True, "banana"]

# Accessing elements based on index
print("List Element at index 0:", my_list[0])  # 10
print("List Element at index 1:", my_list[1])  # 3.14
print("List Element at index 4:", my_list[4])  # banana
print('\n')

# Creating a Tuple with 5 elements
my_tuple = (5, "orange", 7.2, False, "grapes")

# Accessing elements based on index
print("Tuple Element at index 0:", my_tuple[0])  # 5
print("Tuple Element at index 2:", my_tuple[2])  # 7.2
print("Tuple Element at index 3:", my_tuple[3])  # False
print('\n')


# Creating a Dictionary with 5 elements
my_dict = {
    "name": "John",
    "age": 25,
    "city": "New York",
    "is_student": True,
    "grades": [90, 85, 88]
}

# Accessing elements based on keys
print("Dictionary Value for 'name':", my_dict["name"])  # John
print("Dictionary Value for 'age':", my_dict["age"])  # 25
print("Dictionary Value for 'grades':", my_dict["grades"])  # [90, 85, 88]
