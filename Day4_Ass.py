'''Write a Python program to calculate the sum of all even numbers between 1 and a given positive integer n'''

# Taking input for the positive integer n
n = int(input("Enter a positive integer: "))

# Initialize the sum of even numbers
even_sum = 0

# Loop through numbers from 1 to n and add the even ones
for i in range(1, n+1):
    if i % 2 == 0:  # Check if the number is even
        even_sum += i

# Print the sum of even numbers
print("Sum of all even numbers between 1 and", n, "is:", even_sum)
