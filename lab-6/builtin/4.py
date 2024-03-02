import time
import math

def square_root_after_delay(number, milliseconds):
    time.sleep(milliseconds / 1000)
    result = math.sqrt(number)
    return result

input_number = int(input())
delay_milliseconds = int(input())
result = square_root_after_delay(input_number, delay_milliseconds)
print(f"Square root of {input_number} after {delay_milliseconds} milliseconds is {result}")
