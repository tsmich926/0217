for tc in range(1, 11):
    N, S = input().split()
    stack=[]
    for s in S:
        if len(stack) == 0:
            stack.append(s)
        else:
            if stack[-1] == s:
                stack.pop()
            else:
                stack.append(s)
    print(f"#{tc} ", end="")
    for s in stack:
        print(s, end="")
    print()