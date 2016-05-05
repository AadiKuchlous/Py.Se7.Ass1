import re

email = input("enter email id \n")
pattern = "@([a-zA-Z]+)\."
ser = re.search(pattern, email)
print(ser.group(1))
