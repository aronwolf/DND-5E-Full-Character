import dnd_dict, dnd_features, dnd_magic, dnd_skills, dnd_fighting_styles, dnd_level_up

def paladin():
    level = dnd_dict.character_dict['player_class']['paladin']['class_level']

# Level 1
    if level == 1:

        armor_prof = {'light_armor':'Light Armor','medium_armor':'Medium Armor','shields':'Shields'}
        weapon_prof = {'simple_weapons':'Simple Weapons','martial_weapons':'Martial Weapons'}
        dnd_dict.character_dict['Armor_Prof'].update(armor_prof)
        dnd_dict.character_dict['Weapon_Prof'].update(weapon_prof)
        dnd_features.paladin_features()
        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)
        dnd_skills.spell_slot_selection()

# Level 2
    if level == 2:

        dnd_features.paladin2()
        dnd_magic.paladin_first()
        spell_attack = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'])
        dnd_dict.character_dict["spell_modifier"]['charisma']['attack'] = spell_attack
        spell_save = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
        dnd_dict.character_dict["spell_modifier"]['charisma']['save'] = spell_save
        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)
        dnd_dict.character_dict['half_caster_level'] += 2
        dnd_skills.spell_slot_selection()

# Level 3
    if level == 3:

        while True:
            choice = input("""Select the subclass you want to have:
1) Oath of the Ancients
2) Oath of Devotion
3) Oath of Vengeance
Enter your selection: """)
            if choice == '1':
                dnd_features.ancients_paladin3()
                break

            elif choice == '2':
                dnd_features.devotion_paladin3()
                break

            elif choice == '3':
                dnd_features.vengeance_paladin3()
                break

            else:
                print("Error: Invalid Input")
                continue

        dnd_features.paladin3()
        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)
        dnd_dict.character_dict['half_caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 4
    if level == 4:

        dnd_level_up.asi_or_feat()
        dnd_fighting_styles.martial_versatility_style_paladin()
        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)
        dnd_dict.character_dict['half_caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 5
    if level == 5:

        if dnd_dict.character_dict['player_class']['paladin']['subclass'] == 'Oath of the Ancients':
            dnd_features.ancients_paladin5()

        if dnd_dict.character_dict['player_class']['paladin']['subclass'] == 'Oath of Devotion':
            dnd_features.devotion_paladin5()

        if dnd_dict.character_dict['player_class']['paladin']['subclass'] == 'Oath of Vengeance':
            dnd_features.vengeance_paladin5()

        dnd_features.paladin5()
        dnd_magic.paladin_second()
        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)
        dnd_dict.character_dict['half_caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 6
    if level == 6:

        dnd_features.paladin6()
        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)
        dnd_dict.character_dict['half_caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 7
    if level == 7:

        if dnd_dict.character_dict['player_class']['paladin']['subclass'] == 'Oath of the Ancients':
            dnd_features.ancients_paladin7()

        if dnd_dict.character_dict['player_class']['paladin']['subclass'] == 'Oath of Devotion':
            dnd_features.devotion_paladin7()

        if dnd_dict.character_dict['player_class']['paladin']['subclass'] == 'Oath of Vengeance':
            dnd_features.vengeance_paladin7()

        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)
        dnd_dict.character_dict['half_caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 8
    if level == 8:

        dnd_level_up.asi_or_feat()
        dnd_fighting_styles.martial_versatility_style_paladin()
        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)
        dnd_dict.character_dict['half_caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 9
    if level == 9:

        if dnd_dict.character_dict['player_class']['paladin']['subclass'] == 'Oath of the Ancients':
            dnd_features.ancients_paladin9()

        if dnd_dict.character_dict['player_class']['paladin']['subclass'] == 'Oath of Devotion':
            dnd_features.devotion_paladin9()

        if dnd_dict.character_dict['player_class']['paladin']['subclass'] == 'Oath of Vengeance':
            dnd_features.vengeance_paladin9()

        dnd_dict.character_dict['d10'] += 1
        dnd_magic.paladin_third()
        dnd_level_up.level_up(10)
        dnd_dict.character_dict['half_caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 10
    if level == 10:

        dnd_features.paladin10()
        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)
        dnd_dict.character_dict['half_caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 11
    if level == 11:

        dnd_features.paladin11()
        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)
        dnd_dict.character_dict['half_caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 12
    if level == 12:

        dnd_level_up.asi_or_feat()
        dnd_fighting_styles.martial_versatility_style_paladin()
        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)
        dnd_dict.character_dict['half_caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 13
    if level == 13:

        if dnd_dict.character_dict['player_class']['paladin']['subclass'] == 'Oath of the Ancients':
            dnd_features.ancients_paladin13()

        if dnd_dict.character_dict['player_class']['paladin']['subclass'] == 'Oath of Devotion':
            dnd_features.devotion_paladin13()

        if dnd_dict.character_dict['player_class']['paladin']['subclass'] == 'Oath of Vengeance':
            dnd_features.vengeance_paladin13()

        dnd_magic.paladin_fourth()
        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)
        dnd_dict.character_dict['half_caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 14
    if level == 14:

        dnd_features.paladin14()
        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)
        dnd_dict.character_dict['half_caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 15
    if level == 15:

        if dnd_dict.character_dict['player_class']['paladin']['subclass'] == 'Oath of the Ancients':
            dnd_features.ancients_paladin15()

        if dnd_dict.character_dict['player_class']['paladin']['subclass'] == 'Oath of Devotion':
            dnd_features.devotion_paladin15()

        if dnd_dict.character_dict['player_class']['paladin']['subclass'] == 'Oath of Vengeance':
            dnd_features.vengeance_paladin15()

        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)
        dnd_dict.character_dict['half_caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 16
    if level == 16:

        dnd_level_up.asi_or_feat()
        dnd_fighting_styles.martial_versatility_style_paladin()
        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)
        dnd_dict.character_dict['half_caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 17
    if level == 17:

        if dnd_dict.character_dict['player_class']['paladin']['subclass'] == 'Oath of the Ancients':
            dnd_features.ancients_paladin17()

        if dnd_dict.character_dict['player_class']['paladin']['subclass'] == 'Oath of Devotion':
            dnd_features.devotion_paladin17()

        if dnd_dict.character_dict['player_class']['paladin']['subclass'] == 'Oath of Vengeance':
            dnd_features.vengeance_paladin17()

        dnd_magic.paladin_fifth()
        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)
        dnd_dict.character_dict['half_caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 18
    if level == 18:

        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)
        dnd_dict.character_dict['half_caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 19
    if level == 19:

        dnd_level_up.asi_or_feat()
        dnd_fighting_styles.martial_versatility_style_paladin()
        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)
        dnd_dict.character_dict['half_caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 20
    if level == 20:

        if dnd_dict.character_dict['player_class']['paladin']['subclass'] == 'Oath of the Ancients':
            dnd_features.ancients_paladin20()

        if dnd_dict.character_dict['player_class']['paladin']['subclass'] == 'Oath of Devotion':
            dnd_features.devotion_paladin20()

        if dnd_dict.character_dict['player_class']['paladin']['subclass'] == 'Oath of Vengeance':
            dnd_features.vengeance_paladin20()

        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)
        dnd_dict.character_dict['half_caster_level'] += 1
        dnd_skills.spell_slot_selection()
