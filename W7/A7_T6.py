import random
random.seed(1234)

ROCK = "    _______\n---'   ____)\n      (_____)\n      (_____)\n      (____)\n---.__(___)"
PAPER = "     _______\n---'    ____)____\n           ______)\n          _______)\n         _______)\n---.__________)"
SCISSORS = "    _______\n---'   ____)____\n          ______)\n       __________)\n      (____)\n---.__(___)"

def showOptions() -> None:
    print("Options:")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")
    print("0 - Quit game")
    return None

def showChoice(PName: str, PChoice: int) -> None:
    names = ["rock", "paper", "scissors"]
    drawings = [ROCK, PAPER, SCISSORS]
    print("#########################")
    print("{} chose {}.".format(PName, names[PChoice - 1]))
    print()
    print(drawings[PChoice - 1])
    print()
    return None

def main() -> None:
    print("Program starting.")
    print("Welcome to the rock-paper-scissors game!")
    name = input("Insert player name: ")
    print("Welcome {}!".format(name))
    print("Your opponent is RPS-3PO.")
    print("Game starts...")
    print()
    wins = 0
    losses = 0
    draws = 0
    choices = ["rock", "paper", "scissors"]
    while True:
        showOptions()
        choice = input("Your choice: ")
        if choice == "0":
            break
        if choice not in ("1", "2", "3"):
            print("Unknown option!")
            print()
            continue
        player = int(choice)
        bot = random.randint(1, 3)
        print("Rock! Paper! Scissors! Shoot!")
        print()
        showChoice(name, player)
        showChoice("RPS-3PO", bot)
        print("#########################")
        print()
        if player == bot:
            print("Draw! Both players chose {}.".format(choices[player - 1]))
            draws += 1
        elif (player == 1 and bot == 3) or (player == 2 and bot == 1) or (player == 3 and bot == 2):
            print("{} {} beats RPS-3PO {}.".format(name, choices[player - 1], choices[bot - 1]))
            wins += 1
        else:
            print("RPS-3PO {} beats {} {}.".format(choices[bot - 1], name, choices[player - 1]))
            losses += 1
        print()
    print()
    print("Results:")
    print("{} - wins ({}), losses ({}), draws ({})".format(name, wins, losses, draws))
    print("RPS-3PO - wins ({}), losses ({}), draws ({})".format(losses, wins, draws))
    print()
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()
