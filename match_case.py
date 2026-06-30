a = int(input("Enter a number"))
match a:
    case 1:
        print("You won a phone")
    case 6:
        print("you won $3")
    case _:
        print("better luck next time")
