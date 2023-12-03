
import re

pattern = r'\b[^zZ]\w*z\w*[^zZ]\b'

input_string = "Bees make a buzzing sound where Zebra doesnt."
matches = re.search(pattern, input_string, flags=re.IGNORECASE)

print(matches)