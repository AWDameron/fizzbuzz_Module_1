number_list = list(range(1, 101))

def fizz_buzzify(numbers):
    x = 0 
    while x < len(numbers):
        if numbers[x] % 3 == 0 and numbers[x] % 5 == 0:
            numbers[x] = "fizzbuzz"
        elif numbers[x] % 5 == 0:
            numbers[x] = "buzz"
        elif numbers[x] % 3 == 0:
            numbers[x] = "fizz"
        x += 1
    print(numbers)
    return

fizz_buzzify(number_list)


def fizzy_buzzy(x,y):
    fizzy_list = list(range(x, y+1))
    for x in range(len(fizzy_list)):
        match (fizzy_list[x] % 3 == 0, fizzy_list[x] % 5 == 0):
            case (True,True):
                fizzy_list[x] = "fizzbuzz"
            case (False,True):
                fizzy_list[x] = "buzz"
            case (True, False):
                fizzy_list[x] = "fizz"
            case _:
                pass
    print(fizzy_list)
    return

fizzy_buzzy(1,10)
fizzy_buzzy(7,43)
