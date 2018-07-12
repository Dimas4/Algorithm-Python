brackets = "(([{}]))"
stack = []


for i in brackets:
    if i in "([{":
        stack.append(i)
    elif i in ")]}":
        if len(stack) == 0:
            print('It\'s not correct brackets!')
            break
        x = stack.pop()
        if i == ')' and x != '(' or i == ']' and x != '[' or i == '{' and x != '}':
            print('It\'s not correct brackets!')
            break
else:
    print('It\'s correct brackets' if len(stack) == 0 else 'It\'s not correct brackets!')
