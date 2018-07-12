# (2+7)*5 = [2, 7, '+', 5, '*']
expression = [2, 7, '+', 5, '*']
stack = []

for i in expression:
    if str(i).isdigit():
        stack.append(i)
        continue
    y = stack.pop()
    x = stack.pop()
    z = eval(str(x)+i+str(y))
    stack.append(z)

print(stack[0] if len(stack) == 1 else 'You wrote the wrong expression')
