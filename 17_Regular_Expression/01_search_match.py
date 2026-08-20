import re

# re.search()

text = "I love Python."
result = re.search("Python", text)
print(result.group())

# re.match() - match at beginning

text = "Python is easy."
result = re.match("Python", text)
print(result.group())

# re.match() - no match

text = "I love Python."
result = re.match("Python", text)

if result:
    print("Found:", result.group())
else:
    print("Not found.")