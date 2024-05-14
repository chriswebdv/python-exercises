def sum_odd(a,b):
    sum = 0
    for i in range(a, b + 1):
        if i % 2 != 0:
            sum += i
    return sum

result = sum_odd(2, 10)
print(result)
