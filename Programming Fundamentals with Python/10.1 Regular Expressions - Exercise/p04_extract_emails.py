import re

emails_pattern = (r"(^|(?<=\s))[a-z0-9]+((?:\.|\_|\-)(?![\.\_\-]))*(?:[a-z0-9]|\2"
                  r"(?![\.\_\-]))*\@[a-z]+(\-(?!\-))*[a-z]+(\.+[a-z]+(\-(?!\-))*[a-z]+)+")

text = input()

emails = re.finditer(emails_pattern, text)

for email in emails:
    print(email.group())