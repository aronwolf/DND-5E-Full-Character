import dnd_dict, dnd_features, dnd_skills,dnd_level_up

def barbarian():
    level = dnd_dict.character_dict['player_class']['barbarian']['class_level']

# Level 1
    if level == 1:
        armor_prof = {'light_armor':'Light Armor','medium_armor':'Medium Armor','shields':'Shields'}
        weapon_prof = {'simple_weapons':'Simple Weapons','martial_weapons':'Martial Weapons'}
        dnd_dict.character_dict['Weapon_Prof'].update(weapon_prof)
        dnd_dict.character_dict['Armor_Prof'].update(armor_prof)
        dnd_dict.character_dict['rage'] +=2
        dnd_dict.character_dict['rage_damage'] +=2
        dnd_features.barbarian_features()
        dnd_dict.character_dict['d12'] +=1
        dnd_level_up.level_up(12)

# Level 2
    if level == 2:

        dnd_features.barbarian2()
        dnd_dict.character_dict['d12'] +=1
        dnd_level_up.level_up(12)

# Level 3
    if level == 3:

        while True:
            choice = input("""Select the subclass you want to have:
1) Path of the Berserker
2) Path of the Totem Warrior
Enter your selection: """)
            if choice == '1':
                dnd_dict.character_dict['player_class']['barbarian']['subclass'] = 'Path of the Berserker'
                dnd_features.berserker3()
                break
            elif choice == '2':
                dnd_dict.character_dict['player_class']['barbarian']['subclass'] = 'Path of the Totem Warrior'
                dnd_features.totem_warrior3()
                break
            else:
                print("Error: Invalid Input")
                continue

        dnd_features.barbarian3()
        dnd_dict.character_dict['rage']+=1
        dnd_dict.character_dict['d12'] +=1
        dnd_level_up.level_up(12)

# Level 4
    if level == 4:

        dnd_level_up.asi_or_feat()
        dnd_dict.character_dict['d12'] +=1
        dnd_level_up.level_up(12)

# Level 5
    if level == 5:

        dnd_features.barbarian5()
        dnd_dict.character_dict['d12'] +=1
        dnd_level_up.level_up(12)

# Level 6
    if level == 6:
        if dnd_dict.character_dict['player_class']['barbarian']['subclass'] == 'Path of the Berserker':
            dnd_features.berserker6()
        if dnd_dict.character_dict['player_class']['barbarian']['subclass'] == 'Path of the Totem Warrior':
            dnd_features.totem_warrior6()
        dnd_dict.character_dict['rage']+=1
        dnd_dict.character_dict['d12'] +=1
        dnd_level_up.level_up(12)

# Level 7
    if level == 7:

        dnd_features.barbarian7()
        dnd_dict.character_dict['d12'] +=1
        dnd_level_up.level_up(12)

# Level 8
    if level == 8:

        dnd_level_up.asi_or_feat()
        dnd_dict.character_dict['d12'] +=1
        dnd_level_up.level_up(12)

# Level 9
    if level == 9:

        dnd_features.barbarian9()
        dnd_dict.character_dict['rage_damage']+=1
        dnd_dict.character_dict['d12'] +=1
        dnd_level_up.level_up(12)

# level 10
    if level == 10:

        if dnd_dict.character_dict['player_class']['barbarian']['subclass'] == 'Path of the Berserker':
            dnd_features.berserker10()
        if dnd_dict.character_dict['player_class']['barbarian']['subclass'] == 'Path of the Totem Warrior':
            dnd_features.totem_warrior10()

        dnd_features.barbarian3()
        dnd_dict.character_dict['d12'] +=1
        dnd_level_up.level_up(12)

# Level 11
    if level == 11:

        dnd_features.barbarian11()
        dnd_dict.character_dict['d12'] +=1
        dnd_level_up.level_up(12)

# Level 12
    if level == 12:

        dnd_level_up.asi_or_feat()
        dnd_dict.character_dict['rage']+=1
        dnd_dict.character_dict['d12'] +=1
        dnd_level_up.level_up(12)

# Level 13
    if level == 13:

        dnd_dict.character_dict['d12'] +=1
        dnd_level_up.level_up(12)

# Level 14
    if level == 14:

        if dnd_dict.character_dict['player_class']['barbarian']['subclass'] == 'Path of the Berserker':
            dnd_features.berserker14()
        if dnd_dict.character_dict['player_class']['barbarian']['subclass'] == 'Path of the Totem Warrior':
            dnd_features.totem_warrior14()

        dnd_dict.character_dict['d12'] +=1
        dnd_level_up.level_up(12)

# Level 15
    if level == 15:

        dnd_features.barbarian15()
        dnd_dict.character_dict['d12'] +=1
        dnd_level_up.level_up(12)

# Level 16
    if level == 16:

        dnd_level_up.asi_or_feat()
        dnd_dict.character_dict['rage_damage']+=1
        dnd_dict.character_dict['d12'] +=1
        dnd_level_up.level_up(12)

# Level 17
    if level == 17:

        dnd_dict.character_dict['rage']+=1
        dnd_dict.character_dict['d12'] +=1
        dnd_level_up.level_up(12)

# Level 18
    if level == 18:

        dnd_features.barbarian18()
        dnd_dict.character_dict['d12'] +=1
        dnd_level_up.level_up(12)

# Level 19
    if level == 19:

        dnd_level_up.asi_or_feat()
        dnd_dict.character_dict['d12'] +=1
        dnd_level_up.level_up(12)

# Level 20
    if level == 20:

        dnd_features.barbarian20()
        dnd_dict.character_dict['rage']=='Unlimited'
        dnd_dict.character_dict['d12'] +=1
        dnd_level_up.level_up(12)

    else:
        pass




































