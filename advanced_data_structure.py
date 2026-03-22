#last in first out


stack = []

stack.append("Type A")
stack.append("Type B")
stack.append("Delete Word")

print("Actions:", stack)

undo = stack.pop() 
print("Undo:", undo)
print("Remaining:", stack)


