opening = ( '(', '{', '[')
closing = ( ')', '}', ']')
dictionary_parentheses = dict(zip(opening, closing))
valid_list = []


def is_valid_exp(str):

    if (len(str) == 0):
        return False

    elif (len(str) % 2 != 0):
        return False

    elif (str[0] in closing):
        return False

    elif (str[-1] in opening):
        return False
    else:
        for char in str:
            if (char in opening):
                valid_list.append(dictionary_parentheses[char])
            else:
                if (valid_list is None or char != valid_list.pop()):
                    return False
        return True

result = is_valid_exp("{(")
print(result)