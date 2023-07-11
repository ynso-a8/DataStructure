while True:
    str = input()
    if str == '.':
        break

    stack = []
    ans = True
    for ch in str:
        if ch == '(' or ch == '[':
            stack.append(ch);
        elif ch == ')':
            check = len(stack)
            if check == 0:
                ans = False
                break
            if stack.pop() != '(':
                ans = False
                break
        elif ch == ']':
            check = len(stack)
            if check == 0:
                ans = False
                break
            if stack.pop() != '[':
                ans = False
                break

    if len(stack) != 0:
        ans = False
    print('yes' if ans else 'no')

