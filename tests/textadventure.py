def start_adventure():
    print("you are playing your favoriete game, arc raiders")
    gamer_tag = input("please enter your gamer tag to continue\n->")
    print(f"welcome, {gamer_tag}!")
    choose_teammates()

def choose_teammates():
    print("you are about to start playing how many team mates do you want to play with?")
    print("1. 1 teammate")
    print("2. 2 teammates")
    print("3. 3 teammates")
    choice = input("> ")
    if choice == "1":
        print("you have chosen to play with 1 teammate")
        start_game(1)
    elif choice == "2":
        print("you have chosen to play with 2 teammates")
        start_game(2)
    elif choice == "3":
        print("you have chosen to play with 3 teammates")
        start_game(3)
    else:
        print("invalid choice, please try again")
        choose_teammates()

def start_game(num_teammates):
    print(f"\nStarting game with {num_teammates} teammate(s)!")
    print("Get ready for battle!")
    print("choose your loadout")
    load_out()

def load_out():
    print("1. custom loudout")
    print("2.free loudout")
    choice = input("> ")
    if choice == "1":
        print("you have chosen the custom loadout")
        choose_event()
    elif choice == "2":
        print("you have chosen the free loadout")
        choose_event()
    else:
        print("invalid choice, please try again")
        load_out()
def choose_event():
    print("you are about to start the game, pick an event")
    print("1. Hurricane")
    print("2. closed security")
    print("3. night raid")
    choice = input("> ")
    if choice == "1":
        print("you have chosen the hurricane event")
        print("good luck!")
        choose_map("hurricane")
    elif choice == "2":
        print("you have chosen the closed security event")
        print("good luck!")
        choose_map("closed security")
    elif choice == "3":
        print("you have chosen the night raid event")
        print("good luck!")
        choose_map("night raid")
    else:
        print("invalid choice, please try again")
        choose_event()
def choose_map(event_type):
    print(" choose what map you want to play on")
    if event_type == "hurricane":
        print("1. stella montis")
        print("2. blue gate")
        print("3. space port")
        choice = input("> ")
        if choice == "1":
            print("you have chosen stella montis")
            print("good luck!")
        elif choice == "2":
            print("you have chosen blue gate")
            print("good luck!")
        elif choice == "3":
            print("you have chosen space port")
            print("good luck!")
        else:
            print("invalid choice, please try again")
            choose_map(event_type)
    elif event_type == "closed security":
        print("1. Dam battlegrounds")
        print("2. blue gate")
        print("3. Buried City")
        choice = input("> ")
        if choice == "1":
            print("you have chosen dam battlegrounds")
            print("good luck!")
        elif choice == "2":
            print("you have chosen blue gate")
            print("good luck!")
        elif choice == "3":
            print("you have chosen Buried City")
            print("good luck!")
        else:
            print("invalid choice, please try again")
            choose_map(event_type)
    elif event_type == "night raid":
        print("1. Stella Montis")
        print("2. blue gate")
        print("3. Buried City")
        choice = input("> ")
        if choice == "1":
            print("you have chosen Stella Montis")
            print("good luck!")
        elif choice == "2":
            print("you have chosen blue gate")
            print("good luck!")
        elif choice == "3":
            print("you have chosen Buried City")
            print("good luck!")
        else:
            print("invalid choice, please try again")
            choose_map(event_type)
start_adventure()