import re

# [abc]

text = "apple bat cat dog"
result = re.findall(r"[abc]", text)
print(result)

# [a-z]

text = "Python AI 123"
result = re.findall(r"[a-z]", text)
print(result)

# [A-Z]

text = "Python AI"
result = re.findall(r"[A-Z]", text)
print(result)

# [0-9]

text = "Python123"
result = re.findall(r"[0-9]", text)
print(result)

# [A-Za-z]

text = "Python123 AI!"
result = re.findall(r"[A-Za-z]", text)
print(result)

# [A-Za-z0-9]

text = "Python123!"
result = re.findall(r"[A-Za-z0-9]", text)
print(result)

# [^0-9]

text = "Python123"
result = re.findall(r"[^0-9]", text)
print(result)

# \d

text = "Python 123 AI"
result = re.findall(r"\d", text)
print(result)

# \w

text = "Python 123 AI"
result = re.findall(r"\w", text)
print(result)

# \s

text = "Python 123 AI"
result = re.findall(r"\s", text)
print(result)