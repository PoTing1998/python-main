import re

regex  = r"\b[A-Za-z0-9._+%-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
regex2 = r"[^@]+@[^@]+\.[^@]+"


def check_email(email):
    if re.match(regex, email):
        print (f"{email} is a valid email")
    else:
        print (f"{email} is not a valid email")

text = "My phone number is  808-744-000 ,and 64-000-0000"
result = re.findall(r"(\d{2,3})-(\d{3})-(\d{4)",text)