import dnd_dict, dnd_features, dnd_magic, dnd_skills, dnd_tools, dnd_level_up

def bard():
    level = dnd_dict.character_dict['player_class']['bard']['class_level']

# Level 1
    if level == 1:
        dnd_dict.character_dict['Armor_Prof']['light_armor'] = 'Light Armor'
        dnd_skills.skill_choice()
        dnd_tools.musical_instrument()
        
        dnd_features.bard1()
        dnd_magic.bard_magic()
        spell_attack = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'])
        dnd_dict.character_dict["spell_modifier"]['charisma']['attack'] = spell_attack
        spell_save = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
        dnd_dict.character_dict["spell_modifier"]['charisma']['save'] = spell_save
        dnd_dict.character_dict['d8'] +=1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level']+=1
        dnd_skills.spell_slot_selection()

# Level 2
    if level == 2:
        dnd_features.bard2()
        dnd_skills.spell_add(dnd_magic.bard_first,dnd_dict.character_dict['spells'],dnd_dict.character_dict['class_spells']['bard'])
        dnd_skills.first_swap(dnd_magic.bard_first,dnd_dict.character_dict['class_spells']['bard']['first'])
        dnd_dict.character_dict['d8'] +=1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level']+=1
        dnd_skills.spell_slot_selection()

# Level 3
    if level == 3:
        while True:
            choice = input("""Select the subclass you want to have:
1) College of Lore
2) College of Valor
Enter your selection: """)
            if choice == '1':
                dnd_dict.character_dict['player_class']['bard']['subclass'] = 'College of Lore'
                dnd_features.lore_bard3()
                break

            elif choice == '2':
                dnd_dict.character_dict['player_class']['bard']['subclass'] = 'College of Valor'
                dnd_features.valor_bard3()
                break

            else:
                print("Error: Invalid Input")
                continue


        dnd_skills.second_level(dnd_magic.bard_first,dnd_magic.bard_second,dnd_dict.character_dict['class_spells']['bard']['first'],dnd_dict.character_dict['class_spells']['bard']['second'])
        dnd_skills.second_swap(dnd_magic.bard_first,dnd_magic.bard_second,dnd_dict.character_dict['class_spells']['bard']['first'],dnd_dict.character_dict['class_spells']['bard']['second'])
        dnd_features.bard3()
        dnd_dict.character_dict['d8'] +=1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level']+=1
        dnd_skills.spell_slot_selection()

# Level 4
    if level == 4:

        dnd_level_up.asi_or_feat()
        dnd_features.bardic_versatility()
        dnd_skills.second_level(dnd_magic.bard_first,dnd_magic.bard_second,dnd_dict.character_dict['class_spells']['bard']['first'],dnd_dict.character_dict['class_spells']['bard']['second'])
        dnd_skills.second_swap(dnd_magic.bard_first,dnd_magic.bard_second,dnd_dict.character_dict['class_spells']['bard']['first'],dnd_dict.character_dict['class_spells']['bard']['second'])
        dnd_skills.spell_add(dnd_magic.bard_cantrip,dnd_dict.character_dict['spells'],dnd_dict.character_dict['class_spells']['bard_cantrips'])
        dnd_dict.character_dict['d8'] +=1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level']+=1
        dnd_skills.spell_slot_selection()

# Level 5
    if level == 5:

        dnd_features.bard5()
        dnd_skills.third_level(dnd_magic.bard_first,dnd_magic.bard_second,dnd_magic.bard_third,dnd_dict.character_dict['class_spells']['bard']['first'],dnd_dict.character_dict['class_spells']['bard']['second'],dnd_dict.character_dict['class_spells']['bard']['third'])
        dnd_skills.third_swap(dnd_magic.bard_first,dnd_magic.bard_second,dnd_magic.bard_third,dnd_dict.character_dict['class_spells']['bard']['first'],dnd_dict.character_dict['class_spells']['bard']['second'],dnd_dict.character_dict['class_spells']['bard']['third'])
        dnd_dict.character_dict['d8'] +=1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level']+=1
        dnd_skills.spell_slot_selection()

# Level 6
    if level == 6:

        if dnd_dict.character_dict['player_class']['bard']['subclass'] == 'College of Lore':
            dnd_features.lore_bard6()
        if dnd_dict.character_dict['player_class']['bard']['subclass'] == 'College of Valor':
            dnd_features.valor_bard6()

        dnd_features.bard6()
        dnd_skills.third_level(dnd_magic.bard_first,dnd_magic.bard_second,dnd_magic.bard_third,dnd_dict.character_dict['class_spells']['bard']['first'],dnd_dict.character_dict['class_spells']['bard']['second'],dnd_dict.character_dict['class_spells']['bard']['third'])
        dnd_skills.third_swap(dnd_magic.bard_first,dnd_magic.bard_second,dnd_magic.bard_third,dnd_dict.character_dict['class_spells']['bard']['first'],dnd_dict.character_dict['class_spells']['bard']['second'],dnd_dict.character_dict['class_spells']['bard']['third'])
        dnd_dict.character_dict['d8'] +=1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level']+=1
        dnd_skills.spell_slot_selection()

# Level 7
    if level == 7:

        dnd_skills.fourth_level(dnd_magic.bard_first,dnd_magic.bard_second,dnd_magic.bard_third,dnd_magic.bard_fourth,dnd_dict.character_dict['class_spells']['bard']['first'],dnd_dict.character_dict['class_spells']['bard']['second'],dnd_dict.character_dict['class_spells']['bard']['third'],dnd_dict.character_dict['class_spells']['bard']['fourth'])
        dnd_skills.fourth_swap(dnd_magic.bard_first,dnd_magic.bard_second,dnd_magic.bard_third,dnd_magic.bard_fourth,dnd_dict.character_dict['class_spells']['bard']['first'],dnd_dict.character_dict['class_spells']['bard']['second'],dnd_dict.character_dict['class_spells']['bard']['third'],dnd_dict.character_dict['class_spells']['bard']['fourth'])
        dnd_dict.character_dict['d8'] +=1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level']+=1
        dnd_skills.spell_slot_selection()

# Level 8
    if level == 8:

        dnd_level_up.asi_or_feat()
        dnd_features.bardic_versatility()
        dnd_skills.fourth_level(dnd_magic.bard_first,dnd_magic.bard_second,dnd_magic.bard_third,dnd_magic.bard_fourth,dnd_dict.character_dict['class_spells']['bard']['first'],dnd_dict.character_dict['class_spells']['bard']['second'],dnd_dict.character_dict['class_spells']['bard']['third'],dnd_dict.character_dict['class_spells']['bard']['fourth'])
        dnd_skills.fourth_swap(dnd_magic.bard_first,dnd_magic.bard_second,dnd_magic.bard_third,dnd_magic.bard_fourth,dnd_dict.character_dict['class_spells']['bard']['first'],dnd_dict.character_dict['class_spells']['bard']['second'],dnd_dict.character_dict['class_spells']['bard']['third'],dnd_dict.character_dict['class_spells']['bard']['fourth'])
        dnd_dict.character_dict['bardic_inspiration'] = 'd8'
        dnd_dict.character_dict['d8'] +=1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level']+=1
        dnd_skills.spell_slot_selection()

# Level 9
    if level == 9:

        dnd_skills.fifth_level(dnd_magic.bard_first,dnd_magic.bard_second,dnd_magic.bard_third,dnd_magic.bard_fourth,dnd_magic.bard_fifth,dnd_dict.character_dict['class_spells']['bard']['first'],dnd_dict.character_dict['class_spells']['bard']['second'],dnd_dict.character_dict['class_spells']['bard']['third'],dnd_dict.character_dict['class_spells']['bard']['fourth'],dnd_dict.character_dict['class_spells']['bard']['fifth'])
        dnd_skills.fifth_swap(dnd_magic.bard_first,dnd_magic.bard_second,dnd_magic.bard_third,dnd_magic.bard_fourth,dnd_magic.bard_fifth,dnd_dict.character_dict['class_spells']['bard']['first'],dnd_dict.character_dict['class_spells']['bard']['second'],dnd_dict.character_dict['class_spells']['bard']['third'],dnd_dict.character_dict['class_spells']['bard']['fourth'],dnd_dict.character_dict['class_spells']['bard']['fifth'])
        dnd_dict.character_dict['d8'] +=1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level']+=1
        dnd_skills.spell_slot_selection()

# Level 10
    if level == 10:

        dnd_dict.character_dict['bardic_inspiration'] = 'd10'
        dnd_features.bard10()
        dnd_skills.fifth_level(dnd_magic.bard_first,dnd_magic.bard_second,dnd_magic.bard_third,dnd_magic.bard_fourth,dnd_magic.bard_fifth,dnd_dict.character_dict['class_spells']['bard']['first'],dnd_dict.character_dict['class_spells']['bard']['second'],dnd_dict.character_dict['class_spells']['bard']['third'],dnd_dict.character_dict['class_spells']['bard']['fourth'],dnd_dict.character_dict['class_spells']['bard']['fifth'])
        dnd_skills.fifth_swap(dnd_magic.bard_first,dnd_magic.bard_second,dnd_magic.bard_third,dnd_magic.bard_fourth,dnd_magic.bard_fifth,dnd_dict.character_dict['class_spells']['bard']['first'],dnd_dict.character_dict['class_spells']['bard']['second'],dnd_dict.character_dict['class_spells']['bard']['third'],dnd_dict.character_dict['class_spells']['bard']['fourth'],dnd_dict.character_dict['class_spells']['bard']['fifth'])
        dnd_dict.character_dict['d8'] +=1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level']+=1
        dnd_skills.spell_slot_selection()

# Level 11
    if level == 11:

        dnd_skills.sixth_level(dnd_magic.bard_first,dnd_magic.bard_second,dnd_magic.bard_third,dnd_magic.bard_fourth,dnd_magic.bard_fifth,dnd_magic.bard_sixth,dnd_dict.character_dict['class_spells']['bard']['first'],dnd_dict.character_dict['class_spells']['bard']['second'],dnd_dict.character_dict['class_spells']['bard']['third'],dnd_dict.character_dict['class_spells']['bard']['fourth'],dnd_dict.character_dict['class_spells']['bard']['fifth'],dnd_dict.character_dict['class_spells']['bard']['sixth'])
        dnd_skills.sixth_swap(dnd_magic.bard_first,dnd_magic.bard_second,dnd_magic.bard_third,dnd_magic.bard_fourth,dnd_magic.bard_fifth,dnd_magic.bard_sixth,dnd_dict.character_dict['class_spells']['bard']['first'],dnd_dict.character_dict['class_spells']['bard']['second'],dnd_dict.character_dict['class_spells']['bard']['third'],dnd_dict.character_dict['class_spells']['bard']['fourth'],dnd_dict.character_dict['class_spells']['bard']['fifth'],dnd_dict.character_dict['class_spells']['bard']['sixth'])
        dnd_dict.character_dict['d8'] +=1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level']+=1
        dnd_skills.spell_slot_selection()

# Level 12
    if level == 12:

        dnd_level_up.asi_or_feat()
        dnd_features.bardic_versatility()
        dnd_skills.sixth_swap(dnd_magic.bard_first,dnd_magic.bard_second,dnd_magic.bard_third,dnd_magic.bard_fourth,dnd_magic.bard_fifth,dnd_magic.bard_sixth,dnd_dict.character_dict['class_spells']['bard']['first'],dnd_dict.character_dict['class_spells']['bard']['second'],dnd_dict.character_dict['class_spells']['bard']['third'],dnd_dict.character_dict['class_spells']['bard']['fourth'],dnd_dict.character_dict['class_spells']['bard']['fifth'],dnd_dict.character_dict['class_spells']['bard']['sixth'])
        dnd_dict.character_dict['d8'] +=1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level']+=1
        dnd_skills.spell_slot_selection()

# Level 13
    if level == 13:

        dnd_skills.seventh_level(dnd_magic.bard_first,dnd_magic.bard_second,dnd_magic.bard_third,dnd_magic.bard_fourth,dnd_magic.bard_fifth,dnd_magic.bard_sixth,dnd_magic.bard_seventh,dnd_dict.character_dict['class_spells']['bard']['first'],dnd_dict.character_dict['class_spells']['bard']['second'],dnd_dict.character_dict['class_spells']['bard']['third'],dnd_dict.character_dict['class_spells']['bard']['fourth'],dnd_dict.character_dict['class_spells']['bard']['fifth'],dnd_dict.character_dict['class_spells']['bard']['sixth'],dnd_dict.character_dict['class_spells']['bard']['seventh'])
        dnd_skills.seventh_swap(dnd_magic.bard_first,dnd_magic.bard_second,dnd_magic.bard_third,dnd_magic.bard_fourth,dnd_magic.bard_fifth,dnd_magic.bard_sixth,dnd_magic.bard_seventh,dnd_dict.character_dict['class_spells']['bard']['first'],dnd_dict.character_dict['class_spells']['bard']['second'],dnd_dict.character_dict['class_spells']['bard']['third'],dnd_dict.character_dict['class_spells']['bard']['fourth'],dnd_dict.character_dict['class_spells']['bard']['fifth'],dnd_dict.character_dict['class_spells']['bard']['sixth'],dnd_dict.character_dict['class_spells']['bard']['seventh'])
        dnd_dict.character_dict['d8'] +=1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level']+=1
        dnd_skills.spell_slot_selection()

# Level 14
    if level == 14:

        if dnd_dict.character_dict['player_class']['bard']['subclass'] == 'College of Lore':
            dnd_features.lore_bard14()
        if dnd_dict.character_dict['player_class']['bard']['subclass'] == 'College of Valor':
            dnd_features.valor_bard14()

        dnd_features.bard14()
        dnd_skills.seventh_swap(dnd_magic.bard_first,dnd_magic.bard_second,dnd_magic.bard_third,dnd_magic.bard_fourth,dnd_magic.bard_fifth,dnd_magic.bard_sixth,dnd_magic.bard_seventh,dnd_dict.character_dict['class_spells']['bard']['first'],dnd_dict.character_dict['class_spells']['bard']['second'],dnd_dict.character_dict['class_spells']['bard']['third'],dnd_dict.character_dict['class_spells']['bard']['fourth'],dnd_dict.character_dict['class_spells']['bard']['fifth'],dnd_dict.character_dict['class_spells']['bard']['sixth'],dnd_dict.character_dict['class_spells']['bard']['seventh'])
        dnd_dict.character_dict['d8'] +=1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level']+=1
        dnd_skills.spell_slot_selection()

# Level 15
    if level == 15:

        dnd_skills.eighth_level(dnd_magic.bard_first,dnd_magic.bard_second,dnd_magic.bard_third,dnd_magic.bard_fourth,dnd_magic.bard_fifth,dnd_magic.bard_sixth,dnd_magic.bard_seventh,dnd_magic.bard_eighth,dnd_dict.character_dict['class_spells']['bard']['first'],dnd_dict.character_dict['class_spells']['bard']['second'],dnd_dict.character_dict['class_spells']['bard']['third'],dnd_dict.character_dict['class_spells']['bard']['fourth'],dnd_dict.character_dict['class_spells']['bard']['fifth'],dnd_dict.character_dict['class_spells']['bard']['sixth'],dnd_dict.character_dict['class_spells']['bard']['seventh'],dnd_dict.character_dict['class_spells']['bard']['eighth'])
        dnd_skills.eighth_swap(dnd_magic.bard_first,dnd_magic.bard_second,dnd_magic.bard_third,dnd_magic.bard_fourth,dnd_magic.bard_fifth,dnd_magic.bard_sixth,dnd_magic.bard_seventh,dnd_magic.bard_eighth,dnd_dict.character_dict['class_spells']['bard']['first'],dnd_dict.character_dict['class_spells']['bard']['second'],dnd_dict.character_dict['class_spells']['bard']['third'],dnd_dict.character_dict['class_spells']['bard']['fourth'],dnd_dict.character_dict['class_spells']['bard']['fifth'],dnd_dict.character_dict['class_spells']['bard']['sixth'],dnd_dict.character_dict['class_spells']['bard']['seventh'],dnd_dict.character_dict['class_spells']['bard']['eighth'])
        dnd_dict.character_dict['bardic_inspiration'] = 'd12'
        dnd_dict.character_dict['d8'] +=1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level']+=1
        dnd_skills.spell_slot_selection()

# Level 16
    if level == 16:

        dnd_level_up.asi_or_feat()
        dnd_features.bardic_versatility()
        dnd_skills.eighth_swap(dnd_magic.bard_first,dnd_magic.bard_second,dnd_magic.bard_third,dnd_magic.bard_fourth,dnd_magic.bard_fifth,dnd_magic.bard_sixth,dnd_magic.bard_seventh,dnd_magic.bard_eighth,dnd_dict.character_dict['class_spells']['bard']['first'],dnd_dict.character_dict['class_spells']['bard']['second'],dnd_dict.character_dict['class_spells']['bard']['third'],dnd_dict.character_dict['class_spells']['bard']['fourth'],dnd_dict.character_dict['class_spells']['bard']['fifth'],dnd_dict.character_dict['class_spells']['bard']['sixth'],dnd_dict.character_dict['class_spells']['bard']['seventh'],dnd_dict.character_dict['class_spells']['bard']['eighth'])
        dnd_dict.character_dict['d8'] +=1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level']+=1
        dnd_skills.spell_slot_selection()

# Level 17
    if level == 17:

        dnd_skills.ninth_level(dnd_magic.bard_first,dnd_magic.bard_second,dnd_magic.bard_third,dnd_magic.bard_fourth,dnd_magic.bard_fifth,dnd_magic.bard_sixth,dnd_magic.bard_seventh,dnd_magic.bard_eighth,dnd_magic.bard_ninth,dnd_dict.character_dict['class_spells']['bard']['first'],dnd_dict.character_dict['class_spells']['bard']['second'],dnd_dict.character_dict['class_spells']['bard']['third'],dnd_dict.character_dict['class_spells']['bard']['fourth'],dnd_dict.character_dict['class_spells']['bard']['fifth'],dnd_dict.character_dict['class_spells']['bard']['sixth'],dnd_dict.character_dict['class_spells']['bard']['seventh'],dnd_dict.character_dict['class_spells']['bard']['eighth'],dnd_dict.character_dict['class_spells']['bard']['ninth'])
        dnd_skills.ninth_swap(dnd_magic.bard_first,dnd_magic.bard_second,dnd_magic.bard_third,dnd_magic.bard_fourth,dnd_magic.bard_fifth,dnd_magic.bard_sixth,dnd_magic.bard_seventh,dnd_magic.bard_eighth,dnd_magic.bard_ninth,dnd_dict.character_dict['class_spells']['bard']['first'],dnd_dict.character_dict['class_spells']['bard']['second'],dnd_dict.character_dict['class_spells']['bard']['third'],dnd_dict.character_dict['class_spells']['bard']['fourth'],dnd_dict.character_dict['class_spells']['bard']['fifth'],dnd_dict.character_dict['class_spells']['bard']['sixth'],dnd_dict.character_dict['class_spells']['bard']['seventh'],dnd_dict.character_dict['class_spells']['bard']['eighth'],dnd_dict.character_dict['class_spells']['bard']['ninth'])
        dnd_dict.character_dict['d8'] +=1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level']+=1
        dnd_skills.spell_slot_selection()

# Level 18
    if level == 18:

        dnd_features.bard18()
        dnd_skills.ninth_swap(dnd_magic.bard_first,dnd_magic.bard_second,dnd_magic.bard_third,dnd_magic.bard_fourth,dnd_magic.bard_fifth,dnd_magic.bard_sixth,dnd_magic.bard_seventh,dnd_magic.bard_eighth,dnd_magic.bard_ninth,dnd_dict.character_dict['class_spells']['bard']['first'],dnd_dict.character_dict['class_spells']['bard']['second'],dnd_dict.character_dict['class_spells']['bard']['third'],dnd_dict.character_dict['class_spells']['bard']['fourth'],dnd_dict.character_dict['class_spells']['bard']['fifth'],dnd_dict.character_dict['class_spells']['bard']['sixth'],dnd_dict.character_dict['class_spells']['bard']['seventh'],dnd_dict.character_dict['class_spells']['bard']['eighth'],dnd_dict.character_dict['class_spells']['bard']['ninth'])
        dnd_dict.character_dict['d8'] +=1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level']+=1
        dnd_skills.spell_slot_selection()

# Level 19
    if level == 19:

        dnd_level_up.asi_or_feat()
        dnd_features.bardic_versatility()
        dnd_skills.ninth_swap(dnd_magic.bard_first,dnd_magic.bard_second,dnd_magic.bard_third,dnd_magic.bard_fourth,dnd_magic.bard_fifth,dnd_magic.bard_sixth,dnd_magic.bard_seventh,dnd_magic.bard_eighth,dnd_magic.bard_ninth,dnd_dict.character_dict['class_spells']['bard']['first'],dnd_dict.character_dict['class_spells']['bard']['second'],dnd_dict.character_dict['class_spells']['bard']['third'],dnd_dict.character_dict['class_spells']['bard']['fourth'],dnd_dict.character_dict['class_spells']['bard']['fifth'],dnd_dict.character_dict['class_spells']['bard']['sixth'],dnd_dict.character_dict['class_spells']['bard']['seventh'],dnd_dict.character_dict['class_spells']['bard']['eighth'],dnd_dict.character_dict['class_spells']['bard']['ninth'])
        dnd_dict.character_dict['d8'] +=1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level']+=1
        dnd_skills.spell_slot_selection()

# Level 20
    if level == 20:

        dnd_features.bard20()

        dnd_skills.ninth_swap(dnd_magic.bard_first,dnd_magic.bard_second,dnd_magic.bard_third,dnd_magic.bard_fourth,dnd_magic.bard_fifth,dnd_magic.bard_sixth,dnd_magic.bard_seventh,dnd_magic.bard_eighth,dnd_magic.bard_ninth,dnd_dict.character_dict['class_spells']['bard']['first'],dnd_dict.character_dict['class_spells']['bard']['second'],dnd_dict.character_dict['class_spells']['bard']['third'],dnd_dict.character_dict['class_spells']['bard']['fourth'],dnd_dict.character_dict['class_spells']['bard']['fifth'],dnd_dict.character_dict['class_spells']['bard']['sixth'],dnd_dict.character_dict['class_spells']['bard']['seventh'],dnd_dict.character_dict['class_spells']['bard']['eighth'],dnd_dict.character_dict['class_spells']['bard']['ninth'])
        dnd_dict.character_dict['d8'] +=1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level']+=1
        dnd_skills.spell_slot_selection()

    else:
        pass





