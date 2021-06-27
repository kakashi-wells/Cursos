def plusnumbers(list):
    even = 0
    odd = 0
    for value in list:
        if value % 2 ==0:
          even = even + value
        else:
          odd=odd + value
    print("suma de numeros pares",even)    
    print("suma de numeros impares",odd)    

plusnumbers([1,2, 3, 4, 5, 6, 7, 8, 9])