class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {'+','-','*','/'}
        for ch in tokens:
            if ch not in operations:
                stack.append(int(ch))
            else:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                match ch:
                    case '+':
                        num = num1 + num2
                    case '-':
                        num = num2 - num1
                    case '*':
                        num = num1 * num2
                    case '/':
                        num = num2/num1
                stack.append(int(num))
            # print(stack)
        return stack[-1] if stack else ""
