# Define a function to calculate the area of a rectangle
def calculate_area(length, width):
    return length * width

# Call the function and display the result
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = calculate_area(length, width)
print(f"The area of the rectangle is: {area}")