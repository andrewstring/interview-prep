def reverseInt(n):
    output = 0
    counter = 0

    while n > 0:
        output = output * 10 + n%10
        counter += 1
        n = int(n/10)

    return output

def rec_reverse(n):

    if n < 10:
        return str(n)

    return str(n%10) + rec_reverse(int(n/10))


print(rec_reverse(10123))
