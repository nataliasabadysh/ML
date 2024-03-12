# calculating the area and hypotenuse of a right-angled triangle


# S = (a*b) / 2 
# - This formula calculates the area of a right-angled triangle, 
# where a and b are the lengths of the two perpendicular sides (base and height). 
# The area S is equal to half the product of these two sides.

# C = sqrt(a**2 + b**2) 
# - This formula calculates the length of the hypotenuse C of a 
# right-angled triangle using the Pythagorean theorem. 
# The length of the hypotenuse is the square root 
# of the sum of the squares of the other two sides.


from math import sqrt

a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))

# Calculate the area of the triangle
S = (a * b) / 2

# Calculate the length of the hypotenuse
C = ( a**2 + b**2 )**(1/2) 
# or -> C = sqrt(a**2 + b**2)

# Print the results
print(f"Area of the triangle: {S}")
print(f"Length of the hypotenuse: {C}")
