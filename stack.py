class stack:

    def __init__(self):
        self.stack = [] # Define an empty stack

    def st_is_empty(self):
        if(len(self.stack) == 0):
            return True
        else:
            return False

    def st_push(self,data):
        self.stack.append(data)
        print(data ," has been added in the stack")

    def st_pop(self):
        if(obj_stack.st_is_empty()):
            print("Stack is Empty")
            return -1
        else:
            self.stack.pop()

    def st_peek(self):
        if(obj_stack.st_is_empty()):
            print("Stack is Empty")
            return -1
        else:
            return self.stack[-1]

if __name__ == "__main__":
    obj_stack = stack()
    obj_stack.st_push(10)
    obj_stack.st_push(20)
    obj_stack.st_push(30)
    obj_stack.st_push(40)
    top_element = obj_stack.st_peek()
    print("Top element in the stack", top_element)
    obj_stack.st_pop()
    top_element = obj_stack.st_peek()
    print("Top element in the stack", top_element)


