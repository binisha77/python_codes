def add(a,b):
  return a+b
print (add(5,3))

#using lambda function
add = lambda a,b : a+b
print (add(5,3))


#basic 
nums = [5, 2, 9, 1]
print(sorted(nums))


print(sorted(nums, reverse=True))

#sort by key
students =[("Ram",20),("Shyam",18),("Hari",15)]
sorted_students = sorted(students, key=lambda x:x[1])
print(sorted_students)


# used to filter elements based on condition

# filter(function, iterable)

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

