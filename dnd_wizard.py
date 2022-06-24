import dnd_dict, dnd_features, dnd_magic, dnd_skills, dnd_level_up

def wizard():
    level = dnd_dict.character_dict['player_class']['wizard']['class_level']

# Level 1
    if level == 1:

        dnd_dict.character_dict['d6'] += 1
        dnd_features.wizard1()
        dnd_magic.wizard_magic()
        spell_attack = ((dnd_dict.character_dict["Stats"]["intelligence"]['mod']) + dnd_dict.character_dict['prof_bonus'])
        dnd_dict.character_dict["spell_modifier"]['intelligence']['attack'] = spell_attack
        spell_save = ((dnd_dict.character_dict["Stats"]["intelligence"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
        dnd_dict.character_dict["spell_modifier"]['intelligence']['save'] = spell_save
        dnd_level_up.level_up(6)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 2
    if level == 2:

        dnd_dict.character_dict['d6'] += 1
        dnd_features.wizard2()
        while True:
            choice = input("""Select the subclass you want to have:
1) School of Abjuration
2) School of Conjuration
3) School of Divination
4) School of Enchantment
5) School of Evocation
6) School of Illusion
7) School of Necromancy
8) School of Transmutation
Enter your selection: """)
            if choice == '1':
                dnd_dict.character_dict['player_class']['wizard']['subclass'] = 'School of Abjuration'
                dnd_features.abjuration_wizard2()
                break

            elif choice == '2':
                dnd_dict.character_dict['player_class']['wizard']['subclass'] = 'School of Conjuration'
                dnd_features.conjuration_wizard2()
                break

            elif choice == '3':
                dnd_dict.character_dict['player_class']['wizard']['subclass'] = 'School of Divination'
                dnd_features.divination_wizard2()
                break

            elif choice == '4':
                dnd_dict.character_dict['player_class']['wizard']['subclass'] = 'School of Enchantment'
                dnd_features.enchantment_wizard2()
                break

            elif choice == '5':
                dnd_dict.character_dict['player_class']['wizard']['subclass'] = 'School of Evocation'
                dnd_features.evocation_wizard2()
                break

            elif choice == '6':
                dnd_dict.character_dict['player_class']['wizard']['subclass'] = 'School of Illusion'
                dnd_features.illusion_wizard2()
                break

            elif choice == '7':
                dnd_dict.character_dict['player_class']['wizard']['subclass'] = 'School of Necromancy'
                dnd_features.necromancy_wizard2()
                break

            elif choice == '8':
                dnd_dict.character_dict['player_class']['wizard']['subclass'] = 'School of Transmutation'
                dnd_features.transmutation_wizard2()
                break

            else:
                print("Error: Invalid Input")
                continue

        dnd_magic.first_wizard_level_up()
        dnd_level_up.level_up(6)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 3
    if level == 3:

        dnd_dict.character_dict['d6'] += 1
        dnd_features.wizard3()
        dnd_magic.second_wizard_level_up()
        dnd_level_up.level_up(6)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 4
    if level == 4:

        dnd_level_up.asi_or_feat()
        dnd_dict.character_dict['d6'] += 1
        dnd_magic.wizard_cantrips()
        dnd_magic.second_wizard_level_up()
        dnd_level_up.level_up(6)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 5
    if level == 5:

        dnd_dict.character_dict['d6'] += 1
        dnd_magic.third_wizard_level_up()
        dnd_level_up.level_up(6)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 6
    if level == 6:

        dnd_dict.character_dict['d6'] += 1

        if dnd_dict.character_dict['player_class']['wizard']['subclass'] == 'School of Abjuration':
            dnd_features.abjuration_wizard6()

        if dnd_dict.character_dict['player_class']['wizard']['subclass'] == 'School of Conjuration':
            dnd_features.conjuration_wizard6()

        if dnd_dict.character_dict['player_class']['wizard']['subclass'] == 'School of Divination':
            dnd_features.divination_wizard6()

        if dnd_dict.character_dict['player_class']['wizard']['subclass'] == 'School of Enchantment':
            dnd_features.enchantment_wizard6()

        if dnd_dict.character_dict['player_class']['wizard']['subclass'] == 'School of Evocation':
            dnd_features.evocation_wizard6()

        if dnd_dict.character_dict['player_class']['wizard']['subclass'] == 'School of Illusion':
            dnd_features.illusion_wizard6()

        if dnd_dict.character_dict['player_class']['wizard']['subclass'] == 'School of Necromancy':
            dnd_features.necromancy_wizard6()

        if dnd_dict.character_dict['player_class']['wizard']['subclass'] == 'School of Transmutation':
            dnd_features.transmutation_wizard6()

        dnd_magic.third_wizard_level_up()
        dnd_level_up.level_up(6)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 7
    if level == 7:

        dnd_dict.character_dict['d6'] += 1
        dnd_magic.fourth_wizard_level_up()
        dnd_level_up.level_up(6)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 8
    if level == 8:

        dnd_level_up.asi_or_feat()
        dnd_dict.character_dict['d6'] += 1
        dnd_magic.fourth_wizard_level_up()
        dnd_level_up.level_up(6)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 9
    if level == 9:

        dnd_dict.character_dict['d6'] += 1
        dnd_magic.fifth_wizard_level_up()
        dnd_level_up.level_up(6)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 10
    if level == 10:

        dnd_dict.character_dict['d6'] += 1
        if dnd_dict.character_dict['player_class']['wizard']['subclass'] == 'School of Abjuration':
            dnd_features.abjuration_wizard10()

        if dnd_dict.character_dict['player_class']['wizard']['subclass'] == 'School of Conjuration':
            dnd_features.conjuration_wizard10()

        if dnd_dict.character_dict['player_class']['wizard']['subclass'] == 'School of Divination':
            dnd_features.divination_wizard10()

        if dnd_dict.character_dict['player_class']['wizard']['subclass'] == 'School of Enchantment':
            dnd_features.enchantment_wizard10()

        if dnd_dict.character_dict['player_class']['wizard']['subclass'] == 'School of Evocation':
            dnd_features.evocation_wizard10()

        if dnd_dict.character_dict['player_class']['wizard']['subclass'] == 'School of Illusion':
            dnd_features.illusion_wizard10()

        if dnd_dict.character_dict['player_class']['wizard']['subclass'] == 'School of Necromancy':
            dnd_features.necromancy_wizard10()

        if dnd_dict.character_dict['player_class']['wizard']['subclass'] == 'School of Transmutation':
            dnd_features.transmutation_wizard10()

        dnd_magic.wizard_cantrips()
        dnd_magic.fifth_wizard_level_up()
        dnd_level_up.level_up(6)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 11
    if level == 11:

        dnd_dict.character_dict['d6'] += 1
        dnd_magic.sixth_wizard_level_up()
        dnd_level_up.level_up(6)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 12
    if level == 12:

        dnd_level_up.asi_or_feat()
        dnd_magic.sixth_wizard_level_up()
        dnd_dict.character_dict['d6'] += 1
        dnd_level_up.level_up(6)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 13
    if level == 13:

        dnd_dict.character_dict['d6'] += 1
        dnd_magic.seventh_wizard_level_up()
        dnd_level_up.level_up(6)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 14
    if level == 14:

        dnd_dict.character_dict['d6'] += 1

        if dnd_dict.character_dict['player_class']['wizard']['subclass'] == 'School of Abjuration':
            dnd_features.abjuration_wizard14()

        if dnd_dict.character_dict['player_class']['wizard']['subclass'] == 'School of Conjuration':
            dnd_features.conjuration_wizard14()

        if dnd_dict.character_dict['player_class']['wizard']['subclass'] == 'School of Divination':
            dnd_features.divination_wizard14()

        if dnd_dict.character_dict['player_class']['wizard']['subclass'] == 'School of Enchantment':
            dnd_features.enchantment_wizard14()

        if dnd_dict.character_dict['player_class']['wizard']['subclass'] == 'School of Evocation':
            dnd_features.evocation_wizard14()

        if dnd_dict.character_dict['player_class']['wizard']['subclass'] == 'School of Illusion':
            dnd_features.illusion_wizard14()

        if dnd_dict.character_dict['player_class']['wizard']['subclass'] == 'School of Necromancy':
            dnd_features.necromancy_wizard14()

        if dnd_dict.character_dict['player_class']['wizard']['subclass'] == 'School of Transmutation':
            dnd_features.transmutation_wizard14()


        dnd_magic.seventh_wizard_level_up()
        dnd_level_up.level_up(6)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 15
    if level == 15:

        dnd_dict.character_dict['d6'] += 1
        dnd_magic.eighth_wizard_level_up()
        dnd_level_up.level_up(6)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 16
    if level == 16:

        dnd_level_up.asi_or_feat()
        dnd_dict.character_dict['d6'] += 1
        dnd_magic.eighth_wizard_level_up()
        dnd_level_up.level_up(6)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 17
    if level == 17:

        dnd_dict.character_dict['d6'] += 1
        dnd_magic.ninth_wizard_level_up()
        dnd_level_up.level_up(6)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 18
    if level == 18:

        dnd_dict.character_dict['d6'] += 1
        dnd_features.wizard18()
        dnd_magic.ninth_wizard_level_up()
        dnd_level_up.level_up(6)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 19
    if level == 19:

        dnd_level_up.asi_or_feat()
        dnd_dict.character_dict['d6'] += 1
        dnd_magic.ninth_wizard_level_up()
        dnd_level_up.level_up(6)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 20
    if level == 20:

        dnd_dict.character_dict['d6'] += 1
        dnd_features.wizard20()
        dnd_magic.ninth_wizard_level_up()
        dnd_level_up.level_up(6)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()
