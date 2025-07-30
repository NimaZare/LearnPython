import re

email = input("What's your email? ").strip()

# if re.search(r"^.+@.+\.edu$", email): # ==> can set  mail@@@gmail.edu  and valid ! 
# if re.search(r"^[^@]+@[^@]+\.edu$", email): # ==> [^@] means any characters is valid except @ is invalid, can type .edu@xnmzsck.edu valid !
# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email): #==> [a-zA-Z0-9_] is equal to \w
# if re.search(r"^\w+@\w+\.edu$", email):
# if re.search(r"^\w+@\w+\.(com|edu|net|org|gov)$", email): # ==> accept diffrents domain but not accept Mail@EVERY.EDU uppercase !
# if re.search(r"^\w+@\w+\.(com|edu|net|org|gov)$", email.lower()): # ==> or use flags in re.search method
# if re.search(r"^\w+@\w+\.(com|edu|net|org|gov)$", email, re.IGNORECASE): # ==> not accept Mail@sub.domain.edu !
if re.search(r"^(\w|\.)+@(\w+\.)?\.(com|edu|net|org|gov)$", email, re.IGNORECASE): # ==> (\w+\.)?  means this match is optinal for sub domains
    print("Valid")
else:
    print("Invalid")
