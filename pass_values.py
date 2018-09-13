input = 'How are you, eo'
output = 'Hw ar yu'

# split the string into list
list_str = input.split(',')
print(type(list_str))
# parsed string
str_par = list_str[0].strip()
str_del = list_str[1].strip()
print(str_par)
print(str_del)

final_str = ''

for char in str_par:
    if char in str_del:
        pass
    else:
        final_str += char
print("Final string is:", final_str)




