def all_elements_true(tuple_values):
    return all(tuple_values)

bool_tuple = (True, True, True)
if all_elements_true(bool_tuple):
    print("All elements are true")
else:
    print("Not all elements are true")
