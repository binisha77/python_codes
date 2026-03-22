#A string is a sequence of characters.
#Accessing Characters

name = "Python"

print(name[0])
print(name[2])


name = input("Enter your name: ")

print("Upper:", name.upper())
print("Lower:", name.lower())
print("Length:", len(name))


#check if a skill exists tin resume text
resume = input("Enter resume text: ")

if "python" in resume.lower():
   print("Python skill found")
else:
   print("Python skill not found")

