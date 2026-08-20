import re

# Capturing Groups()

text = "Name: Sadia, Age: 18"
result = re.search(r"Name: (\w+), Age: (\d+)", text)

print(result.group())
print(result.group(1))
print(result.group(2))
print(result.groups())

# Named Groups

text = "Name: Sadia, Age: 18"
result = re.search(r"Name: (?P<name>\w+), Age: (?P<age>\d+)", text)

print(result.group("name"))
print(result.group("age"))
print(result.groupdict())

