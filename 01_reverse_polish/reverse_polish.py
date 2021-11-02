from math import floor, ceil

operators = ["+", "-", "*", "/"]

class Solution:
    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            if token in operators:
                # operator
                operand1 = stack.pop(0)
                operand2 = stack.pop(0)
                if token == "+":
                    result = operand1 + operand2
                elif token == "-":
                    result = operand2 - operand1
                elif token == "*":
                    result = operand1 * operand2
                elif token == "/":
                    result = operand2 / operand1
                    if result > 0:
                        result = floor(result)
                    else:
                        result = ceil(result)
                else:
                    raise Exception("Invalid token")
                stack.insert(0, result)
            else:
                # number
                num = int(token)
                stack.insert(0, num)
        return stack[0]
        
solution = Solution()
tokens = ["2","1","+","3","*"]
result = solution.evalRPN(tokens)
print("Result 1:", result)

tokens = ["4","13","5","/","+"]
result = solution.evalRPN(tokens)
print("Result 2:", result)

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
result = solution.evalRPN(tokens)
print("Result 2:", result)