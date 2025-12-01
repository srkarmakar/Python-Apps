"""
Requirement: 
As a system administrator, I need to clean up and validate user-submitted product codes. 
The code should be stripped of any leading/trailing whitespace, and then its first letter must be checked to ensure 
it is capitalized (True/False check). Finally, the entire code must be converted to uppercase for database storage.

Example Input String: "  pROD-xY-2024 \n " (Note the leading/trailing spaces and newline character)

Action Steps (String Methods to Use):

1.Use a method to remove whitespace from both ends.
2.Use a method to check if the string starts with a capital letter.
3.Use a method to convert the entire cleaned string to uppercase.

Expected Output:
A boolean value (True/False) that answers: "Is the first character of the cleaned string capitalized?" 
(Value: $\text{False}$).
The final, Uppercase, Cleaned String (Value: "PROD-XY-2024").
"""

def string_cleaner_validator():
    product_code = input('Please enter your product code:')
    product_code = product_code.strip()  # Remove leading/trailing whitespace and newline
    is_capitalized = product_code[0].isupper()  # Check if the first character is capitalized
    result = product_code.upper()  # Convert to uppercase
    print(f'Is the first character of the cleaned string capitalized? {is_capitalized}')

    print(f'The final, Uppercase, Cleaned String:"{result}"')

input = string_cleaner_validator()