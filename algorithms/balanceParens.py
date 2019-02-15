def balanceParens (str):
    stack = []
    for paren in str:
        if paren == '(' or paren == '[' or paren == '{':
            stack.append(paren)
        else:
            dict = {
                ')': '(',
                ']': '[',
                '}': '{'
            }
            if len(stack) > 0 and dict[paren] == stack[-1]:
                stack.pop()
            else:
                return False 
    return len(stack) == 0
