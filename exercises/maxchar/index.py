def max_char(input):
    max_char = ''
    max_count = 0

    current_char = ''
    current_count = 0

    for i in range(len(input)-1):
        current_char = input[i]
        current_count = 1
        for j in range(i+1,len(input)):
            if input[i] == input[j]:
                current_count += 1
        if current_count > max_count:
            max_count = current_count
            max_char = current_char

    return max_char

print(max_char('abcdcddd1cd1cc1dcd1<11111'))


def dict_max_char(input):
    counter = {}
    max_char = ''
    max_count = 0

    for char in input:
        if char in counter.keys():
            counter[char] += 1
        else: counter[char] = 1
        if counter[char] > max_count:
            max_char = char
            max_count = counter[char]

    return max_char

print(dict_max_char('testing1111111222111'))