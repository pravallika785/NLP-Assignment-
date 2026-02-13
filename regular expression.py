import re

text = "Contact us at info@gmail.com or support@yahoo.com"

# regex pattern for email
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

emails = re.findall(pattern, text)

print("Emails found:")
for email in emails:
    print(email)
