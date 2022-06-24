import dnd_dict, dnd_features, dnd_magic, dnd_skills, dnd_language, dnd_fighting_styles, dnd_level_up
def ranger():
    level = dnd_dict.character_dict['player_class']['ranger']['class_level']

# Level 1
    if level == 1:

        armor_prof = {'light_armor':'Light Armor','medium_armor':'Medium Armor','shields':'Shields'}
        weapon_prof = {'simple_weapons':'Simple Weapons','martial_weapons':'Martial Weapons'}
        dnd_dict.character_dict['Armor_Prof'].update(armor_prof)
        dnd_dict.character_dict['Weapon_Prof'].update(weapon_prof)
        skill_list = ['Animal Handling','Athletics','Insight','Investigation','Nature','Perception','Stealth','Survival']
        skill_prof = dnd_dict.character_dict['skill_prof']
        if not ('animal_handling' in skill_prof and 'athletics' in skill_prof and 'insight' in skill_prof and 'investigation' in skill_prof and 'nature' in skill_prof and 'perception' in skill_prof and 'stealth' in skill_prof and 'survival' in skill_prof):
            dnd_skills.skill_addition(skill_list,skill_prof)
        dnd_features.ranger_features()
        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)
        dnd_skills.spell_slot_selection()

# Level 2
    if level == 2:

        dnd_features.ranger2()
        dnd_dict.character_dict['d10'] += 1
        spell_attack = ((dnd_dict.character_dict["Stats"]["wisdom"]['mod']) + dnd_dict.character_dict['prof_bonus'])
        dnd_dict.character_dict["spell_modifier"]['wisdom']['attack'] = spell_attack
        spell_save = ((dnd_dict.character_dict["Stats"]["wisdom"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
        dnd_dict.character_dict["spell_modifier"]['wisdom']['save'] = spell_save
        dnd_level_up.level_up(10)
        dnd_dict.character_dict['half_caster_level'] += 2
        dnd_skills.spell_slot_selection()

# Level 3
    if level == 3:

        while True:
            choice = input("""Select the subclass you want to have:
1) Beast Master
2) Hunter
Enter your selection: """)
            if choice == '1':
                dnd_dict.character_dict['player_class']['ranger']['subclass'] = 'Beast Master Conclave'
                dnd_features.beast_master_ranger3()
                break

            elif choice == '2':
                dnd_dict.character_dict['player_class']['ranger']['subclass'] = 'Hunter Conclave'
                dnd_features.hunter_ranger3()
                break

            else:
                print("Error: Invalid Selection")
                continue

        dnd_features.ranger3()
        dnd_skills.spell_add(dnd_magic.ranger_first,dnd_dict.character_dict['spells']['first'],dnd_dict.character_dict['class_spells']['ranger']['first'])
        dnd_skills.first_swap(dnd_magic.ranger_first,dnd_dict.character_dict['class_spells']['ranger']['first'])
        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)
        dnd_dict.character_dict['half_caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 4
    if level == 4:

        dnd_level_up.asi_or_feat()
        dnd_fighting_styles.martial_versatility_style_ranger()
        dnd_skills.first_swap(dnd_magic.ranger_first,dnd_dict.character_dict['class_spells']['ranger']['first'])
        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)
        dnd_dict.character_dict['half_caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 5
    if level == 5:

        dnd_features.ranger5()
        dnd_skills.second_level(dnd_magic.ranger_first,dnd_magic.ranger_second,dnd_dict.character_dict['class_spells']['ranger']['first'],dnd_dict.character_dict['class_spells']['ranger']['second'])
        dnd_skills.second_swap(dnd_magic.ranger_first,dnd_magic.ranger_second,dnd_dict.character_dict['class_spells']['ranger']['first'],dnd_dict.character_dict['class_spells']['ranger']['second'])
        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)
        dnd_dict.character_dict['half_caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 6
    if level == 6:

        dnd_features.ranger6()
        dnd_skills.second_swap(dnd_magic.ranger_first,dnd_magic.ranger_second,dnd_dict.character_dict['class_spells']['ranger']['first'],dnd_dict.character_dict['class_spells']['ranger']['second'])
        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)
        dnd_dict.character_dict['half_caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 7
    if level == 7:

        if dnd_dict.character_dict['player_class']['ranger']['subclass'] == 'Beast Master Conclave':
            dnd_features.beast_master_ranger7()
        if dnd_dict.character_dict['player_class']['ranger']['subclass'] == 'Hunter Conclave':
            dnd_features.hunter_ranger7()
        dnd_skills.second_level(dnd_magic.ranger_first,dnd_magic.ranger_second,dnd_dict.character_dict['class_spells']['ranger']['first'],dnd_dict.character_dict['class_spells']['ranger']['second'])
        dnd_skills.second_swap(dnd_magic.ranger_first,dnd_magic.ranger_second,dnd_dict.character_dict['class_spells']['ranger']['first'],dnd_dict.character_dict['class_spells']['ranger']['second'])
        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)
        dnd_dict.character_dict['half_caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 8
    if level == 8:

        dnd_level_up.asi_or_feat()
        dnd_fighting_styles.martial_versatility_style_ranger()
        dnd_features.ranger8()
        dnd_skills.second_swap(dnd_magic.ranger_first,dnd_magic.ranger_second,dnd_dict.character_dict['class_spells']['ranger']['first'],dnd_dict.character_dict['class_spells']['ranger']['second'])
        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)
        dnd_dict.character_dict['half_caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 9
    if level == 9:

        dnd_features.ranger9()
        dnd_skills.third_level(dnd_magic.ranger_first,dnd_magic.ranger_second,dnd_magic.ranger_third,dnd_dict.character_dict['class_spells']['ranger']['first'],dnd_dict.character_dict['class_spells']['ranger']['second'],dnd_dict.character_dict['class_spells']['ranger']['third'])
        dnd_skills.third_swap(dnd_magic.ranger_first,dnd_magic.ranger_second,dnd_magic.ranger_third,dnd_dict.character_dict['class_spells']['ranger']['first'],dnd_dict.character_dict['class_spells']['ranger']['second'],dnd_dict.character_dict['class_spells']['ranger']['third'])
        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)
        dnd_dict.character_dict['half_caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 10
    if level == 10:

        dnd_features.ranger10()
        dnd_skills.third_swap(dnd_magic.ranger_first,dnd_magic.ranger_second,dnd_magic.ranger_third,dnd_dict.character_dict['class_spells']['ranger']['first'],dnd_dict.character_dict['class_spells']['ranger']['second'],dnd_dict.character_dict['class_spells']['ranger']['third'])
        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)
        dnd_dict.character_dict['half_caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 11
    if level == 11:

        if dnd_dict.character_dict['player_class']['ranger']['subclass'] == 'Beast Master Conclave':
            dnd_features.beast_master_ranger11()
        if dnd_dict.character_dict['player_class']['ranger']['subclass'] == 'Hunter Conclave':
            dnd_features.hunter_ranger11()
        dnd_skills.third_level(dnd_magic.ranger_first,dnd_magic.ranger_second,dnd_magic.ranger_third,dnd_dict.character_dict['class_spells']['ranger']['first'],dnd_dict.character_dict['class_spells']['ranger']['second'],dnd_dict.character_dict['class_spells']['ranger']['third'])
        dnd_skills.third_swap(dnd_magic.ranger_first,dnd_magic.ranger_second,dnd_magic.ranger_third,dnd_dict.character_dict['class_spells']['ranger']['first'],dnd_dict.character_dict['class_spells']['ranger']['second'],dnd_dict.character_dict['class_spells']['ranger']['third'])
        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)
        dnd_dict.character_dict['half_caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 12
    if level == 12:

        dnd_level_up.asi_or_feat()
        dnd_fighting_styles.martial_versatility_style_ranger()
        dnd_skills.third_swap(dnd_magic.ranger_first,dnd_magic.ranger_second,dnd_magic.ranger_third,dnd_dict.character_dict['class_spells']['ranger']['first'],dnd_dict.character_dict['class_spells']['ranger']['second'],dnd_dict.character_dict['class_spells']['ranger']['third'])
        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)
        dnd_dict.character_dict['half_caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 13
    if level == 13:

        dnd_features.ranger13()
        dnd_skills.fourth_level(dnd_magic.ranger_first,dnd_magic.ranger_second,dnd_magic.ranger_third,dnd_magic.ranger_fourth,dnd_dict.character_dict['class_spells']['ranger']['first'],dnd_dict.character_dict['class_spells']['ranger']['second'],dnd_dict.character_dict['class_spells']['ranger']['third'],dnd_dict.character_dict['class_spells']['ranger']['fourth'])
        dnd_skills.fourth_swap(dnd_magic.ranger_first,dnd_magic.ranger_second,dnd_magic.ranger_third,dnd_magic.ranger_fourth,dnd_dict.character_dict['class_spells']['ranger']['first'],dnd_dict.character_dict['class_spells']['ranger']['second'],dnd_dict.character_dict['class_spells']['ranger']['third'],dnd_dict.character_dict['class_spells']['ranger']['fourth'])
        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)
        dnd_dict.character_dict['half_caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 14
    if level == 14:

        dnd_features.ranger14()
        dnd_skills.fourth_swap(dnd_magic.ranger_first,dnd_magic.ranger_second,dnd_magic.ranger_third,dnd_magic.ranger_fourth,dnd_dict.character_dict['class_spells']['ranger']['first'],dnd_dict.character_dict['class_spells']['ranger']['second'],dnd_dict.character_dict['class_spells']['ranger']['third'],dnd_dict.character_dict['class_spells']['ranger']['fourth'])
        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)
        dnd_dict.character_dict['half_caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 15
    if level == 15:

        if dnd_dict.character_dict['player_class']['ranger']['subclass'] == 'Beast Master Conclave':
            dnd_features.beast_master_ranger15()
        if dnd_dict.character_dict['player_class']['ranger']['subclass'] == 'Hunter Conclave':
            dnd_features.hunter_ranger15()
        dnd_skills.fourth_level(dnd_magic.ranger_first,dnd_magic.ranger_second,dnd_magic.ranger_third,dnd_magic.ranger_fourth,dnd_dict.character_dict['class_spells']['ranger']['first'],dnd_dict.character_dict['class_spells']['ranger']['second'],dnd_dict.character_dict['class_spells']['ranger']['third'],dnd_dict.character_dict['class_spells']['ranger']['fourth'])
        dnd_skills.fourth_swap(dnd_magic.ranger_first,dnd_magic.ranger_second,dnd_magic.ranger_third,dnd_magic.ranger_fourth,dnd_dict.character_dict['class_spells']['ranger']['first'],dnd_dict.character_dict['class_spells']['ranger']['second'],dnd_dict.character_dict['class_spells']['ranger']['third'],dnd_dict.character_dict['class_spells']['ranger']['fourth'])
        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)
        dnd_dict.character_dict['half_caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 16
    if level == 16:

        dnd_level_up.asi_or_feat()
        dnd_fighting_styles.martial_versatility_style_ranger()
        dnd_skills.fourth_swap(dnd_magic.ranger_first,dnd_magic.ranger_second,dnd_magic.ranger_third,dnd_magic.ranger_fourth,dnd_dict.character_dict['class_spells']['ranger']['first'],dnd_dict.character_dict['class_spells']['ranger']['second'],dnd_dict.character_dict['class_spells']['ranger']['third'],dnd_dict.character_dict['class_spells']['ranger']['fourth'])
        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)
        dnd_dict.character_dict['half_caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 17
    if level == 17:

        dnd_features.ranger17()

        dnd_skills.fifth_level(dnd_magic.ranger_first,dnd_magic.ranger_second,dnd_magic.ranger_third,dnd_magic.ranger_fourth,dnd_magic.ranger_fifth,dnd_dict.character_dict['class_spells']['ranger']['first'],dnd_dict.character_dict['class_spells']['ranger']['second'],dnd_dict.character_dict['class_spells']['ranger']['third'],dnd_dict.character_dict['class_spells']['ranger']['fourth'],dnd_dict.character_dict['class_spells']['ranger']['fifth'])
        dnd_skills.fifth_swap(dnd_magic.ranger_first,dnd_magic.ranger_second,dnd_magic.ranger_third,dnd_magic.ranger_fourth,dnd_magic.ranger_fifth,dnd_dict.character_dict['class_spells']['ranger']['first'],dnd_dict.character_dict['class_spells']['ranger']['second'],dnd_dict.character_dict['class_spells']['ranger']['third'],dnd_dict.character_dict['class_spells']['ranger']['fourth'],dnd_dict.character_dict['class_spells']['ranger']['fifth'])

        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)
        dnd_dict.character_dict['half_caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 18
    if level == 18:

        dnd_features.ranger18()
        dnd_skills.fifth_swap(dnd_magic.ranger_first,dnd_magic.ranger_second,dnd_magic.ranger_third,dnd_magic.ranger_fourth,dnd_magic.ranger_fifth,dnd_dict.character_dict['class_spells']['ranger']['first'],dnd_dict.character_dict['class_spells']['ranger']['second'],dnd_dict.character_dict['class_spells']['ranger']['third'],dnd_dict.character_dict['class_spells']['ranger']['fourth'],dnd_dict.character_dict['class_spells']['ranger']['fifth'])
        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)
        dnd_dict.character_dict['half_caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 19
    if level == 19:

        dnd_level_up.asi_or_feat()
        dnd_fighting_styles.martial_versatility_style_ranger()
        dnd_skills.fifth_level(dnd_magic.ranger_first,dnd_magic.ranger_second,dnd_magic.ranger_third,dnd_magic.ranger_fourth,dnd_magic.ranger_fifth,dnd_dict.character_dict['class_spells']['ranger']['first'],dnd_dict.character_dict['class_spells']['ranger']['second'],dnd_dict.character_dict['class_spells']['ranger']['third'],dnd_dict.character_dict['class_spells']['ranger']['fourth'],dnd_dict.character_dict['class_spells']['ranger']['fifth'])
        dnd_skills.fifth_swap(dnd_magic.ranger_first,dnd_magic.ranger_second,dnd_magic.ranger_third,dnd_magic.ranger_fourth,dnd_magic.ranger_fifth,dnd_dict.character_dict['class_spells']['ranger']['first'],dnd_dict.character_dict['class_spells']['ranger']['second'],dnd_dict.character_dict['class_spells']['ranger']['third'],dnd_dict.character_dict['class_spells']['ranger']['fourth'],dnd_dict.character_dict['class_spells']['ranger']['fifth'])
        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)
        dnd_dict.character_dict['half_caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 20
    if level == 20:

        dnd_features.ranger20()
        dnd_skills.fifth_swap(dnd_magic.ranger_first,dnd_magic.ranger_second,dnd_magic.ranger_third,dnd_magic.ranger_fourth,dnd_magic.ranger_fifth,dnd_dict.character_dict['class_spells']['ranger']['first'],dnd_dict.character_dict['class_spells']['ranger']['second'],dnd_dict.character_dict['class_spells']['ranger']['third'],dnd_dict.character_dict['class_spells']['ranger']['fourth'],dnd_dict.character_dict['class_spells']['ranger']['fifth'])
        dnd_dict.character_dict['d10'] += 1
        dnd_level_up.level_up(10)
        dnd_dict.character_dict['half_caster_level'] += 1
        dnd_skills.spell_slot_selection()
