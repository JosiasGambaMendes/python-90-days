def collatz(number):
    if number % 2 == 0:
        result = number/2
       
    else:
        result = 3 * number + 1

    print(result)
    return result

while True:
    try:
        typNum = int(input("Type an Integer Number: "))
        break
    except ValueError:
        print("You must enter an integer.")

while typNum != 1:
    typNum = collatz(typNum)
    
