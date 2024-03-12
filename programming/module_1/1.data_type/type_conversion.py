# Type Conversion in Python

int(2.8)  # returns 2
int("123")  # returns 123
int("hello")  # ValueError: invalid literal for int() with base 10: 'hello'


float(2)  # returns 2.0
float("3.14")  # returns 3.14

str(123)  # returns "123"
str(3.14)  # returns "3.14"

list("hello")  # returns ['h', 'e', 'l', 'l', 'o']

tuple([1, 2, 3])  # returns (1, 2, 3)

set([1, 2, 2, 3])  # returns {1, 2, 3}

dict([(1, 'one'), (2, 'two')])  # returns {1: 'one', 2: 'two'}

chr(65)  # returns 'A'

ord('A')  # returns 65

hex(255)  # returns '0xff'

oct(8)  # returns '0o10'

bin(5)  # returns '0b101'

bool(0)  # returns False
bool(1)  # returns True
bool([])  # returns False (empty list)
bool([1, 2])  # returns True (non-empty list)