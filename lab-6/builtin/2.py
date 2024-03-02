def count_upper_lower(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count

input_string = "Kbtu LaB"
upper, lower = count_upper_lower(input_string)
print(f"Uppercase letters: {upper}, Lowercase letters: {lower}")
