import re

# + - One or More

text = "I have 123 apples and 45 oranges."
result = re.findall(r"\d+", text)
print(result)

# * - Zero or More

text = "color colour"
result = re.findall(r"colou*r", text)
print(result)

# ? - Zero or One

text = "color colour"
result = re.findall(r"colou?r", text)
print(result)

# {n} - Exactly n

text = "My code is 1234."
result = re.findall(r"\d{4}", text)
print(result)

# {n, m} - Between n and m

text = "5 25 250 2500 25000"
result = re.findall(r"\d{2,4}", text)
print(result)

# ^ - Beginning

text = "Python is easy."
result = re.findall(r"^Python", text)
print(result)

# $ - End

text = "I love Python"
result = re.findall(r"Python$", text)
print(result)

# Combine quantifier+anchor

text = "12345"
result = re.findall(r"^\d{5}$", text)
print(result)