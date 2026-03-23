


try:
    x = 10/2
except ZeroDivisionError:
    print("you can't divide by zero")
else:
    print("success",x)
finally:
    print("this always runs and works")
