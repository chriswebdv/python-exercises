s = "abcadeeeef"
string = ""
count = 0

for i in s:
    if i not in string:
        string += i
        count += 1
print(count)