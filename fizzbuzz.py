def series(num):
    count = 1
    if count != num:
        while True:
            if count % 15 == 0:
                print("FizzBuzz")
            elif count % 3 == 0:
                print("Fizz")
            elif count % 5 == 0:
                print("Buzz")
            else:    
                print(count)
            count = count + 1
            if count > num:
                break


num = int(input("Write a number to print the series: "))
series(num)