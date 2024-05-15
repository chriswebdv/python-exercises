def count_words(sen):
    num = 0
    new_list = sen.split()
    for i in new_list:
        num += 1
    return num

print(count_words("I have to tell you"))

