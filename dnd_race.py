#!/usr/bin/python3
import os, math, dnd_features, dnd_class, dnd_dict, dnd_skills, dnd_language, dnd_magic

def dragonborn():

 
    dnd_dict.character_dict['Stats']['strength']['base'] += 2
    dnd_dict.character_dict['Stats']['charisma']['base'] += 1


#Define race, movement speed, size, and language known
    dnd_class.RaceStats.racial_choice("Dragonborn", 30, "Medium")
    dnd_dict.character_dict['race'] = 'Dragonborn'
    dnd_dict.character_dict["speed"] = 30
    dnd_dict.character_dict['size'] = 'Medium'
#Update Stats to Dictionary

#Update all modifiers
    mod1 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['strength']['base'])
    mod2 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['dexterity']['base'])
    mod3 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['constitution']['base'])
    mod4 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['intelligence']['base'])
    mod5 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['wisdom']['base'])
    mod6 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['charisma']['base'])


    dnd_dict.character_dict['Stats']['strength']['mod'] = mod1
    dnd_dict.character_dict['Stats']['dexterity']['mod'] = mod2
    dnd_dict.character_dict['Stats']['constitution']['mod'] = mod3
    dnd_dict.character_dict['Stats']['intelligence']['mod'] = mod4
    dnd_dict.character_dict['Stats']['wisdom']['mod'] = mod5
    dnd_dict.character_dict['Stats']['charisma']['mod'] = mod6
# Starts the initial level
    dnd_dict.character_dict['total_level'] = 1
# Gives the proficiency bonus
    dnd_skills.prof_modifier()
# Hit points: Constitution mod (except Hill Dwarves who get an additional +1)
    dnd_dict.character_dict['hp']= dnd_dict.character_dict["Stats"]['constitution']['mod']

#Put a new language into the Language dictionary
    dnd_dict.character_dict["Languages"]['draconic'] = "Draconic"

    dnd_features.dragonborn_features()
    dnd_skills.set_skill()

def dwarf_hill():

#Update Stats to Dictionary
    dnd_dict.character_dict['Stats']['constitution']['base'] += 2
    dnd_dict.character_dict['Stats']['wisdom']['base'] += 1


    dnd_class.RaceStats.racial_choice("Hill Dwarf", 25, "Medium")
    dnd_dict.character_dict['race'] = 'Hill Dwarf'
    dnd_dict.character_dict["speed"] = 25
    dnd_dict.character_dict['size'] = 'Medium'
    dnd_dict.character_dict["Languages"]['dwarvish'] = "Dwarvish"


#Update all modifiers
    mod1 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['strength']['base'])
    mod2 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['dexterity']['base'])
    mod3 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['constitution']['base'])
    mod4 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['intelligence']['base'])
    mod5 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['wisdom']['base'])
    mod6 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['charisma']['base'])


    dnd_dict.character_dict['Stats']['strength']['mod'] = mod1
    dnd_dict.character_dict['Stats']['dexterity']['mod'] = mod2
    dnd_dict.character_dict['Stats']['constitution']['mod'] = mod3
    dnd_dict.character_dict['Stats']['intelligence']['mod'] = mod4
    dnd_dict.character_dict['Stats']['wisdom']['mod'] = mod5
    dnd_dict.character_dict['Stats']['charisma']['mod'] = mod6

# Starts the initial level
    dnd_dict.character_dict['total_level'] = 1
# Gives the proficiency bonus
    dnd_skills.prof_modifier()
# Hit points: Constitution mod (except Hill Dwarves who get an additional +1)
    hit_points = (dnd_dict.character_dict["Stats"]['constitution']['mod'] + 1)
    dnd_dict.character_dict['hp'] = hit_points


    while True:
        choice = input("Select the artisan's tools you want proficiency in:\n1) Smith's Tools\n2) Brewer's Supplies\n3) Mason's Tools\nEnter your selection: ")
   
        if choice == '1':
            dnd_dict.character_dict["Tools"]['smith_tools'] = "Smith's Tools"
            break

        elif choice == '2':
            dnd_dict.character_dict["Tools"]['brewer_tools'] = "Brewer's Tools"
            break

        elif choice == '3':
            dnd_dict.character_dict["Tools"]['mason_tools'] = "Mason's Tools"
            break

        else:
            print("Invalid Selection")
            continue

    dnd_skills.set_skill()


    dwarf_weapon = {'battleaxes':'Battleaxes','handaxes':'Handaxes','light_hammers':'Light Hammers','warhammers':'Warhammers'}
    dnd_dict.character_dict["Weapon_Prof"].update(dwarf_weapon)


    dnd_features.dwarf_hill_features()

def dwarf_mountain():
    dnd_dict.character_dict['Stats']['constitution']['base'] += 2 
    dnd_dict.character_dict['Stats']['wisdom']['base'] += 2

    dnd_class.RaceStats.racial_choice("Mountain Dwarf", 25, "Medium")
    dnd_dict.character_dict["Languages"]['dwarvish'] = "Dwarvish"
    dnd_dict.character_dict["speed"] = 25
    dnd_dict.character_dict['size'] = 'Medium'
    dnd_dict.character_dict['race'] = 'Mountain Dwarf'


#Update all modifiers
    mod1 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['strength']['base'])
    mod2 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['dexterity']['base'])
    mod3 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['constitution']['base'])
    mod4 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['intelligence']['base'])
    mod5 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['wisdom']['base'])
    mod6 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['charisma']['base'])


    dnd_dict.character_dict['Stats']['strength']['mod'] = mod1
    dnd_dict.character_dict['Stats']['dexterity']['mod'] = mod2
    dnd_dict.character_dict['Stats']['constitution']['mod'] = mod3
    dnd_dict.character_dict['Stats']['intelligence']['mod'] = mod4
    dnd_dict.character_dict['Stats']['wisdom']['mod'] = mod5
    dnd_dict.character_dict['Stats']['charisma']['mod'] = mod6

# Starts the initial level
    dnd_dict.character_dict['total_level'] = 1
# Gives the proficiency bonus
    dnd_skills.prof_modifier()
# Hit points: Constitution mod (except Hill Dwarves who get an additional +1)
    dnd_dict.character_dict['hp']= dnd_dict.character_dict["Stats"]['constitution']['mod']

    while True:
        choice = input("Select the artisan's tools you want proficiency in:\n1) Smith's Tools\n2) Brewer's Supplies\n3) Mason's Tools\nEnter your selection: ")
   
        if choice == '1':
            dnd_dict.character_dict["Tools"]['smith_tools'] = "Smith's Tools"
            break

        elif choice == '2':
            dnd_dict.character_dict["Tools"]['brewer_tools'] = "Brewer's Tools"
            break

        elif choice == '3':
            dnd_dict.character_dict["Tools"]['mason_tools'] = "Mason's Tools"
            break

        else:
            print("Invalid Selection")
            continue


    dnd_skills.set_skill()


    dwarf_weapon = {'battleaxe':'Battleaxes','handaxe':'Handaxes','light_hammer':'Light Hammers','warhammer':'Warhammers'}
    dnd_dict.character_dict["Weapon_Prof"].update(dwarf_weapon)


    dnd_features.dwarf_mountain_features()

def elf_high():
    race1 = (dnd_dict.character_dict["Stats"]["dexterity"]["base"] + 2)
    race2 = (dnd_dict.character_dict["Stats"]["intelligence"]["base"] + 1)

    dnd_dict.character_dict['Stats']['dexterity']['base'] = race1
    dnd_dict.character_dict['Stats']['intelligence']['base'] = race2

    dnd_language.elf_lang()

    dnd_class.RaceStats.racial_choice("High Elf", 30, "Medium")
    dnd_dict.character_dict["speed"] = 30
    dnd_dict.character_dict['size'] = 'Medium'
    dnd_dict.character_dict['race'] = 'High Elf'
    dnd_dict.character_dict["Languages"]['elven'] = "Elven"


#Update all modifiers
    mod1 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['strength']['base'])
    mod2 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['dexterity']['base'])
    mod3 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['constitution']['base'])
    mod4 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['intelligence']['base'])
    mod5 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['wisdom']['base'])
    mod6 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['charisma']['base'])


    dnd_dict.character_dict['Stats']['strength']['mod'] = mod1
    dnd_dict.character_dict['Stats']['dexterity']['mod'] = mod2
    dnd_dict.character_dict['Stats']['constitution']['mod'] = mod3
    dnd_dict.character_dict['Stats']['intelligence']['mod'] = mod4
    dnd_dict.character_dict['Stats']['wisdom']['mod'] = mod5
    dnd_dict.character_dict['Stats']['charisma']['mod'] = mod6
# Starts the initial level
    dnd_dict.character_dict['total_level'] = 1
# Gives the proficiency bonus
    dnd_skills.prof_modifier()

# Hit points: Constitution mod (except Hill Dwarves who get an additional +1)
    dnd_dict.character_dict['hp']= dnd_dict.character_dict["Stats"]['constitution']['mod']



    elf_weapon_prof = {'longswords':'Longswords', 'shortswords':'Shortswords', 'shortbows':'Shortbows', 'longbows':'Longbows'}
    dnd_dict.character_dict["Weapon_Prof"].update(elf_weapon_prof)

    dnd_skills.set_skill()
    dnd_skills.spell_add(dnd_magic.wizard_cantrip,dnd_dict.character_dict['spells']['cantrips'],dnd_dict.character_dict['special_spells']['cantrips'])

    dnd_dict.character_dict['skill_prof']['perception'] = 'Perception'

    dnd_features.elf_features()

def elf_wood():

    race1 = (dnd_dict.character_dict["Stats"]["dexterity"]["base"] + 2)
    race2 = (dnd_dict.character_dict["Stats"]["wisdom"]["base"] + 1)

    dnd_dict.character_dict['Stats']['dexterity']['base'] = race1
    dnd_dict.character_dict['Stats']['wisdom']['base'] = race2

#Update all modifiers
    mod1 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['strength']['base'])
    mod2 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['dexterity']['base'])
    mod3 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['constitution']['base'])
    mod4 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['intelligence']['base'])
    mod5 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['wisdom']['base'])
    mod6 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['charisma']['base'])


    dnd_dict.character_dict['Stats']['strength']['mod'] = mod1
    dnd_dict.character_dict['Stats']['dexterity']['mod'] = mod2
    dnd_dict.character_dict['Stats']['constitution']['mod'] = mod3
    dnd_dict.character_dict['Stats']['intelligence']['mod'] = mod4
    dnd_dict.character_dict['Stats']['wisdom']['mod'] = mod5
    dnd_dict.character_dict['Stats']['charisma']['mod'] = mod6
# Starts the initial level
    dnd_dict.character_dict['total_level'] = 1
# Gives the proficiency bonus
    dnd_skills.prof_modifier()

    dnd_class.RaceStats.racial_choice("Wood Elf", 35, "Medium")
    dnd_dict.character_dict["speed"] = 35
    dnd_dict.character_dict['size'] = 'Medium'
    dnd_dict.character_dict["Languages"]['elven'] = "Elven"
    dnd_dict.character_dict['race'] = 'Wood Elf'

# Hit points: Constitution mod (except Hill Dwarves who get an additional +1)
    dnd_dict.character_dict['hp']= dnd_dict.character_dict["Stats"]['constitution']['mod']

    dnd_skills.set_skill()
    dnd_dict.character_dict['skill_prof']['perception'] = 'Perception'
    


    elf_weapon_prof = {'longswords':'Longswords', 'shortswords':'Shortswords', 'shortbows':'Shortbows', 'longbows':'Longbows'}
    dnd_dict.character_dict["Weapon_Prof"].update(elf_weapon_prof)

    dnd_features.elf_features()



def gnome_forest():

    race1 = (dnd_dict.character_dict["Stats"]["intelligence"]["base"] + 2)
    race2 = (dnd_dict.character_dict["Stats"]["dexterity"]["base"] + 1)

    dnd_dict.character_dict['Stats']['intelligence']['base'] = race1
    dnd_dict.character_dict['Stats']['dexterity']['base'] = race2

#Update all modifiers
    mod1 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['strength']['base'])
    mod2 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['dexterity']['base'])
    mod3 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['constitution']['base'])
    mod4 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['intelligence']['base'])
    mod5 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['wisdom']['base'])
    mod6 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['charisma']['base'])


    dnd_dict.character_dict['Stats']['strength']['mod'] = mod1
    dnd_dict.character_dict['Stats']['dexterity']['mod'] = mod2
    dnd_dict.character_dict['Stats']['constitution']['mod'] = mod3
    dnd_dict.character_dict['Stats']['intelligence']['mod'] = mod4
    dnd_dict.character_dict['Stats']['wisdom']['mod'] = mod5
    dnd_dict.character_dict['Stats']['charisma']['mod'] = mod6

# Starts the initial level
    dnd_dict.character_dict['total_level'] = 1
# Gives the proficiency bonus
    dnd_skills.prof_modifier()
# Hit points: Constitution mod (except Hill Dwarves who get an additional +1)
    dnd_dict.character_dict['hp']= dnd_dict.character_dict["Stats"]['constitution']['mod']

    dnd_skills.set_skill()

    dnd_class.RaceStats.racial_choice("Forest Gnome", 25, "Small")
    dnd_dict.character_dict["speed"] = 25
    dnd_dict.character_dict['size'] = 'Small'
    dnd_dict.character_dict["Languages"]['gnomish'] = "Gnomish"
    dnd_dict.character_dict['race'] = 'Forest Gnome'

    dnd_features.gnome_forest_features()

def gnome_rock():

    race1 = (dnd_dict.character_dict["Stats"]["intelligence"]["base"] + 2)
    race2 = (dnd_dict.character_dict["Stats"]["constitution"]["base"] + 1)

    dnd_dict.character_dict['Stats']['intelligence']['base'] = race1
    dnd_dict.character_dict['Stats']['constitution']['base'] = race2

#Update all modifiers
    mod1 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['strength']['base'])
    mod2 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['dexterity']['base'])
    mod3 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['constitution']['base'])
    mod4 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['intelligence']['base'])
    mod5 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['wisdom']['base'])
    mod6 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['charisma']['base'])


    dnd_dict.character_dict['Stats']['strength']['mod'] = mod1
    dnd_dict.character_dict['Stats']['dexterity']['mod'] = mod2
    dnd_dict.character_dict['Stats']['constitution']['mod'] = mod3
    dnd_dict.character_dict['Stats']['intelligence']['mod'] = mod4
    dnd_dict.character_dict['Stats']['wisdom']['mod'] = mod5
    dnd_dict.character_dict['Stats']['charisma']['mod'] = mod6

# Starts the initial level
    dnd_dict.character_dict['total_level'] = 1
# Gives the proficiency bonus
    dnd_skills.prof_modifier()
# Hit points: Constitution mod (except Hill Dwarves who get an additional +1)
    dnd_dict.character_dict['hp']= dnd_dict.character_dict["Stats"]['constitution']['mod']

    dnd_skills.set_skill()

    dnd_class.RaceStats.racial_choice("Rock Gnome", 25, "Small")
    dnd_dict.character_dict["speed"] = 25
    dnd_dict.character_dict['size'] = 'Small'
    dnd_dict.character_dict["Languages"]['gnomish'] = "Gnomish"
    dnd_dict.character_dict['race'] = 'Rock Gnome'

    dnd_features.gnome_rock_features()

def half_elf():

# Increase Charisma score by 2
    race1 = (dnd_dict.character_dict["Stats"]["charisma"]["base"] + 2)
    dnd_dict.character_dict['Stats']['charisma']['base'] = race1

# Choose 2 stats (not counting charisma) to increase by 1
    while True:
        choice1 = input("Select the first stat you want to improve:\n1) Strength\n2) Dexterity\n3) Constitution\n4) Intelligence\n5) Wisdom\nEnter your Selection: ")
        if choice1=='1':                    
            race2 = (dnd_dict.character_dict["Stats"]["strength"]["base"] + 1)
            dnd_dict.character_dict['Stats']['strength']['base'] = race2
            break
 
        elif choice1=='2':
            race2 = (dnd_dict.character_dict["Stats"]["dexterity"]["base"] + 1)
            dnd_dict.character_dict['Stats']['dexterity']['base'] = race2
            break
 
        elif choice1=='3':
            race2 = (dnd_dict.character_dict["Stats"]["constitution"]["base"] + 1)
            dnd_dict.character_dict['Stats']['constitution']['base'] = race2
            break
 
        elif choice1=='4':
            race2 = (dnd_dict.character_dict["Stats"]["intelligence"]["base"] + 1)
            dnd_dict.character_dict['Stats']['intelligence']['base'] = race2
            break
 
        elif choice1=='5':
            race2 = (dnd_dict.character_dict["Stats"]["wisdom"]["base"] + 1)
            dnd_dict.character_dict['Stats']['wisdom']['base'] = race2
            break


        else:
            print("Invalid Selection")
            continue

    while True:
        choice2 = input("Select the second stat you want to improve:\n1) Strength\n2) Dexterity\n3) Constitution\n4) Intelligence\n5) Wisdom\nEnter your Selection: ")
        if choice2=='1':
            if choice1=='1':
                print("Already Selected")
                continue
            else:
                race3 = (dnd_dict.character_dict["Stats"]["strength"]["base"] + 1)
                dnd_dict.character_dict['Stats']['strength']['base'] = race3
                break
 
        elif choice2=='2':
            if choice1=='2':
                print("Already Selected")
                continue
            else:
                race3 = (dnd_dict.character_dict["Stats"]["dexterity"]["base"] + 1)
                dnd_dict.character_dict['Stats']['dexterity']['base'] = race3
                break
 
        elif choice2=='3':
            if choice1=='3':
                print("Already Selected")
                continue
            else:
                race3 = (dnd_dict.character_dict["Stats"]["constitution"]["base"] + 1)
                dnd_dict.character_dict['Stats']['constitution']['base'] = race3
                break
 
        elif choice2=='4':
            if choice1=='4':
                print("Already Selected")
                continue
            else:
                race3 = (dnd_dict.character_dict["Stats"]["intelligence"]["base"] + 1)
                dnd_dict.character_dict['Stats']['intelligence']['base'] = race3
                break
 
        elif choice2=='5':
            if choice1=='5':
                print("Already Selected")
                continue
            else:
                race3 = (dnd_dict.character_dict["Stats"]["wisdom"]["base"] + 1)
                dnd_dict.character_dict['Stats']['wisdom']['base'] = race3
                break

        else:
            print("Invalid Selection")
            continue

#Update all modifiers
    mod1 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['strength']['base'])
    mod2 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['dexterity']['base'])
    mod3 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['constitution']['base'])
    mod4 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['intelligence']['base'])
    mod5 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['wisdom']['base'])
    mod6 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['charisma']['base'])


    dnd_dict.character_dict['Stats']['strength']['mod'] = mod1
    dnd_dict.character_dict['Stats']['dexterity']['mod'] = mod2
    dnd_dict.character_dict['Stats']['constitution']['mod'] = mod3
    dnd_dict.character_dict['Stats']['intelligence']['mod'] = mod4
    dnd_dict.character_dict['Stats']['wisdom']['mod'] = mod5
    dnd_dict.character_dict['Stats']['charisma']['mod'] = mod6

# Starts the initial level
    dnd_dict.character_dict['total_level'] = 1
# Gives the proficiency bonus
    dnd_skills.prof_modifier()
# Hit points: Constitution mod (except Hill Dwarves who get an additional +1)
    dnd_dict.character_dict['hp']= dnd_dict.character_dict["Stats"]['constitution']['mod']

    dnd_skills.set_skill()

# Select the languages known.
    dnd_dict.character_dict["Languages"]['elven'] = "Elven"
    dnd_language.elf_lang()

    dnd_class.RaceStats.racial_choice("Half-Elf", 30, "Medium")
    dnd_dict.character_dict["speed"] = 30
    dnd_dict.character_dict['size'] = 'Medium'
    dnd_dict.character_dict['race'] = 'Half-Elf'
    dnd_skills.half_elf_skills()

    dnd_features.half_elf_features()

def halfling_lightfoot():

    race1 = (dnd_dict.character_dict["Stats"]["dexterity"]["base"] + 2)
    race2 = (dnd_dict.character_dict["Stats"]["charisma"]["base"] + 1)

    dnd_dict.character_dict['Stats']['dexterity']['base'] = race1
    dnd_dict.character_dict['Stats']['charisma']['base'] = race2

#Update all modifiers
    mod1 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['strength']['base'])
    mod2 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['dexterity']['base'])
    mod3 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['constitution']['base'])
    mod4 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['intelligence']['base'])
    mod5 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['wisdom']['base'])
    mod6 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['charisma']['base'])


    dnd_dict.character_dict['Stats']['strength']['mod'] = mod1
    dnd_dict.character_dict['Stats']['dexterity']['mod'] = mod2
    dnd_dict.character_dict['Stats']['constitution']['mod'] = mod3
    dnd_dict.character_dict['Stats']['intelligence']['mod'] = mod4
    dnd_dict.character_dict['Stats']['wisdom']['mod'] = mod5
    dnd_dict.character_dict['Stats']['charisma']['mod'] = mod6

# Starts the initial level
    dnd_dict.character_dict['total_level'] = 1
# Gives the proficiency bonus
    dnd_skills.prof_modifier()
# Hit points: Constitution mod (except Hill Dwarves who get an additional +1)
    dnd_dict.character_dict['hp']= dnd_dict.character_dict["Stats"]['constitution']['mod']

    dnd_skills.set_skill()

    dnd_class.RaceStats.racial_choice("Lightfoot Halfling", 25, "Small")
    dnd_dict.character_dict["speed"] = 25
    dnd_dict.character_dict['size'] = 'Small'
    dnd_dict.character_dict["Languages"]['halfling'] = "Halfling"
    dnd_dict.character_dict['race'] = 'Lightfoot Halfling'

    dnd_features.halfling_lightfoot_features()

def halfling_stout():

    race1 = (dnd_dict.character_dict["Stats"]["dexterity"]["base"] + 2)
    race2 = (dnd_dict.character_dict["Stats"]["constitution"]["base"] + 1)

    dnd_dict.character_dict['Stats']['dexterity']['base'] = race1
    dnd_dict.character_dict['Stats']['constitution']['base'] = race2

#Update all modifiers
    mod1 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['strength']['base'])
    mod2 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['dexterity']['base'])
    mod3 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['constitution']['base'])
    mod4 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['intelligence']['base'])
    mod5 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['wisdom']['base'])
    mod6 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['charisma']['base'])


    dnd_dict.character_dict['Stats']['strength']['mod'] = mod1
    dnd_dict.character_dict['Stats']['dexterity']['mod'] = mod2
    dnd_dict.character_dict['Stats']['constitution']['mod'] = mod3
    dnd_dict.character_dict['Stats']['intelligence']['mod'] = mod4
    dnd_dict.character_dict['Stats']['wisdom']['mod'] = mod5
    dnd_dict.character_dict['Stats']['charisma']['mod'] = mod6

# Starts the initial level
    dnd_dict.character_dict['total_level'] = 1
# Gives the proficiency bonus
    dnd_skills.prof_modifier()
# Hit points: Constitution mod (except Hill Dwarves who get an additional +1)
    dnd_dict.character_dict['hp']= dnd_dict.character_dict["Stats"]['constitution']['mod']

    dnd_skills.set_skill()

    dnd_class.RaceStats.racial_choice("Stout Halfling", 25, "Small")
    dnd_dict.character_dict["speed"] = 25
    dnd_dict.character_dict['size'] = 'Small'
    dnd_dict.character_dict["Languages"]['halfling'] = "Halfling"
    dnd_dict.character_dict['race'] = 'Stout Halfling'

    dnd_features.halfling_stout_features()

def half_orc():

    race1 = (dnd_dict.character_dict["Stats"]["strength"]["base"] + 2)
    race2 = (dnd_dict.character_dict["Stats"]["constitution"]["base"] + 1)

    dnd_dict.character_dict['Stats']['strength']['base'] = race1
    dnd_dict.character_dict['Stats']['constitution']['base'] = race2

#Update all modifiers
    mod1 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['strength']['base'])
    mod2 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['dexterity']['base'])
    mod3 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['constitution']['base'])
    mod4 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['intelligence']['base'])
    mod5 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['wisdom']['base'])
    mod6 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['charisma']['base'])


    dnd_dict.character_dict['Stats']['strength']['mod'] = mod1
    dnd_dict.character_dict['Stats']['dexterity']['mod'] = mod2
    dnd_dict.character_dict['Stats']['constitution']['mod'] = mod3
    dnd_dict.character_dict['Stats']['intelligence']['mod'] = mod4
    dnd_dict.character_dict['Stats']['wisdom']['mod'] = mod5
    dnd_dict.character_dict['Stats']['charisma']['mod'] = mod6

# Starts the initial level
    dnd_dict.character_dict['total_level'] = 1
# Gives the proficiency bonus
    dnd_skills.prof_modifier()
# Hit points: Constitution mod (except Hill Dwarves who get an additional +1)
    dnd_dict.character_dict['hp']= dnd_dict.character_dict["Stats"]['constitution']['mod']

    dnd_skills.set_skill()

    dnd_class.RaceStats.racial_choice("Half-Orc", 30, "Medium")
    dnd_dict.character_dict["speed"] = 30
    dnd_dict.character_dict['size'] = 'Medium'
    dnd_dict.character_dict["Languages"]['orc'] = "Orc"
    dnd_dict.character_dict['race'] = 'Half-Orc'

#   Proficiency with Intimidation
    dnd_dict.character_dict['skill_prof']['intimidation'] = 'Intimidation'

    dnd_features.half_orc_features()


def human_regular():

    race1 = (dnd_dict.character_dict["Stats"]["strength"]["base"] + 1)
    race2 = (dnd_dict.character_dict["Stats"]["dexterity"]["base"] + 1)
    race3 = (dnd_dict.character_dict["Stats"]["constitution"]["base"] + 1)
    race4 = (dnd_dict.character_dict["Stats"]["intelligence"]["base"] + 1)
    race5 = (dnd_dict.character_dict["Stats"]["wisdom"]["base"] + 1)
    race6 = (dnd_dict.character_dict["Stats"]["charisma"]["base"] + 1)

    dnd_dict.character_dict['Stats']['strength']['base'] = race1
    dnd_dict.character_dict['Stats']['dexterity']['base'] = race2
    dnd_dict.character_dict['Stats']['constitution']['base'] = race3
    dnd_dict.character_dict['Stats']['intelligence']['base'] = race4
    dnd_dict.character_dict['Stats']['wisdom']['base'] = race5
    dnd_dict.character_dict['Stats']['charisma']['base'] = race6

#Update all modifiers
    mod1 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['strength']['base'])
    mod2 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['dexterity']['base'])
    mod3 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['constitution']['base'])
    mod4 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['intelligence']['base'])
    mod5 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['wisdom']['base'])
    mod6 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['charisma']['base'])


    dnd_dict.character_dict['Stats']['strength']['mod'] = mod1
    dnd_dict.character_dict['Stats']['dexterity']['mod'] = mod2
    dnd_dict.character_dict['Stats']['constitution']['mod'] = mod3
    dnd_dict.character_dict['Stats']['intelligence']['mod'] = mod4
    dnd_dict.character_dict['Stats']['wisdom']['mod'] = mod5
    dnd_dict.character_dict['Stats']['charisma']['mod'] = mod6

# Starts the initial level
    dnd_dict.character_dict['total_level'] = 1
# Gives the proficiency bonus
    dnd_skills.prof_modifier()
# Hit points: Constitution mod (except Hill Dwarves who get an additional +1)
    dnd_dict.character_dict['hp']= dnd_dict.character_dict["Stats"]['constitution']['mod']

    dnd_skills.set_skill()

    dnd_language.language()
    dnd_class.RaceStats.racial_choice("Human", 30, "Medium")
    dnd_dict.character_dict["speed"] = 30
    dnd_dict.character_dict['size'] = 'Medium'
    dnd_dict.character_dict['race'] = 'Human'

def tiefling():

    race1 = (dnd_dict.character_dict["Stats"]["charisma"]["base"] + 2)
    race2 = (dnd_dict.character_dict["Stats"]["intelligence"]["base"] + 1)

    dnd_dict.character_dict['Stats']['charisma']['base'] = race1
    dnd_dict.character_dict['Stats']['intelligence']['base'] = race2

#Update all modifiers
    mod1 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['strength']['base'])
    mod2 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['dexterity']['base'])
    mod3 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['constitution']['base'])
    mod4 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['intelligence']['base'])
    mod5 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['wisdom']['base'])
    mod6 = dnd_class.Character.mod(dnd_dict.character_dict["Stats"]['charisma']['base'])


    dnd_dict.character_dict['Stats']['strength']['mod'] = mod1
    dnd_dict.character_dict['Stats']['dexterity']['mod'] = mod2
    dnd_dict.character_dict['Stats']['constitution']['mod'] = mod3
    dnd_dict.character_dict['Stats']['intelligence']['mod'] = mod4
    dnd_dict.character_dict['Stats']['wisdom']['mod'] = mod5
    dnd_dict.character_dict['Stats']['charisma']['mod'] = mod6

# Starts the initial level
    dnd_dict.character_dict['total_level'] = 1
# Gives the proficiency bonus
    dnd_skills.prof_modifier()
# Hit points: Constitution mod (except Hill Dwarves who get an additional +1)
    dnd_dict.character_dict['hp']= dnd_dict.character_dict["Stats"]['constitution']['mod']

    dnd_skills.set_skill()

    dnd_class.RaceStats.racial_choice("Tiefling", 30, "Medium")
    dnd_dict.character_dict["speed"] = 30
    dnd_dict.character_dict['size'] = 'Medium'
    dnd_dict.character_dict["Languages"]['infernal'] = "Infernal"
    dnd_dict.character_dict['race'] = 'Tiefling'

    dnd_features.tiefling_features()

def player_race():
    while True:
        choose_race = input("""Choose your race:
1) Dragonborn
2) Dwarf (Hill)
3) Dwarf (Mountain)
4) Elf (High)
5) Elf (Wood)
6) Gnome (Forest)
7) Gnome (Rock)
8) Half-Elf
9) Halfling (Lightfoot)
10) Halfling (Stout)
11) Half-Orc
12) Human (Regular)
13) Tiefling
0) Exit
Enter your selection: """)

        if choose_race =='1':
            dragonborn() 
            break
 
        elif choose_race =='2':
            dwarf_hill()
            break

        elif choose_race =='3':
            dwarf_mountain()
            break

        elif choose_race =='4':
            elf_high()
            break
 
        elif choose_race =='5':
            elf_wood()
            break

        elif choose_race =='6':
            gnome_forest()
            break

        elif choose_race =='7':
            gnome_rock()
            break

        elif choose_race =='8':
            half_elf()
            break

        elif choose_race =='9':
            halfling_lightfoot()
            break

        elif choose_race =='10':
            halfling_stout()
            break

        elif choose_race =='11':
            half_orc()
            break

        elif choose_race =='12':
            human_regular()
            break

        elif choose_race =='13':
            tiefling()
            break

        elif choose_race == '0':
            print("Exiting program")
            exit()

        else:
            print("Invalid Selection")
            continue
