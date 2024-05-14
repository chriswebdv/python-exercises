number_input = int(input("Please give me a number: "))

if number_input < 0:
    print("negative")
elif number_input > 0:
    print("positive")
else:
    print("equals zero")