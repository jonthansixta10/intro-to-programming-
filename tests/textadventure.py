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
def custom_loot(num_teammates):
    print("pick you loadout")
    print("1. a ferro 2 with a kettle two and 3 shield rechargers and 5 bandages and 3 snap grenades")
    print("2. a osprey with a sticher 2 and 2 shield rechargers and 3 bandages and 2 smoke grenades")
    print("3. a anvil 2 and a torento with 5 shield rechargers and 5 bandages and 5 snap grenades")
    choice = input("> ")
    if choice == "1":
        loadout = "ferro 2 with a kettle two and 3 shield rechargers and 5 bandages and 3 snap grenades"
        print("you have chosen the ferro 2 loadout")
        choose_event(num_teammates, loadout)
    elif choice == "2":
        loadout = "osprey with a sticher 2 and 2 shield rechargers and 3 bandages and 2 smoke grenades"
        print("you have chosen the osprey loadout")
        choose_event(num_teammates, loadout)
    elif choice == "3":
        loadout = "anvil 2 and a torento with 5 shield rechargers and 5 bandages and 5 snap grenades"
        print("you have chosen the anvil 2 and torento loadout")
        choose_event(num_teammates, loadout)
    else:
        print("invalid choice, please try again")
        custom_loot(num_teammates)
def choose_event(num_teammates, loadout=None):
    print("you are about to start the game, pick an event")
    print("1. Hurricane")
    print("2. closed security")
    print("3. night raid")
    choice = input("> ")
    if choice == "1":
        print("you have chosen the hurricane event")
        print("good luck!")
        choose_map(num_teammates, "hurricane", loadout)
    elif choice == "2":
        print("you have chosen the closed security event")
        print("good luck!")
        choose_map(num_teammates, "closed security", loadout)
    elif choice == "3":
        print("you have chosen the night raid event")
        print("good luck!")
        choose_map(num_teammates, "night raid", loadout)
    else:
        print("invalid choice, please try again")
        choose_event(num_teammates, loadout)
def choose_map(num_teammates, event_type, loadout=None):
    print(" choose what map you want to play on")
    if event_type == "hurricane":
        print("1. Buried City")
        choice = input("> ")
        if choice == "1":
            print("you have chosen Buried City")
            buried_city_hurricane(num_teammates, loadout)
        else:
            print("invalid choice, please try again")
            choose_map(num_teammates, event_type, loadout)
    elif event_type == "closed security":
        print("1. Dam battlegrounds")
        choice = input("> ")
        if choice == "1":
            print("you have chosen dam battlegrounds")
            dam_closed_security(num_teammates, loadout)
        else:
            print("invalid choice, please try again")
            choose_map(num_teammates, event_type, loadout)
    elif event_type == "night raid":
        print("1. Stella Montis")
        choice = input("> ")
        if choice == "1":
            print("you have chosen Stella Montis")
            stella_montis_night_raid(num_teammates, loadout)
        else:
            print("invalid choice, please try again")
            choose_map(num_teammates, event_type, loadout)
def buried_city_hurricane(num_teammates, loadout):
    print("you have entered the buried city map for the hurricane event")
    print("good luck!")
    choose_loot_spot(num_teammates, loadout)
def choose_loot_spot(num_teammates, loadout):
    print("where do you want to go looting?")
    print("1. the new District, it is a high tier loot spot but that means that their is a greater chance of running into other players")
    print("2. the old town, it has a medium tier loot but that means that there is a lower chance of running into other players")
    choice = input("> ")
    if choice == "1":
            new_district(num_teammates, loadout)
    elif choice == "2":
            old_town(num_teammates, loadout)
    else:
        print("invalid choice, please try again")
        choose_loot_spot(num_teammates, loadout)

def new_district(num_teammates, loadout):
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
            fight_outcome(num_teammates, loadout)
        elif choice == "2":
            print("you have chosen to outplay the player")
            outplay_outcome(num_teammates, loadout)
        elif choice == "3":
            print("you have chosen to run away")
            print("you run away and you find another loot spot!")
            print("you find some good loot and you are now ready to head to the extraction point!")
            leave_now_or_later(num_teammates, loadout)
        else:
            print("invalid choice, please try again")
            new_district(num_teammates, loadout)
    elif choice == "2":
        print("you have chosen to ignore the flare")
        print("you ignore the flare and you keep looting, you end up finding some good loot!")
        leave_now_or_later(num_teammates, loadout)
    else:
        print("invalid choice, please try again")
        new_district(num_teammates, loadout)

def fight_outcome(num_teammates, loadout):
        # Determine if loadout is custom or random
    is_custom = "ferro 2" in loadout or "osprey" in loadout or "anvil 2" in loadout
        
    if is_custom:
            # Custom loadout randomizer for fight (sneak)
        if num_teammates == 0:
            outcomes = ["win", "win", "lose", "lose"]
        elif num_teammates == 1:
            outcomes = ["win", "win1", "win", "lose"]
        elif num_teammates == 2:
            outcomes = ["win", "win", "win1", "lose"]
        else:
            outcomes = ["win1", "win", "win", "lose"]  # default
    else:
            # Free loadout randomizer for fight (sneak)
        if num_teammates == 0:
            outcomes = ["win", "lose", "lose", "lose"]
        elif num_teammates == 1:
            outcomes = ["win1", "win1", "lose", "lose"]
        elif num_teammates == 2:
            outcomes = ["win", "win1", "win", "lose"]
        else:
            outcomes = ["win", "win1", "win", "lose"]  # default
        
    result = random.choice(outcomes)
    if result == "win":
        print("you have won the fight and you have looted the players body, you end up finding some good loot and your inventory is now full!")
        leave_now_or_later1(num_teammates, loadout)
    elif result == "win1":
        print("you have won the fight but you got downed in the process, your teammate was able to finish off the player and revive you, you end up finding some good loot and your inventory is now full!")
        leave_now_or_later1(num_teammates, loadout)
    elif result == "lose":
        print("you have lost the fight and you have been killed by the player, better luck next time!")
        print("you have lost the game, better luck next time! Do you want to play again?")
        print("1. yes") 
        print("2. no")
        choice = input("> ")
        if choice == "1":
            print("you have chosen to play again")
            start_adventure()

def outplay_outcome(num_teammates, loadout):
        # Determine if loadout is custom or random
    is_custom = "ferro 2" in loadout or "osprey" in loadout or "anvil 2" in loadout
        
    if is_custom:
            # Custom loadout randomizer for outplay
        if num_teammates == 0:
            outcomes = ["win", "win", "win", "lose"]
        elif num_teammates == 1:
            outcomes = ["win1", "win", "win1", "lose"]
        elif num_teammates == 2:
            outcomes = ["win", "win1", "win", "lose"]
        else:
            outcomes = ["win", "win", "win", "lose"]  # default
    else:
            # Free loadout randomizer for outplay
        if num_teammates == 0:
            outcomes = ["win", "win", "lose", "lose"]
        elif num_teammates == 1:
            outcomes = ["win", "win1", "win", "lose"]
        elif num_teammates == 2:
            outcomes = ["win", "win1", "win", "lose"]
        else:
            outcomes = ["win1", "win", "win", "lose"]  # default
        
    result = random.choice(outcomes)
    if result == "win":
        print("you have successfully outplayed the player and eliminated them! You loot their body and find some excellent gear.")
        leave_now_or_later1(num_teammates, loadout)
    elif result == "win1":
        print("you attempted to outplay the player and while you were successful in eliminating them, you got downed in the process. Your teammate was able to finish off the player and revive you, you end up finding some good loot and your inventory is now full!")
        leave_now_or_later1(num_teammates, loadout)
    elif result == "lose":
        print("you tried to outplay the player but they were too skilled and ended up killing you. Better luck next time!")
        print("you have lost the game, better luck next time! Do you want to play again?")
        print("1. yes")
        print("2. no")
        choice = input("> ")
        if choice == "1":
            print("you have chosen to play again")
            start_adventure()
def leave_now_or_later(num_teammates, loadout):
    print("you have a choice to make you have found some good loot but only 3 exstraction points are left do you want to leave now or risk it and keep looting?")
    print("1. leave the area now and head for the nearest extraction point")
    print("2. stay in the area and keep looting, but there is a chance that you might run into other players and might not get to the extraction point in time")
    choice = input("> ")
    if choice == "1":
        print("you have chosen to leave the area")
        print("you leave the area and you head to the closest extraction point!")
        extraction_outcome(num_teammates, loadout)
    elif choice == "2":
        print("you have chosen to stay in the area")
        print("you decide to stay in the area and keep looting!")
        print("while you are looting you run into another player and they end up killing you, better luck next time!")
        print("you have lost the game, better luck next time! Do you want to play again?")
        print("1. yes")
        print("2. no")
        choice = input("> ")
        if choice == "1":
            print("you have chosen to play again")
            start_adventure()
    else:
        print("invalid choice, please try again")
        leave_now_or_later(num_teammates, loadout)
def leave_now_or_later1(num_teammates, loadout):
    print("you have a choice to make you have found some good loot from the team you just killed but only 3 exstraction points are left do you want to leave now or risk it and keep looting?")
    print("1. leave the area now and head for the nearest extraction point")
    print("2. stay in the area and keep looting, but there is a chance that you might run into other players and might not get to the extraction point in time")
    choice = input("> ")
    if choice == "1":
        print("you have chosen to leave the area")
        print("you leave the area and you head to the closest extraction point!")
        extraction_outcome(num_teammates, loadout)
    elif choice == "2":
        print("you have chosen to stay in the area")
        print("you decide to stay in the area and keep looting!")
        print("while you are looting you run into another player and they end up killing you, better luck next time!")
        print("you have lost the game, better luck next time! Do you want to play again?")
        print("1. yes")
        print("2. no")
        choice = input("> ")
        if choice == "1":
            print("you have chosen to play again")
            start_adventure()
def extraction_outcome(num_teammates, loadout):
    print("you have made it to the extraction point and you are waiting for the helicopter to arrive, but you see a player running towards you, do you want to fight them or see if they are friendly?")
    print("1. fight the player")
    print("2. see if the player is friendly")
    choice = input("> ")
    if choice == "1":
        print("you decide to fight the player!")
        fight_outcome2(num_teammates, loadout)
    elif choice == "2":
        print("you decide to see if the player is friendly!")
        friendly_outcome(num_teammates, loadout)
    else:
        print("invalid choice, please try again")
        extraction_outcome(num_teammates, loadout)
def friendly_outcome(num_teammates, loadout):
    print("you approach the player and you ask if they are friendly, they respond by saying that they are friendly and they want to team up with you, do you want to team up with them or do you want to fight them?")
    print("1. team up with the player")
    print("2. fight the player")
    choice = input("> ")
    if choice == "1":
        print("you decide to team up with the player!")
        print("you and the player work together to defend the extraction point and you both successfully extract with your loot, congratulations on winning the game! Do you want to play again?")
        print("1. yes")
        print("2. no")
        choice = input("> ")
        if choice == "1":
            print("you have chosen to play again")
            start_adventure()
    elif choice == "2":
        print("you decide to fight the player!")
        fight_outcome2(num_teammates, loadout)
    else:
        print("invalid choice, please try again")
        friendly_outcome(num_teammates, loadout)
def fight_outcome2(num_teammates, loadout):
        # Determine if loadout is custom or random
    is_custom = "ferro 2" in loadout or "osprey" in loadout or "anvil 2" in loadout
        
    if is_custom:
            # Custom loadout randomizer for fight (sneak)
        if num_teammates == 0:
            outcomes = ["win", "win", "lose", "lose"]
        elif num_teammates == 1:
            outcomes = ["win", "win1", "win", "lose"]
        elif num_teammates == 2:
            outcomes = ["win", "win", "win1", "lose"]
        else:
            outcomes = ["win1", "win", "win", "lose"]  # default
    else:
            # Free loadout randomizer for fight (sneak)
        if num_teammates == 0:
            outcomes = ["win", "lose", "lose", "lose"]
        elif num_teammates == 1:
            outcomes = ["win1", "win1", "lose", "lose"]
        elif num_teammates == 2:
            outcomes = ["win", "win1", "win", "lose"]
        else:
            outcomes = ["win", "win1", "win", "lose"]  # default
        
    result = random.choice(outcomes)
    if result == "win":
        print("you have won the fight and you have looted the players body, you end up finding some good loot and your inventory is now full!")
        leave_now(num_teammates, loadout)
    elif result == "win1":
        print("you have won the fight but you got downed in the process, your teammate was able to finish off the player and revive you, you end up finding some good loot and your inventory is now full!")
        leave_now(num_teammates, loadout)
    elif result == "lose":
        print("you have lost the fight and you have been killed by the player, better luck next time!")
        print("you have lost the game, better luck next time! Do you want to play again?")
        print("1. yes")     
        print("2. no")
        choice = input("> ")
        if choice == "1":
            print("you have chosen to play again")
            start_adventure()
def leave_now(num_teammates, loadout):
    print("you have have now extracted with your loot, congratulations on winning the game! Do you want to play again?")
    print("1. yes")
    print("2. no")
    choice = input("> ")
    if choice == "1":
        start_adventure()
def old_town(num_teammates, loadout):
    print("you spwan in old town, what do you want to loot?")
    print("1. key card room")
    print("2. loot houses")
    choice = input("> ")
    if choice == "1":
        print("you have chosen the key card room, it has higher tier loot but their are stronger arc matchines guarding it")
        key_card_room(num_teammates, loadout)
    elif choice == "2":
        print("you have chosen the loot houses, it has decent loot but is less guarded")
        loot_houses(num_teammates, loadout)
    else:
        print("invalid choice, please try again")
        old_town(num_teammates, loadout)
def key_card_room(num_teammates, loadout):
    print("you are heading towards the key card room, you see a rocketer coming towards you, do you want to fight it or run away?")
    print("1. fight the rocketer")
    print("2. run away")
    choice = input("> ")
    if choice == "1":
        print("you have chosen to fight the rocketer")
        fight_rocketer(num_teammates, loadout)
    elif choice == "2":
        print("you have chosen to run away")
        print("you run away and you find another loot spot!")
        print("you find some good loot and you are now ready to head to the extraction point!")
        leave_now_or_later2(num_teammates, loadout)
def fight_rocketer(num_teammates, loadout):
        # Determine if loadout is custom or random
    is_custom = "ferro 2" in loadout or "osprey" in loadout or "anvil 2" in loadout
        
    if is_custom:
            # Custom loadout randomizer for fight (sneak)
        if num_teammates == 0:
            outcomes = ["win", "lose", "lose", "lose"]
        elif num_teammates == 1:
            outcomes = ["win", "win1", "lose", "lose"]
        elif num_teammates == 2:
            outcomes = ["win", "win", "win1", "lose"]
        else:
            outcomes = ["win1", "win", "win", "lose"]  # default
    else:
            # Free loadout randomizer for fight (sneak)
        if num_teammates == 0:
            outcomes = ["win", "lose", "lose", "lose"]
        elif num_teammates == 1:
            outcomes = ["win1", "lose", "lose", "lose"]
        elif num_teammates == 2:
            outcomes = ["win", "win1", "lose", "lose"]
        else:
            outcomes = ["win", "win1", "win", "lose"]  # default
        
    result = random.choice(outcomes)
    if result == "win":
        print("you have won the fight and you have looted the rocketer, you end up finding some good loot and your inventory is now full!")
        leave_now_or_later2(num_teammates, loadout)
    elif result == "win1":
        print("you have won the fight but you got downed in the process, your teammate was able to finish off the rocketer and revive you, you end up finding some good loot and your inventory is now full!")
        leave_now_or_later2(num_teammates, loadout)
    elif result == "lose":
        print("you have lost the fight and you have been killed by the rocketer, better luck next time!")
        print("you have lost the game, better luck next time! Do you want to play again?")
        print("1. yes")     
        print("2. no")
        choice = input("> ")
        if choice == "1":
            print("you have chosen to play again")
            start_adventure()
def leave_now_or_later2(num_teammates, loadout):
    print("you have a choice to make you have found some good loot 2 extraction points are left do you want to leave now or risk it and keep looting?")
    print("1. leave the area now and head for the nearest extraction point")
    print("2. stay in the area and keep looting, but there is a chance that you might run into other players or arcs and might not get to the extraction point in time")
    choice = input("> ")
    if choice == "1":
        print("you have chosen to leave the area")
        print("you leave the area and you head to the closest extraction point!")
        extraction_outcome2(num_teammates, loadout)
    elif choice == "2":
        print("you have chosen to stay in the area")
        print("you decide to stay in the area and keep looting!")
        print("you find some good loot and dont run into any players or arcs, you are now ready to head to the extraction point!")
        extraction_outcome2(num_teammates, loadout)
    else:
        print("invalid choice, please try again")
        leave_now_or_later2(num_teammates, loadout)
def extraction_outcome2(num_teammates, loadout):
    print("you have made it to the extraction point and you are waiting for the extraction to arrive, but you see a player running towards you, they are being chased by arcs, do you want to fight them or see if they are friendly and help them?")
    print("1. fight the player")
    print("2. see if the player is friendly and help them")
    choice = input("> ")
    if choice == "1":
        print("you decide to fight the player!")
        fight_outcome3(num_teammates, loadout)
    elif choice == "2":
        print("you decide to see if the player is friendly!")
        friendly_outcome1(num_teammates, loadout)
    else:
        print("invalid choice, please try again")
        extraction_outcome2(num_teammates, loadout)
def friendly_outcome1(num_teammates, loadout):
    print("you approach the player and you ask if they are friendly, they respond by saying that they are friendly and they need help defending the extraction point from the arcs, do you want to help them or do you want to fight them?")
    print("1. help the player defend the extraction point from the arcs")
    print("2. fight the player")
    choice = input("> ")
    if choice == "1":
        print("you decide to help the player defend the extraction point from the arcs!")
        print("you and the player work together to defend the extraction point from the arcs as you are about to leave the player kills you and takes all of your loot, better luck next time! Do you want to play again?")
        print("1. yes")
        print("2. no")
        choice = input("> ")
        if choice == "1":
            print("you have chosen to play again")
            start_adventure()
    elif choice == "2":
        print("you decide to fight the player!")
        fight_outcome3(num_teammates, loadout)
    else:
        print("invalid choice, please try again")
        friendly_outcome1(num_teammates, loadout)
def fight_outcome3(num_teammates, loadout):
        # Determine if loadout is custom or random
    is_custom = "ferro 2" in loadout or "osprey" in loadout or "anvil 2" in loadout
        
    if is_custom:
            # Custom loadout randomizer for fight (sneak)
        if num_teammates == 0:
            outcomes = ["win", "win", "lose", "lose"]
        elif num_teammates == 1:
            outcomes = ["win1", "win", "lose", "lose"]
        elif num_teammates == 2:
            outcomes = ["win", "win1", "win", "lose"]
        else:
            outcomes = ["win", "win1", "win", "lose"]  # default
    else:
            # Free loadout randomizer for fight (sneak)
        if num_teammates == 0:
            outcomes = ["win", "lose", "lose", "lose"]
        elif num_teammates == 1:
            outcomes = ["win1", "lose", "lose", "lose"]
        elif num_teammates == 2:
            outcomes = ["win", "win1", "lose", "lose"]
        else:
            outcomes = ["win", "win1", "win", "lose"]  # default
        
    result = random.choice(outcomes)
    if result == "win":
        print("you have won the fight and you have looted the player, you end up finding some good loot and your inventory is now full!")
        fight_arc_or_leave(num_teammates, loadout)
    elif result == "win1":
        print("you have won the fight but you got downed in the process, your teammate was able to finish off the player and revive you, you end up finding some good loot and your inventory is now full!")
        fight_arc_or_leave(num_teammates, loadout)
    elif result == "lose":
        print("you have lost the fight and you have been killed by the player, better luck next time!")
        print("you have lost the game, better luck next time! Do you want to play again?")
        print("1. yes")     
        print("2. no")
        choice = input("> ")
        if choice == "1":
            print("you have chosen to play again")
            start_adventure()
def fight_arc_or_leave(num_teammates, loadout):
    print("after the fight you see that there are arcs coming towards you, do you want to fight the arcs or try to leave the area?")
    print("1. fight the arcs")
    print("2. extract")
    choice = input("> ")
    if choice == "1":
        print("you decide to fight the arcs!")
        fight_arcs(num_teammates, loadout)
    elif choice == "2":
        print("you decide to extract!")
        print("you have successfully extracted with your loot, congratulations on winning the game! Do you want to play again?")
        print("1. yes")
        print("2. no")
        choice = input("> ")
        if choice == "1":
            print("you have chosen to play again")
            start_adventure()
    else:
        print("invalid choice, please try again")
        fight_arc_or_leave(num_teammates, loadout)

def fight_arcs(num_teammates, loadout):
        # Determine if loadout is custom or random
    is_custom = "ferro 2" in loadout or "osprey" in loadout or "anvil 2" in loadout
        
    if is_custom:
            # Custom loadout randomizer for fight (sneak)
        if num_teammates == 0:
            outcomes = ["win", "lose", "lose", "lose"]
        elif num_teammates == 1:
            outcomes = ["win", "win1", "lose", "lose"]
        elif num_teammates == 2:
            outcomes = ["win", "win", "win1", "lose"]
        else:
            outcomes = ["win1", "win", "win", "lose"]  # default
    else:
            # Free loadout randomizer for fight (sneak)
        if num_teammates == 0:
            outcomes = ["win", "lose", "lose", "lose"]
        elif num_teammates == 1:
            outcomes = ["win1", "lose", "lose", "lose"]
        elif num_teammates == 2:
            outcomes = ["win", "win1", "lose", "lose"]
        else:
            outcomes = ["win", "win1", "win", "lose"]  # default
        
    result = random.choice(outcomes)
    if result == "win":
        print("you have won the fight and you have looted the arcs, you end up finding some good loot and your inventory is now full and you are overencumbered!")
        print("you now extract successfully with your loot, congratulations on winning the game! Do you want to play again?")
        print("1. yes")
        print("2. no")
        choice = input("> ")
        if choice == "1":
            print("you have chosen to play again")
            start_adventure()
    elif result == "win1":
        print("you have won the fight but you got downed in the process, your teammate was able to finish off the arcs and revive you, you end up finding some good loot and your inventory is now full!")
        print("you now extract successfully with your loot, congratulations on winning the game! Do you want to play again?")
        print("1. yes")
        print("2. no")
        choice = input("> ")
        if choice == "1":
            print("you have chosen to play again")
            start_adventure()
    elif result == "lose":
        print("you have lost the fight and you have been killed by the arcs, better luck next time!")
        print("Do you want to play again?")
        print("1. yes")     
        print("2. no")
        choice = input("> ")
        if choice == "1":
            print("you have chosen to play again")
            start_adventure()

def loot_houses(num_teammates, loadout):
    print("you are heading towards the loot houses, you see a player running towards you, do you want to fight them or run away?")
    print("1. fight the player")
    print("2. run away")
    choice = input("> ")
    if choice == "1":
        print("you have chosen to fight the player")
        fight_player(num_teammates, loadout)
    elif choice == "2":
        print("you have chosen to run away")
        print("you run away and you find another loot spot!")
        print("you find some good loot and you are now ready to head to the extraction point!")
        leave_now_or_later2(num_teammates, loadout)
    else:
        print("invalid choice, please try again")
        loot_houses(num_teammates, loadout)

def fight_player(num_teammates, loadout):
        # Determine if loadout is custom or random
    is_custom = "ferro 2" in loadout or "osprey" in loadout or "anvil 2" in loadout
        
    if is_custom:
            # Custom loadout randomizer for fight (sneak)
        if num_teammates == 0:
            outcomes = ["win", "lose", "lose", "lose"]
        elif num_teammates == 1:
            outcomes = ["win1", "win", "lose", "lose"]
        elif num_teammates == 2:
            outcomes = ["win", "win1", "win", "lose"]
        else:
            outcomes = ["win", "win1", "win", "lose"]  # default
    else:
            # Free loadout randomizer for fight (sneak)
        if num_teammates == 0:
            outcomes = ["win", "lose", "lose", "lose"]
        elif num_teammates == 1:
            outcomes = ["win1", "lose", "lose", "lose"]
        elif num_teammates == 2:
            outcomes = ["win", "win1", "lose", "lose"]
        else:
            outcomes = ["win", "win1", "win", "lose"]  # default
        
    result = random.choice(outcomes)
    if result == "win":
        print("you have won the fight and you have looted the player, you end up finding some good loot!")
        leave_now_or_later2(num_teammates, loadout)
    elif result == "win1":
        print("you have won the fight but you got downed in the process, your teammate was able to finish off the player and revive you, you end up finding some good loot!")
        leave_now_or_later2(num_teammates, loadout)
    elif result == "lose":
        print("you have lost the fight and you have been killed by the player, better luck next time!")
        print("you have lost the game, better luck next time! Do you want to play again?")
        print("1. yes")     
        print("2. no")
        choice = input("> ")
        if choice == "1":
            print("you have chosen to play again")
            start_adventure()

def west_village(num_teammates, loadout):
    print("You chose west village. This area is under development. Better luck next time!")

def blue_gate_hurricane(num_teammates, loadout):
    print("You chose blue gate for hurricane. This area is under development. Better luck next time!")

def space_port_hurricane(num_teammates, loadout):
    print("You chose space port for hurricane. This area is under development. Better luck next time!")

def dam_closed_security(num_teammates, loadout):
    print("You chose dam battlegrounds for closed security. This area is under development. Better luck next time!")

def blue_gate_closed_security(num_teammates, loadout):
    print("You chose blue gate for closed security. This area is under development. Better luck next time!")

def buried_city_closed_security(num_teammates, loadout):
    print("You chose buried city for closed security. This area is under development. Better luck next time!")

def stella_montis_night_raid(num_teammates, loadout):
    print("You chose stella montis for night raid. This area is under development. Better luck next time!")

def blue_gate_night_raid(num_teammates, loadout):
    print("You chose blue gate for night raid. This area is under development. Better luck next time!")

def buried_city_night_raid(num_teammates, loadout):
    print("You chose buried city for night raid. This area is under development. Better luck next time!")


    
start_adventure()