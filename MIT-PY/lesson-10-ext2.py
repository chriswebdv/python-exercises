def remove_elem(my_list, element):
    new_list = []
    for i in my_list:
        if i != element:
            new_list.append(i)
    return new_list

result = remove_elem([1,2,3,4,4,6,4,7], 4)
print(result)