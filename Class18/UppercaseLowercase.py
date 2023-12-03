import re

def find_sequences(input_string):
    pattern = re.compile(r'[A-Z][a-z]+')
    sequences = pattern.findall(input_string)
    
    if sequences:
        print(f'Sequences found: {sequences}')
    else:
        print('No sequences found.')

input_string = "Sample Program"
find_sequences(input_string)
