def oddNumbers(n:int) -> str:
    number_string = ""
    if n < 1:
        return ""
    for i in range(1, n + 1):
        if i % 2 != 0:
            if number_string == "":
                number_string = str(i)
            else:
                number_string = number_string + " " + str(i)
    return number_string


def backwards(n) -> str:
    rewind = ""
    if n < 1:
        return ""
    for i in range(n, 0, -1):
        if rewind == "":
            rewind = str(i)
        else:
            rewind = rewind + " " + str(i)
    return rewind


def randomRepeating():
    import random
    tries = 0
    num = 0
    while num != 10:
        num = random.randint(1, 10)
        tries += 1
    print(f"it took {tries} tries to get a 10")


def randomRange(n):
    import random
    if n <= 0:
        return
    lowest = 100
    highest = 1
    count = 0

    while count < n:
        num = random.randint(1, 100)
        if num < lowest:
            lowest = num
        if num > highest:
            highest = num
        count += 1

    print("Lowest number:", lowest)
    print("Highest number:", highest)


def reverse(word: str) -> str:
    reverseString = ""
    for i in range(len(word) - 1, -1, -1):
        reverseString = reverseString + word[i]
    return reverseString


def fizzBuzzContinuous(n):
    result = ""
    if n < 1:
        return ""
    m = 1
    while m <= n:
        if m % 3 == 0 and m % 5 == 0:
            result = result + "fizzbuzz"
        elif m % 3 == 0:
            result = result + "fizz"
        elif m % 5 == 0:
            result = result + "buzz"
        else:
            result = result + str(m)

        if m != n:
            result = result + " "
        m += 1
    return result


def collatz(n):
    if n < 1:
        return ""
    result = ""
    while True:
        result = result + str(n)
        if n == 1:
            break
        result = result + " "
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    return result


def fibonacci(n):
    if n <= 0:
        return ""

    a = 0
    b = 1
    result = ""
    count = 0

    while count < n:
        if result == "":
            result = str(a)
        else:
            result = result + " " + str(a)
        c = a + b
        a = b
        b = c
        count += 1

    return result


print(fibonacci(300))

