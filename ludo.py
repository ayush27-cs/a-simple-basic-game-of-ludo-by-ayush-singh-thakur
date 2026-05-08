import random 

while True:
    test_your_luck = random.randint(1, 6)
    die_roll=int(input("select your number from (1,6): "))
    if die_roll == 6:
        print("You can unlock your die")
    else:
        print("Better luck")

    play_again = input("Do you want to play again? (y/n): ")
    if play_again != "y":
        print("Game over. Thanks for playing!")
        break