import re
st="hello everyone"
pattern="everyone"
if re.match(pattern,st):
    print("match found")
else:
    print(pattern,"is not present in the string")