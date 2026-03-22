#A tuple is like a list but cannot be changed (immutable).

location = (27.7172, 85.3240)

print("Latitude:", location[0])
print("Longitude:", location[1])


#dictionary
student = {
   "name": "Ram",
   "age": 20,
   "city": "Kathmandu"
}
#3 access data
print(student["name"])
print(student["city"])

# add data
student["course"] = "Python"

print(student)

# example 

student = {}

student["name"] = input("Enter name: ")
student["age"] = input("Enter age: ")
student["course"] = input("Enter course: ")

print(student)
