# Create an empty list to store the numbers in
numbers = []

# User input
for i in range(5):
    num = float(input("Input a number: "))
    numbers.append(num)

# Sort the numbers from highest to lowest
numbers.sort(reverse=True)

# Display the sorted list
print("Numbers from highest to lowest:", numbers)