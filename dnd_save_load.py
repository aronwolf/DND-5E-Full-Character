#import dnd_dict, dnd_display, dnd_class, dnd_skills, os,json 
import dnd_dict, dnd_class, dnd_skills, os,json , dnd_display, dnd_new_char,dnd_infusions,dnd_invocations,dnd_magic,dnd_level_up,dnd_features,dnd_fighting_styles,dnd_maneuvers, dnd_feats, dnd_weapon, dnd_boons, dnd_tools



save_data = ("SAVE_DATA.text")

# Filepath is the current working directory plus SAVE_DATA
#filepath = print("{}/{}".format(os.getcwd(),save_data))


# Create a file if it doesn"t exist
def create_file():
    if not os.path.exists(save_data):
        open(save_data, "w")

#if os.path.exists(filepath):
#    file_syntax(filepath)


# Delete data from file
def delete_data():
    f = open(save_data, "r+")
    f.seek(0)
    f.truncate()
    f = open(save_data, "w")
    object = json.dumps(dnd_dict.character_dict, indent=4)
    f.write(object)
    f.close()




# Choose if you want to view your data or create a new character
def load_choice():
#    create_file()
    while True:
        choice = input("""Do you want to load your data, create a new character, or delete your existing data?
1) Load Data
2) New Character
3) Delete Data
0) Exit
Enter your selection: """)
        if choice == "1":

# Takes the information from the JSON file and puts it into the character_dict
# Note: Also used to check certain things before implementing them
            with open(save_data,'r') as fh:
                dnd_dict.character_dict = json.load(fh)


            dnd_display.char_display()

#            f = open(save_data, "w")
#            object = json.dumps(dnd_dict.character_dict, indent=4)
#            f.write(object)
#            f.close()


            exit()
# Continue with the program
        elif choice == "2":
            break
        elif choice == "3":
            delete_data()
            print("Data Deleted")
            exit()
        elif choice == "0":
            print("Closing Application")
            exit()
        else:
            print("Invalid input, please choose again")
            continue


# Copy the data from SAVE_DATA into the temp file.
def save_display():
#    create_file()
    while True:
        choice = input("Do you want to save your data?\n1) Yes\n2) No\nEnter your selection: ")
        if choice == "1":
            f = open(save_data, "w")
            object = json.dumps(dnd_dict.character_dict, indent=4)
            f.write(object)
            f.close()
            break
        elif choice =="2":
            break
        else:
            print("Invalid input, please choose again")
            continue

