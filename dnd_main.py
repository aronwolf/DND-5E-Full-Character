#!/usr/bin/python3
import os, stat_roller, dnd_new_char, dnd_save_load, dnd_features, dnd_language, dnd_tools, dnd_dict, dnd_skills, dnd_race, dnd_class, dnd_background, dnd_display, dnd_save_load, dnd_artificer,dnd_barbarian,dnd_bard,dnd_cleric,dnd_druid,dnd_fighter,dnd_monk,dnd_ranger,dnd_rogue,dnd_sorcerer,dnd_warlock,dnd_wizard,json,dnd_level_up

# Main Menu
def main():

    while True:
        choice1 = input("""Welcome, please select an option:
1) Load Data
2) Delete Data
3) Delete Data and Start a New Character
0) Exit
Enter your selection: """)
        if choice1 == '1':
            break

        elif choice1 == '2':
            dnd_save_load.delete_data()
            print("Data Deleted")
            exit()
            break 

        elif choice1 == '3':
            dnd_save_load.delete_data()
            dnd_new_char.initial_char()
            break 

        elif choice1 == '0':
            exit()

        else:
            print("Error: Invalid Selection")
            continue


# Takes information from the json file and puts it into the character_dict
    with open(dnd_save_load.save_data,'r') as fh:
        dnd_dict.character_dict = json.load(fh)

    while True:
        choice = input("""1) New Character
2) Show Stats
3) Level Up
4) Save
0) Exit
Enter your selection: """)
# Starts a new character
        if choice=='1':
            dnd_new_char.initial_char()
            continue


# Display the character data
        elif choice=='2':
            dnd_display.char_display()
            continue

        elif choice=='3':
# Prevents the player from leveling up past 20.
            if dnd_dict.character_dict['total_level'] == 20:
                print("You are at the maximum level, you cannot level up any further.")
                continue
# Increases the total level and class level and then gives the buffs
            else:
                dnd_level_up.class_level_up()
                continue

# Save data
        elif choice=='4':
            dnd_save_load.save_display()
            continue

        elif choice=='0':
            exit()

        else:
            print("Error: Invalid Input")
            continue




if __name__ == '__main__':
    main()
