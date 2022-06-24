import dnd_dict, dnd_features, dnd_magic, dnd_skills, dnd_level_up

def druid():
    level = dnd_dict.character_dict['player_class']['druid']['class_level']

# Level 1
    if level == 1:

        armor_prof = {'light_armor':'Light Armor','medoum_armor':'Medium Armor','shields':'Shields'}
        dnd_magic.druid_magic()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 2
    if level == 2:

        while True:
            choice = input("""Select your subclass:
1) Circle of the Land
2) Circle of the Moon
Enter your selection: """)
            if choice == '1':
                dnd_features.land_druid2()
                break

            elif choice == '2':
                dnd_features.moon_druid2()
                break

            else:
                print("Error: Invalid Input")
                continue

        dnd_features.druid2()
        spell_attack = ((dnd_dict.character_dict["Stats"]["wisdom"]['mod']) + dnd_dict.character_dict['prof_bonus'])
        dnd_dict.character_dict["spell_modifier"]['wisdom']['attack'] = spell_attack
        spell_save = ((dnd_dict.character_dict["Stats"]["wisdom"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
        dnd_dict.character_dict["spell_modifier"]['wisdom']['save'] = spell_save
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 3
    if level == 3:

        if dnd_dict.character_dict['player_class']['druid']['subclass'] == 'Circle of the Land':
            dnd_features.land_druid3()

        dnd_magic.druid_second()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 4
    if level == 4:

        dnd_level_up.asi_or_feat()
        dnd_features.cantrip_versatility(dnd_magic.druid_cantrip,dnd_dict.character_dict['spells'],dnd_dict.character_dict['class_spells']['druid_cantrips'])
        dnd_skills.spell_add(dnd_magic.druid_cantrip,dnd_dict.character_dict['spells'],dnd_dict.character_dict['class_spells']['druid_cantrips'])
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 5
    if level == 5:

        if dnd_dict.character_dict['player_class']['druid']['subclass'] == 'Circle of the Land':
            dnd_features.land_druid5()

        dnd_magic.druid_third()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 6
    if level == 6:

        if dnd_dict.character_dict['player_class']['druid']['subclass'] == 'Circle of the Land':
            dnd_features.land_druid6()

        if dnd_dict.character_dict['player_class']['druid']['subclass'] == 'Circle of the Moon':
            dnd_features.moon_druid6()

        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 7
    if level == 7:

        if dnd_dict.character_dict['player_class']['druid']['subclass'] == 'Circle of the Land':
            dnd_features.land_druid7()

        dnd_magic.druid_fourth()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 8
    if level == 8:

        dnd_level_up.asi_or_feat()
        dnd_features.cantrip_versatility(dnd_magic.druid_cantrip,dnd_dict.character_dict['spells'],dnd_dict.character_dict['class_spells']['druid_cantrips'])
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 9
    if level == 9:

        if dnd_dict.character_dict['player_class']['druid']['subclass'] == 'Circle of the Land':
            dnd_features.land_druid9()

        dnd_magic.druid_fifth()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 10
    if level == 10:

        if dnd_dict.character_dict['player_class']['druid']['subclass'] == 'Circle of the Land':
            dnd_features.land_druid10()

        if dnd_dict.character_dict['player_class']['druid']['subclass'] == 'Circle of the Moon':
            dnd_features.moon_druid10()

        dnd_skills.spell_add(dnd_magic.druid_cantrip,dnd_dict.character_dict['spells'],dnd_dict.character_dict['class_spells']['druid'])
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 11
    if level == 11:

        dnd_magic.druid_sixth()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 12
    if level == 12:

        dnd_level_up.asi_or_feat()
        dnd_features.cantrip_versatility(dnd_magic.druid_cantrip,dnd_dict.character_dict['spells'],dnd_dict.character_dict['class_spells']['druid_cantrips'])
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 13
    if level == 13:

        dnd_magic.druid_seventh()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 14
    if level == 14:

        if dnd_dict.character_dict['player_class']['druid']['subclass'] == 'Circle of the Land':
            dnd_features.land_druid14()

        if dnd_dict.character_dict['player_class']['druid']['subclass'] == 'Circle of the Moon':
            dnd_features.moon_druid14()

        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 15
    if level == 15:

        dnd_magic.druid_eighth()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 16
    if level == 16:

        dnd_level_up.asi_or_feat()
        dnd_features.cantrip_versatility(dnd_magic.druid_cantrip,dnd_dict.character_dict['spells'],dnd_dict.character_dict['class_spells']['druid_cantrips'])
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 17
    if level == 17:

        dnd_magic.druid_ninth()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 18
    if level == 18:

        dnd_features.druid18()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 19
    if level == 19:

        dnd_level_up.asi_or_feat()
        dnd_features.cantrip_versatility(dnd_magic.druid_cantrip,dnd_dict.character_dict['spells'],dnd_dict.character_dict['class_spells']['druid_cantrips'])
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 20
    if level == 20:

        dnd_features.druid20()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()
