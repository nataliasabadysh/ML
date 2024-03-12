
# Prompt the user to input a four-digit number
four_digit_num = input("Input a four-digit number: ")

# Check if the input has exactly 4 digits
if len(four_digit_num) == 4:
    # Convert each digit to an integer and calculate the average
    first_digit = int(four_digit_num[0])
    second_digit = int(four_digit_num[1])
    third_digit = int(four_digit_num[2])
    fourth_digit = int(four_digit_num[3])

    average = (first_digit + second_digit + third_digit + fourth_digit) / 4
    print("The average of the digits is:", average)
else:
    print("Please enter a valid four-digit number.")
