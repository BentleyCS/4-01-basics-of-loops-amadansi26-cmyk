#All questions must use a loop for full points.

def oddNumbers(n:int) ->str:
    a = 1
    number = ""
    while a<= n:
        number = number + str(a) + " "
        a=a+2
        return number

def backwards(n)-> int:
    result = ""
    while n>1:
        result = result + str(n)+ " "
        n = n - 1
        return result

def randomRepeating():
    tries = 0
    while True:
        tries = tries + 1
        num = random.randint(1, 10)
        print(num)
        if num == 10:
            break
    print("it took", tries, "tries to get a 10")

def randomRange(n):
    def randomRange(n):
        counting = 0
        lowest = 100
        highest = 1

        while counting < n:
            num = random.randint(1, 100)
            print(num)

            if num < lowest:
                lowest = num
            if num > highest:
                highest = num

            counting = count + 1

        print("Lowest number:", lowest)
        print("Highest number:", highest)

def reverse(word:str)->str:
    def reverse(word: str) -> str:
        result = ""
        m = len(word) - 1
        while m >= 0:
            result = result + word[m]
            m = m - 1
        return result

def fizzBuzzContinuous(n):
    result = ""
    m = 1
    while m <= n:
        if m % 3 == 0 and m % 5 == 0:
            result = result + "fizzbuzz "
        elif m % 3 == 0:
            result = result + "fizz "
        elif m % 5 == 0:
            result = result + "buzz "
        else:
            result = result + str(m) + " "
        m = m + 1
    return result

def collatz(n):
    while n != 1:
        print(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    print(1)

def fibonacci(n):
    if n <= 0:
        return ""

    if n == 1:
        return "0 "

    result = "0 1 "
    a = 0
    b = 1
    count = 2

    while count < n:
        c = a + b
        result = result + str(c) + " "
        a = b
        b = c
        count = count + 1

    return result

print(fibonacci(300))
