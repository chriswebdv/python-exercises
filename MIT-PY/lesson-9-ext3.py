def mean(*args):
    total = 0
    for i in args:
        total =+ i
    return total/len(args)  

result = mean(1,2,3,4,5,6,15) 
print(result)
