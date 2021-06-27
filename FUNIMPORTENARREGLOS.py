colors = ["Verde", "Morado", "Negro"]
person = {"name":"kakashi", "lastname": "wells", "age":24}

colors.remove("Verde")
for value in colors:
    print(value)

for key,value in person.items():
    print(key,"",value)
