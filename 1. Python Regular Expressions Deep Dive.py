
import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)

# Task 1

for email in emails:
    email_match = re.search(r"@exclude.com", email)
    if email_match:
        emails.remove(email)
    

print(emails)