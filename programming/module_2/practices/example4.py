# Sum of the last two digits of a number

nums = input('Input number: ')

if len(nums) >= 2:
    # Convert the last two digits to integers and sum them

    # same as len(nums)-1 and len(nums)-2 
    result = int(nums[-1]) + int(nums[-2])
    print(f"The sum of the last two digits is: {result}")
else:
    print("The number must have at least two digits.")
