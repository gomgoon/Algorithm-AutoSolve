while True:
    a = input()
    stack= []
    nf = 0
    
    if a == '.':
        break
    
    for i in a:
        if i == '[':
            stack.append('[')
        elif i == '(':
            stack.append('(')
        elif i == ']':
            if stack:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    nf=1
                    break
            else:
                nf=1
                break
        elif i == ')':
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    nf=1
                    break
            else:
                nf=1
                break
    
    if not stack and nf==0:
        print('yes')
    else:
        print('no')