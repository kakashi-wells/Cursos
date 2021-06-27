colors = ["Verde", "Morado", "Negro", "Verde"]
numbers = {1, 2, 3, 4, 5}
person = {"name":"kakashi", "lastname": "wells", "age":24}
numbers.extend()
for value in numbers:
    print(value)

for key,value in person.items():
    print(key,"",value)