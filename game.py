import random

level = 1 # Starting level
exp = 0 # Starting experience points
stage = 1 # Starting stage
player_health = 100 # Starting health
monster_health = 50 # Starting monster health
encounter_message = random.choice(["You encounter a wild monster!", "A monster appears!", "A monster blocks your path!"]) # Randomly display a message when encountering a monster
goblin = {"name": "Goblin", "health": 30, "exp": 10, "damage": 5}
skeleton = {"name": "Skeleton", "health": 40, "exp": 15, "damage": 10}
orc = {"name": "Orc", "health": 60, "exp": 20, "damage": 15}
slime = {"name": "Slime", "health": 20, "exp": 5, "damage": 3}
monsters = [goblin, skeleton, orc, slime] # List of possible monsters to encounter
current_monster = random.choice(monsters) # Randomly select a monster to encounter
random_boss = {"name": "Dragon", "health": 200, "exp": 100, "damage": 30} # Define a boss monster
inventory = [] # Player's inventory (not implemented in this version)

while True:
    print("1. FIght Monster") # Option to fight a monster and gain EXP
    print("2. Go to the next stage") # Option to progress to the next stage, which requires a certain level
    print("3. Status") # Option to check the player's current level, EXP, and stage
    print("4. boss fight") # Option to fight a boss, which becomes available every 3 stages and requires the player to be at a certain level
    print("5. Inventory") # Option to check the player's inventory (not implemented in this version)
    print("6. Save") # Option to save the current game state to a file
    print("7. Exit") # Option to exit the game
    print("8. Load game") # Option to load the game state from a file

    choice = input("Choose an action: ")

    if choice == "1": # Fight a monster to gain EXP
        exp_gain = random.randint(5, 20)
        exp += exp_gain
        print(f"You defeated a monster and gained {exp_gain} EXP!")

        if exp >= 100: # Level up every 100 EXP
            level += 1 # Increase level by 1
            exp -= 100 # Reset EXP after leveling up
            print(f"Congratulations! You've leveled up to Level {level}!")
            health_decrease = random.randint(0, 10)
            print(f"Your health decreased by {health_decrease} due to the battle.")
            player_health -= health_decrease # Decrease player's health based on the battle
            if player_health <= 0: # Check if the player has died
                print("You have been defeated. Game over.")
                break

    elif choice == "2":
        if level >= stage * 2: # Require the player to be at least twice the stage number in level to progress
            stage += 1 # Move to the next stage
            print("Stage cleared! Moving to the next stage.")
        else:
            print("You need to be at least Level {} to move to the next stage.".format(stage * 2))

    elif choice == "3": # Display the player's current level, EXP, and stage
        print(f"Level: {level}, EXP: {exp}, Stage: {stage} Health: {player_health}")

    elif choice == "4": # Boss fight available every 3 stages
        print("You encounter a powerful boss!")
        # Add boss fight logic here

    elif choice == "5": # Inventory option
     print("Inventory is in development please follow the updates.") # Placeholder for inventory functionality (not implemented in this version)

    elif choice == "6":
        print("Game saved.") # Save the current game state to a file
        with open("savefile.txt", "w") as savefile:
            savefile.write(f"{level},{exp},{stage}")

    elif choice == "7": # Exit the game
        print("Exiting the game. Goodbye!")
        break

    elif choice == "8": # Load the game state from a file
        print("Loading game...")
        try:
            with open("savefile.txt", "r") as savefile:
                level, exp, stage = map(int, savefile.read().split(","))
            print("Game loaded successfully.")
        except FileNotFoundError:
            print("No save file found.") # Handle the case where the save file does not exist

    else:
        print("Invalid choice. Please try again.") 