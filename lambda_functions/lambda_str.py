


# a function without a name is called an anonymous function or a lambda function
#when we need a short dunction for a short period of time ,we can use a lambda function
# syntax of a lambda agruments: expression

def add(x,y):
    return x+y

print (add(2,3))
#using lambda function
add_lambda = lambda x,y : x+y
print (add_lambda(2,3))

squar_no = lambda x : x**2
print (squar_no(5))


numbers = [1,2,3,4,5]
for num in numbers:
    print (num)

    for i,num in enumerate(numbers):
        print (f"index: {i}","Number: {num} ")

        #sorting
        
    
    
