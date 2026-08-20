import re

# re.sub() - Replace a word

text = "I love Python. Python is easy."
result = re.sub("Python", "Regex", text)
print(result)

# re.sub() - Remove unwanted characters

text = "Hello!!! Python!!!"
result = re.sub(r"[!]", "", text)
print(result)

# re.sub() - Clean extra whitespace

text = "Python  is  very  easy."
result = re.sub(r"\s+", " ", text)
print(result)

# re.split() - Basic split

text = "apple,banana,orange"
result = re.split(r",", text)
print(result)

# re.split() - Handle different separators

text = "apple, banana; orange, mango"
result = re.split(r"[,;]\s*", text)
print(result)