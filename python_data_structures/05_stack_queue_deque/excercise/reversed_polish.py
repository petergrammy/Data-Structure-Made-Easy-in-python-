def eval_rpn(tokens: list[str]) -> int:
    numbers=[]
    for item in tokens:
        if item.isalnum():
            numbers.append(item)
        else:
            if item=='+':
                A=numbers.pop()
                B=numbers.pop()
                numbers.append(A+B)
            if item=='*':
                A=numbers.pop()
                B=numbers.pop()
                numbers.append(A*B)
            if item=='/':
                A=numbers.pop()
                B=numbers.pop()
                numbers.append(A/B)

    return numbers[0]