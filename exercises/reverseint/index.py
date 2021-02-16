def reverseInt(n):
    output = 0
    power = 0

    while(n/10 >= 1):
        output += 10**power * n%10
        n = int(n/10)
        power += 1

    output += n 
    
    return output
    
print(reverseInt(125))