# 1st Question - Printing numbers and summing
n = int(input("Enter a positive integer: "))
print("Numbers from 1 to", n, "using a for loop:")
for i in range(1, n + 1):
    print(i)

sum_numbers = 0
i = 1
while i <= n:
    sum_numbers += i
    i += 1
print("Sum of numbers from 1 to", n, "is:", sum_numbers)

# 2nd Question - Square of a number
def calculate_square(n):
    return n ** 2

n = int(input("Enter a positive integer for calculating its square: "))
square = calculate_square(n)
print(f"The square of {n} is: {square}")