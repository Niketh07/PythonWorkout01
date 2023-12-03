# import re

# def find_numbers(input_string):
    
#     pattern = '\A \b \B[z|Z]'
#     char =re.search(pattern,input_string)
    
#     if char:
#         print(f'Z or z found: {char}')
#     else:
#         print('No Z or z found.')

# input_string = "There will be many animals in the zoo. Zebra can be also seen in a zoo"
# find_numbers(input_string)

import re

pattern = r'\b\w*[zZ]\w*\b'

input_string = "There will be many animals in the zoo. Zebra can be also seen in a zoo"
matches = re.findall(pattern, input_string, flags=re.IGNORECASE)

print(matches)
