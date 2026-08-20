import re

# re.findall()

text = "I have 10 apples, 20 oranges, and 30 bananas."
result = re.findall(r"\d+", text)
print(result)

# re.finditer()

text = "I have 10 apples, 20 oranges, and 30 bananas."
matches = re.finditer(r"\d+", text)

for match in matches:
    print(match.group())