#A list stores multiple values.

skills = ["Python", "Java", "React"]

# access elements
print(skills[0])
print(skills[2])

# add item to list
skills.append("Docker")

print(skills)

#loop through list 
skills = ["Python", "Java", "React"]

for skill in skills:
   print(skill)

students = []

for i in range(3):
  
   name = input("Enter student name: ")
  
   students.append(name)

print(students)
