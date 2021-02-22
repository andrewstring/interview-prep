def fizz_buzz(n):
    for num in range(1, n+1):
        if not num % 3 and not num % 5:
            print('fizzbuzz')
        elif not num % 3:
            print('fizz')
        elif not num % 5:
            print('buzz')
        else: print(num)

fizz_buzz(100)