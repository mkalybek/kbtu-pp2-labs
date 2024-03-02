def is_palindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string

input_str = "radar"
if is_palindrome(input_str):
    print(f"{input_str} is a palindrome.")
else:
    print(f"{input_str} is not a palindrome.")
