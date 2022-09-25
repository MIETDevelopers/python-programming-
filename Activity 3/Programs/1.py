#Count the number of alphabets in the given string.

#using isalpha()
#isalpha() method returns True if the given string contains only alphabets.
str = 'welcomeToWorldOfPython'
count = 0
for i in str:    # i holds each character in String s for every iteration of loop
    if (i.isalpha()):  
        count = count + 1    # Increment Count by 1
print("Number of Alphabet :",count)     

str = 'welcomeToWorldOfPython123@string'
count = 0
for i in str:    # i holds each character in String s for every iteration of loop
    if (i.isalpha()):  
        count = count + 1    # Increment Count by 1
print("Number of Alphabet :",count) 