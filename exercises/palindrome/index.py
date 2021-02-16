def palindrome(str):
    alpha_counter = [0] * 26

    for index in range(len(str)):
        if index < int(len(str)/2) + 1:
            alpha_counter[numRep(str[index])] += 1
        else:
            alpha_counter[numRep(str[index])] -= 1

    print(alpha_counter)

    return pal_list(alpha_counter)

def pal_list(count):
    counter = 0

    for val in count:
        if val < 0:
            return False
        if val > 0:
            counter += 1

    if counter > 1:
        return False
    
    return True

def numRep(char):
    return ord(char) - ord('a')



# Much easier way... check reverse equality
def rev_palindrome(str):
    return str == reverse(str)

def reverse(str):
    if len(str) < 2:
        return str
    
    return str[len(str)-1] + reverse(str[:len(str)-1])


# Traversal Solution
def trav_palindrome(str):
    for index in range(len(str)):
        if str[index] != str[len(str)-1-index]:
            return False
    return True