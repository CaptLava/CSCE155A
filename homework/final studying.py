

def cal(a, b, depth):
    b = a % b
    if b == 0:
        return a
    else:
        return cal(b + b, a + a, depth + 1)
result = cal(1,2,0)
print(result)