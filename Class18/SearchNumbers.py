import re

def find_numbers(input_string):
    
    pattern = re.compile(r'\b\d{1,3}\b')
    numbers = pattern.findall(input_string)
    
    if numbers:
        print(f'Numbers found: {numbers}')
    else:
        print('No numbers found.')

input_string = "Exercises number 1, 12, 13, and 345 are important"
find_numbers(input_string)
