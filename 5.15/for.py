AGE = 56

count = 0
for i in range(10):

    if count == 3:

        user_confirm = input("do you want to keep guessing..?").strip()

        if user_confirm == "y":
            count == 0
        else:
            break

    guess_num = int(input("your guess num:"))

    if guess_num == AGE:

        print("Congratulations, you got it")
        break
    elif guess_num > AGE:

        print("try smaller...")
    else:

        print("try smaller...")

    count += 1