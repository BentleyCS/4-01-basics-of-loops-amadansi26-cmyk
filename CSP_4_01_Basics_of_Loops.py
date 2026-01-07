#All questions must use a loop for full points.

def oddNumbers(n:int) ->str:
    number_string = ""
    for i in range(1,n):
        if i % 2 != 0:
            number_string = number_string + " " + str(i)
    return number_string
print(oddNumbers(10))

def backwards(n)-> int:
    rewind = ""
    for i in range(n, 0, -1):
        rewind = rewind + str(i) + " "
    return rewind
print(backwards(8))

def randomRepeating(n):
    import random
    highest = 1
    lowest = 100
    for i in range(n):
        randomNum = random.randint(1, 100)
        if randomNum > highest:
            highest = randomNum
        if randomNum < lowest:
            lowest = randomNum
    print(highest, lowest)
randomRepeating(5)

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
    reverseString = ""
    for i in range(len(word)-1, -1, -1):
        reverseString = reverseString + word[i]
    print(reverseString)
reverse("zeug")

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
    while n > 1:
        if n % 2 == 0:
            print(n)
            n = n/2
            continue
        if n % 2 != 0:
            print(n)
            n = (n*3) + 1
collatz(99)

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
