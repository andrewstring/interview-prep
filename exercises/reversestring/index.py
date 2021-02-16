def reverse_rec(str):
    if len(str) < 2:
        return str
    
    return str[len(str)-1] + reverse_rec(str[:len(str)-1])

def reverse_iter(str):
    reverse = ''

    for index in reversed(range(len(str))):
        reverse += str[index]
    return reverse

if reverse_rec('abcd') == 'dcba': print('1')
if reverse_rec('    abcd') == 'dcba    ': print('2')

if reverse_iter('abcd') == 'dcba': print('3')
if reverse_iter('    abcd') == 'dcba    ': print('4')