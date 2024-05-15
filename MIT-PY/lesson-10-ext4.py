def sort_words(sen):
    new_list = sen.split(" ")
    new_list.sort()
    return new_list
    
print(sort_words("zebras uniform is kind of appy"))