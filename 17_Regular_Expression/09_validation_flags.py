import re

# re.fullmatch() - Digits

text = "12345"
result = re.fullmatch(r"\d+", text)
if result:
    print(result.group())
else:
    print("Invalid")

# re.fullmatch() - Valid exactly 5 digits

text = "12345"
result = re.fullmatch(r"\d{5}", text)
if result:
    print(result.group())
else:
    print("Invalid")

# re.fullmatch() - Invalid

text = "1234"
result = re.fullmatch(r"\d{5}", text)
if result:
    print(result.group())
else:
    print("Invalid")

# re.fullmatch()- Validate only English letters

text = "Python"
result = re.fullmatch(r"[A-Za-z]+", text)
if result:
    print(result.group())
else:
    print("Invalid")

# re.fullmatch() - Invalid

text = "Python123"
result = re.fullmatch(r"[A-Za-z]+", text)
if result:
    print(result.group())
else:
    print("Invalid")

# re.IGNORECASE()

text = "I LOVE PYTHON"
result = re.search(r"python", text, re.IGNORECASE)
if result:
    print(result.group())
else:
    print("Not found")

# re.MULTILINE()

text = """Python is easy.
Java is popular.
Python is powerful."""
result = re.findall(r"Python", text, re.MULTILINE)
if result:
    print(result)
else:
    print("Not found")

# re.DOTALL()
text = """Hello
Python"""
result = re.search(r"Hello.Python", text, re.DOTALL)
if result:
    print(result.group())
else:
    print("Not found")

# Combine flags

text = """Python
PYTHON
python
Java"""
result = re.findall(r"^python", text, re.IGNORECASE | re.MULTILINE)
if result:
    print(result)
else:
    print("Not found")