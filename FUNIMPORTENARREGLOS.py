colors = ["Verde", "Morado", "Negro", "Verde"]
numbers = {1, 2, 3, 4, 5}
person = {"name":"kakashi", "lastname": "wells", "age":24}
animal = {"name":"hawk","colors":"white","age":4}
print(len(colors))
print(len(person))
for value in colors:
    print(value)
    

for key,value in person.items():
    print(key,"",value)