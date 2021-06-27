colors = ["Verde", "Morado", "Negro", "Verde"]
numbers = {1, 2, 3, 4, 5}
person = {"name":"kakashi", "lastname": "wells", "age":24}

for value in colors:
    (value)

person.update({"phone":"1234567890"})
for key,value in person.items():
    print(key,"",value)