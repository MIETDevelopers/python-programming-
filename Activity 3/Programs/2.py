#To extract characters in the given, range from the given string.
#using list comprehension and join()
str = ["welcome","To","World","Of","Python"]
print("String",str)
start,end = 6, 12
newstr = "".join([sub for sub in str])[start:end]
print(f"Required Output = {newstr}")