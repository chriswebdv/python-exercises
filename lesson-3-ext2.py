where = input ("Go left or right?: ")
counter = 0
while where == "right":
    counter = counter + 1
    if counter > 2:
        print(":( sad face!")
    where = input ("Go left or right?: ")
print("You are out")