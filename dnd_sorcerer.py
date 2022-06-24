import dnd_dict,dnd_features, dnd_magic, dnd_skills, dnd_level_up, dnd_metamagic


def sorcerer():
    level = dnd_dict.character_dict['player_class']['sorcerer']['class_level']

# Level 1
    if level == 1:

# Choose the subclass
        while True:
            subclass_choice = input("""Select your Sorcerous Origin:
1) Draconic Bloodline
2) Wild Magic
Enter your Selection: """)
            if subclass_choice=='1':
                dnd_features.draconic_sorcerer1()
                dnd_dict.character_dict['player_class']['sorcerer']['subclass'] = 'Draconic Bloodline'
#Armor Class = 13 + Dex mod because of DB feature
                AC= (13 + dnd_dict.character_dict['Stats']['dexterity']['mod'])
                print("Draconic Bloodline Armor Class: ",AC)
                dnd_dict.character_dict["sorcerer_armor_class"] = AC
                break
            elif subclass_choice=='2':
                dnd_features.wild_magic_sorcerer1()
                dnd_dict.character_dict['player_class']['sorcerer']['subclass'] = 'Wild Magic'
                break

            else:
                print("Invalid Selection")
                continue

        dnd_magic.sorcerer_magic()
        spell_attack = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'])
        dnd_dict.character_dict["spell_modifier"]['charisma']['attack'] = spell_attack
        spell_save = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
        dnd_dict.character_dict["spell_modifier"]['charisma']['save'] = spell_save
        dnd_dict.character_dict['d6'] += 1
        dnd_level_up.level_up(6)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 2
    if level == 2:

        dnd_features.sorcerer2()
        dnd_skills.spell_add(dnd_magic.sorcerer_first,dnd_dict.character_dict['spells']['first'],dnd_dict.character_dict['class_spells']['sorcerer'])
        dnd_skills.first_swap(dnd_magic.sorcerer_first,dnd_dict.character_dict['class_spells']['sorcerer']['first'])
        dnd_dict.character_dict['d6'] += 1
        dnd_level_up.level_up(6)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 3
    if level == 3:

        dnd_features.sorcerer3()
        dnd_skills.second_level(dnd_magic.sorcerer_first,dnd_magic.sorcerer_second,dnd_dict.character_dict['class_spells']['sorcerer']['first'],dnd_dict.character_dict['class_spells']['sorcerer']['second'])
        dnd_skills.second_swap(dnd_magic.sorcerer_first,dnd_magic.sorcerer_second,dnd_dict.character_dict['class_spells']['sorcerer']['first'],dnd_dict.character_dict['class_spells']['sorcerer']['second'])
        dnd_dict.character_dict['d6'] += 1
        dnd_level_up.level_up(6)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 4
    if level == 4:

        dnd_level_up.asi_or_feat()
        dnd_features.sorcerous_versatility()
        dnd_skills.spell_add(dnd_magic.sorcerer_cantrip,dnd_dict.character_dict['spells']['cantrips'],dnd_dict.character_dict['class_spells']['sorcerer_cantrips'])
        dnd_skills.second_level(dnd_magic.sorcerer_first,dnd_magic.sorcerer_second,dnd_dict.character_dict['class_spells']['sorcerer']['first'],dnd_dict.character_dict['class_spells']['sorcerer']['second'])
        dnd_skills.second_swap(dnd_magic.sorcerer_first,dnd_magic.sorcerer_second,dnd_dict.character_dict['class_spells']['sorcerer']['first'],dnd_dict.character_dict['class_spells']['sorcerer']['second'])
        dnd_dict.character_dict['d6'] += 1
        dnd_level_up.level_up(6)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 5
    if level == 5:

        dnd_features.sorcerer5()
        dnd_skills.third_level(dnd_magic.sorcerer_first,dnd_magic.sorcerer_second,dnd_magic.sorcerer_third,dnd_dict.character_dict['class_spells']['sorcerer']['first'],dnd_dict.character_dict['class_spells']['sorcerer']['second'],dnd_dict.character_dict['class_spells']['sorcerer']['third'])
        dnd_skills.third_swap(dnd_magic.sorcerer_first,dnd_magic.sorcerer_second,dnd_magic.sorcerer_third,dnd_dict.character_dict['class_spells']['sorcerer']['first'],dnd_dict.character_dict['class_spells']['sorcerer']['second'],dnd_dict.character_dict['class_spells']['sorcerer']['third'])
        dnd_dict.character_dict['d6'] += 1
        dnd_level_up.level_up(6)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 6
    if level == 6:
        if dnd_dict.character_dict['player_class']['sorcerer']['subclass'] == 'Draconic Bloodline':
            dnd_features.draconic_sorcerer6()

        if dnd_dict.character_dict['player_class']['sorcerer']['subclass'] == 'Wild Magic':
            dnd_features.wild_magic_sorcerer6()

        dnd_skills.third_level(dnd_magic.sorcerer_first,dnd_magic.sorcerer_second,dnd_magic.sorcerer_third,dnd_dict.character_dict['class_spells']['sorcerer']['first'],dnd_dict.character_dict['class_spells']['sorcerer']['second'],dnd_dict.character_dict['class_spells']['sorcerer']['third'])
        dnd_skills.third_swap(dnd_magic.sorcerer_first,dnd_magic.sorcerer_second,dnd_magic.sorcerer_third,dnd_dict.character_dict['class_spells']['sorcerer']['first'],dnd_dict.character_dict['class_spells']['sorcerer']['second'],dnd_dict.character_dict['class_spells']['sorcerer']['third'])
        dnd_dict.character_dict['d6'] += 1
        dnd_level_up.level_up(6)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 7
    if level == 7:

        dnd_skills.fourth_level(dnd_magic.sorcerer_first,dnd_magic.sorcerer_second,dnd_magic.sorcerer_third,dnd_magic.sorcerer_fourth,dnd_dict.character_dict['class_spells']['sorcerer']['first'],dnd_dict.character_dict['class_spells']['sorcerer']['second'],dnd_dict.character_dict['class_spells']['sorcerer']['third'],dnd_dict.character_dict['class_spells']['sorcerer']['fourth'])
        dnd_skills.fourth_swap(dnd_magic.sorcerer_first,dnd_magic.sorcerer_second,dnd_magic.sorcerer_third,dnd_magic.sorcerer_fourth,dnd_dict.character_dict['class_spells']['sorcerer']['first'],dnd_dict.character_dict['class_spells']['sorcerer']['second'],dnd_dict.character_dict['class_spells']['sorcerer']['third'],dnd_dict.character_dict['class_spells']['sorcerer']['fourth'])
        dnd_dict.character_dict['d6'] += 1
        dnd_level_up.level_up(6)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 8
    if level == 8:

        dnd_level_up.asi_or_feat()
        dnd_skills.fourth_level(dnd_magic.sorcerer_first,dnd_magic.sorcerer_second,dnd_magic.sorcerer_third,dnd_magic.sorcerer_fourth,dnd_dict.character_dict['class_spells']['sorcerer']['first'],dnd_dict.character_dict['class_spells']['sorcerer']['second'],dnd_dict.character_dict['class_spells']['sorcerer']['third'],dnd_dict.character_dict['class_spells']['sorcerer']['fourth'])
        dnd_skills.fourth_swap(dnd_magic.sorcerer_first,dnd_magic.sorcerer_second,dnd_magic.sorcerer_third,dnd_magic.sorcerer_fourth,dnd_dict.character_dict['class_spells']['sorcerer']['first'],dnd_dict.character_dict['class_spells']['sorcerer']['second'],dnd_dict.character_dict['class_spells']['sorcerer']['third'],dnd_dict.character_dict['class_spells']['sorcerer']['fourth'])
        dnd_features.sorcerous_versatility()
        dnd_dict.character_dict['d6'] += 1
        dnd_level_up.level_up(6)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 9
    if level == 9:

        dnd_skills.fifth_level(dnd_magic.sorcerer_first,dnd_magic.sorcerer_second,dnd_magic.sorcerer_third,dnd_magic.sorcerer_fourth,dnd_magic.sorcerer_fifth,dnd_dict.character_dict['class_spells']['sorcerer']['first'],dnd_dict.character_dict['class_spells']['sorcerer']['second'],dnd_dict.character_dict['class_spells']['sorcerer']['third'],dnd_dict.character_dict['class_spells']['sorcerer']['fourth'],dnd_dict.character_dict['class_spells']['sorcerer']['fifth'])
        dnd_skills.fifth_swap(dnd_magic.sorcerer_first,dnd_magic.sorcerer_second,dnd_magic.sorcerer_third,dnd_magic.sorcerer_fourth,dnd_magic.sorcerer_fifth,dnd_dict.character_dict['class_spells']['sorcerer']['first'],dnd_dict.character_dict['class_spells']['sorcerer']['second'],dnd_dict.character_dict['class_spells']['sorcerer']['third'],dnd_dict.character_dict['class_spells']['sorcerer']['fourth'],dnd_dict.character_dict['class_spells']['sorcerer']['fifth'])
        dnd_dict.character_dict['d6'] += 1
        dnd_level_up.level_up(6)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 10
    if level == 10:

        dnd_features.sorcerer10()
        dnd_skills.spell_add(dnd_magic.sorcerer_cantrip,dnd_dict.character_dict['spells']['cantrips'],dnd_dict.character_dict['class_spells']['sorcerer_cantrips'])
        dnd_skills.fifth_level(dnd_magic.sorcerer_first,dnd_magic.sorcerer_second,dnd_magic.sorcerer_third,dnd_magic.sorcerer_fourth,dnd_magic.sorcerer_fifth,dnd_dict.character_dict['class_spells']['sorcerer']['first'],dnd_dict.character_dict['class_spells']['sorcerer']['second'],dnd_dict.character_dict['class_spells']['sorcerer']['third'],dnd_dict.character_dict['class_spells']['sorcerer']['fourth'],dnd_dict.character_dict['class_spells']['sorcerer']['fifth'])
        dnd_skills.fifth_swap(dnd_magic.sorcerer_first,dnd_magic.sorcerer_second,dnd_magic.sorcerer_third,dnd_magic.sorcerer_fourth,dnd_magic.sorcerer_fifth,dnd_dict.character_dict['class_spells']['sorcerer']['first'],dnd_dict.character_dict['class_spells']['sorcerer']['second'],dnd_dict.character_dict['class_spells']['sorcerer']['third'],dnd_dict.character_dict['class_spells']['sorcerer']['fourth'],dnd_dict.character_dict['class_spells']['sorcerer']['fifth'])
        dnd_dict.character_dict['d6'] += 1
        dnd_level_up.level_up(6)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 11
    if level == 11:

        dnd_skills.sixth_level(dnd_magic.sorcerer_first,dnd_magic.sorcerer_second,dnd_magic.sorcerer_third,dnd_magic.sorcerer_fourth,dnd_magic.sorcerer_fifth,dnd_magic.sorcerer_sixth,dnd_dict.character_dict['class_spells']['sorcerer']['first'],dnd_dict.character_dict['class_spells']['sorcerer']['second'],dnd_dict.character_dict['class_spells']['sorcerer']['third'],dnd_dict.character_dict['class_spells']['sorcerer']['fourth'],dnd_dict.character_dict['class_spells']['sorcerer']['fifth'],dnd_dict.character_dict['class_spells']['sorcerer']['sixth'])
        dnd_skills.sixth_swap(dnd_magic.sorcerer_first,dnd_magic.sorcerer_second,dnd_magic.sorcerer_third,dnd_magic.sorcerer_fourth,dnd_magic.sorcerer_fifth,dnd_magic.sorcerer_sixth,dnd_dict.character_dict['class_spells']['sorcerer']['first'],dnd_dict.character_dict['class_spells']['sorcerer']['second'],dnd_dict.character_dict['class_spells']['sorcerer']['third'],dnd_dict.character_dict['class_spells']['sorcerer']['fourth'],dnd_dict.character_dict['class_spells']['sorcerer']['fifth'],dnd_dict.character_dict['class_spells']['sorcerer']['sixth'])
        dnd_dict.character_dict['d6'] += 1
        dnd_level_up.level_up(6)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 12
    if level == 12:

        dnd_level_up.asi_or_feat()
        dnd_features.sorcerous_versatility()
        dnd_skills.sixth_swap(dnd_magic.sorcerer_first,dnd_magic.sorcerer_second,dnd_magic.sorcerer_third,dnd_magic.sorcerer_fourth,dnd_magic.sorcerer_fifth,dnd_magic.sorcerer_sixth,dnd_dict.character_dict['class_spells']['sorcerer']['first'],dnd_dict.character_dict['class_spells']['sorcerer']['second'],dnd_dict.character_dict['class_spells']['sorcerer']['third'],dnd_dict.character_dict['class_spells']['sorcerer']['fourth'],dnd_dict.character_dict['class_spells']['sorcerer']['fifth'],dnd_dict.character_dict['class_spells']['sorcerer']['sixth'])
        dnd_dict.character_dict['d6'] += 1
        dnd_level_up.level_up(6)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 13
    if level == 13:

        dnd_skills.seventh_level(dnd_magic.sorcerer_first,dnd_magic.sorcerer_second,dnd_magic.sorcerer_third,dnd_magic.sorcerer_fourth,dnd_magic.sorcerer_fifth,dnd_magic.sorcerer_sixth,dnd_magic.sorcerer_seventh,dnd_dict.character_dict['class_spells']['sorcerer']['first'],dnd_dict.character_dict['class_spells']['sorcerer']['second'],dnd_dict.character_dict['class_spells']['sorcerer']['third'],dnd_dict.character_dict['class_spells']['sorcerer']['fourth'],dnd_dict.character_dict['class_spells']['sorcerer']['fifth'],dnd_dict.character_dict['class_spells']['sorcerer']['sixth'],dnd_dict.character_dict['class_spells']['sorcerer']['seventh'])
        dnd_skills.seventh_swap(dnd_magic.sorcerer_first,dnd_magic.sorcerer_second,dnd_magic.sorcerer_third,dnd_magic.sorcerer_fourth,dnd_magic.sorcerer_fifth,dnd_magic.sorcerer_sixth,dnd_magic.sorcerer_seventh,dnd_dict.character_dict['class_spells']['sorcerer']['first'],dnd_dict.character_dict['class_spells']['sorcerer']['second'],dnd_dict.character_dict['class_spells']['sorcerer']['third'],dnd_dict.character_dict['class_spells']['sorcerer']['fourth'],dnd_dict.character_dict['class_spells']['sorcerer']['fifth'],dnd_dict.character_dict['class_spells']['sorcerer']['sixth'],dnd_dict.character_dict['class_spells']['sorcerer']['seventh'])
        dnd_dict.character_dict['d6'] += 1
        dnd_level_up.level_up(6)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 14
    if level == 14:

        if dnd_dict.character_dict['player_class']['sorcerer']['subclass'] == 'Draconic Bloodline':
            dnd_features.draconic_sorcerer14()

        if dnd_dict.character_dict['player_class']['sorcerer']['subclass'] == 'Wild Magic':
            dnd_features.wild_magic_sorcerer14()

        dnd_skills.seventh_swap(dnd_magic.sorcerer_first,dnd_magic.sorcerer_second,dnd_magic.sorcerer_third,dnd_magic.sorcerer_fourth,dnd_magic.sorcerer_fifth,dnd_magic.sorcerer_sixth,dnd_magic.sorcerer_seventh,dnd_dict.character_dict['class_spells']['sorcerer']['first'],dnd_dict.character_dict['class_spells']['sorcerer']['second'],dnd_dict.character_dict['class_spells']['sorcerer']['third'],dnd_dict.character_dict['class_spells']['sorcerer']['fourth'],dnd_dict.character_dict['class_spells']['sorcerer']['fifth'],dnd_dict.character_dict['class_spells']['sorcerer']['sixth'],dnd_dict.character_dict['class_spells']['sorcerer']['seventh'])
        dnd_dict.character_dict['d6'] += 1
        dnd_level_up.level_up(6)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 15
    if level == 15:

        dnd_skills.eighth_level(dnd_magic.sorcerer_first,dnd_magic.sorcerer_second,dnd_magic.sorcerer_third,dnd_magic.sorcerer_fourth,dnd_magic.sorcerer_fifth,dnd_magic.sorcerer_sixth,dnd_magic.sorcerer_seventh,dnd_magic.sorcerer_eighth,dnd_dict.character_dict['class_spells']['sorcerer']['first'],dnd_dict.character_dict['class_spells']['sorcerer']['second'],dnd_dict.character_dict['class_spells']['sorcerer']['third'],dnd_dict.character_dict['class_spells']['sorcerer']['fourth'],dnd_dict.character_dict['class_spells']['sorcerer']['fifth'],dnd_dict.character_dict['class_spells']['sorcerer']['sixth'],dnd_dict.character_dict['class_spells']['sorcerer']['seventh'],dnd_dict.character_dict['class_spells']['sorcerer']['eighth'])
        dnd_skills.eighth_swap(dnd_magic.sorcerer_first,dnd_magic.sorcerer_second,dnd_magic.sorcerer_third,dnd_magic.sorcerer_fourth,dnd_magic.sorcerer_fifth,dnd_magic.sorcerer_sixth,dnd_magic.sorcerer_seventh,dnd_magic.sorcerer_eighth,dnd_dict.character_dict['class_spells']['sorcerer']['first'],dnd_dict.character_dict['class_spells']['sorcerer']['second'],dnd_dict.character_dict['class_spells']['sorcerer']['third'],dnd_dict.character_dict['class_spells']['sorcerer']['fourth'],dnd_dict.character_dict['class_spells']['sorcerer']['fifth'],dnd_dict.character_dict['class_spells']['sorcerer']['sixth'],dnd_dict.character_dict['class_spells']['sorcerer']['seventh'],dnd_dict.character_dict['class_spells']['sorcerer']['eighth'])
        dnd_dict.character_dict['d6'] += 1
        dnd_level_up.level_up(6)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 16
    if level == 16:

        dnd_level_up.asi_or_feat()
        dnd_features.sorcerous_versatility()
        dnd_skills.eighth_swap(dnd_magic.sorcerer_first,dnd_magic.sorcerer_second,dnd_magic.sorcerer_third,dnd_magic.sorcerer_fourth,dnd_magic.sorcerer_fifth,dnd_magic.sorcerer_sixth,dnd_magic.sorcerer_seventh,dnd_magic.sorcerer_eighth,dnd_dict.character_dict['class_spells']['sorcerer']['first'],dnd_dict.character_dict['class_spells']['sorcerer']['second'],dnd_dict.character_dict['class_spells']['sorcerer']['third'],dnd_dict.character_dict['class_spells']['sorcerer']['fourth'],dnd_dict.character_dict['class_spells']['sorcerer']['fifth'],dnd_dict.character_dict['class_spells']['sorcerer']['sixth'],dnd_dict.character_dict['class_spells']['sorcerer']['seventh'],dnd_dict.character_dict['class_spells']['sorcerer']['eighth'])
        dnd_dict.character_dict['d6'] += 1
        dnd_level_up.level_up(6)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 17
    if level == 17:

        dnd_features.sorcerer10()
        dnd_skills.ninth_level(dnd_magic.sorcerer_first,dnd_magic.sorcerer_second,dnd_magic.sorcerer_third,dnd_magic.sorcerer_fourth,dnd_magic.sorcerer_fifth,dnd_magic.sorcerer_sixth,dnd_magic.sorcerer_seventh,dnd_magic.sorcerer_eighth,dnd_magic.sorcerer_ninth,dnd_dict.character_dict['class_spells']['sorcerer']['first'],dnd_dict.character_dict['class_spells']['sorcerer']['second'],dnd_dict.character_dict['class_spells']['sorcerer']['third'],dnd_dict.character_dict['class_spells']['sorcerer']['fourth'],dnd_dict.character_dict['class_spells']['sorcerer']['fifth'],dnd_dict.character_dict['class_spells']['sorcerer']['sixth'],dnd_dict.character_dict['class_spells']['sorcerer']['seventh'],dnd_dict.character_dict['class_spells']['sorcerer']['eighth'],dnd_dict.character_dict['class_spells']['sorcerer']['ninth'])
        dnd_skills.ninth_swap(dnd_magic.sorcerer_first,dnd_magic.sorcerer_second,dnd_magic.sorcerer_third,dnd_magic.sorcerer_fourth,dnd_magic.sorcerer_fifth,dnd_magic.sorcerer_sixth,dnd_magic.sorcerer_seventh,dnd_magic.sorcerer_eighth,dnd_magic.sorcerer_ninth,dnd_dict.character_dict['class_spells']['sorcerer']['first'],dnd_dict.character_dict['class_spells']['sorcerer']['second'],dnd_dict.character_dict['class_spells']['sorcerer']['third'],dnd_dict.character_dict['class_spells']['sorcerer']['fourth'],dnd_dict.character_dict['class_spells']['sorcerer']['fifth'],dnd_dict.character_dict['class_spells']['sorcerer']['sixth'],dnd_dict.character_dict['class_spells']['sorcerer']['seventh'],dnd_dict.character_dict['class_spells']['sorcerer']['eighth'],dnd_dict.character_dict['class_spells']['sorcerer']['ninth'])
        dnd_dict.character_dict['d6'] += 1
        dnd_level_up.level_up(6)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 18
    if level == 18:

        if dnd_dict.character_dict['player_class']['sorcerer']['subclass'] == 'Draconic Bloodline':
            dnd_features.draconic_sorcerer18()

        if dnd_dict.character_dict['player_class']['sorcerer']['subclass'] == 'Wild Magic':
            dnd_features.wild_magic_sorcerer18()

        dnd_skills.ninth_swap(dnd_magic.sorcerer_first,dnd_magic.sorcerer_second,dnd_magic.sorcerer_third,dnd_magic.sorcerer_fourth,dnd_magic.sorcerer_fifth,dnd_magic.sorcerer_sixth,dnd_magic.sorcerer_seventh,dnd_magic.sorcerer_eighth,dnd_magic.sorcerer_ninth,dnd_dict.character_dict['class_spells']['sorcerer']['first'],dnd_dict.character_dict['class_spells']['sorcerer']['second'],dnd_dict.character_dict['class_spells']['sorcerer']['third'],dnd_dict.character_dict['class_spells']['sorcerer']['fourth'],dnd_dict.character_dict['class_spells']['sorcerer']['fifth'],dnd_dict.character_dict['class_spells']['sorcerer']['sixth'],dnd_dict.character_dict['class_spells']['sorcerer']['seventh'],dnd_dict.character_dict['class_spells']['sorcerer']['eighth'],dnd_dict.character_dict['class_spells']['sorcerer']['ninth'])
        dnd_dict.character_dict['d6'] += 1
        dnd_level_up.level_up(6)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 19
    if level == 19:

        dnd_level_up.asi_or_feat()
        dnd_features.sorcerous_versatility()
        dnd_skills.ninth_swap(dnd_magic.sorcerer_first,dnd_magic.sorcerer_second,dnd_magic.sorcerer_third,dnd_magic.sorcerer_fourth,dnd_magic.sorcerer_fifth,dnd_magic.sorcerer_sixth,dnd_magic.sorcerer_seventh,dnd_magic.sorcerer_eighth,dnd_magic.sorcerer_ninth,dnd_dict.character_dict['class_spells']['sorcerer']['first'],dnd_dict.character_dict['class_spells']['sorcerer']['second'],dnd_dict.character_dict['class_spells']['sorcerer']['third'],dnd_dict.character_dict['class_spells']['sorcerer']['fourth'],dnd_dict.character_dict['class_spells']['sorcerer']['fifth'],dnd_dict.character_dict['class_spells']['sorcerer']['sixth'],dnd_dict.character_dict['class_spells']['sorcerer']['seventh'],dnd_dict.character_dict['class_spells']['sorcerer']['eighth'],dnd_dict.character_dict['class_spells']['sorcerer']['ninth'])
        dnd_dict.character_dict['d6'] += 1
        dnd_level_up.level_up(6)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 20
    if level == 20:

        dnd_features.sorcerer20()
        dnd_skills.ninth_swap(dnd_magic.sorcerer_first,dnd_magic.sorcerer_second,dnd_magic.sorcerer_third,dnd_magic.sorcerer_fourth,dnd_magic.sorcerer_fifth,dnd_magic.sorcerer_sixth,dnd_magic.sorcerer_seventh,dnd_magic.sorcerer_eighth,dnd_magic.sorcerer_ninth,dnd_dict.character_dict['class_spells']['sorcerer']['first'],dnd_dict.character_dict['class_spells']['sorcerer']['second'],dnd_dict.character_dict['class_spells']['sorcerer']['third'],dnd_dict.character_dict['class_spells']['sorcerer']['fourth'],dnd_dict.character_dict['class_spells']['sorcerer']['fifth'],dnd_dict.character_dict['class_spells']['sorcerer']['sixth'],dnd_dict.character_dict['class_spells']['sorcerer']['seventh'],dnd_dict.character_dict['class_spells']['sorcerer']['eighth'],dnd_dict.character_dict['class_spells']['sorcerer']['ninth'])
        dnd_dict.character_dict['d6'] += 1
        dnd_level_up.level_up(6)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()
