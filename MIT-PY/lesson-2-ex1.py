secret_num = 7
question = int(input("Guess my secret number: "))
if question < secret_num:
    print(f"{question} is too low")
elif question > secret_num:
    print(f"{question} is too high")
else:
    print(f"{question} and {secret_num} are the same")

