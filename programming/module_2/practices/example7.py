a = 3
b = 5
c = '*'

if c == '+':
    result = a + b
elif c == '-':
    result = a - b
elif c == '*':
    result = a * b
# elif c == '/':
#     if b != 0:
#         result = a / b
#     else:
#         result = 'Division by zero error'
elif c == '/' and b != 0:
    result = a / b

else:
    result = 'Invalid operation'

print(result)
