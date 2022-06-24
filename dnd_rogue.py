import dnd_dict, dnd_features, dnd_magic, dnd_skills, dnd_level_up
def rogue():
    level = dnd_dict.character_dict['player_class']['rogue']['class_level']

# Level 1
    if level == 1:

        dnd_dict.character_dict['Armor_Prof']['light_armor'] = 'Light Armor'
        dnd_skills.rogue_skills()
        dnd_dict.character_dict['Kits']['thieves_tools'] = 'Thieves\' Tools'
        dnd_features.rogue_features()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)

# Level 2
    if level == 2:

        dnd_features.rogue2()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)

# Level 3
    if level == 3:

        while True:
            choice = input("""Select the subclass you want to have:
1) Arcane Trickster
2) Assassin
3) Thief
Enter your selection: """)
            if choice == '1':
                dnd_dict.character_dict['player_class']['rogue']['subclass'] = 'Arcane Trickster'
                dnd_features.arcane_trickster_rogue3()
                break

            elif choice == '2':
                dnd_dict.character_dict['player_class']['rogue']['subclass'] = 'Assassin'
                dnd_features.assassin_rogue3()
                break

            elif choice == '3':
                dnd_dict.character_dict['player_class']['rogue']['subclass'] = 'Thief'
                dnd_features.thief_rogue3()
                break

        dnd_features.rogue3()
        dnd_dict.character_dict['sneak_attack'] += 1
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)

# Level 4
    if level == 4:

        dnd_level_up.asi_or_feat()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
        dnd_dict.character_dict['semi_caster_level'] += 1
        if dnd_dict.character_dict['player_class']['rogue']['subclass'] == 'Arcane Trickster':
            dnd_skills.spell_add(dnd_magic.arcane_trickster_first,dnd_dict.character_dict['spells']['first'],dnd_dict.character_dict['class_spells']['rogue']['first'])
            dnd_skills.first_swap(dnd_magic.arcane_trickster_first,dnd_dict.character_dict['class_spells']['rogue']['first'])
            dnd_skills.spell_slot_selection()

# Level 5
    if level == 5:

        dnd_features.rogue5()
        if dnd_dict.character_dict['player_class']['rogue']['subclass'] == 'Arcane Trickster':
            dnd_skills.first_swap(dnd_magic.arcane_trickster_first,dnd_dict.character_dict['class_spells']['rogue']['first'])
            dnd_dict.character_dict['semi_caster_level'] += 1
            dnd_skills.spell_slot_selection()
        dnd_dict.character_dict['sneak_attack'] += 1
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)

# Level 6
    if level == 6:

        dnd_skills.expertise_choice()
        if dnd_dict.character_dict['player_class']['rogue']['subclass'] == 'Arcane Trickster':
            dnd_skills.first_swap(dnd_magic.arcane_trickster_first,dnd_dict.character_dict['class_spells']['rogue']['first'])
            dnd_dict.character_dict['semi_caster_level'] += 1
            dnd_skills.spell_slot_selection()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)

# Level 7
    if level == 7:

        dnd_features.rogue7()
        if dnd_dict.character_dict['player_class']['rogue']['subclass'] == 'Arcane Trickster':
            dnd_skills.first_swap(dnd_magic.arcane_trickster_first,dnd_dict.character_dict['class_spells']['rogue']['first'])
            dnd_skills.second_level(dnd_magic.arcane_trickster_first,dnd_magic.arcane_trickster_second,dnd_dict.character_dict['class_spells']['rogue']['first'],dnd_dict.character_dict['class_spells']['rogue']['second'])
            dnd_dict.character_dict['semi_caster_level'] += 1
            dnd_skills.spell_slot_selection()
        dnd_dict.character_dict['sneak_attack'] += 1
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)

# Level 8
    if level == 8:

        dnd_level_up.asi_or_feat()
        if dnd_dict.character_dict['player_class']['rogue']['subclass'] == 'Arcane Trickster':
            dnd_skills.second_swap(dnd_magic.arcane_trickster_first,dnd_magic.arcane_trickster_second,dnd_dict.character_dict['class_spells']['rogue']['first'],dnd_dict.character_dict['class_spells']['rogue']['second'])
            dnd_skills.second_level(dnd_magic.wizard_first,dnd_magic.wizard_second,dnd_dict.character_dict['class_spells']['rogue_special']['first'],dnd_dict.character_dict['class_spells']['rogue_special']['second'])
            dnd_dict.character_dict['semi_caster_level'] += 1
            dnd_skills.spell_slot_selection()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)

# Level 9
    if level == 9:

        if dnd_dict.character_dict['player_class']['rogue']['subclass'] == 'Arcane Trickster':
            dnd_features.rogue_spell_swap_second()
            dnd_dict.character_dict['semi_caster_level'] += 1
            dnd_skills.spell_slot_selection()
            dnd_features.arcane_trickster_rogue9()

        if dnd_dict.character_dict['player_class']['rogue']['subclass'] == 'Assassin':
            dnd_features.assassin_rogue9()

        if dnd_dict.character_dict['player_class']['rogue']['subclass'] == 'Thief':
            dnd_features.thief_rogue9()

        dnd_dict.character_dict['sneak_attack'] += 1
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)

# Level 10
    if level == 10:

        dnd_level_up.asi_or_feat()
        if dnd_dict.character_dict['player_class']['rogue']['subclass'] == 'Arcane Trickster':
            dnd_features.rogue_spell_swap_second()
            dnd_skills.spell_add(dnd_magic.wizard_cantrip,dnd_dict.character_dict['spells']['cantrips'],dnd_dict.character_dict['class_spells']['rogue_cantrips'])
            dnd_skills.second_level(dnd_magic.arcane_trickster_first,dnd_magic.arcane_trickster_second,dnd_dict.character_dict['class_spells']['rogue']['first'],dnd_dict.character_dict['class_spells']['rogue']['second'])
            dnd_dict.character_dict['semi_caster_level'] += 1
            dnd_skills.spell_slot_selection()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)

# Level 11
    if level == 11:

        dnd_features.rogue11()
        if dnd_dict.character_dict['player_class']['rogue']['subclass'] == 'Arcane Trickster':
            dnd_features.rogue_spell_swap_second()
            dnd_skills.second_level(dnd_magic.arcane_trickster_first,dnd_magic.arcane_trickster_second,dnd_dict.character_dict['class_spells']['rogue']['first'],dnd_dict.character_dict['class_spells']['rogue']['second'])
            dnd_dict.character_dict['semi_caster_level'] += 1
            dnd_skills.spell_slot_selection()
        dnd_dict.character_dict['sneak_attack'] += 1
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)

# Level 12
    if level == 12:

        dnd_level_up.asi_or_feat()
        if dnd_dict.character_dict['player_class']['rogue']['subclass'] == 'Arcane Trickster':
            dnd_features.rogue_spell_swap_second()
            dnd_dict.character_dict['semi_caster_level'] += 2
            dnd_skills.spell_slot_selection()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)

# Level 13
    if level == 13:

        if dnd_dict.character_dict['player_class']['rogue']['subclass'] == 'Arcane Trickster':
            dnd_features.arcane_trickster_rogue13()
            dnd_features.rogue_spell_swap_second()
            dnd_skills.third_level(dnd_magic.arcane_trickster_first,dnd_magic.arcane_trickster_second,dnd_magic.arcane_trickster_third,dnd_dict.character_dict['class_spells']['rogue']['first'],dnd_dict.character_dict['class_spells']['rogue']['second'],dnd_dict.character_dict['class_spells']['rogue']['third'])
            dnd_dict.character_dict['semi_caster_level'] += 1
            dnd_skills.spell_slot_selection()

        if dnd_dict.character_dict['player_class']['rogue']['subclass'] == 'Assassin':
            dnd_features.assassin_rogue13()

        if dnd_dict.character_dict['player_class']['rogue']['subclass'] == 'Thief':
            dnd_features.thief_rogue13()

        dnd_dict.character_dict['sneak_attack'] += 1
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)

# Level 14
    if level == 14:

        dnd_features.rogue14()
        if dnd_dict.character_dict['player_class']['rogue']['subclass'] == 'Arcane Trickster':
            dnd_features.rogue_spell_swap_third_early()
            dnd_skills.third_level(dnd_magic.wizard_first,dnd_magic.wizard_second,dnd_magic.wizard_third,dnd_dict.character_dict['class_spells']['rogue_special']['first'],dnd_dict.character_dict['class_spells']['rogue_special']['second'],dnd_dict.character_dict['class_spells']['rogue_special']['third'])
            dnd_dict.character_dict['semi_caster_level'] += 1
            dnd_skills.spell_slot_selection()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)

# Level 15
    if level == 15:

        dnd_features.rogue15()
        if dnd_dict.character_dict['player_class']['rogue']['subclass'] == 'Arcane Trickster':
            dnd_features.rogue_spell_swap_third()
            dnd_dict.character_dict['semi_caster_level'] += 1
            dnd_skills.spell_slot_selection()
        dnd_dict.character_dict['sneak_attack'] += 1
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)

# Level 16
    if level == 16:

        dnd_level_up.asi_or_feat()
        if dnd_dict.character_dict['player_class']['rogue']['subclass'] == 'Arcane Trickster':
            dnd_features.rogue_spell_swap_third()
            dnd_skills.third_level(dnd_magic.arcane_trickster_first,dnd_magic.arcane_trickster_second,dnd_magic.arcane_trickster_third,dnd_dict.character_dict['class_spells']['rogue']['first'],dnd_dict.character_dict['class_spells']['rogue']['second'],dnd_dict.character_dict['class_spells']['rogue']['third'])
            dnd_dict.character_dict['semi_caster_level'] += 1
            dnd_skills.spell_slot_selection()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)

# Level 17
    if level == 17:

        if dnd_dict.character_dict['player_class']['rogue']['subclass'] == 'Arcane Trickster':
            dnd_features.rogue_spell_swap_third()
            dnd_dict.character_dict['semi_caster_level'] += 1
            dnd_skills.spell_slot_selection()
            dnd_features.arcane_trickster_rogue17()

        if dnd_dict.character_dict['player_class']['rogue']['subclass'] == 'Assassin':
            dnd_features.assassin_rogue17()

        if dnd_dict.character_dict['player_class']['rogue']['subclass'] == 'Thief':
            dnd_features.thief_rogue17()

        dnd_dict.character_dict['sneak_attack'] += 1
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)

# Level 18
    if level == 18:

        dnd_features.rogue18()
        if dnd_dict.character_dict['player_class']['rogue']['subclass'] == 'Arcane Trickster':
            dnd_features.rogue_spell_swap_third()
            dnd_dict.character_dict['semi_caster_level'] += 1
            dnd_skills.spell_slot_selection()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)

# Level 19
    if level == 19:

        dnd_level_up.asi_or_feat()
        if dnd_dict.character_dict['player_class']['rogue']['subclass'] == 'Arcane Trickster':
            dnd_features.rogue_spell_swap_third()
            dnd_skills.fourth_level(dnd_magic.arcane_trickster_first,dnd_magic.arcane_trickster_second,dnd_magic.arcane_trickster_third,dnd_magic.arcane_trickster_fourth,dnd_dict.character_dict['class_spells']['rogue']['first'],dnd_dict.character_dict['class_spells']['rogue']['second'],dnd_dict.character_dict['class_spells']['rogue']['third'],dnd_dict.character_dict['class_spells']['rogue']['fourth'])
            dnd_dict.character_dict['semi_caster_level'] += 1
            dnd_skills.spell_slot_selection()
        dnd_dict.character_dict['sneak_attack'] += 1
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)

# Level 20
    if level == 20:

        dnd_features.rogue20()
        if dnd_dict.character_dict['player_class']['rogue']['subclass'] == 'Arcane Trickster':
            dnd_features.rogue_spell_swap_fourth()
            dnd_skills.fourth_level(dnd_magic.wizard_first,dnd_magic.wizard_second,dnd_magic.wizard_third,dnd_magic.wizard_fourth,dnd_dict.character_dict['class_spells']['rogue_special']['first'],dnd_dict.character_dict['class_spells']['rogue_special']['second'],dnd_dict.character_dict['class_spells']['rogue_special']['third'],dnd_dict.character_dict['class_spells']['rogue_special']['fourth'])
            dnd_dict.character_dict['semi_caster_level'] += 1
            dnd_skills.spell_slot_selection()
        dnd_dict.character_dict['d8'] += 1
        dnd_level_up.level_up(8)
