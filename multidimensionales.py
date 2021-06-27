shoes = {
"Nike":["tenis 1","tenis 2","tenis 3"],
"Converse":["tenis 3","tenis 4","tenis 5"],
"Vans":["tenis 6", "tenis 7", "tenis 8"]}

for key, list in shoes.items():
    for value in list:
        print ("EStos son los tenis", key, value)