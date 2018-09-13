class valid_expression:
    def __init__(self):
        self.stack = [] # An empty stack

    def st_push(self,item): # to push the open parentheses
        self.stack.append(item)

    def to_check_valid(self,input_str):

        # Case1 is to check if string is empty
        if(len(input_str) == 0):
            return False

        for char in input_str:
            if (char in ("(","{","[")): # if char has any open parenthes then push it into the stack
                obj_valid.st_push(char)
            else:
                if len(self.stack) == 0:
                    return False
                top_item = self.stack.pop()
                # if it makes a valid pair
                if (char == ')'and top_item == '(' ):
                    pass
                elif (char == '}'and top_item == '{' ): # if it makes a valid pair
                    pass
                elif (char == ']'and top_item == '[' ): # if it makes a valid pair
                    pass
                else:
                    return False

        if len(self.stack) == 0: # length will be 0 only when we get pair for each char
            return True
        else:
            return False # if len is not 0 then it has only open parentheses hence invalid


#Define main function where program actually run
if __name__ == "__main__":
    obj_valid = valid_expression()
    result = obj_valid.to_check_valid(')')
    if(result == True):
        print('Valid Parentheses')
    else:
        print('Invalid Parentheses')
