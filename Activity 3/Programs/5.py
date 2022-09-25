#to perform upper case of later part of string
#using upper + loop + len()
str = 'welcometoworldofpython'
print("String =",str)
l =len(str) #calculate the length 
h = l/2  # divides the length by 2
newstr = " " #creating a new string 
for i in range(l):
    if i>=h:
        newstr += str[i].upper()
    else:
        newstr += str[i]
print(f"The new string = {newstr}")

#using string slicing
str = "helloworld"
print(f"\nThe string is {str}")
print(f"The new string is {str[:5]}{str[5:].upper()}")