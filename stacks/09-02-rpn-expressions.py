def evaluate(expr):
    tokens = expr.split(',')

    stack = []
    for token in tokens:
        if token in ['+', '-', '*', '/']:
            second, first = stack.pop(), stack.pop()
            stack.append(str(eval(first + token + second)))
        else:
            stack.append(token)

    return stack[-1]

print(evaluate("1,2,+,3,*"))



