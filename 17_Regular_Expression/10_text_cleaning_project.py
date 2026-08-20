import re

# Original messy text

text = """
Hello!!! Contact us at ali@gmail.com or sara@yahoo.com.
Call 03001234567 or 0300-1234567.
Python is easy!!!
"""

# 1. Clean whitespace

cleaned_text = re.sub(r"\s+", " ", text)

# 2. Remove unwanted punctuation

cleaned_text = re.sub(r"[!]", "", cleaned_text)

print(cleaned_text)

# 3. Extract email addresses

emails = re.findall(r"[\w.-]+@[\w.-]+\.\w+", text)

print(emails)

# 4. Extract phone numbers

phones = re.findall(r"\d{4}[- ]?\d{7}", text)

print(phones)

# 5. Escaping

result = re.findall(r"\.com", text)

print(result)

# 6. Alternation

result = re.findall(r"Python|Hello", text)

print(result)