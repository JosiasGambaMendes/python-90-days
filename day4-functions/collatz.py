def collatz(number):
    if number % 2 == 0:
        result = number/2
       
    else:
        result = 3 * number + 1

    print(result)
    return result

typNum = int(input("Type an Integer Number: "))

while typNum != 1:
    typNum = collatz(typNum)
    
