import dnd_dict, dnd_features, dnd_skills, dnd_four_elements, dnd_level_up

def monk():
    level = dnd_dict.character_dict['player_class']['monk']['class_level']

# Level 1
    if level == 1:

        weapon_prof = {'simple_weapons':'Simple Weapons','shortswords':'Shortswords'}
        dnd_dict.character_dict['Weapon_Prof'].update(weapon_prof)
        dnd_features.monk_features()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)

# Level 2
    if level == 2:

        dnd_features.monk2()
        spell_save = ((dnd_dict.character_dict["Stats"]["wisdom"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
        dnd_dict.character_dict["spell_modifier"]['ki_save'] = spell_save
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['ki_points'] += 2

# Level 3
    if level == 3:

        while True:
            choice = input("""Select the subclass you want to have:
1) Way of the Four Elements
2) Way of the Open Hand
3) Way of the Shadow
Enter your selection: """)
            if choice == '1':
                dnd_features.four_elements_monk3()
                break

            elif choice == '2':
                dnd_features.open_hand_monk3()
                break

            elif choice == '3':
                dnd_features.shadow_monk3()
                break

            else:
                print("Error: Invalid Input")
                continue

        dnd_features.monk3()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['ki_points'] += 1

# Level 4
    if level == 4:

        dnd_level_up.asi_or_feat()
        dnd_features.monk4()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['ki_points'] += 1

# Level 5
    if level == 5:

        dnd_features.monk5()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['ki_points'] += 1
        dnd_dict.character_dict['martial_arts'] = '1d6'

# Level 6
    if level == 6:

        dnd_features.monk6()

        if dnd_dict.character_dict['player_class']['monk']['subclass'] == 'Way of the Four Elements':
            dnd_features.four_elements_monk6()
        if dnd_dict.character_dict['player_class']['monk']['subclass'] == 'Way of the Open Hand':
            dnd_features.open_hand_monk6()
        if dnd_dict.character_dict['player_class']['monk']['subclass'] == 'Way of the Shadow':
            dnd_features.shadow_monk6()

        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['ki_points'] += 1

# Level 7
    if level == 7:

        dnd_features.monk7()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['ki_points'] += 1

# Level 8
    if level == 8:

        dnd_level_up.asi_or_feat()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['ki_points'] += 1

# Level 9
    if level == 9:

        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['ki_points'] += 1

# Level 10
    if level == 10:

        dnd_features.monk10()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['ki_points'] += 1

# Level 11
    if level == 11:

        if dnd_dict.character_dict['player_class']['monk']['subclass'] == 'Way of the Four Elements':
            dnd_features.four_elements_monk11()
        if dnd_dict.character_dict['player_class']['monk']['subclass'] == 'Way of the Open Hand':
            dnd_features.open_hand_monk11()
        if dnd_dict.character_dict['player_class']['monk']['subclass'] == 'Way of the Shadow':
            dnd_features.shadow_monk11()

        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['ki_points'] += 1
        dnd_dict.character_dict['martial_arts'] = '1d8'

# Level 12
    if level == 12:

        dnd_level_up.asi_or_feat()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['ki_points'] += 1

# Level 13
    if level == 13:

        dnd_features.monk13()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['ki_points'] += 1

# Level 14
    if level == 14:

        dnd_features.monk14()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['ki_points'] += 1

# Level 15
    if level == 15:

        dnd_features.monk15()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['ki_points'] += 1

# Level 16
    if level == 16:

        dnd_level_up.asi_or_feat()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['ki_points'] += 1

# Level 17
    if level == 17:

        if dnd_dict.character_dict['player_class']['monk']['subclass'] == 'Way of the Four Elements':
            dnd_features.four_elements_monk17()
        if dnd_dict.character_dict['player_class']['monk']['subclass'] == 'Way of the Open Hand':
            dnd_features.open_hand_monk17()
        if dnd_dict.character_dict['player_class']['monk']['subclass'] == 'Way of the Shadow':
            dnd_features.shadow_monk17()

        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['ki_points'] += 1
        dnd_dict.character_dict['martial_arts'] = '1d10'

# Level 18
    if level == 18:

        dnd_features.monk18()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['ki_points'] += 1

# Level 19
    if level == 19:

        dnd_level_up.asi_or_feat()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['ki_points'] += 1

# Level 20
    if level == 20:

        dnd_features.monk20()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['ki_points'] += 1
