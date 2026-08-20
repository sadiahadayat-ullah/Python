import re

text = "Call 03001234567, 0300-1234567 or 0311 7654321."
result = re.findall(r"\d{4}[- ]?\d{7}", text)
print(result)