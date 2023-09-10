import re

# Input string
input_str = "This is some text [[jalla]] [[keep|remove]] more text [[keep ]] final text"

# Create the regex pattern
pattern = re.compile(r'\[\[(.*?\|.*?)\]\]|\[\[(.*?)\]\]')

# Function to handle the replacement
def replace(match):
    if match.group(1):
        return "[[" + match.group(1) + "]]"
    else:
        return match.group(2)

# Replace using the pattern and the custom function
result = pattern.sub(replace, input_str)

print(result)

