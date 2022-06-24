import dnd_dict, dnd_features, dnd_magic, dnd_skills, dnd_level_up


def fighter():
    level = dnd_dict.character_dict['player_class']['fighter']['class_level']

# Level 1
    if level == 1:

        armor_prof = {'light_armor':'Light Armor','medium_armor':'Medium Armor','heavy_armor':'Heavy Armor','shields':'Shields'}
        weapon_prof = {'simple_weapons':'Simple Weapons','martial_weapons':'Martial Weapons'}
        dnd_dict.character_dict['Armor_Prof'].update(armor_prof)
        dnd_dict.character_dict['Weapon_Prof'].update(weapon_prof)
        dnd_features.fighter1()
        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)

# Level 2
    if level == 2:

        dnd_features.fighter2()
        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)

# Level 3
    if level == 3:

        while True:
            choice = input("""Select the subclass you want to have:
1) Battle Master
2) Champion
3) Eldritch Knight
Enter your selection: """)
            if choice == '1':
                dnd_dict.character_dict['player_class']['fighter']['subclass'] = 'Battle Master'
                dnd_features.battle_master3()
                break

            elif choice == '2':
                dnd_dict.character_dict['player_class']['fighter']['subclass'] = 'Champion'
                dnd_features.champion3()
                break

            elif choice == '3':
                dnd_dict.character_dict['player_class']['fighter']['subclass'] = 'Eldritch Knight'
                dnd_features.eldritch_knight3()
                break

        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)

# Level 4
    if level == 4:

        dnd_level_up.asi_or_feat()
        if dnd_dict.character_dict['player_class']['fighter']['subclass'] == 'Eldritch Knight':
            dnd_skills.first_swap(dnd_magic.eldritch_knight_first,dnd_dict.character_dict['class_spells']['fighter']['first'])
            dnd_skills.spell_add(dnd_magic.eldritch_knight_first,dnd_dict.character_dict['spells']['first'],dnd_dict.character_dict['class_spells']['fighter'])
            dnd_dict.character_dict['semi_caster_level'] += 1
            dnd_skills.spell_slot_selection()
        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)

# Level 5
    if level == 5:

        dnd_features.fighter5()
        if dnd_dict.character_dict['player_class']['fighter']['subclass'] == 'Eldritch Knight':
            dnd_skills.first_swap(dnd_magic.eldritch_knight_first,dnd_dict.character_dict['class_spells']['fighter']['first'])

            dnd_dict.character_dict['semi_caster_level'] += 1
            dnd_skills.spell_slot_selection()
        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)

# Level 6
    if level == 6:

        dnd_level_up.asi_or_feat()
        if dnd_dict.character_dict['player_class']['fighter']['subclass'] == 'Eldritch Knight':
            dnd_skills.first_swap(dnd_magic.eldritch_knight_first,dnd_dict.character_dict['class_spells']['fighter']['first'])
            dnd_dict.character_dict['semi_caster_level'] += 1
            dnd_skills.spell_slot_selection()
        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)

# Level 7
    if level == 7:

        if dnd_dict.character_dict['player_class']['fighter']['subclass'] == 'Battle Master':
            dnd_features.battle_master7()

        if dnd_dict.character_dict['player_class']['fighter']['subclass'] == 'Champion':
            dnd_features.champion7()

        if dnd_dict.character_dict['player_class']['fighter']['subclass'] == 'Eldritch Knight':
            dnd_features.eldritch_knight7()
            dnd_skills.first_swap(dnd_magic.eldritch_knight_first,dnd_dict.character_dict['class_spells']['fighter']['first'])
            dnd_skills.second_level(dnd_magic.eldritch_knight_first,dnd_magic.eldritch_knight_second,dnd_dict.character_dict['class_spells']['fighter']['first'],dnd_dict.character_dict['class_spells']['fighter']['second'])
            dnd_dict.character_dict['semi_caster_level'] += 2
            dnd_skills.spell_slot_selection()

        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)

# Level 8
    if level == 8:

        dnd_level_up.asi_or_feat()
        if dnd_dict.character_dict['player_class']['fighter']['subclass'] == 'Eldritch Knight':
            dnd_features.fighter_spell_swap_second()
            dnd_skills.second_swap(dnd_magic.eldritch_knight_first,dnd_magic.eldritch_knight_second,dnd_dict.character_dict['class_spells']['fighter']['first'],dnd_dict.character_dict['class_spells']['fighter']['second'])
            dnd_skills.second_level(dnd_magic.wizard_first,dnd_magic.wizard_second,dnd_dict.character_dict['class_spells']['fighter_special']['first'],dnd_dict.character_dict['class_spells']['fighter_special']['second'])
            dnd_dict.character_dict['semi_caster_level'] += 1
            dnd_skills.spell_slot_selection()
        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)

# Level 9
    if level == 9:

        dnd_features.fighter9()
        if dnd_dict.character_dict['player_class']['fighter']['subclass'] == 'Eldritch Knight':
            dnd_features.fighter_spell_swap_second()
            dnd_dict.character_dict['semi_caster_level'] += 1
            dnd_skills.spell_slot_selection()
        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)

# Level 10
    if level == 10:

        if dnd_dict.character_dict['player_class']['fighter']['subclass'] == 'Battle Master':
            dnd_features.battle_master10()

        if dnd_dict.character_dict['player_class']['fighter']['subclass'] == 'Champion':
            dnd_features.champion10()

        if dnd_dict.character_dict['player_class']['fighter']['subclass'] == 'Eldritch Knight':
            dnd_features.eldritch_knight10()
            dnd_features.fighter_spell_swap_second()
            dnd_skills.spell_add(dnd_magic.wizard_cantrip,dnd_dict.character_dict['spells']['cantrips'],dnd_dict.character_dict['class_spells']['fighter_cantrips'])
            dnd_skills.second_level(dnd_magic.eldritch_knight_first,dnd_magic.eldritch_knight_second,dnd_dict.character_dict['class_spells']['fighter']['first'],dnd_dict.character_dict['class_spells']['fighter']['second'])
            dnd_dict.character_dict['semi_caster_level'] += 1
            dnd_skills.spell_slot_selection()

        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)

# Level 11
    if level == 11:

        if dnd_dict.character_dict['player_class']['fighter']['subclass'] == 'Eldritch Knight':
            dnd_features.fighter_spell_swap_second()
            dnd_skills.second_level(dnd_magic.eldritch_knight_first,dnd_magic.eldritch_knight_second,dnd_dict.character_dict['class_spells']['fighter']['first'],dnd_dict.character_dict['class_spells']['fighter']['second'])
            dnd_dict.character_dict['semi_caster_level'] += 1
            dnd_skills.spell_slot_selection()
        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)

# Level 12
    if level == 12:

        dnd_level_up.asi_or_feat()
        if dnd_dict.character_dict['player_class']['fighter']['subclass'] == 'Eldritch Knight':
            dnd_features.fighter_spell_swap_second()
            dnd_dict.character_dict['semi_caster_level'] += 1
            dnd_skills.spell_slot_selection()
        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)

# Level 13
    if level == 13:

        if dnd_dict.character_dict['player_class']['fighter']['subclass'] == 'Eldritch Knight':
            dnd_features.fighter_spell_swap_second()
            dnd_skills.third_level(dnd_magic.eldritch_knight_first,dnd_magic.eldritch_knight_second,dnd_magic.eldritch_knight_third,dnd_dict.character_dict['class_spells']['fighter']['first'],dnd_dict.character_dict['class_spells']['fighter']['second'],dnd_dict.character_dict['class_spells']['fighter']['third'])
            dnd_dict.character_dict['semi_caster_level'] += 1
            dnd_skills.spell_slot_selection()
        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)

# Level 14
    if level == 14:

        dnd_level_up.asi_or_feat()
        if dnd_dict.character_dict['player_class']['fighter']['subclass'] == 'Eldritch Knight':
            dnd_features.fighter_spell_swap_third_early()
            dnd_skills.third_level(dnd_magic.wizard_first,dnd_magic.wizard_second,dnd_magic.wizard_third,dnd_dict.character_dict['class_spells']['fighter_special']['first'],dnd_dict.character_dict['class_spells']['fighter_special']['second'],dnd_dict.character_dict['class_spells']['fighter']['third'])

            dnd_dict.character_dict['semi_caster_level'] += 1
            dnd_skills.spell_slot_selection()
        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)

# Level 15
    if level == 15:

        if dnd_dict.character_dict['player_class']['fighter']['subclass'] == 'Battle Master':
            dnd_features.battle_master15()

        if dnd_dict.character_dict['player_class']['fighter']['subclass'] == 'Champion':
            dnd_features.champion15()

        if dnd_dict.character_dict['player_class']['fighter']['subclass'] == 'Eldritch Knight':
            dnd_features.eldritch_knight15()
            dnd_features.fighter_spell_swap_third()
            dnd_dict.character_dict['semi_caster_level'] += 1
            dnd_skills.spell_slot_selection()

        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)

# Level 16
    if level == 16:

        dnd_level_up.asi_or_feat()
        if dnd_dict.character_dict['player_class']['fighter']['subclass'] == 'Eldritch Knight':
            dnd_features.fighter_spell_swap_third()
            dnd_skills.third_level(dnd_magic.eldritch_knight_first,dnd_magic.eldritch_knight_second,dnd_magic.eldritch_knight_third,dnd_dict.character_dict['class_spells']['fighter']['first'],dnd_dict.character_dict['class_spells']['fighter']['second'],dnd_dict.character_dict['class_spells']['fighter']['third'])
            dnd_dict.character_dict['semi_caster_level'] += 1
            dnd_skills.spell_slot_selection()
        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)

# Level 17
    if level == 17:

        if dnd_dict.character_dict['player_class']['fighter']['subclass'] == 'Eldritch Knight':
            dnd_features.fighter_spell_swap_third()
            dnd_dict.character_dict['semi_caster_level'] += 1
            dnd_skills.spell_slot_selection()
        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)

# Level 18
    if level == 18:

        if dnd_dict.character_dict['player_class']['fighter']['subclass'] == 'Battle Master':
            dnd_features.battle_master18()

        if dnd_dict.character_dict['player_class']['fighter']['subclass'] == 'Champion':
            dnd_features.champion18()

        if dnd_dict.character_dict['player_class']['fighter']['subclass'] == 'Eldritch Knight':
            dnd_features.eldritch_knight18()
            dnd_features.fighter_spell_swap_third()
            dnd_dict.character_dict['semi_caster_level'] += 1
            dnd_skills.spell_slot_selection()

        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)

# Level 19
    if level == 19:

        dnd_level_up.asi_or_feat()
        if dnd_dict.character_dict['player_class']['fighter']['subclass'] == 'Eldritch Knight':
            dnd_features.fighter_spell_swap_third()
            dnd_skills.fourth_level(dnd_magic.eldritch_knight_first,dnd_magic.eldritch_knight_second,dnd_magic.eldritch_knight_third,dnd_magic.eldritch_knight_fourth,dnd_dict.character_dict['class_spells']['fighter']['first'],dnd_dict.character_dict['class_spells']['fighter']['second'],dnd_dict.character_dict['class_spells']['fighter']['third'],dnd_dict.character_dict['class_spells']['fighter']['fourth'])
            dnd_dict.character_dict['semi_caster_level'] += 1
            dnd_skills.spell_slot_selection()
        dnd_dict.character_dict['d10'] += 1
        print(dnd_dict.character_dict['semi_caster_level'])
        dnd_level_up.level_up(10)

# Level 20
    if level == 20:

        if dnd_dict.character_dict['player_class']['fighter']['subclass'] == 'Eldritch Knight':
            dnd_features.fighter_spell_swap_fourth()
            dnd_skills.fourth_level(dnd_magic.wizard_first,dnd_magic.wizard_second,dnd_magic.wizard_third,dnd_magic.wizard_fourth,dnd_dict.character_dict['class_spells']['fighter_special']['first'],dnd_dict.character_dict['class_spells']['fighter_special']['second'],dnd_dict.character_dict['class_spells']['fighter_special']['third'],dnd_dict.character_dict['class_spells']['fighter_special']['fourth'])
            dnd_dict.character_dict['semi_caster_level'] += 1
            dnd_skills.spell_slot_selection()
        dnd_dict.character_dict['d10'] += 2
        dnd_level_up.level_up(10)
