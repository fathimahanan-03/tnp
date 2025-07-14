n=int(input())
instructions=[input().strip().split() for _ in range(n)]

stack=[]
register=0
ip=0  

while ip<n:
    instr=instructions[ip]
    cmd=instr[0]
    arg=int(instr[1]) if len(instr) > 1 else None

    if cmd == 'PUSH':
        stack.append(arg)

    elif cmd == 'STORE':
        if stack:
            register = stack.pop()

    elif cmd == 'LOAD':
        stack.append(register)

    elif cmd == 'PLUS':
        if len(stack) >= 2:
            a = stack.pop()
            b = stack.pop()
            stack.append(a + b)

    elif cmd == 'TIMES':
        if len(stack) >= 2:
            a = stack.pop()
            b = stack.pop()
            stack.append(a * b)

    elif cmd == 'IFZERO':
        if stack:
            val = stack.pop()
            if val == 0:
                ip = arg
                continue  

    elif cmd == 'DONE':
        if stack:
            print(stack[-1])
        else:
            print(0)
        break

    ip += 1
