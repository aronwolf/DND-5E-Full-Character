#!/usr/bin/python3
import dnd_dict, dnd_skills,re

# Determine the type of artisan tools the player wants proficiency in
artisan_tool_list = ['Alchemist\'s Supplies','Tinker\'s Tools','Glassblower\'s Tools','Jewler\'s Tools','Brewer\'s Supplies','Smith\'s Tools','Cartographer\'s Tools','Mason\'s Tools','Calligrapher\'s Supplies','Painter\'s Tools','Carpenter\'s Tools','Cobbler\'s Tools','Leatherworker\'s Tools','Cook\'s Utensils','Weaver\'s Tools','Woodcarver\'s Tools']

def artisan_tools():
    dnd_skills.skill_addition(artisan_tool_list,dnd_dict.character_dict['Tools'])


#Used for Guild Artisan to give a set of artisan's tools

def artisan_tools_equip():
    while True:
        choice = input("""Choose the Artisan Tools you want to have:
1) Alchemist's Supplies
2) Tinker's Tools
3) Glassblower's Tools
4) Jewler's Tools
5) Brewer's Supplies
6) Smith's Tools
7) Cartographer's Tools
8) Mason's Tools
9) Calligrapher's Supplies
10) Painter's Tools
11) Carpenter's Tools
12) Cobbler's Tools
13) Leatherworker's Tools
14) Cook's Utensils
15) Weaver's Tools
16) Woodcarver's Tools
Enter your selection: """)

        if choice=='1':
            dnd_skills.equip_mod('alchemist_supplies1','Alchemist\'s Supplies')
            break
 
        elif choice=='2':
            dnd_skills.equip_mod('tinker_tools1','Tinker\'s Tools')
            break
 
 
        elif choice=='3':
            dnd_skills.equip_mod('glassblower_tools1','Glassblower\'s Tools')
            break
 
        elif choice=='4':
            dnd_skills.equip_mod('jewler_tools1','Jewler\'s Tools')
            break
 
        elif choice=='5':
            dnd_skills.equip_mod('brewer_supplies1','Brewer\'s Supplies')
            break
 
        elif choice=='6':
            dnd_skills.equip_mod('smith_tools1','Smith\'s Tools')
            break
 
        elif choice=='7':
            dnd_skills.equip_mod('cartographer_tools1','Cartographer\'s Tools')
            break
 
        elif choice=='8':
            dnd_skills.equip_mod('mason_tools1','Mason\'s Tools')
            break
 
        elif choice=='9':
            dnd_skills.equip_mod('calligrapher_supplies1','Calligrapher\'s Supplies')
            break
 
        elif choice=='10':
            dnd_skills.equip_mod('painter_tools1','Painter\'s Tools')
            break
 
        elif choice=='11':
            dnd_skills.equip_mod('carpenter_tools1','Carpenter\'s Tools')
            break
 
        elif choice=='12':
            dnd_skills.equip_mod('cobbler_tools1','Cobbler\'s Tools')
            break
 
        elif choice=='13':
            dnd_skills.equip_mod('leatherworker_tools1','Leatherworker\'s Tools')
            break
 
        elif choice=='14':
            dnd_skills.equip_mod('cook_utelsils1','Cook\'s Utensils')
            break
         
        elif choice=='15':
            dnd_skills.equip_mod('weaver_tools1','Weaver\'s Tools')
            break
        
 
        elif choice=='16':
            dnd_skills.equip_mod('woodcarver_tools1','Woodcarver\'s Tools')
            break

        else:
            print("Invalid input.")
            continue


def gaming_set():
    while True:
        choice=input("""Choose gaming set are you proficient with:
1) Dice
2) Cards
Enter your selection: """)
        if choice =='1':
            print("Dice Chosen")
            dnd_dict.character_dict["Gaming_Set"]['dice'] = 'Dice'
            break
 
        elif choice =='2':
            print("Cards Chosen")
            dnd_dict.character_dict["Gaming_Set"]['cards'] = 'Cards'
            break

        else:
            print("Invalid Selection")
            continue

def musical_instrument():
    while True:
        musical_choice = input("What instrument are your proficient with? ")
# Instruments should not have numbers or special characters
        regex = re.compile(r'^[a-zA-Z\s]*$')
# Makes the key for the intrument all lowercase and turn spaces into underscores
        new_key = musical_choice.lower().replace(' ','_')
        if regex.search(musical_choice) == None:
            print("Do not use numbers or special characters. Please pick again.")
            continue

        if new_key in dnd_dict.character_dict['Instruments']:
            print("You are already proficient with that instrument.")
            continue

        else:
            dnd_dict.character_dict["Instruments"][new_key] = musical_choice
            break
