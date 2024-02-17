def fibonacci(length):
    serie = [0,1]

    n1 = 0
    n2 = 1

    count = 2

    while count < length:
        newNum = n1+n2
        serie.append(newNum)

        n1 = n2
        n2 = newNum

        count+=1

    return serie           

print( fibonacci(30))