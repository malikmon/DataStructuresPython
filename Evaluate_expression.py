# Class is defined to evaluate the expression

Class evaluate_expression:

    # init method to initialise the variables
    def __init__(self):
        # An empty stack
        stack = []
        # A tuple for valid operators
        operators = ('+','-','/','*')

    # to check if stack is empty
    def is_empty(self):
        if (self.stack is None):
            print("Stack is empty")
            return False

     # to push item into the stack
    def push_stack(self, item):
        self.stack.append(item)


     # function to calculate expression
     def to_eval_expr(self, str):
        Case1 : If string is empty
        if (len(str) == 0):
            return False
        else:
            for char in str:
                if char in self.operators:





