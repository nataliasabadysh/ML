// Type Conversion in JavaScript

parseInt("2.8"); // returns 2
parseInt("123"); // returns 123
parseInt("hello"); // returns NaN (Not a Number)

parseFloat(2); // returns 2
parseFloat("3.14"); // returns 3.14

String(123); // returns "123"
String(3.14); // returns "3.14"

Array.from("hello"); // returns ['h', 'e', 'l', 'l', 'o']

// There is no direct equivalent for tuple in JavaScript

// Convert array to Set to remove duplicates
new Set([1, 2, 2, 3]); // returns Set {1, 2, 3}

// Convert array of key-value pairs to an object (similar to dict in Python)
Object.fromEntries([
  [1, "one"],
  [2, "two"]
]); // returns {1: 'one', 2: 'two'}

String.fromCharCode(65); // returns 'A'

"A".charCodeAt(0); // returns 65

// JavaScript doesn't have built-in functions for converting numbers to hex, octal, or binary,
// but you can use the toString method with a radix:
(255).toString(16); // returns 'ff'
(8).toString(8); // returns '10'
(5).toString(2); // returns '101'

Boolean(0); // returns false
Boolean(1); // returns true
Boolean([]); // returns true (empty array is truthy in JavaScript)
Boolean([1, 2]); // returns true (non-empty array)

// Implicit Type Conversion (Type Coercion)
let result = "5" + 2; // returns '52' (string concatenation)
let sum = "5" - 2; // returns 3 (numeric subtraction)

// Explicit Type Conversion
let num = Number("42"); // returns 42 (string to number)
let str = String(42); // returns '42' (number to string)

// Converting to Boolean
let truthyValue = Boolean("hello"); // returns true
let falsyValue = Boolean(""); // returns false

// Converting between Arrays and Strings
let arr = Array.from("123"); // returns ['1', '2', '3']
let joinedStr = arr.join("-"); // returns '1-2-3'

// Converting Objects to Arrays
let obj = { a: 1, b: 2, c: 3 };
let keys = Object.keys(obj); // returns ['a', 'b', 'c']
let values = Object.values(obj); // returns [1, 2, 3]
let entries = Object.entries(obj); // returns [['a', 1], ['b', 2], ['c', 3]]

// Converting a Set to an Array
let mySet = new Set([1, 2, 3]);
let myArray = Array.from(mySet); // returns [1, 2, 3]

// Converting a NodeList to an Array (common in DOM manipulation)
let nodeList = document.querySelectorAll("div");
let divArray = Array.from(nodeList);
