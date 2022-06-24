import dnd_dict, dnd_features, dnd_magic, dnd_skills, dnd_level_up

def cleric():
    level = dnd_dict.character_dict['player_class']['cleric']['class_level']

# Level 1
    if level == 1:

        armor_prof = {'light_armor':'Light Armor','medium_armor':'Medium Armor','shields':'Shields'}
        dnd_dict.character_dict['Armor_Prof'].update(armor_prof)

        while True:
            choice = input("""Select the subclass you want to have:
1) Knowledge Domain
2) Life Domain
3) Light Domain
4) Nature Domain
5) Tempest Domain
6) Trickery Domain
7) War Domain
Enter your selection: """)
            if choice == '1':
                dnd_features.knowledge_cleric1()
                break
    
            elif choice == '2':
                dnd_features.life_cleric1()
                break
    
            elif choice == '3':
                dnd_features.light_cleric1()
                break
    
            elif choice == '4':
                dnd_features.nature_cleric1()
                break
    
            elif choice == '5':
                dnd_features.tempest_cleric1()
                break
    
            elif choice == '6':
                dnd_features.trickery_cleric1()
                break
    
            elif choice == '7':
                dnd_features.war_cleric1()
                break
    
            else:
                print("Error: Invalid Input")
                continue
    
    
        dnd_magic.cleric_magic()
        spell_attack = ((dnd_dict.character_dict["Stats"]["wisdom"]['mod']) + dnd_dict.character_dict['prof_bonus'])
        dnd_dict.character_dict["spell_modifier"]['wisdom']['attack'] = spell_attack
        spell_save = ((dnd_dict.character_dict["Stats"]["wisdom"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
        dnd_dict.character_dict["spell_modifier"]['wisdom']['save'] = spell_save
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 2
    if level == 2:

        dnd_features.cleric2()
    
        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'Knowledge Domain':
            dnd_features.knowledge_cleric2()
    
        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'Life Domain':
            dnd_features.life_cleric2()
    
        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'Light Domain':
            dnd_features.light_cleric2()
    
        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'Nature Domain':
            dnd_features.nature_cleric2()
    
        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'Tempest Domain':
            dnd_features.tempest_cleric2()
    
        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'Trickery Domain':
            dnd_features.trickery_cleric2()
    
        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'War Domain':
            dnd_features.war_cleric2()
    
    
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 3
    if level == 3:

        dnd_magic.cleric_second()
    
        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'Knowledge Domain':
            dnd_features.knowledge_cleric3()
    
        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'Life Domain':
            dnd_features.life_cleric3()
    
        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'Light Domain':
            dnd_features.light_cleric3()
    
        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'Nature Domain':
            dnd_features.nature_cleric3()
    
        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'Tempest Domain':
            dnd_features.tempest_cleric3()
    
        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'Trickery Domain':
            dnd_features.trickery_cleric3()
    
        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'War Domain':
            dnd_features.war_cleric3()
    
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 4
    if level == 4:

        dnd_level_up.asi_or_feat()
        dnd_skills.spell_add(dnd_magic.cleric_cantrip,dnd_dict.character_dict['spells'],dnd_dict.character_dict['class_spells']['cleric_cantrips'])
        dnd_features.cantrip_versatility(dnd_magic.cleric_cantrip,dnd_dict.character_dict['spells'],dnd_dict.character_dict['class_spells']['cleric_cantrips'])
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 5
    if level == 5:

        dnd_magic.cleric_third()
    
        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'Knowledge Domain':
            dnd_features.knowledge_cleric5()
    
        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'Life Domain':
            dnd_features.life_cleric5()
    
        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'Light Domain':
            dnd_features.light_cleric5()
    
        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'Nature Domain':
            dnd_features.nature_cleric5()
    
        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'Tempest Domain':
            dnd_features.tempest_cleric5()
    
        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'Trickery Domain':
            dnd_features.trickery_cleric5()
    
        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'War Domain':
            dnd_features.war_cleric5()
    
        dnd_features.cleric5()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 6
    if level == 6:

        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'Knowledge Domain':
            dnd_features.knowledge_cleric6()
    
        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'Life Domain':
            dnd_features.life_cleric6()
    
        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'Light Domain':
            dnd_features.light_cleric6()
    
        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'Nature Domain':
            dnd_features.nature_cleric6()
    
        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'Tempest Domain':
            dnd_features.tempest_cleric6()
    
        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'Trickery Domain':
            dnd_features.trickery_cleric6()
    
        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'War Domain':
            dnd_features.war_cleric6()
    
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 7
    if level == 7:

        dnd_magic.cleric_fourth()
    
        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'Knowledge Domain':
            dnd_features.knowledge_cleric7()
    
        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'Life Domain':
            dnd_features.life_cleric7()
    
        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'Light Domain':
            dnd_features.light_cleric7()
    
        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'Nature Domain':
            dnd_features.nature_cleric7()
    
        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'Tempest Domain':
            dnd_features.tempest_cleric7()
    
        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'Trickery Domain':
            dnd_features.trickery_cleric7()
    
        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'War Domain':
            dnd_features.war_cleric7()
    
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 8
    if level == 8:

        dnd_level_up.asi_or_feat()
        dnd_features.cantrip_versatility(dnd_magic.cleric_cantrip,dnd_dict.character_dict['spells'],dnd_dict.character_dict['class_spells']['cleric_cantrips'])
    
        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'Knowledge Domain':
            dnd_features.knowledge_cleric8()
    
        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'Life Domain':
            dnd_features.life_cleric8()
    
        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'Light Domain':
            dnd_features.light_cleric8()
    
        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'Nature Domain':
            dnd_features.nature_cleric8()
    
        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'Tempest Domain':
            dnd_features.tempest_cleric8()
    
        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'Trickery Domain':
            dnd_features.trickery_cleric8()
    
        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'War Domain':
            dnd_features.war_cleric8()
    
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 9
    if level == 9:

        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'Knowledge Domain':
            dnd_features.knowledge_cleric9()
    
        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'Life Domain':
            dnd_features.life_cleric9()
    
        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'Light Domain':
            dnd_features.light_cleric9()
    
        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'Nature Domain':
            dnd_features.nature_cleric9()
    
        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'Tempest Domain':
            dnd_features.tempest_cleric9()
    
        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'Trickery Domain':
            dnd_features.trickery_cleric9()
    
        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'War Domain':
            dnd_features.war_cleric9()
    
        dnd_magic.cleric_fifth()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 10
    if level == 10:

        dnd_features.cleric10()
        dnd_skills.spell_add(dnd_magic.cleric_cantrip,dnd_dict.character_dict['spells'],dnd_dict.character_dict['class_spells']['cleric_cantrips'])
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 11
    if level == 11:

        dnd_magic.cleric_sixth()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 12
    if level == 12:

        dnd_level_up.asi_or_feat()
        dnd_features.cantrip_versatility(dnd_magic.cleric_cantrip,dnd_dict.character_dict['spells'],dnd_dict.character_dict['class_spells']['cleric_cantrips'])
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 13
    if level == 13:

        dnd_magic.cleric_seventh()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 14
    if level == 14:

        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 15
    if level == 15:

        dnd_magic.cleric_eighth()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 16
    if level == 16:

        dnd_level_up.asi_or_feat()
        dnd_features.cantrip_versatility(dnd_magic.cleric_cantrip,dnd_dict.character_dict['spells'],dnd_dict.character_dict['class_spells']['cleric_cantrips'])
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 17
    if level == 17:

        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'Knowledge Domain':
            dnd_features.knowledge_cleric17()
    
        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'Life Domain':
            dnd_features.life_cleric17()
    
        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'Light Domain':
            dnd_features.light_cleric17()
    
        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'Nature Domain':
            dnd_features.nature_cleric17()
    
        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'Tempest Domain':
            dnd_features.tempest_cleric17()
    
        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'Trickery Domain':
            dnd_features.trickery_cleric17()
    
        if dnd_dict.character_dict['player_class']['cleric']['subclass'] == 'War Domain':
            dnd_features.war_cleric17()
    
        dnd_magic.cleric_ninth()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 18
    if level == 18:

        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 19
    if level == 19:

        dnd_level_up.asi_or_feat()
        dnd_features.cantrip_versatility(dnd_magic.cleric_cantrip,dnd_dict.character_dict['spells'],dnd_dict.character_dict['class_spells']['cleric_cantrips'])
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()

# Level 20
    if level == 20:

        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['caster_level'] += 1
        dnd_skills.spell_slot_selection()








