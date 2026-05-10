import random
def roll_dice():
    return random.randint(1, 6)

def play_ludo(num_players, track_length=27):
    positions = [0] * num_players        
    unlocked = [False] * num_players     

    while True:
        for player in range(num_players):
            input(f"\nPlayer {player+1}, press Enter to roll the dice.")
            dice = roll_dice()
            print(f"🎲 Player {player+1} rolled: {dice}")

            if not unlocked[player]:
                if dice == 6:
                    unlocked[player] = True
                    positions[player] = 1
                    print(f"✅ Player {player+1} unlocked their piece!")
                else:
                    print(f"❌ Player {player+1} needs a 6 to unlock.")
            else:
                positions[player] += dice
                print(f"➡️ Player {player+1} moved to position {positions[player]}")

                if positions[player] >= track_length:
                    print(f"\n🏆 Player {player+1} wins the game!")
                    return  # End the game

# Ask for number of players
num_players = int(input("Enter number of players (2-5): "))
play_ludo(num_players)
