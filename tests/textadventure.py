import random
def start_adventure():
    print("you are playing your favoriete game, arc raiders")
    gamer_tag = input("please enter your gamer tag to continue\n->")
    print(f"welcome, {gamer_tag}!")
    choose_teammates()

def choose_teammates():
    print("you are about to start playing how many teammates do you want to play with?")
    print("1. 1 teammate")
    print("2. 2 teammates")
    print("3. 0 teammates (solo)")
    choice = input("> ")
    if choice == "1":
        print("you have chosen to play with 1 teammate")
        start_game(1)
    elif choice == "2":
        print("you have chosen to play with 2 teammates")
        start_game(2)
    elif choice == "3":
        print("you have chosen to play solo")
        start_game(0)
    else:
        print("invalid choice, please try again")
        choose_teammates()

def start_game(num_teammates):
    print(f"\nStarting game with {num_teammates} teammate(s)!")
    print("Get ready for battle!")
    print("choose your loadout")
    load_out()

def randomize_loadout():
    """Generate a random loadout and return it"""
    loadouts = [
        "ferro 2 with a kettle two and 3 shield rechargers and 5 bandages and 3 snap gernades",
        "osprey with a sticher 2 and 2 shield rechargers and 3 bandages and 2 smoke gernades",
        "anvil 2 and a torento with 5 shield rechargers and 5 bandages and 5 snap gernades"
    ]
    return random.choice(loadouts)

def load_out():
    print("1. custom loudout")
    print("2.free loudout")
    choice = input("> ")
    if choice == "1":
        print("you have chosen the custom loadout")
        custom_loot()
    elif choice == "2":
        print("you have chosen the free loadout")
        random_loadout = randomize_loadout()
        print(f"Your random loadout is: {random_loadout}")
        choose_event(random_loadout)
    else:
        print("invalid choice, please try again")
        load_out()
def custom_loot():
    print("pick you loudout")
    print("1. a ferro 2 with a kettle two and 3 shield rechargers and 5 bandages and 3 snap gernades")
    print("2. a osprey with a sticher 2 and 2 shield rechargers and 3 bandages and 2 smoke gernades")
    print("3. a anvil 2 and a torento with 5 shield rechargers and 5 bandages and 5 snap gernades")
    choice = input("> ")
    if choice == "1":
        print("you have chosen the ferro 2 loadout")
        choose_event()
    elif choice == "2":
        print("you have chosen the osprey loadout")
        choose_event()
    elif choice == "3":
        print("you have chosen the anvil 2 and torento loadout")
        choose_event()
    else:
        print("invalid choice, please try again")
        custom_loot()
def choose_event(loadout=None):
    print("you are about to start the game, pick an event")
    print("1. Hurricane")
    print("2. closed security")
    print("3. night raid")
    choice = input("> ")
    if choice == "1":
        print("you have chosen the hurricane event")
        print("good luck!")
        choose_map("hurricane", loadout)
    elif choice == "2":
        print("you have chosen the closed security event")
        print("good luck!")
        choose_map("closed security", loadout)
    elif choice == "3":
        print("you have chosen the night raid event")
        print("good luck!")
        choose_map("night raid", loadout)
    else:
        print("invalid choice, please try again")
        choose_event(loadout)
def choose_map(event_type, loadout=None):
    print(" choose what map you want to play on")
    if event_type == "hurricane":
        print("1. Buried City")
        print("2. blue gate")
        print("3. space port")
        choice = input("> ")
        if choice == "1":
            print("you have chosen Buried City")
            print(f"Your loadout: {loadout}")
            print("good luck!")
        elif choice == "2":
            print("you have chosen blue gate")
            print(f"Your loadout: {loadout}")
            print("good luck!")
        elif choice == "3":
            print("you have chosen space port")
            print(f"Your loadout: {loadout}")
            print("good luck!")
        else:
            print("invalid choice, please try again")
            choose_map(event_type, loadout)
    elif event_type == "closed security":
        print("1. Dam battlegrounds")
        print("2. blue gate")
        print("3. Buried City")
        choice = input("> ")
        if choice == "1":
            print("you have chosen dam battlegrounds")
            print(f"Your loadout: {loadout}")
            print("good luck!")
        elif choice == "2":
            print("you have chosen blue gate")
            print(f"Your loadout: {loadout}")
            print("good luck!")
        elif choice == "3":
            print("you have chosen Buried City")
            print(f"Your loadout: {loadout}")
            print("good luck!")
        else:
            print("invalid choice, please try again")
            choose_map(event_type, loadout)
    elif event_type == "night raid":
        print("1. Stella Montis")
        print("2. blue gate")
        print("3. Buried City")
        choice = input("> ")
        if choice == "1":
            print("you have chosen Stella Montis")
            print(f"Your loadout: {loadout}")
            print("good luck!")
        elif choice == "2":
            print("you have chosen blue gate")
            print(f"Your loadout: {loadout}")
            print("good luck!")
        elif choice == "3":
            print("you have chosen Buried City")
            print(f"Your loadout: {loadout}")
            print("good luck!")
        else:
            print("invalid choice, please try again")
            choose_map(event_type, loadout)
start_adventure()