def swap_pos():
    string = input('String: ')
    l_string = list(string)
    temp = l_string[0]
    l_string[0] = l_string[1]
    l_string[1] = temp
    print(''.join(l_string))

def replace_char():
    string = input('String: ')
    old_char = input('Old char: ')
    new_char = input('New char: ')
    new_string = string.replace(old_char, new_char)
    print(new_string)
    
print('1. Swap 1st and 2nd char')
print('2. Replace char')
choose = int(input('Enter choice (1) or (2): '))
if choose == 1:
    swap_pos()
elif choose == 2:
    replace_char()
