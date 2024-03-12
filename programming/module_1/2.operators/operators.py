
# 'AND', 'OR', and "NOT" operators
age = 25
is_student = True

if age >= 18 and is_student:
    print("You qualify for a student discount.")
else:
    print("Regular pricing applies.")



# 

default_name = 'User'
name = 'Natalia'

current_name = default_name and name # Natalia
current_name = default_name or name # User

current_name = not name # False
current_name = not default_name # False


# IF ELSE
age = int(input('How old are you ?'))

if age >= 21:
    print('Welcome!')

    if age > 100:
        print("Wow")

elif 0 < age < 21:
     print('Too early for you!')
     
else:
    print('Wrong input')

print('Thanks anywhere!')