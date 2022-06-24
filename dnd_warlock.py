import dnd_dict, dnd_magic, dnd_features, dnd_magic, dnd_level_up, dnd_invocations, dnd_skills

def warlock():
    level = dnd_dict.character_dict['player_class']['warlock']['class_level']

# Level 1
    if level == 1:

        dnd_dict.character_dict['Armor_Prof']['light_armor'] = 'Light Armor'
        dnd_dict.character_dict['Weapon_Prof']['simple_weapons'] = 'Simple Weapons'

# Choose the subclass
        while True:
            subclass_choice = input("""Select your patron:
1) Archfey
2) Fiend
3) Great Old One
Enter your Selection: """)
            if subclass_choice=='1':
                dnd_dict.character_dict['player_class']['warlock']['subclass'] = 'Archfey'
                dnd_features.archfey_warlock1()
                dnd_magic.archfey_warlock_magic()
                break
    
            elif subclass_choice=='2':
                dnd_dict.character_dict['player_class']['warlock']['subclass'] = 'Fiend'
                dnd_features.fiend_warlock1()
                dnd_magic.fiend_warlock_magic()
                break
    
            elif subclass_choice=='3':
                dnd_dict.character_dict['player_class']['warlock']['subclass'] = 'Great Old One'
                dnd_features.goo_warlock1()
                dnd_magic.goo_warlock_magic()
                break
    
            else:
                print("Invalid Selection")
                continue
        dnd_dict.character_dict['pact_magic']['first'] = 1
        spell_attack = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'])
        dnd_dict.character_dict["spell_modifier"]['charisma']['attack'] = spell_attack
        spell_save = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
        dnd_dict.character_dict["spell_modifier"]['charisma']['save'] = spell_save
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)

# Level 2
    if level == 2:

        dnd_invocations.first_invocations()
        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Archfey':
            dnd_skills.first_swap(dnd_magic.archfey_warlock_first,dnd_dict.character_dict['class_spells']['warlock']['first'])


        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Fiend':
            dnd_skills.first_swap(dnd_magic.fiend_warlock_first,dnd_dict.character_dict['class_spells']['warlock']['first'])


        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Great Old One':
            dnd_skills.first_swap(dnd_magic.goo_warlock_first,dnd_dict.character_dict['class_spells']['warlock']['first'])


        dnd_dict.character_dict['pact_magic']['first'] = 2
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)

# Level 3
    if level == 3:

        dnd_features.warlock3()
        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Archfey':
            dnd_skills.second_swap(dnd_magic.archfey_warlock_first,dnd_magic.archfey_warlock_second,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'])


        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Fiend':
            dnd_skills.second_swap(dnd_magic.fiend_warlock_first,dnd_magic.fiend_warlock_second,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'])


        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Great Old One':
            dnd_skills.second_swap(dnd_magic.goo_warlock_first,dnd_magic.goo_warlock_second,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'])

        dnd_invocations.invocation_swap()
        dnd_dict.character_dict['pact_magic']['first'] = 0
        dnd_dict.character_dict['pact_magic']['second'] = 2
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)

# Level 4
    if level == 4:

        dnd_level_up.asi_or_feat()
        dnd_features.eldritch_versatility()
        dnd_skills.spell_add(dnd_magic.warlock_cantrip,dnd_dict.character_dict['spells']['cantrips'],dnd_dict.character_dict['class_spells']['warlock_cantrips'])
        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Archfey':
            dnd_skills.second_swap(dnd_magic.archfey_warlock_first,dnd_magic.archfey_warlock_second,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'])


        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Fiend':
            dnd_skills.second_swap(dnd_magic.fiend_warlock_first,dnd_magic.fiend_warlock_second,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'])


        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Great Old One':
            dnd_skills.second_swap(dnd_magic.goo_warlock_first,dnd_magic.goo_warlock_second,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'])


        dnd_invocations.invocation_swap()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)

# Level 5
    if level == 5:

        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Archfey':
            dnd_skills.third_level(dnd_magic.archfey_warlock_first,dnd_magic.archfey_warlock_second,dnd_magic.archfey_warlock_third,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'])
            dnd_skills.third_swap(dnd_magic.archfey_warlock_first,dnd_magic.archfey_warlock_second,dnd_magic.archfey_warlock_third,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'])



        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Fiend':
            dnd_skills.third_level(dnd_magic.fiend_warlock_first,dnd_magic.fiend_warlock_second,dnd_magic.fiend_warlock_third,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'])
            dnd_skills.third_swap(dnd_magic.fiend_warlock_first,dnd_magic.fiend_warlock_second,dnd_magic.fiend_warlock_third,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'])



        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Great Old One':
            dnd_skills.third_level(dnd_magic.goo_warlock_first,dnd_magic.goo_warlock_second,dnd_magic.goo_warlock_third,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'])
            dnd_skills.third_swap(dnd_magic.goo_warlock_first,dnd_magic.goo_warlock_second,dnd_magic.goo_warlock_third,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'])

        dnd_invocations.invocation_swap()
        dnd_invocations.invocations()
        dnd_dict.character_dict['pact_magic']['second'] = 0
        dnd_dict.character_dict['pact_magic']['third'] = 2
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)

# Level 6
    if level == 6:

        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Archfey':
            dnd_skills.third_swap(dnd_magic.archfey_warlock_first,dnd_magic.archfey_warlock_second,dnd_magic.archfey_warlock_third,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'])
            dnd_features.archfey_warlock6()


        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Fiend':
            dnd_skills.third_swap(dnd_magic.fiend_warlock_first,dnd_magic.fiend_warlock_second,dnd_magic.fiend_warlock_third,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'])
            dnd_features.fiend_warlock6()


        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Great Old One':
            dnd_skills.third_swap(dnd_magic.goo_warlock_first,dnd_magic.goo_warlock_second,dnd_magic.goo_warlock_third,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'])
            dnd_features.goo_warlock6()


        dnd_invocations.invocation_swap()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)

# Level 7
    if level == 7:

        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Archfey':
            dnd_skills.fourth_level(dnd_magic.archfey_warlock_first,dnd_magic.archfey_warlock_second,dnd_magic.archfey_warlock_third,dnd_magic.archfey_warlock_fourth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'])
            dnd_skills.fourth_swap(dnd_magic.archfey_warlock_first,dnd_magic.archfey_warlock_second,dnd_magic.archfey_warlock_third,dnd_magic.archfey_warlock_fourth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'])


        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Fiend':
            dnd_skills.fourth_level(dnd_magic.fiend_warlock_first,dnd_magic.fiend_warlock_second,dnd_magic.fiend_warlock_third,dnd_magic.fiend_warlock_fourth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'])
            dnd_skills.fourth_swap(dnd_magic.fiend_warlock_first,dnd_magic.fiend_warlock_second,dnd_magic.fiend_warlock_third,dnd_magic.fiend_warlock_fourth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'])


        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Great Old One':
            dnd_skills.fourth_level(dnd_magic.goo_warlock_first,dnd_magic.goo_warlock_second,dnd_magic.goo_warlock_third,dnd_magic.goo_warlock_fourth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'])
            dnd_skills.fourth_swap(dnd_magic.goo_warlock_first,dnd_magic.goo_warlock_second,dnd_magic.goo_warlock_third,dnd_magic.goo_warlock_fourth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'])

        dnd_invocations.invocation_swap()
        dnd_invocations.invocations()
        dnd_dict.character_dict['pact_magic']['third'] = 0
        dnd_dict.character_dict['pact_magic']['fourth'] = 2
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)

# Level 8
    if level == 8:

        dnd_level_up.asi_or_feat()
        dnd_features.eldritch_versatility()

        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Archfey':
            dnd_skills.fourth_swap(dnd_magic.archfey_warlock_first,dnd_magic.archfey_warlock_second,dnd_magic.archfey_warlock_third,dnd_magic.archfey_warlock_fourth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'])


        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Fiend':
            dnd_skills.fourth_swap(dnd_magic.fiend_warlock_first,dnd_magic.fiend_warlock_second,dnd_magic.fiend_warlock_third,dnd_magic.fiend_warlock_fourth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'])


        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Great Old One':
            dnd_skills.fourth_swap(dnd_magic.goo_warlock_first,dnd_magic.goo_warlock_second,dnd_magic.goo_warlock_third,dnd_magic.goo_warlock_fourth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'])


        dnd_invocations.invocation_swap()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)

# Level 9
    if level == 9:

        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Archfey':
            dnd_skills.fifth_level(dnd_magic.archfey_warlock_first,dnd_magic.archfey_warlock_second,dnd_magic.archfey_warlock_third,dnd_magic.archfey_warlock_fourth,dnd_magic.archfey_warlock_fifth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'],dnd_dict.character_dict['class_spells']['warlock']['fifth'])
            dnd_skills.fifth_swap(dnd_magic.archfey_warlock_first,dnd_magic.archfey_warlock_second,dnd_magic.archfey_warlock_third,dnd_magic.archfey_warlock_fourth,dnd_magic.archfey_warlock_fifth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'],dnd_dict.character_dict['class_spells']['warlock']['fifth'])

        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Fiend':
            dnd_skills.fifth_level(dnd_magic.fiend_warlock_first,dnd_magic.fiend_warlock_second,dnd_magic.fiend_warlock_third,dnd_magic.fiend_warlock_fourth,dnd_magic.fiend_warlock_fifth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'],dnd_dict.character_dict['class_spells']['warlock']['fifth'])
            dnd_skills.fifth_swap(dnd_magic.fiend_warlock_first,dnd_magic.fiend_warlock_second,dnd_magic.fiend_warlock_third,dnd_magic.fiend_warlock_fourth,dnd_magic.fiend_warlock_fifth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'],dnd_dict.character_dict['class_spells']['warlock']['fifth'])



        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Great Old One':
            dnd_skills.fifth_level(dnd_magic.goo_warlock_first,dnd_magic.goo_warlock_second,dnd_magic.goo_warlock_third,dnd_magic.goo_warlock_fourth,dnd_magic.goo_warlock_fifth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'],dnd_dict.character_dict['class_spells']['warlock']['fifth'])
            dnd_skills.fifth_swap(dnd_magic.goo_warlock_first,dnd_magic.goo_warlock_second,dnd_magic.goo_warlock_third,dnd_magic.goo_warlock_fourth,dnd_magic.goo_warlock_fifth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'],dnd_dict.character_dict['class_spells']['warlock']['fifth'])


        dnd_invocations.invocation_swap()
        dnd_invocations.invocations()
        dnd_dict.character_dict['pact_magic']['fourth'] = 0
        dnd_dict.character_dict['pact_magic']['fifth'] = 2
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)

# Level 10
    if level == 10:

        dnd_skills.spell_add(dnd_magic.warlock_cantrip,dnd_dict.character_dict['spells']['cantrips'],dnd_dict.character_dict['class_spells']['warlock_cantrips'])

        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Archfey':
            dnd_skills.fifth_swap(dnd_magic.archfey_warlock_first,dnd_magic.archfey_warlock_second,dnd_magic.archfey_warlock_third,dnd_magic.archfey_warlock_fourth,dnd_magic.archfey_warlock_fifth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'],dnd_dict.character_dict['class_spells']['warlock']['fifth'])
            dnd_features.archfey_warlock10()

        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Fiend':
            dnd_skills.fifth_swap(dnd_magic.fiend_warlock_first,dnd_magic.fiend_warlock_second,dnd_magic.fiend_warlock_third,dnd_magic.fiend_warlock_fourth,dnd_magic.fiend_warlock_fifth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'],dnd_dict.character_dict['class_spells']['warlock']['fifth'])
            dnd_features.fiend_warlock10()

        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Great Old One':
            dnd_skills.fifth_swap(dnd_magic.goo_warlock_first,dnd_magic.goo_warlock_second,dnd_magic.goo_warlock_third,dnd_magic.goo_warlock_fourth,dnd_magic.goo_warlock_fifth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'],dnd_dict.character_dict['class_spells']['warlock']['fifth'])
            dnd_features.goo_warlock10()


        dnd_invocations.invocation_swap()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)

# Level 11
    if level == 11:

        dnd_features.warlock11()
        dnd_skills.spell_add(dnd_magic.warlock_sixth,dnd_dict.character_dict['spells'],dnd_dict.character_dict['class_spells']['warlock']['sixth_level_arcanum'])

        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Archfey':
            dnd_skills.fifth_swap(dnd_magic.archfey_warlock_first,dnd_magic.archfey_warlock_second,dnd_magic.archfey_warlock_third,dnd_magic.archfey_warlock_fourth,dnd_magic.archfey_warlock_fifth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'],dnd_dict.character_dict['class_spells']['warlock']['fifth'])

        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Fiend':
            dnd_skills.fifth_swap(dnd_magic.fiend_warlock_first,dnd_magic.fiend_warlock_second,dnd_magic.fiend_warlock_third,dnd_magic.fiend_warlock_fourth,dnd_magic.fiend_warlock_fifth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'],dnd_dict.character_dict['class_spells']['warlock']['fifth'])

        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Great Old One':
            dnd_skills.fifth_swap(dnd_magic.goo_warlock_first,dnd_magic.goo_warlock_second,dnd_magic.goo_warlock_third,dnd_magic.goo_warlock_fourth,dnd_magic.goo_warlock_fifth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'],dnd_dict.character_dict['class_spells']['warlock']['fifth'])


        dnd_invocations.invocation_swap()
        dnd_dict.character_dict['pact_magic']['fifth'] = 3
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)

# Level 12
    if level == 12:

        dnd_level_up.asi_or_feat()
        dnd_features.eldritch_versatility()
        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Archfey':
            dnd_skills.fifth_level(dnd_magic.archfey_warlock_first,dnd_magic.archfey_warlock_second,dnd_magic.archfey_warlock_third,dnd_magic.archfey_warlock_fourth,dnd_magic.archfey_warlock_fifth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'],dnd_dict.character_dict['class_spells']['warlock']['fifth'])
            dnd_skills.fifth_swap(dnd_magic.archfey_warlock_first,dnd_magic.archfey_warlock_second,dnd_magic.archfey_warlock_third,dnd_magic.archfey_warlock_fourth,dnd_magic.archfey_warlock_fifth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'],dnd_dict.character_dict['class_spells']['warlock']['fifth'])

        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Fiend':
            dnd_skills.fifth_level(dnd_magic.fiend_warlock_first,dnd_magic.fiend_warlock_second,dnd_magic.fiend_warlock_third,dnd_magic.fiend_warlock_fourth,dnd_magic.fiend_warlock_fifth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'],dnd_dict.character_dict['class_spells']['warlock']['fifth'])
            dnd_skills.fifth_swap(dnd_magic.fiend_warlock_first,dnd_magic.fiend_warlock_second,dnd_magic.fiend_warlock_third,dnd_magic.fiend_warlock_fourth,dnd_magic.fiend_warlock_fifth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'],dnd_dict.character_dict['class_spells']['warlock']['fifth'])



        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Great Old One':
            dnd_skills.fifth_level(dnd_magic.goo_warlock_first,dnd_magic.goo_warlock_second,dnd_magic.goo_warlock_third,dnd_magic.goo_warlock_fourth,dnd_magic.goo_warlock_fifth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'],dnd_dict.character_dict['class_spells']['warlock']['fifth'])
            dnd_skills.fifth_swap(dnd_magic.goo_warlock_first,dnd_magic.goo_warlock_second,dnd_magic.goo_warlock_third,dnd_magic.goo_warlock_fourth,dnd_magic.goo_warlock_fifth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'],dnd_dict.character_dict['class_spells']['warlock']['fifth'])

        dnd_invocations.invocation_swap()
        dnd_invocations.invocations()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)

# Level 13
    if level == 13:

        dnd_skills.spell_add(dnd_magic.warlock_seventh,dnd_dict.character_dict['spells'],dnd_dict.character_dict['class_spells']['warlock']['seventh_level_arcanum'])

        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Archfey':
            dnd_skills.fifth_swap(dnd_magic.archfey_warlock_first,dnd_magic.archfey_warlock_second,dnd_magic.archfey_warlock_third,dnd_magic.archfey_warlock_fourth,dnd_magic.archfey_warlock_fifth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'],dnd_dict.character_dict['class_spells']['warlock']['fifth'])

        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Fiend':
            dnd_skills.fifth_swap(dnd_magic.fiend_warlock_first,dnd_magic.fiend_warlock_second,dnd_magic.fiend_warlock_third,dnd_magic.fiend_warlock_fourth,dnd_magic.fiend_warlock_fifth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'],dnd_dict.character_dict['class_spells']['warlock']['fifth'])

        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Great Old One':
            dnd_skills.fifth_swap(dnd_magic.goo_warlock_first,dnd_magic.goo_warlock_second,dnd_magic.goo_warlock_third,dnd_magic.goo_warlock_fourth,dnd_magic.goo_warlock_fifth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'],dnd_dict.character_dict['class_spells']['warlock']['fifth'])


        dnd_invocations.invocation_swap()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)

# Level 14
    if level == 14:

        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Archfey':
            dnd_skills.fifth_swap(dnd_magic.archfey_warlock_first,dnd_magic.archfey_warlock_second,dnd_magic.archfey_warlock_third,dnd_magic.archfey_warlock_fourth,dnd_magic.archfey_warlock_fifth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'],dnd_dict.character_dict['class_spells']['warlock']['fifth'])
            dnd_features.archfey_warlock14()

        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Fiend':
            dnd_skills.fifth_swap(dnd_magic.fiend_warlock_first,dnd_magic.fiend_warlock_second,dnd_magic.fiend_warlock_third,dnd_magic.fiend_warlock_fourth,dnd_magic.fiend_warlock_fifth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'],dnd_dict.character_dict['class_spells']['warlock']['fifth'])
            dnd_features.fiend_warlock14()

        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Great Old One':
            dnd_skills.fifth_swap(dnd_magic.goo_warlock_first,dnd_magic.goo_warlock_second,dnd_magic.goo_warlock_third,dnd_magic.goo_warlock_fourth,dnd_magic.goo_warlock_fifth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'],dnd_dict.character_dict['class_spells']['warlock']['fifth'])
            dnd_features.goo_warlock14()

        dnd_invocations.invocation_swap()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)

# Level 15
    if level == 15:

        dnd_skills.spell_add(dnd_magic.warlock_eighth,dnd_dict.character_dict['spells'],dnd_dict.character_dict['class_spells']['warlock']['eighth_level_arcanum'])

        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Archfey':
            dnd_skills.fifth_level(dnd_magic.archfey_warlock_first,dnd_magic.archfey_warlock_second,dnd_magic.archfey_warlock_third,dnd_magic.archfey_warlock_fourth,dnd_magic.archfey_warlock_fifth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'],dnd_dict.character_dict['class_spells']['warlock']['fifth'])
            dnd_skills.fifth_swap(dnd_magic.archfey_warlock_first,dnd_magic.archfey_warlock_second,dnd_magic.archfey_warlock_third,dnd_magic.archfey_warlock_fourth,dnd_magic.archfey_warlock_fifth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'],dnd_dict.character_dict['class_spells']['warlock']['fifth'])

        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Fiend':
            dnd_skills.fifth_level(dnd_magic.fiend_warlock_first,dnd_magic.fiend_warlock_second,dnd_magic.fiend_warlock_third,dnd_magic.fiend_warlock_fourth,dnd_magic.fiend_warlock_fifth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'],dnd_dict.character_dict['class_spells']['warlock']['fifth'])
            dnd_skills.fifth_swap(dnd_magic.fiend_warlock_first,dnd_magic.fiend_warlock_second,dnd_magic.fiend_warlock_third,dnd_magic.fiend_warlock_fourth,dnd_magic.fiend_warlock_fifth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'],dnd_dict.character_dict['class_spells']['warlock']['fifth'])



        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Great Old One':
            dnd_skills.fifth_level(dnd_magic.goo_warlock_first,dnd_magic.goo_warlock_second,dnd_magic.goo_warlock_third,dnd_magic.goo_warlock_fourth,dnd_magic.goo_warlock_fifth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'],dnd_dict.character_dict['class_spells']['warlock']['fifth'])
            dnd_skills.fifth_swap(dnd_magic.goo_warlock_first,dnd_magic.goo_warlock_second,dnd_magic.goo_warlock_third,dnd_magic.goo_warlock_fourth,dnd_magic.goo_warlock_fifth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'],dnd_dict.character_dict['class_spells']['warlock']['fifth'])



        dnd_invocations.invocation_swap()
        dnd_invocations.invocations()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)

# Level 16
    if level == 16:

        dnd_level_up.asi_or_feat()
        dnd_features.eldritch_versatility()

        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Archfey':
            dnd_skills.fifth_swap(dnd_magic.archfey_warlock_first,dnd_magic.archfey_warlock_second,dnd_magic.archfey_warlock_third,dnd_magic.archfey_warlock_fourth,dnd_magic.archfey_warlock_fifth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'],dnd_dict.character_dict['class_spells']['warlock']['fifth'])

        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Fiend':
            dnd_skills.fifth_swap(dnd_magic.fiend_warlock_first,dnd_magic.fiend_warlock_second,dnd_magic.fiend_warlock_third,dnd_magic.fiend_warlock_fourth,dnd_magic.fiend_warlock_fifth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'],dnd_dict.character_dict['class_spells']['warlock']['fifth'])

        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Great Old One':
            dnd_skills.fifth_swap(dnd_magic.goo_warlock_first,dnd_magic.goo_warlock_second,dnd_magic.goo_warlock_third,dnd_magic.goo_warlock_fourth,dnd_magic.goo_warlock_fifth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'],dnd_dict.character_dict['class_spells']['warlock']['fifth'])


        dnd_invocations.invocation_swap()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)

# Level 17
    if level == 17:

        dnd_skills.spell_add(dnd_magic.warlock_ninth,dnd_dict.character_dict['spells'],dnd_dict.character_dict['class_spells']['warlock']['ninth_level_arcanum'])

        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Archfey':
            dnd_skills.fifth_swap(dnd_magic.archfey_warlock_first,dnd_magic.archfey_warlock_second,dnd_magic.archfey_warlock_third,dnd_magic.archfey_warlock_fourth,dnd_magic.archfey_warlock_fifth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'],dnd_dict.character_dict['class_spells']['warlock']['fifth'])

        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Fiend':
            dnd_skills.fifth_swap(dnd_magic.fiend_warlock_first,dnd_magic.fiend_warlock_second,dnd_magic.fiend_warlock_third,dnd_magic.fiend_warlock_fourth,dnd_magic.fiend_warlock_fifth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'],dnd_dict.character_dict['class_spells']['warlock']['fifth'])

        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Great Old One':
            dnd_skills.fifth_swap(dnd_magic.goo_warlock_first,dnd_magic.goo_warlock_second,dnd_magic.goo_warlock_third,dnd_magic.goo_warlock_fourth,dnd_magic.goo_warlock_fifth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'],dnd_dict.character_dict['class_spells']['warlock']['fifth'])

        dnd_invocations.invocation_swap()
        dnd_dict.character_dict['pact_magic']['fifth'] = 4
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)

# Level 18
    if level == 18:

        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Archfey':
            dnd_skills.fifth_level(dnd_magic.archfey_warlock_first,dnd_magic.archfey_warlock_second,dnd_magic.archfey_warlock_third,dnd_magic.archfey_warlock_fourth,dnd_magic.archfey_warlock_fifth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'],dnd_dict.character_dict['class_spells']['warlock']['fifth'])
            dnd_skills.fifth_swap(dnd_magic.archfey_warlock_first,dnd_magic.archfey_warlock_second,dnd_magic.archfey_warlock_third,dnd_magic.archfey_warlock_fourth,dnd_magic.archfey_warlock_fifth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'],dnd_dict.character_dict['class_spells']['warlock']['fifth'])

        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Fiend':
            dnd_skills.fifth_level(dnd_magic.fiend_warlock_first,dnd_magic.fiend_warlock_second,dnd_magic.fiend_warlock_third,dnd_magic.fiend_warlock_fourth,dnd_magic.fiend_warlock_fifth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'],dnd_dict.character_dict['class_spells']['warlock']['fifth'])
            dnd_skills.fifth_swap(dnd_magic.fiend_warlock_first,dnd_magic.fiend_warlock_second,dnd_magic.fiend_warlock_third,dnd_magic.fiend_warlock_fourth,dnd_magic.fiend_warlock_fifth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'],dnd_dict.character_dict['class_spells']['warlock']['fifth'])



        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Great Old One':
            dnd_skills.fifth_level(dnd_magic.goo_warlock_first,dnd_magic.goo_warlock_second,dnd_magic.goo_warlock_third,dnd_magic.goo_warlock_fourth,dnd_magic.goo_warlock_fifth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'],dnd_dict.character_dict['class_spells']['warlock']['fifth'])
            dnd_skills.fifth_swap(dnd_magic.goo_warlock_first,dnd_magic.goo_warlock_second,dnd_magic.goo_warlock_third,dnd_magic.goo_warlock_fourth,dnd_magic.goo_warlock_fifth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'],dnd_dict.character_dict['class_spells']['warlock']['fifth'])




        dnd_invocations.invocation_swap()
        dnd_invocations.invocations()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)

# Level 19
    if level == 19:

        dnd_level_up.asi_or_feat()
        dnd_features.eldritch_versatility()
        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Archfey':
            dnd_skills.fifth_swap(dnd_magic.archfey_warlock_first,dnd_magic.archfey_warlock_second,dnd_magic.archfey_warlock_third,dnd_magic.archfey_warlock_fourth,dnd_magic.archfey_warlock_fifth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'],dnd_dict.character_dict['class_spells']['warlock']['fifth'])

        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Fiend':
            dnd_skills.fifth_swap(dnd_magic.fiend_warlock_first,dnd_magic.fiend_warlock_second,dnd_magic.fiend_warlock_third,dnd_magic.fiend_warlock_fourth,dnd_magic.fiend_warlock_fifth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'],dnd_dict.character_dict['class_spells']['warlock']['fifth'])

        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Great Old One':
            dnd_skills.fifth_swap(dnd_magic.goo_warlock_first,dnd_magic.goo_warlock_second,dnd_magic.goo_warlock_third,dnd_magic.goo_warlock_fourth,dnd_magic.goo_warlock_fifth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'],dnd_dict.character_dict['class_spells']['warlock']['fifth'])


        dnd_invocations.invocation_swap()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)

# Level 20
    if level == 20:

        dnd_features.warlock20()

        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Archfey':
            dnd_skills.fifth_swap(dnd_magic.archfey_warlock_first,dnd_magic.archfey_warlock_second,dnd_magic.archfey_warlock_third,dnd_magic.archfey_warlock_fourth,dnd_magic.archfey_warlock_fifth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'],dnd_dict.character_dict['class_spells']['warlock']['fifth'])

        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Fiend':
            dnd_skills.fifth_swap(dnd_magic.fiend_warlock_first,dnd_magic.fiend_warlock_second,dnd_magic.fiend_warlock_third,dnd_magic.fiend_warlock_fourth,dnd_magic.fiend_warlock_fifth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'],dnd_dict.character_dict['class_spells']['warlock']['fifth'])

        if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Great Old One':
            dnd_skills.fifth_swap(dnd_magic.goo_warlock_first,dnd_magic.goo_warlock_second,dnd_magic.goo_warlock_third,dnd_magic.goo_warlock_fourth,dnd_magic.goo_warlock_fifth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'],dnd_dict.character_dict['class_spells']['warlock']['fifth'])



        dnd_invocations.invocation_swap()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
