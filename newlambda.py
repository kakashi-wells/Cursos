numbers =[1,2,3,4,5]
update = []
for value in numbers:
    update.append(value*2)
print(update)

def operation(value):
    return value*2
print((list(map(operation,numbers))))