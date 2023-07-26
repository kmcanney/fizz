print("FizzBang!")

top = int(input("How high should we count? "))
for number in range(1,top):
    if number % 5 == 0 and number % 3 == 0:
        print("FizzBang")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Bang")
    else:
        print(number)