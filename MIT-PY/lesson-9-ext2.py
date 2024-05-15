def char_counts(s):
    (c, v) = (0,0)
    vowels = "aeiou"
    for char in s:
        if char in vowels:
            v += 1
        else:
            c += 1
    return (v,c)


print(char_counts("aaeerio"))
