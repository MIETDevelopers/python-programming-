#Check if the string is alphanumeric or not
str = 'welcomeToWorldOfPython'
print("String =",str)
print(str.isalnum())  #prints true if string contains only alphabet and numeric part and no whitespaces 

str = 'welcomeToWorldOfPython123'
print("String =",str)
print(str.isalnum()) 

str = 'welcomeToWorldOfPython 123'
print("String =",str)
print(str.isalnum()) #prints false as it contains whitespaces

str = 'welcomeToWorldOfPython_123'
print("String =",str)  #prints false as it contains special character
print(str.isalnum()) 