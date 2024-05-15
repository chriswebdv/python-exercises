
def sum_and_prod(L):
    total1 = 0
    total2 = 1
    for num in L:
        total1 += num
        total2 *= num
    return(total1, total2)


L = [1,4,7,45,32]
print(sum_and_prod(L))
