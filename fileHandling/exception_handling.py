
#exception handling in python
#sytax error -wrong code
#runtime error - during program executon
#basic try except
#only test during development not during production
#during production the value must be analysed at initial point


# try:
#     print('inside try except block')
#     num = int(input("enter a number:"))
#     print(10/num)
#
# except :
#      print("Invalid input")


try:
    print('inside try except block')
    num = int(input("enter a number:"))
    print(10/num)

except ValueError :
     print("Invalid input: please enter a number")
except ZeroDivisionError :
    print ("Yoy cant divide by zero")