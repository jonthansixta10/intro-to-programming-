import random
def start_adventure():
    print("you are playing your favorite game, arc raiders")
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
    load_out(num_teammates)

def randomize_loadout():
    """Generate a random loadout and return it"""
    loadouts = [
        "ferro, 1 shield rechargers and 2 bandages and 2 snap grenades",
        "sticher, 1 shield rechargers and 2 bandages and 1 defibulator",
        "kettle, 1 shield rechargers and 2 bandages and 2 jolt mines"
    ]
    return random.choice(loadouts)

def load_out(num_teammates):
    print("1. custom loadout")
    print("2.free loadout")
    choice = input("> ")
    if choice == "1":
        print("you have chosen the custom loadout")
        custom_loot(num_teammates)
    elif choice == "2":
        print("you have chosen the free loadout")
        random_loadout = randomize_loadout()
        print(f"Your random loadout is: {random_loadout}")
        choose_event(num_teammates, random_loadout)
    else:
        print("invalid choice, please try again")
        load_out(num_teammates)
def custom_loot():
    print("pick you loadout")
    print("1. a ferro 2 with a kettle two and 3 shield rechargers and 5 bandages and 3 snap grenades")
    print("2. a osprey with a sticher 2 and 2 shield rechargers and 3 bandages and 2 smoke grenades")
    print("3. a anvil 2 and a torento with 5 shield rechargers and 5 bandages and 5 snap grenades")
    choice = input("> ")
    if choice == "1":
        loadout = "ferro 2 with a kettle two and 3 shield rechargers and 5 bandages and 3 snap grenades"
        print("you have chosen the ferro 2 loadout")
        choose_event(loadout)
    elif choice == "2":
        loadout = "osprey with a sticher 2 and 2 shield rechargers and 3 bandages and 2 smoke grenades"
        print("you have chosen the osprey loadout")
        choose_event(loadout)
    elif choice == "3":
        loadout = "anvil 2 and a torento with 5 shield rechargers and 5 bandages and 5 snap grenades"
        print("you have chosen the anvil 2 and torento loadout")
        choose_event(loadout)
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
            buried_city_hurricane(loadout)
        elif choice == "2":
            print("you have chosen blue gate")
            blue_gate_hurricane(loadout)
        elif choice == "3":
            print("you have chosen space port")
            space_port_hurricane(loadout)
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
            dam_closed_security(loadout)
        elif choice == "2":
            print("you have chosen blue gate")
            blue_gate_closed_security(loadout)
        elif choice == "3":
            print("you have chosen Buried City")
            buried_city_closed_security(loadout)
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
            stella_montis_night_raid(loadout)
        elif choice == "2":
            print("you have chosen blue gate")
            blue_gate_night_raid(loadout)
        elif choice == "3":
            print("you have chosen Buried City")
            buried_city_night_raid(loadout)
        else:
            print("invalid choice, please try again")
            choose_map(event_type, loadout)
def buried_city_hurricane(loadout):
    print("you have entered the buried city map for the hurricane event")
    print("good luck!")
    choose_loot_spot(loadout)

    def choose_loot_spot(loadout):
        print("where do you want to go looting?")
        print("1. the new District, it is a high tier loot spot but that means that their is a greater chance of running into other players")
        print("2. the old town, it has a medium tier loot but that means that there is a lower chance of running into other players")
        print("3. the west village, it has medium tier loot and was on the outsides of the map so the chance of running into players is very low")
        choice = input("> ")
        if choice == "1":
            new_district(loadout)
        elif choice == "2":
            old_town(loadout)
        elif choice == "3":
            west_villige(loadout)

    def new_district(loadout):
        print("you have entered the new District")
        print("you hear a raider flare go off in the distance meaning a player just got knocked")
        print("you have a choice to make")
        print("1. go to the flare and try to get the players loot")
        print("2. ignore the flare and keep looting")
        choice = input("> ")
        if choice == "1":
            print("you have chosen to go to the flare")
            print("you run towards the flare and you see a player looting the body")
            print("you have a choice to make")
            print("1. try to sneak up on the player and kill them")
            print("2. try to outplay the player and kill them")
            print("3. run away and try to find another loot spot")
            choice = input("> ")
            if choice == "1":
                print("you have chosen to sneak up on the player")
                fight_outcome(loadout)
            elif choice == "2":
                print("you have chosen to outplay the player")
                print("you try to outplay the player but they are too good and they end up killing you, better luck next time!")
            elif choice == "3":
                print("you have chosen to run away")
                print("you run away and you find another loot spot but it is not as good as the one you just left, better luck next time!")
            else:
                print("invalid choice, please try again")
                new_district(loadout)
        elif choice == "2":
            print("you have chosen to ignore the flare")
            print("you ignore the flare and you keep looting, you end up finding some good loot but you are not in a good position to win the game, better luck next time!")
        else:
            print("invalid choice, please try again")
            new_district(loadout)
        def fight_outcome(loadout):
            custom_loadout = randomize.choice([win, win, win, lose])
            if custom_loadout == "win":
                print("you have won the fight and you have looted the players body, you end up finding some good loot and your inventory is now full!")
            elif custom_loadout == "lose":
                print("you have lost the fight and you have been killed by the player, better luck next time!")
    
start_adventure()