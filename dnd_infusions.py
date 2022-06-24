import dnd_dict,dnd_skills

# Requires to be a level 2 artificer
artificer_2 = ['Alchemy Jug','Armor of Magical Strength','Bag of Holding','Cap of Water Breathing','Enhanced Arcane Focus','Enhanced Defense','Enhanced Weapon','Goggles of Night','Homunculus Servant','Mind Sharpener','Repeating Shot','Returning Weapon','Rope of Climbing','Sending Stones','Wand of Magic Detection','Wand of Secrets']

# Requires to be a level 6 artificer
artificer_6 = ['Alchemy Jug','Armor of Magical Strength','Bag of Holding','Boots of Elvenkind','Boots of Winding Path','Cap of Water Breathing','Cloak of Elvenkind','Cloak of the Manta Ray','Enhanced Arcane Focus','Enhanced Defense','Enhanced Weapon','Eyes of Charming','Gloves of Thievery','Goggles of Night','Homunculus Servant','Lantern of Revealing','Mind Sharpener','Pipes of Haunting','Radiant Weapon','Repeating Shot','Repulsion Shield','Resistant Armor','Returning Weapon','Ring of Waterwalking','Rope of Climbing','Sending Stones','Spell-Refueling Ring','Wand of Magic Detection','Wand of Secrets']


# Requires to be a level 10 artificer
artificer_10 = ['Alchemy Jug','Armor of Magical Strength','Bag of Holding','Boots of Elvenkind','Boots of Striding and Springing','Boots of Winding Path','Boots of the Winterlands','Bracers of Archery','Brooch of Shielding','Cap of Water Breathing','Cloak of Elvenkind','Cloak of Protection','Cloak of the Manta Ray','Enhanced Arcane Focus','Enhanced Defense','Enhanced Weapon','Eyes of Charming','Eyes of the Eagle','Gauntlets of Ogre Power','Gloves of Missile Snaring','Gloves of Swimming and Climbing','Gloves of Thievery','Goggles of Night','Hat of Disguise','Headband of Intellect','Helm of Telepathy','Homunculus Servant','Lantern of Revealing','Medallion of Thought','Mind Sharpener','Necklace of Adaptation','Periapt of Wound Closure','Pipes of Haunting','Pipes of the Sewers','Quiver of Ehlonna','Radiant Weapon','Repeating Shot','Repulsion Shield','Resistant Armor','Returning Weapon','Ring of Jumping','Ring of Mind Shielding','Ring of Waterwalking','Rope of Climbing','Sending Stones','Slippers of Spider Climbing','Spell-Refueling Ring','Ventilating Lungs','Wand of Magic Detection','Wand of Secrets','Winged Boots']


# Requires to be a level 14 artificer
artificer_14 = ['Alchemy Jug','Amulet of Health','Arcane Propulsion Arm','Arcane Propulsion Armor','Armor of Magical Strength','Bag of Holding','Belt of Hill Giant Strength','Boots of Elvenkind','Boots of Levitation','Boots of Speed','Boots of Striding and Springing','Boots of Winding Path','Boots of the Winterlands','Bracers of Archery','Bracers of Defense','Brooch of Shielding','Cap of Water Breathing','Cloak of Elvenkind','Cloak of Protection','Cloak of the Bat','Cloak of the Manta Ray','Dimensional Shackles','Enhanced Arcane Focus','Enhanced Defense','Enhanced Weapon','Eyes of Charming','Eyes of the Eagle','Gauntlets of Ogre Power','Gem of Seeing','Gloves of Missile Snaring','Gloves of Swimming and Climbing','Gloves of Thievery','Goggles of Night','Hat of Disguise','Headband of Intellect','Helm of Telepathy','Homunculus Servant','Horn of Blasting','Lantern of Revealing','Medallion of Thought','Mind Sharpener','Necklace of Adaptation','Periapt of Wound Closure','Pipes of Haunting','Pipes of the Sewers','Quiver of Ehlonna','Radiant Weapon','Repeating Shot','Repulsion Shield','Resistant Armor','Returning Weapon','Ring of Free Action','Ring of Jumping','Ring of Mind Shielding','Ring of Protection','Ring of the Ram','Ring of Waterwalking','Rope of Climbing','Sending Stones','Slippers of Spider Climbing','Spell-Refueling Ring','Ventilating Lungs','Wand of Magic Detection','Wand of Secrets','Winged Boots']


# Get four infusions at the start
def art_infusions2():
    i = 1
    for i in range(i,5):
        if i < 5:
            print(f'{i}/4')
            dnd_skills.skill_addition(artificer_2,dnd_dict.character_dict['infusions'])
            i+=1
            continue

        if i == 5:
            break

# Gain two new infusions periodically
def art_infusions6():
    i = 1
    for i in range(i,3):
        if i < 3:
            print(f'{i}/2')
            dnd_skills.skill_addition(artificer_6,dnd_dict.character_dict['infusions'])
            i+=1
            continue

        if i == 3:
            break


def art_infusions10():
    i = 1
    for i in range(i,3):
        if i < 3:
            print(f'{i}/2')
            dnd_skills.skill_addition(artificer_10,dnd_dict.character_dict['infusions'])
            i+=1
            continue

        if i == 3:
            break

def art_infusions14():
    i = 1
    for i in range(i,3):
        if i < 3:
            print(f'{i}/2')
            dnd_skills.skill_addition(artificer_14,dnd_dict.character_dict['infusions'])
            i+=1
            continue

        if i == 3:
            break


# Swapping artificer infusions, inputting the level you need to swap
def art_swap(dict):
    while True:
        choice = input("""Do you want to swap an infusion at this level?
1) Yes
2) No
Enter your selection: """)
        if choice == '1':
            dnd_skills.skill_swap(dnd_dict.character_dict['infusions'])
            print("Select the infusion you want to add: ")
            dnd_skills.skill_addition(dict,dnd_dict.character_dict['infusions'])
            break

        elif choice == '2':
            break

        else:
            print("Invalid Input, please choose again")
            continue
