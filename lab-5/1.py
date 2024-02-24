import re

# Task 1: Match a string with an 'a' followed by zero or more 'b's.
pattern1 = re.compile(r'ab*')

# Task 2: Match a string with an 'a' followed by two to three 'b's.
pattern2 = re.compile(r'ab{2,3}')

# Task 3: Find sequences of lowercase letters joined with an underscore.
pattern3 = re.compile(r'[a-z]+_[a-z]+')

# Task 4: Find sequences of one uppercase letter followed by lowercase letters.
pattern4 = re.compile(r'[A-Z][a-z]+')

# Task 5: Match a string with an 'a' followed by anything, ending in 'b'.
pattern5 = re.compile(r'a.*b$')

# Task 6: Replace all occurrences of space, comma, or dot with a colon.
def replace_with_colon(input_string):
    return re.sub(r'[ ,.]', ':', input_string)

# Task 7: Convert snake case string to camel case string.
def snake_case_to_camel_case(snake_case):
    words = snake_case.split('_')
    return words[0] + ''.join(word.capitalize() for word in words[1:])

# Task 8: Split a string at uppercase letters.
def split_at_uppercase(input_string):
    return re.split(r'(?=[A-Z])', input_string)

# Task 9: Insert spaces between words starting with capital letters.
def insert_spaces_at_caps(input_string):
    return re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', input_string)

# Task 10: Convert camel case string to snake case.
def camel_case_to_snake_case(camel_case):
    return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', camel_case).lower()

# Example usage:
input_string = "abbbb"
if pattern1.fullmatch(input_string):
    print("Task 1: Match!")
else:
    print("Task 1: No match.")

input_string = "abb"
if pattern2.fullmatch(input_string):
    print("Task 2: Match!")
else:
    print("Task 2: No match.")

input_string = "hello_world"
matches = pattern3.findall(input_string)
print("Task 3: Matches:", matches)

input_string = "CamelCaseString"
matches = pattern4.findall(input_string)
print("Task 4: Matches:", matches)

input_string = "aanythingb"
if pattern5.match(input_string):
    print("Task 5: Match!")
else:
    print("Task 5: No match.")

input_string = "This, is. a string"
result = replace_with_colon(input_string)
print("Task 6: Result:", result)

snake_case = "snake_case_string"
result = snake_case_to_camel_case(snake_case)
print("Task 7: Camel Case:", result)

input_string = "SplitAtUppercase"
result = split_at_uppercase(input_string)
print("Task 8: Result:", result)

input_string = "InsertSpacesAtCaps"
result = insert_spaces_at_caps(input_string)
print("Task 9: Result:", result)

camel_case = "CamelCaseString"
result = camel_case_to_snake_case(camel_case)
print("Task 10: Snake Case:", result)
