import re

text = "Contact us at ali@gmail.com or sara@yahoo.com or student@university.edu"
result = re.findall(r"[\w.-]+@[\w.-]+\.\w+", text)
print(result)