number = 10

def decimalToBinary(number):
    if number >=1 :
        decimalToBinary(number // 2)

    print(number % 2, end=" ")


decimalToBinary(number)