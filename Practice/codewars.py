"""
TEXT-BASED ADVENTURE GAME: The Enchanted Quest
A fantasy adventure game with multiple paths and endings.
"""

# Game state tracking
game_state = {
    "health": 100,
    "inventory": [],
    "allies": 0,
    "dark_choices": 0,
    "puzzle_solved": False,
    "royal_trust": False,
}


def start_game():
    """Introduction to the game."""
    print("\n" + "="*60)
    print("WELCOME TO: THE ENCHANTED QUEST")
    print("="*60)
    print("\nYou wake up in a mysterious forest with no memory of how you got here.")
    print("You must make choices to survive and uncover the truth...\n")
    encounter_crossroads()


def encounter_crossroads():
    """First encounter: Choose a direction."""
    print("You find yourself at a crossroads with three paths:")
    print("1. Follow the narrow path to the LEFT (towards mountains)")
    print("2. Take the middle path STRAIGHT (towards village lights)")
    print("3. Go RIGHT (into the deep forest)")
    
    choice = input("\nWhat is your choice? (1/2/3): ").strip()
    
    if choice == "1":
        encounter_mountain_cave()
    elif choice == "2":
        encounter_village_entrance()
    elif choice == "3":
        encounter_forest_edge()
    else:
        print("Invalid choice. Try again.")
        encounter_crossroads()


def encounter_mountain_cave():
    """Encounter: Discover a mysterious cave."""
    print("\n--- Mountain Cave ---")
    print("You climb the mountain and find a glowing cave entrance.")
    print("Strange symbols cover the walls. Do you:")
    print("1. Enter cautiously")
    print("2. Examine the symbols first")
    
    choice = input("Your choice (1/2): ").strip()
    
    if choice == "1":
        encounter_ancient_guardian()
    elif choice == "2":
        game_state["puzzle_solved"] = True
        encounter_symbol_puzzle()
    else:
        encounter_mountain_cave()


def encounter_symbol_puzzle():
    """Encounter: Solve an ancient puzzle."""
    print("\n--- Ancient Puzzle ---")
    print("The symbols form a riddle: 'I speak without a mouth and hear without ears.'")
    print("What am I?")
    print("1. Echo")
    print("2. Wind")
    print("3. Water")
    
    choice = input("Your answer (1/2/3): ").strip()
    
    if choice == "1":
        print("\nThe symbols glow brightly. You've unlocked the cave's secrets!")
        game_state["inventory"].append("Ancient Scroll")
        encounter_ancient_guardian()
    else:
        print("\nThe symbols dim. Try again...")
        encounter_symbol_puzzle()


def encounter_ancient_guardian():
    """Encounter: Meet a guardian creature."""
    print("\n--- Ancient Guardian ---")
    print("A glowing creature emerges from the shadows.")
    print("'State your purpose, traveler.'")
    print("1. 'I seek knowledge'")
    print("2. 'I seek power'")
    print("3. 'I mean no harm'")
    
    choice = input("Your response (1/2/3): ").strip()
    
    if choice == "1":
        print("\nThe Guardian nods approvingly and gives you a glowing amulet.")
        game_state["inventory"].append("Amulet of Wisdom")
        encounter_crystal_chamber()
    elif choice == "2":
        print("\nThe Guardian's eyes turn red. It attacks!")
        game_state["dark_choices"] += 1
        game_state["health"] -= 30
        encounter_guardian_battle()
    else:
        print("\nThe Guardian seems satisfied with your honesty.")
        game_state["allies"] += 1
        encounter_crystal_chamber()


def encounter_guardian_battle():
    """Encounter: Fight the guardian."""
    print("\n--- Battle ---")
    print(f"Your health: {game_state['health']}")
    print("1. Fight back")
    print("2. Flee")
    print("3. Use magic")
    
    choice = input("Your choice (1/2/3): ").strip()
    
    if choice == "1":
        print("After a fierce battle, you defeat the guardian!")
        game_state["health"] -= 20
        encounter_treasure_vault()
    elif choice == "2":
        print("You manage to escape!")
        encounter_village_entrance()
    elif choice == "3":
        print("You channel mystical energy and weaken the guardian.")
        game_state["inventory"].append("Crystal of Power")
        encounter_treasure_vault()
    else:
        encounter_guardian_battle()


def encounter_crystal_chamber():
    """Encounter: Discover a crystal chamber."""
    print("\n--- Crystal Chamber ---")
    print("You find a chamber filled with glowing crystals.")
    print("1. Take the crystals (greedy choice)")
    print("2. Leave them untouched (respectful choice)")
    print("3. Study them carefully (knowledge choice)")
    
    choice = input("Your choice (1/2/3): ").strip()
    
    if choice == "1":
        game_state["dark_choices"] += 1
        game_state["inventory"].append("Dark Crystals")
        encounter_curse_appears()
    elif choice == "2":
        game_state["allies"] += 1
        encounter_magical_portal()
    elif choice == "3":
        game_state["inventory"].append("Crystal Knowledge")
        encounter_magical_portal()
    else:
        encounter_crystal_chamber()


def encounter_curse_appears():
    """Encounter: A curse takes hold."""
    print("\n--- Curse Unleashed ---")
    print("Dark energy surrounds you! A voice warns: 'You will face consequences.'")
    print("1. Accept the curse and continue (dark path)")
    print("2. Seek redemption (light path)")
    
    choice = input("Your choice (1/2): ").strip()
    
    if choice == "1":
        game_state["dark_choices"] += 2
        encounter_dark_sorcerer()
    elif choice == "2":
        encounter_healing_shrine()
    else:
        encounter_curse_appears()


def encounter_dark_sorcerer():
    """Encounter: Meet a dark sorcerer."""
    print("\n--- The Dark Sorcerer ---")
    print("A shadowy figure offers you immense power in exchange for your service.")
    print("1. Accept the dark offer")
    print("2. Refuse and fight")
    print("3. Pretend to accept but seek another way")
    
    choice = input("Your choice (1/2/3): ").strip()
    
    if choice == "1":
        print("\nYou embrace the darkness...")
        ending_dark_ruler()
    elif choice == "2":
        print("\nYou reject the sorcerer!")
        encounter_final_confrontation()
    else:
        game_state["allies"] += 1
        encounter_rebel_hideout()
    
    if choice != "1" and choice != "2" and choice != "3":
        encounter_dark_sorcerer()


def encounter_rebel_hideout():
    """Encounter: Find a safe haven."""
    print("\n--- Rebel Hideout ---")
    print("You find refuge with rebels who oppose the sorcerer.")
    print("1. Join them in battle")
    print("2. Help them with information")
    print("3. Suggest a different plan")
    
    choice = input("Your choice (1/2/3): ").strip()
    
    if choice in ["1", "2", "3"]:
        game_state["allies"] += 2
        encounter_final_confrontation()
    else:
        encounter_rebel_hideout()


def encounter_village_entrance():
    """Encounter: Arrive at a village."""
    print("\n--- Village of Thornwick ---")
    print("You enter a peaceful village. The townspeople welcome you cautiously.")
    print("1. Speak with the Elder")
    print("2. Visit the Tavern")
    print("3. Search the Library")
    
    choice = input("Your choice (1/2/3): ").strip()
    
    if choice == "1":
        encounter_village_elder()
    elif choice == "2":
        encounter_tavern_secrets()
    elif choice == "3":
        encounter_ancient_library()
    else:
        encounter_village_entrance()


def encounter_village_elder():
    """Encounter: Meet the village elder."""
    print("\n--- The Elder's Tale ---")
    print("The Elder tells you of an ancient evil threatening the land.")
    print("1. Volunteer to help")
    print("2. Ask for a reward first")
    print("3. Express doubt about the threat")
    
    choice = input("Your choice (1/2/3): ").strip()
    
    if choice == "1":
        game_state["allies"] += 1
        game_state["royal_trust"] = True
        encounter_royal_messenger()
    elif choice == "2":
        print("The Elder seems disappointed but offers gold.")
        game_state["inventory"].append("Gold Coins")
        encounter_royal_messenger()
    else:
        game_state["dark_choices"] += 1
        encounter_tavern_secrets()


def encounter_royal_messenger():
    """Encounter: Receive a royal message."""
    print("\n--- Royal Summons ---")
    print("A royal messenger arrives with an urgent message.")
    print("The king requests your aid against a mysterious threat.")
    print("1. Accept the quest")
    print("2. Demand to know more first")
    print("3. Ignore the summons")
    
    choice = input("Your choice (1/2/3): ").strip()
    
    if choice == "1":
        encounter_castle_arrival()
    elif choice == "2":
        game_state["allies"] += 1
        encounter_castle_arrival()
    else:
        game_state["dark_choices"] += 1
        encounter_forest_edge()


def encounter_castle_arrival():
    """Encounter: Arrive at the castle."""
    print("\n--- Royal Castle ---")
    print("You stand before the magnificent castle of the King.")
    print("1. Enter through the main gate")
    print("2. Look for a secret entrance")
    print("3. Request an audience formally")
    
    choice = input("Your choice (1/2/3): ").strip()
    
    if choice in ["1", "3"]:
        encounter_throne_room()
    elif choice == "2":
        encounter_secret_passage()
    else:
        encounter_castle_arrival()


def encounter_throne_room():
    """Encounter: Meet the king."""
    print("\n--- The Throne Room ---")
    print("Before you sits the King, looking troubled.")
    print("'A curse has befallen our kingdom. Only you can break it.'")
    print("1. Accept the challenge")
    print("2. Ask about the curse first")
    print("3. Suspect a trap")
    
    choice = input("Your choice (1/2/3): ").strip()
    
    if choice == "1":
        encounter_curse_hunt()
    elif choice == "2":
        game_state["inventory"].append("Curse Knowledge")
        encounter_curse_hunt()
    else:
        game_state["dark_choices"] += 1
        encounter_secret_passage()


def encounter_secret_passage():
    """Encounter: Discover secret chambers."""
    print("\n--- Secret Passage ---")
    print("You find hidden chambers beneath the castle.")
    print("Ancient texts reveal the king's hidden secrets.")
    print("1. Confront the king with this knowledge")
    print("2. Use this as leverage for reward")
    print("3. Destroy the evidence")
    
    choice = input("Your choice (1/2/3): ").strip()
    
    if choice == "1":
        encounter_throne_room()
    elif choice == "2":
        game_state["dark_choices"] += 2
        game_state["inventory"].append("Royal Secret")
        encounter_final_confrontation()
    else:
        encounter_curse_hunt()


def encounter_curse_hunt():
    """Encounter: Search for the source of the curse."""
    print("\n--- Curse Hunt ---")
    print("You venture into the cursed lands seeking the source of evil.")
    print("1. Follow the magical aura north")
    print("2. Interview cursed villagers")
    print("3. Perform a ritual to locate it")
    
    choice = input("Your choice (1/2/3): ").strip()
    
    if choice in ["1", "2", "3"]:
        encounter_dark_tower()
    else:
        encounter_curse_hunt()


def encounter_dark_tower():
    """Encounter: Reach the dark tower."""
    print("\n--- The Dark Tower ---")
    print("A massive, sinister tower looms before you.")
    print("1. Climb the tower immediately")
    print("2. Search for an alternate entrance")
    print("3. Seek allies before entering")
    
    choice = input("Your choice (1/2/3): ").strip()
    
    if choice == "1":
        encounter_tower_battle()
    elif choice == "2":
        game_state["inventory"].append("Hidden Artifact")
        encounter_tower_battle()
    elif choice == "3":
        game_state["allies"] += 2
        encounter_tower_battle()
    else:
        encounter_dark_tower()


def encounter_tower_battle():
    """Encounter: Final battle in the tower."""
    print("\n--- Tower Battle ---")
    print("At the tower's peak, you face the source of the curse!")
    print("1. Attack with strength")
    print("2. Use wisdom to understand it")
    print("3. Try to communicate with it")
    
    choice = input("Your choice (1/2/3): ").strip()
    
    if choice == "1":
        game_state["health"] -= 40
        if game_state["health"] > 0:
            encounter_final_confrontation()
        else:
            ending_fallen_hero()
    elif choice == "2":
        encounter_final_confrontation()
    elif choice == "3":
        game_state["allies"] += 1
        encounter_final_confrontation()
    else:
        encounter_tower_battle()


def encounter_tavern_secrets():
    """Encounter: Visit the tavern."""
    print("\n--- The Tavern ---")
    print("You hear rumors of a powerful artifact hidden nearby.")
    print("1. Ask the bartender for details")
    print("2. Follow a mysterious stranger")
    print("3. Ignore the rumors")
    
    choice = input("Your choice (1/2/3): ").strip()
    
    if choice == "1":
        game_state["inventory"].append("Map Fragment")
        encounter_hidden_temple()
    elif choice == "2":
        game_state["dark_choices"] += 1
        encounter_trap_sprung()
    else:
        encounter_village_entrance()


def encounter_hidden_temple():
    """Encounter: Discover a hidden temple."""
    print("\n--- Hidden Temple ---")
    print("You find an ancient temple filled with mystical energy.")
    print("1. Enter and search for the artifact")
    print("2. Perform a blessing ritual first")
    print("3. Document what you see")
    
    choice = input("Your choice (1/2/3): ").strip()
    
    if choice in ["1", "2", "3"]:
        game_state["inventory"].append("Sacred Artifact")
        encounter_final_confrontation()
    else:
        encounter_hidden_temple()


def encounter_trap_sprung():
    """Encounter: Fall into a trap."""
    print("\n--- Trap! ---")
    print("It was an ambush! Dark forces surround you.")
    print("1. Fight your way out")
    print("2. Use magic to escape")
    print("3. Surrender")
    
    choice = input("Your choice (1/2/3): ").strip()
    
    if choice == "1" or choice == "2":
        game_state["health"] -= 25
        encounter_forest_edge()
    elif choice == "3":
        ending_prisoner()
    else:
        encounter_trap_sprung()


def encounter_ancient_library():
    """Encounter: Explore a library."""
    print("\n--- Ancient Library ---")
    print("Dusty tomes line the shelves. A librarian greets you.")
    print("1. Ask about the village's history")
    print("2. Research a specific threat")
    print("3. Search for rare magic books")
    
    choice = input("Your choice (1/2/3): ").strip()
    
    if choice in ["1", "2", "3"]:
        game_state["inventory"].append("Ancient Knowledge")
        encounter_village_elder()
    else:
        encounter_ancient_library()


def encounter_forest_edge():
    """Encounter: Edge of the forbidden forest."""
    print("\n--- Forbidden Forest ---")
    print("You reach the edge of an ancient, forbidden forest.")
    print("Legends speak of powerful magic here.")
    print("1. Enter the forest")
    print("2. Turn back")
    print("3. Send for help")
    
    choice = input("Your choice (1/2/3): ").strip()
    
    if choice == "1":
        encounter_forest_guardian()
    elif choice == "2":
        encounter_village_entrance()
    else:
        game_state["allies"] += 1
        encounter_forest_guardian()


def encounter_forest_guardian():
    """Encounter: Meet a guardian of the forest."""
    print("\n--- Forest Guardian ---")
    print("A mystical being blocks your path.")
    print("'What brings you to these ancient woods?'")
    print("1. Explain your noble quest")
    print("2. Claim you're just passing through")
    print("3. Challenge the guardian")
    
    choice = input("Your choice (1/2/3): ").strip()
    
    if choice == "1":
        game_state["allies"] += 1
        encounter_healing_shrine()
    elif choice == "2":
        encounter_healing_shrine()
    else:
        game_state["dark_choices"] += 1
        encounter_forest_duel()


def encounter_forest_duel():
    """Encounter: Duel with the guardian."""
    print("\n--- Forest Duel ---")
    print("The guardian challenges you to combat.")
    print("1. Engage in combat")
    print("2. Surrender immediately")
    print("3. Propose a contest of wits")
    
    choice = input("Your choice (1/2/3): ").strip()
    
    if choice == "1":
        game_state["health"] -= 30
        print("After a hard-fought battle, you prevail!")
        encounter_healing_shrine()
    elif choice == "2":
        ending_defeated()
    elif choice == "3":
        print("The guardian respects your wisdom.")
        game_state["allies"] += 2
        encounter_healing_shrine()
    else:
        encounter_forest_duel()


def encounter_healing_shrine():
    """Encounter: Discover a healing shrine."""
    print("\n--- Healing Shrine ---")
    print("You find a sacred shrine with restorative powers.")
    game_state["health"] = min(100, game_state["health"] + 50)
    print(f"You feel renewed! Health: {game_state['health']}")
    encounter_final_confrontation()


def encounter_final_confrontation():
    """Encounter: The ultimate choice."""
    print("\n--- Final Confrontation ---")
    print("You've gathered knowledge, allies, and artifacts.")
    print("Now you must decide the fate of the realm.")
    print(f"\nYour Stats:")
    print(f"  Health: {game_state['health']}")
    print(f"  Allies: {game_state['allies']}")
    print(f"  Dark Choices: {game_state['dark_choices']}")
    print(f"  Inventory: {len(game_state['inventory'])} items")
    print("\n1. Seal away the darkness forever (sacrifice choice)")
    print("2. Seek redemption for the cursed land")
    print("3. Take the power for yourself")
    
    choice = input("Your final choice (1/2/3): ").strip()
    
    if choice == "1":
        ending_noble_hero()
    elif choice == "2":
        ending_redeemer()
    elif choice == "3":
        ending_dark_ruler() if game_state["dark_choices"] > 3 else ending_noble_hero()
    else:
        encounter_final_confrontation()


# ============ GAME ENDINGS (5+ Distinct Endings) ============

def ending_noble_hero():
    """Ending 1: The Noble Hero"""
    print("\n" + "="*60)
    print("ENDING: THE NOBLE HERO")
    print("="*60)
    print("\nYou sacrifice your power to seal away the darkness forever.")
    print("The land is saved, and you become a legend.")
    print("Statues are erected in your honor across the kingdoms.")
    print("Final Score: Legendary Hero\n")


def ending_dark_ruler():
    """Ending 2: The Dark Ruler"""
    print("\n" + "="*60)
    print("ENDING: THE DARK RULER")
    print("="*60)
    print("\nYou embrace the darkness and claim ultimate power.")
    print("The realm bows before you, but at what cost?")
    print("Your humanity fades as darkness consumes you.")
    print("Final Score: Corrupted Tyrant\n")


def ending_redeemer():
    """Ending 3: The Redeemer"""
    print("\n" + "="*60)
    print("ENDING: THE REDEEMER")
    print("="*60)
    print("\nYou reach the cursed being with compassion.")
    print("Through understanding, you break the curse peacefully.")
    print("Together, you bring harmony to both realms.")
    print("Final Score: Wise Redeemer\n")


def ending_fallen_hero():
    """Ending 4: The Fallen Hero"""
    print("\n" + "="*60)
    print("ENDING: THE FALLEN HERO")
    print("="*60)
    print("\nYou fought valiantly but your strength failed you.")
    print("Yet your sacrifice inspires others to finish your quest.")
    print("You will be remembered as a hero who gave everything.")
    print("Final Score: Honorable Sacrifice\n")


def ending_prisoner():
    """Ending 5: The Prisoner"""
    print("\n" + "="*60)
    print("ENDING: THE PRISONER")
    print("="*60)
    print("\nYou surrendered, but the darkness has other plans.")
    print("Imprisoned in shadow, you realize too late your mistake.")
    print("Perhaps another will finish what you could not.")
    print("Final Score: Captured and Lost\n")


def ending_defeated():
    """Ending 6: The Defeated Wanderer"""
    print("\n" + "="*60)
    print("ENDING: THE DEFEATED WANDERER")
    print("="*60)
    print("\nYou accept defeat and abandon your quest.")
    print("You wander the world, always wondering 'what if?'")
    print("Perhaps someone braver will face the darkness.")
    print("Final Score: Wandering Regret\n")


def play_again():
    """Ask if the player wants to play again."""
    again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if again == "yes" or again == "y":
        # Reset game state
        for key in game_state:
            if isinstance(game_state[key], list):
                game_state[key] = []
            elif isinstance(game_state[key], int):
                game_state[key] = 100 if key == "health" else 0
            else:
                game_state[key] = False
        start_game()
    else:
        print("\nThanks for playing The Enchanted Quest!")
        print("May your next adventure be even greater.\n")


# Main game loop
if __name__ == "__main__":
    start_game()
    play_again()
