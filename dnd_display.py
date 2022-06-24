#!/usr/bin/python3
import os, stat_roller, dnd_features, dnd_language, dnd_tools, dnd_dict, dnd_skills, dnd_race, dnd_class, dnd_background, dnd_magic, json,dnd_save_load,tabulate
from tabulate import tabulate

# Print out Stats
def stat_table():
    strength = dnd_dict.character_dict['Stats']['strength']
    dex = dnd_dict.character_dict['Stats']['dexterity']
    con = dnd_dict.character_dict['Stats']['constitution']
    intel = dnd_dict.character_dict['Stats']['intelligence']
    wis = dnd_dict.character_dict['Stats']['wisdom']
    cha = dnd_dict.character_dict['Stats']['charisma']
    stat_list = []
# Note if you have proficiency in a saving throw
# Expertise is just to fill out the class
    strength_list = ['Strength',strength['base'],strength['mod'],dnd_class.Character.show_prof(strength['save'],'strength',dnd_dict.character_dict['expertise'],dnd_dict.character_dict['saving_throws'])]
    stat_list.append(strength_list)

    dex_list = ['Dexterity',dex['base'],dex['mod'],dnd_class.Character.show_prof(dex['save'],'dexterity',dnd_dict.character_dict['expertise'],dnd_dict.character_dict['saving_throws'])]
    stat_list.append(dex_list)

    con_list = ['Constitution',con['base'],con['mod'],dnd_class.Character.show_prof(con['save'],'constitution',dnd_dict.character_dict['expertise'],dnd_dict.character_dict['saving_throws'])]
    stat_list.append(con_list)

    int_list = ['Intelligence',intel['base'],intel['mod'],dnd_class.Character.show_prof(intel['save'],'intelligence',dnd_dict.character_dict['expertise'],dnd_dict.character_dict['saving_throws'])]
    stat_list.append(int_list)

    wis_list = ['Wisdom',wis['base'],wis['mod'],dnd_class.Character.show_prof(wis['save'],'wisdom',dnd_dict.character_dict['expertise'],dnd_dict.character_dict['saving_throws'])]
    stat_list.append(wis_list)

    cha_list = ['Charisma',cha['base'],cha['mod'],dnd_class.Character.show_prof(cha['save'],'charisma',dnd_dict.character_dict['expertise'],dnd_dict.character_dict['saving_throws'])]
    stat_list.append(cha_list)

    print((tabulate(stat_list, headers = ['Stat','Score','Mod','Save'],tablefmt = 'psql')))


# Displays the skills
def skill_table():
    skill_list = []
    acr_list = ["Acrobatics",dnd_class.Character.show_prof(dnd_dict.character_dict.get("acrobatics"),'acrobatics',dnd_dict.character_dict.get('expertise'),dnd_dict.character_dict.get('skill_prof'))]
    skill_list.append(acr_list)

    anm_list = ["Animal Handling",dnd_class.Character.show_prof(dnd_dict.character_dict.get("animal_handling"),'animal_handling',dnd_dict.character_dict.get('expertise'),dnd_dict.character_dict.get('skill_prof'))]
    skill_list.append(anm_list)

    arc_list = ["Arcana",dnd_class.Character.show_prof(dnd_dict.character_dict.get("arcana"),'arcana',dnd_dict.character_dict.get('expertise'),dnd_dict.character_dict.get('skill_prof'))]
    skill_list.append(arc_list)

    ath_list = ["Athletics",dnd_class.Character.show_prof(dnd_dict.character_dict.get("athletics"),'athletics',dnd_dict.character_dict.get('expertise'),dnd_dict.character_dict.get('skill_prof'))]
    skill_list.append(ath_list)

    dec_list = ["Deception",dnd_class.Character.show_prof(dnd_dict.character_dict.get("deception"),'deception',dnd_dict.character_dict.get('expertise'),dnd_dict.character_dict.get('skill_prof'))]
    skill_list.append(dec_list)

    his_list = ["History",dnd_class.Character.show_prof(dnd_dict.character_dict.get("history"),'history',dnd_dict.character_dict.get('expertise'),dnd_dict.character_dict.get('skill_prof'))]
    skill_list.append(his_list)

    ins_list = ["Insight",dnd_class.Character.show_prof(dnd_dict.character_dict.get("insight"),'insight',dnd_dict.character_dict.get('expertise'),dnd_dict.character_dict.get('skill_prof'))]
    skill_list.append(ins_list)

    int_list = ["Intimidation",dnd_class.Character.show_prof(dnd_dict.character_dict.get("intimidation"),'intimidation',dnd_dict.character_dict.get('expertise'),dnd_dict.character_dict.get('skill_prof'))]
    skill_list.append(int_list)

    inv_list = ["Investigation",dnd_class.Character.show_prof(dnd_dict.character_dict.get("investigation"),'investigation',dnd_dict.character_dict.get('expertise'),dnd_dict.character_dict.get('skill_prof'))]
    skill_list.append(inv_list)

    med_list = ["Medicine",dnd_class.Character.show_prof(dnd_dict.character_dict.get("medicine"),'medicine',dnd_dict.character_dict.get('expertise'),dnd_dict.character_dict.get('skill_prof'))]
    skill_list.append(med_list)

    nat_list = ["Nature",dnd_class.Character.show_prof(dnd_dict.character_dict.get("nature"),'nature',dnd_dict.character_dict.get('expertise'),dnd_dict.character_dict.get('skill_prof'))]
    skill_list.append(nat_list)

    prc_list = ["Perception",dnd_class.Character.show_prof(dnd_dict.character_dict.get("perception"),'perception',dnd_dict.character_dict.get('expertise'),dnd_dict.character_dict.get('skill_prof'))]
    skill_list.append(prc_list)

    prf_list = ["Performance",dnd_class.Character.show_prof(dnd_dict.character_dict.get("performance"),'performance',dnd_dict.character_dict.get('expertise'),dnd_dict.character_dict.get('skill_prof'))]
    skill_list.append(prf_list)

    per_list = ["Persuasion",dnd_class.Character.show_prof(dnd_dict.character_dict.get("persuasion"),'persuasion',dnd_dict.character_dict.get('expertise'),dnd_dict.character_dict.get('skill_prof'))]
    skill_list.append(per_list)

    rel_list = ["Religion",dnd_class.Character.show_prof(dnd_dict.character_dict.get("religion"),'religion',dnd_dict.character_dict.get('expertise'),dnd_dict.character_dict.get('skill_prof'))]
    skill_list.append(rel_list)

    soh_list = ["Sleight of Hand",dnd_class.Character.show_prof(dnd_dict.character_dict.get("sleight_of_hand"),'sleight_of_hand',dnd_dict.character_dict.get('expertise'),dnd_dict.character_dict.get('skill_prof'))]
    skill_list.append(soh_list)

    stl_list = ["Stealth",dnd_class.Character.show_prof(dnd_dict.character_dict.get("stealth"),'stealth',dnd_dict.character_dict.get('expertise'),dnd_dict.character_dict.get('skill_prof'))]
    skill_list.append(stl_list)

    sur_list = ["Survival",dnd_class.Character.show_prof(dnd_dict.character_dict.get("survival"),'survival',dnd_dict.character_dict.get('expertise'),dnd_dict.character_dict.get('skill_prof'))]
    skill_list.append(sur_list)

    print((tabulate(skill_list,headers = ['Skill','Score'],tablefmt = 'psql')))

# Displays proficiencies with Tools, Kits, Vehicles, Gaming Sets, and Instruments
def tool_prof_display():
    tool_list = []
    if dnd_dict.character_dict["Tools"]:
        tool_prof = ['Tool Proficiencies',', '.join(dnd_dict.character_dict['Tools'].values()) ]
#{', '.join(dnd_dict.character_dict['Tools'].values())}
        tool_list.append(tool_prof)

    if dnd_dict.character_dict["tool_expertise"]:
        tool_expertise = ['Tool Expertise',', '.join(dnd_dict.character_dict['tool_expertise'].values())]
        tool_list.append(tool_expertise)

    if dnd_dict.character_dict["Kits"]:
        kit_list = ['Kit Proficiencies',', '.join( dnd_dict.character_dict['Kits'].values())]
        tool_list.append(kit_list)

    if dnd_dict.character_dict["Vehicles"]:
        vhc_list = ['Vehicle Proficiencies',', '.join(dnd_dict.character_dict['Vehicles'].values())]
        tool_list.append(vhc_list)

    if dnd_dict.character_dict["Gaming_Set"]:
        gms_list = ['Gaming Set Proficiencies',', '.join(dnd_dict.character_dict['Gaming_Set'].values())]
        tool_list.append(gms_list)

    if dnd_dict.character_dict["Instruments"]:
        ins_list = ['Instrument Proficiencies',', '.join(dnd_dict.character_dict['Instruments'].values())]
        tool_list.append(ins_list)

    if dnd_dict.character_dict['Tools'] or dnd_dict.character_dict['tool_expertise'] or dnd_dict.character_dict['Kits'] or dnd_dict.character_dict['Vehicles'] or dnd_dict.character_dict['Gaming_Set'] or dnd_dict.character_dict['Instruments']:
        print((tabulate(tool_list,tablefmt = 'grid')))

# Item Display
def item_display():
    item_list = []
    equip_list = ["Equipment", ', '.join(dnd_dict.character_dict['Equipment'].values())]
    item_list.append(equip_list)
    misc_list = ["Misc. Items", ', '.join(dnd_dict.character_dict['Misc'].values())]
    item_list.append(misc_list)
    print((tabulate(item_list,tablefmt = 'grid')))

# Displays the attack rolls and saving throws
def spell_table():
    con = dnd_dict.character_dict['spell_modifier']['constitution']
    intel = dnd_dict.character_dict['spell_modifier']['intelligence']
    wis = dnd_dict.character_dict['spell_modifier']['wisdom']
    cha = dnd_dict.character_dict['spell_modifier']['charisma']
    ki = dnd_dict.character_dict['spell_modifier']['ki_save']
    stat_list = []
    if con["attack"] > 0:
        con_attack = ["Constitution",con['attack'],con['save']]
        stat_list.append(con_attack)


    if intel["save"] > 0:
        intel_attack = ["Intelligence",intel['attack'],intel['save']]
        stat_list.append(intel_attack)


    if wis["save"] > 0:
        wis_attack = ["Wisdom",wis['attack'],wis['save']]
        stat_list.append(wis_attack)


    if ki > 0:
        ki_save = ["Ki",'N/A',ki]


    if cha["save"] > 0:
        cha_attack = ["Charisma",cha['attack'],cha['save']]
        stat_list.append(cha_attack)

    if con['attack'] > 0 or intel['attack'] > 0 or intel['save'] > 0 or wis['attack'] > 0 or wis['save'] > 0 or cha['attack'] > 0 or cha['save'] > 0:
        print((tabulate(stat_list,headers = ['Stat', 'Attack Modifier','Save DC'],tablefmt = 'psql')))

# Displays the spell slots and pact magic
def spell_slot_display():
    spell_slot = dnd_dict.character_dict['spell_slots']
    pact_magic = dnd_dict.character_dict['pact_magic']
    slot_list = []

    first_level = ['First Level Spell Slot',spell_slot['first']]
    slot_list.append(first_level)

    second_level = ['Second Level Spell Slot',spell_slot['second']]
    slot_list.append(second_level)

    third_level = ['Third Level Spell Slot',spell_slot['third']]
    slot_list.append(third_level)

    fourth_level = ['Fourth Level Spell Slot',spell_slot['fourth']]
    slot_list.append(fourth_level)

    fifth_level = ['Fifth Level Spell Slot',spell_slot['fifth']]
    slot_list.append(fifth_level)

    sixth_level = ['Sixth Level Spell Slot',spell_slot['sixth']]
    slot_list.append(sixth_level)

    seventh_level = ['Seventh Level Spell Slot',spell_slot['seventh']]
    slot_list.append(seventh_level)

    eighth_level = ['Eighth Level Spell Slot',spell_slot['eighth']]
    slot_list.append(eighth_level)

    ninth_level = ['Ninth Level Spell Slot',spell_slot['ninth']]
    slot_list.append(ninth_level)

# Separate the two types of slots
    pact_list = []

    first_pact = ['First Level Pact Magic',pact_magic['first']]
    pact_list.append(first_pact)

    second_pact = ['Second Level Pact Magic',pact_magic['second']]
    pact_list.append(second_pact)

    third_pact = ['Third Level Pact Magic',pact_magic['third']]
    pact_list.append(third_pact)

    fourth_pact = ['Fourth Level Pact Magic',pact_magic['fourth']]
    pact_list.append(fourth_pact)

    fifth_pact = ['Fifth Level Pact Magic',pact_magic['fifth']]
    pact_list.append(fifth_pact)

    print((tabulate(slot_list,headers = ['Spell Slot','Amount'],tablefmt = 'psql')))
    print((tabulate(pact_list,headers = ['Pact Magic','Amount'],tablefmt = 'psql')))

# Display any armor equipped
def armor_display():
    armor_list = []
    armor_dict = dnd_dict.character_dict

    if armor_dict['chest_armor']:
        chest_armor = ['Chest Armor',armor_dict['chest_armor']]
        armor_list.append(chest_armor)

    if armor_dict['shield']:
        shield = ['Shield',armor_dict['shield']]
        armor_list.append(shield)

    if armor_dict['boots']:
        boots = ['Boots',armor_dict['boots']]
        armor_list.append(boots)

    if armor_dict['bracers']:
        bracers = ['Bracers',armor_dict['bracers']]
        armor_list.append(bracers)

    if armor_dict['chest_armor'] or armor_dict['shield'] or armor_dict['boots'] or armor_dict['bracers']:
        print((tabulate(armor_list,headers = ['Armor Type', 'Armor Equipped'],tablefmt = 'psql')))

# Displays any spells known
def display_magic():
    spell_list = []
    spell_dict = dnd_dict.character_dict['spells']
    if spell_dict['cantrips']:
        if dnd_dict.character_dict['special_spells']['tome_cantrips']: 
            full_dict = {**dnd_dict.character_dict['spells']['cantrips'], **dnd_dict.character_dict['special_spells']['tome_cantrips']}
            first = ['Cantrips',', '.join(full_dict.values())]
            spell_list.append(first)
        else:
            cantrips = ['Cantrips',', '.join(spell_dict['cantrips'].values())]
            spell_list.append(cantrips)



    if spell_dict['first']:
# Combines the dictionaries if you have spells from the Book of Ancient Secrets invocation
        if dnd_dict.character_dict['special_spells']['tome_ritual']: 
            full_dict = {**dnd_dict.character_dict['spells'], **dnd_dict.character_dict['special_spells']['tome_ritual']}
            first = ['First Level',', '.join(full_dict.values())]
            spell_list.append(first)
        else:
            first = ['First Level',', '.join(spell_dict['first'].values())]
            spell_list.append(first)


    if spell_dict['second']:
        second = ['Second Level',', '.join(spell_dict['second'].values())]
        spell_list.append(second)

    if spell_dict['third']:
        third = ['Third Level',', '.join(spell_dict['third'].values())]
        spell_list.append(third)

    if spell_dict['fourth']:
        fourth = ['Fourth Level',', '.join(spell_dict['fourth'].values())]
        spell_list.append(fourth)

    if spell_dict['fifth']:
        fifth = ['Fifth Level',', '.join(spell_dict['fifth'].values())]
        spell_list.append(fifth)

    if spell_dict['sixth']:
        sixth = ['Sixth Level',', '.join(spell_dict['sixth'].values())]
        spell_list.append(sixth)

    if spell_dict['seventh']:
        seventh = ['Seventh Level',', '.join(spell_dict['seventh'].values())]
        spell_list.append(seventh)

    if spell_dict['eighth']:
        eighth = ['Eighth Level',', '.join(spell_dict['eighth'].values())]
        spell_list.append(eighth)

    if spell_dict['ninth']:
        ninth = ['Ninth Level',', '.join(spell_dict['ninth'].values())]
        spell_list.append(ninth)


    if dnd_dict.character_dict['class_spells']['warlock']['sixth_level_arcanum']:
        ninth = ['Ninth Level',', '.join(spell_dict['ninth'].values())]
        spell_list.append(ninth)

    if dnd_dict.character_dict['class_spells']['warlock']['sixth_level_arcanum']:
        arc_six = ['Sixth Level Arcanum',', '.join(dnd_dict.character_dict['class_spells']['warlock']['sixth_level_arcanum'].values())]
        spell_list.append(arc_six)

    if dnd_dict.character_dict['class_spells']['warlock']['seventh_level_arcanum']:
        arc_seven = ['Seventh Level Arcanum',', '.join(dnd_dict.character_dict['class_spells']['warlock']['seventh_level_arcanum'].values())]
        spell_list.append(arc_seven)

    if dnd_dict.character_dict['class_spells']['warlock']['eighth_level_arcanum']:
        arc_eight = ['Eighth Level Arcanum',', '.join(dnd_dict.character_dict['class_spells']['warlock']['eighth_level_arcanum'].values())]
        spell_list.append(arc_eight)

    if dnd_dict.character_dict['class_spells']['warlock']['ninth_level_arcanum']:
        arc_nine = ['Ninth Level Arcanum',', '.join(dnd_dict.character_dict['class_spells']['warlock']['ninth_level_arcanum'].values())]
        spell_list.append(arc_nine)


# Checks to make sure you have a spell
    if spell_dict['cantrips'] or spell_dict['first']:
        print((tabulate(spell_list,headers = ['Level', 'Spell'],tablefmt = 'grid')))

# Displays the gold value in gold, silver, and copper pieces.
# 10 copper = 1 silver, 10 silver = 1 gold
def gold_display():
    value = dnd_dict.character_dict['gold']
# Displays the gold value at 2 decimal places
    res = "{:.2f}".format(value)
# Display up until the third last value (before the decimal point)
    gold = res[:-3]
# Display the silver value, which is 1/10th the value of gold and will always be at the second last entry
    silver = res[-2]
    copper = res[-1]
    print("gp: {} sp: {} cp: {}".format(gold,silver,copper))

# Used to check if a value is positive or negative.
# If positive, add a plus sign, otherwise do nothing
def check_positive(stat):
    if stat > 0:
        return f'+ {stat}'
    elif stat < 0:
        return f'{stat}'
    else:
        return '+ 0'

# Used to check if a value is positive or negative.
# If positive, add a plus sign, otherwise do nothing.
# Add parenthesis around the total
# "Value" is if the Proficiency Bonus is added. Otherwise, put 0
def check_positive_prof(stat,value):
    total = stat + value
    if total > 0:
        return f'+ {total}'
    elif total < 0:
        return f'{total}'
    elif total == 0:
        return '+ 0'

# Used to check if the damage type for a Versatile weapon should use Strength or Dexterity
def check_damage():
    strength = dnd_dict.character_dict['Stats']['strength']['mod']
    dexterity = dnd_dict.character_dict['Stats']['dexterity']['mod']
    if strength > dexterity:
        if strength > 0:
            return f'+ {strength}'
        elif strength < 0:
            return f'{strength}'
        else:
            return "+ 0"

    elif dexterity > strength:
        if dexterity > 0:
            return f'+ {dexterity}'
        elif dexterity < 0:
            return f'{dexterity}'
        else:
            return "+ 0"

    else:
        if dexterity > 0:
            return f'+ {dexterity}'
        elif dexterity < 0:
            return f'{dexterity}'
        else:
            return "+ 0"

# Used to check if the hit bonus for a Versatile weapon should use Strength or Dexterity. If the character is not proficient, set bonus to 0
def versatile_hit(bonus):
    strength = dnd_dict.character_dict['Stats']['strength']['mod'] + bonus
    dexterity = dnd_dict.character_dict['Stats']['dexterity']['mod'] + bonus
    if strength > dexterity:
        if strength > 0:
            return f'+ {strength}'
        elif strength < 0:
            return f'{strength}'
        else:
            return "+ 0"

    elif dexterity > strength:
        if dexterity > 0:
            return f'+ {dexterity}'
        elif dexterity < 0:
            return f'{dexterity}'
        else:
            return "+ 0"

    else:
        if dexterity > 0:
            return f'+ {dexterity}'
        elif dexterity < 0:
            return f'{dexterity}'
        else:
            return "+ 0"

    

# Used to display the hit and attack values of the weapons.
# Add weapons as needed
def weapon_display():
    weapon_prof = dnd_dict.character_dict['Weapon_Prof']
    weapons = dnd_dict.character_dict['weapons']
    strength = dnd_dict.character_dict['Stats']['strength']['mod']
    dexterity = dnd_dict.character_dict['Stats']['dexterity']['mod']
    prof = dnd_dict.character_dict['prof_bonus']
    str_prof = check_positive_prof(strength,prof)
    dex_prof = check_positive_prof(dexterity,prof)
# Used if the stats have no proficiency bonus
    str_not_prof = check_positive_prof(strength,0)
    dex_not_prof = check_positive_prof(dexterity,0)
    vers_prof = versatile_hit(prof)
    vers_not_prof = versatile_hit(0)
    str_damage = check_positive(strength)
    dex_damage = check_positive(dexterity)
    simple = 'simple_weapons'
    martial = 'martial_weapons'
    martial_arts = dnd_dict.character_dict['martial_arts']
#    weapon_list = [['Weapon','Attack Bonus','Damage/Type','Properties']]
    weapon_list = []

# Simple Melee Weapons
    if 'club' in weapons:
        if simple in weapon_prof or 'clubs' in weapon_prof:
            damage_type = f'1d4 {str_prof} Bludgeoning'
            new_list = ['Club',check_positive_prof(strength,prof),damage_type,'Light']
            weapon_list.append(new_list)           

        elif simple not in weapon_prof and 'clubs' not in weapon_prof:
            damage_type = f'1d4 {str_not_prof} Bludgeoning'
            new_list = ['Club',str_damage,damage_type,'Light']
            weapon_list.append(new_list)           


    if 'dagger' in weapons:
        if simple in weapon_prof or 'daggers' in weapon_prof:
            damage_type = f'1d4 {check_damage()} Piercing'
            new_list = ['Dagger',vers_prof,damage_type,'Finesse, light, thrown (range 20/60)']
            weapon_list.append(new_list)           

        elif simple not in weapon_prof and 'daggers' not in weapon_prof:
            damage_type = f'1d4 {check_damage()} Piercing'
            new_list = ['Dagger',vers_not_prof,damage_type,'Finesse, light, thrown (range 20/60)']
            weapon_list.append(new_list)           


    if 'greatclub' in weapons:
        if simple in weapon_prof or 'greatclubs' in weapon_prof:
            damage_type = f'1d8 {str_prof} Bludgeoning'
            new_list = ['Greatclub',check_positive_prof(strength,prof),damage_type,'Two-handed']
            weapon_list.append(new_list)           

        elif simple not in weapon_prof and 'greatclubs' not in weapon_prof:
            damage_type = f'1d8 {str_not_prof} Bludgeoning'
            new_list = ['Greatclub',str_damage,damage_type,'Two-handed']
            weapon_list.append(new_list)           


    if 'handaxe' in weapons:
        if simple in weapon_prof or 'handaxes' in weapon_prof:
            damage_type = f'1d6 {str_prof} Slashing'
            new_list = ['Handaxe',check_positive_prof(strength,prof),damage_type,'Light, thrown (range 20/60)']
            weapon_list.append(new_list)           

        elif simple not in weapon_prof and 'handaxes' not in weapon_prof:
            damage_type = f'1d6 {str_not_prof} Slashing'
            new_list = ['Handaxe',str_damage,damage_type,'Light, thrown (range 20/60)']
            weapon_list.append(new_list)           


    if 'javelin' in weapons:
        if simple in weapon_prof or 'javelins' in weapon_prof:
            damage_type = f'1d6 {str_prof} Piercing'
            new_list = ['Javelin',check_positive_prof(strength,prof),damage_type,'Thrown (range 30/120)']
            weapon_list.append(new_list)           

        elif simple not in weapon_prof and 'javelins' not in weapon_prof:
            damage_type = f'1d6 {str_not_prof} Piercing'
            new_list = ['Javelin',str_damage,damage_type,'Thrown (range 30/120)']
            weapon_list.append(new_list)           


    if 'light_hammer' in weapons:
        if simple in weapon_prof or 'light_hammers' in weapon_prof:
            damage_type = f'1d4 {str_prof} Bludgeoning'
            new_list = ['Light Hammer',check_positive_prof(strength,prof),damage_type,'Light, thrown (range 20/60)']
            weapon_list.append(new_list)           

        elif simple not in weapon_prof and 'light_hammers' not in weapon_prof:
            damage_type = f'1d4 {str_not_prof} Bludgeoning'
            new_list = ['Light Hammer',str_damage,damage_type,'Light, thrown (range 20/60)']
            weapon_list.append(new_list)           


    if 'mace' in weapons:
        if simple in weapon_prof or 'maces' in weapon_prof:
            damage_type = f'1d6 {str_prof} Bludgeoning'
            new_list = ['Mace',check_positive_prof(strength,prof),damage_type,'None']
            weapon_list.append(new_list)           

        elif simple not in weapon_prof and 'maces' not in weapon_prof:
            damage_type = f'1d6 {str_not_prof} Bludgeoning'
            new_list = ['Mace',str_damage,damage_type,'None']
            weapon_list.append(new_list)           


    if 'quarterstaff' in weapons:
        if simple in weapon_prof or 'quarterstaffs' in weapon_prof:
            damage_type = f'1d6 {str_prof} Bludgeoning'
            new_list = ['Quarterstaff',check_positive_prof(strength,prof),damage_type,'Versatile (1d8)']
            weapon_list.append(new_list)           

        elif simple not in weapon_prof and 'quarterstaffs' not in weapon_prof:
            damage_type = f'1d6 {str_not_prof} Bludgeoning'
            new_list = ['Quarterstaff',str_damage,damage_type,'Versatile (1d8)']
            weapon_list.append(new_list)           


    if 'sickle' in weapons:
        if simple in weapon_prof or 'sickles' in weapon_prof:
            damage_type = f'1d4 {str_prof} Slashing'
            new_list = ['Sickle',check_positive_prof(strength,prof),damage_type,'Light']
            weapon_list.append(new_list)           

        elif simple not in weapon_prof and 'sickles' not in weapon_prof:
            damage_type = f'1d4 {str_not_prof} Slashing'
            new_list = ['Sickle',str_damage,damage_type,'Light']
            weapon_list.append(new_list)           


    if 'spear' in weapons:
        if simple in weapon_prof or 'spears' in weapon_prof:
            damage_type = f'1d6 {str_prof} Piercing'
            new_list = ['Spear',check_positive_prof(strength,prof),damage_type,'Thrown (range 20/60), versatile (1d8)']
            weapon_list.append(new_list)           

        elif simple not in weapon_prof and 'spears' not in weapon_prof:
            damage_type = f'1d6 {str_not_prof} Piercing'
            new_list = ['Spear',str_damage,damage_type,'Thrown (range 20/60), versatile (1d8)']
            weapon_list.append(new_list)           

# Simple Ranged Weapons
    if 'light_crossbow' in weapons:
        if simple in weapon_prof or 'light_crossbows' in weapon_prof:
            damage_type = f'1d8 {dex_prof} Piercing'
            new_list = ['Light Crossbow',check_positive_prof(dexterity,prof),damage_type,'Ammunition (range 80/320), loading, two-handed']
            weapon_list.append(new_list)           

        elif simple not in weapon_prof and 'light_crossbows' not in weapon_prof:
            damage_type = f'1d8 {dex_not_prof} Piercing'
            new_list = ['Light Crossbow',dex_damage,damage_type,'Ammunition (range 80/320), loading, two-handed']
            weapon_list.append(new_list)           


    if 'dart' in weapons:
        if simple in weapon_prof or 'darts' in weapon_prof:
            damage_type = f'1d4 {check_damage()} Piercing'
            new_list = ['Dart',vers_prof,damage_type,'Finesse, thrown (range 20/60)']
            weapon_list.append(new_list)           
        elif simple not in weapon_prof and 'darts' not in weapon_prof:
            damage_type = f'1d4 {check_damage()} Piercing'
            new_list = ['Dart',vers_not_prof,damage_type,'Finesse, thrown (range 20/60)']
            weapon_list.append(new_list)           


    if 'shortbow' in weapons:
        if simple in weapon_prof or 'shortbows' in weapon_prof:
            damage_type = f'1d6 {dex_prof} Piercing'
            new_list = ['Shortbow',check_positive_prof(dexterity,prof),damage_type,'Ammunition (range 80/320), two-handed']
            weapon_list.append(new_list)           

        elif simple not in weapon_prof and 'shortbows' not in weapon_prof:
            damage_type = f'1d6 {dex_not_prof} Piercing'
            new_list = ['Shortbow',dex_damage,damage_type,'Ammunition (range 80/320), two-handed']
            weapon_list.append(new_list)           


    if 'sling' in weapons:
        if simple in weapon_prof or 'sling' in weapon_prof:
            damage_type = f'1d4 {dex_prof} Bludgeoning'
            new_list = ['Sling',check_positive_prof(dexterity,prof),damage_type,'Ammunition (range 30/120)']
            weapon_list.append(new_list)           

        elif simple not in weapon_prof and 'slings' not in weapon_prof:
            damage_type = f'1d4 {dex_not_prof} Bludgeoning'
            new_list = ['Sling',dex_damage,damage_type,'Ammunition (range 30/120)']
            weapon_list.append(new_list)           

# Martial Melee Weapons
    if 'battleaxe' in weapons:
        if martial in weapon_prof or 'battleaxes' in weapon_prof:
            damage_type = f'1d8 {str_prof} Slashing'
            new_list = ['Battleaxe',check_positive_prof(strength,prof),damage_type,'Versatile (1d10)']
            weapon_list.append(new_list)           

        elif martial not in weapon_prof and 'battleaxes' not in weapon_prof:
            damage_type = f'1d8 {str_not_prof} Slashing'
            new_list = ['Battleaxe',str_damage,damage_type,'Versatile (1d10)']
            weapon_list.append(new_list)           


    if 'flail' in weapons:
        if martial in weapon_prof or 'flails' in weapon_prof:
            damage_type = f'1d8 {str_prof} Bludgeoning'
            new_list = ['Flail',check_positive_prof(strength,prof),damage_type,'None']
            weapon_list.append(new_list)           

        elif martial not in weapon_prof and 'flails' not in weapon_prof:
            damage_type = f'1d8 {str_not_prof} Bludgeoning'
            new_list = ['Flail',str_damage,damage_type,'None']
            weapon_list.append(new_list)           


    if 'glaive' in weapons:
        if martial in weapon_prof or 'glaives' in weapon_prof:
            damage_type = f'1d10 {str_prof} Slashing'
            new_list = ['Glaive',check_positive_prof(strength,prof),damage_type,'Heavy, reach, two-handed']
            weapon_list.append(new_list)           

        elif martial not in weapon_prof and 'glaives' not in weapon_prof:
            damage_type = f'1d10 {str_not_prof} Slashing'
            new_list = ['Glaive',str_damage,damage_type,'Heavy, reach, two-handed']
            weapon_list.append(new_list)           


    if 'greataxe' in weapons:
        if martial in weapon_prof or 'greataxes' in weapon_prof:
            damage_type = f'1d12 {str_prof} Slashing'
            new_list = ['Greataxe',check_positive_prof(strength,prof),damage_type,'Heavy, two-handed']
            weapon_list.append(new_list)           

        elif martial not in weapon_prof and 'greataxes' not in weapon_prof:
            damage_type = f'1d12 {str_not_prof} Slashing'
            new_list = ['Greataxe',str_damage,damage_type,'Heavy, two-handed']
            weapon_list.append(new_list)           


    if 'greatsword' in weapons:
        if martial in weapon_prof or 'greatswords' in weapon_prof:
            damage_type = f'2d6 {str_prof} Slashing'
            new_list = ['Greatsword',check_positive_prof(strength,prof),damage_type,'Heavy, two-handed']
            weapon_list.append(new_list)           

        elif martial not in weapon_prof and 'greatswords' not in weapon_prof:
            damage_type = f'2d6 {str_not_prof} Slashing'
            new_list = ['Greatsword',str_damage,damage_type,'Heavy, two-handed']
            weapon_list.append(new_list)           


    if 'halberd' in weapons:
        if martial in weapon_prof or 'halberds' in weapon_prof:
            damage_type = f'1d10 {str_prof} Slashing'
            new_list = ['Halberd',check_positive_prof(strength,prof),damage_type,'Heavy, reach, two-handed']
            weapon_list.append(new_list)           

        elif martial not in weapon_prof and 'halberds' not in weapon_prof:
            damage_type = f'1d10 {str_not_prof} Slashing'
            new_list = ['Halberd',str_damage,damage_type,'Heavy, reach, two-handed']
            weapon_list.append(new_list)           


    if 'lance' in weapons:
        if martial in weapon_prof or 'lances' in weapon_prof:
            damage_type = f'1d12 {str_prof} Piercing'
            new_list = ['Lance',check_positive_prof(strength,prof),damage_type,'Reach, special']
            weapon_list.append(new_list)           

        elif martial not in weapon_prof and 'lances' not in weapon_prof:
            damage_type = f'1d12 {str_not_prof} Piercing'
            new_list = ['Lance',str_damage,damage_type,'Reach, special']
            weapon_list.append(new_list)           


    if 'longsword' in weapons:
        if martial in weapon_prof or 'longswords' in weapon_prof:
            damage_type = f'1d8 {str_prof} Slashing'
            new_list = ['Longsword',check_positive_prof(strength,prof),damage_type,'Versatile (1d10)']
            weapon_list.append(new_list)           

        elif martial not in weapon_prof and 'longswords' not in weapon_prof:
            damage_type = f'1d8 {str_not_prof} Slashing'
            new_list = ['Longsword',str_damage,damage_type,'Versatile (1d10)']
            weapon_list.append(new_list)           


    if 'maul' in weapons:
        if martial in weapon_prof or 'mauls' in weapon_prof:
            damage_type = f'2d6 {str_prof} Bludgeoning'
            new_list = ['Maul',check_positive_prof(strength,prof),damage_type,'Heavy, two-handed']
            weapon_list.append(new_list)           

        elif martial not in weapon_prof and 'mauls' not in weapon_prof:
            damage_type = f'2d6 {str_not_prof} Bludgeoning'
            new_list = ['Maul',str_damage,damage_type,'Heavy, two-handed']
            weapon_list.append(new_list)           


    if 'morningstar' in weapons:
        if martial in weapon_prof or 'morningstars' in weapon_prof:
            damage_type = f'1d8 {str_prof} Piercing'
            new_list = ['Morningstar',check_positive_prof(strength,prof),damage_type,'None']
            weapon_list.append(new_list)           

        elif martial not in weapon_prof and 'morningstars' not in weapon_prof:
            damage_type = f'1d8 {str_not_prof} Piercing'
            new_list = ['Morningstar',str_damage,damage_type,'None']
            weapon_list.append(new_list)           


    if 'pike' in weapons:
        if martial in weapon_prof or 'pikes' in weapon_prof:
            damage_type = f'1d10 {str_prof} Piercing'
            new_list = ['Pike',check_positive_prof(strength,prof),damage_type,'Heavy, reach, two-handed']
            weapon_list.append(new_list)           

        elif martial not in weapon_prof and 'pikes' not in weapon_prof:
            damage_type = f'1d10 {str_not_prof} Piercing'
            new_list = ['Pike',str_damage,damage_type,'Heavy, reach, two-handed']
            weapon_list.append(new_list)           


    if 'rapier' in weapons:
        if martial in weapon_prof or 'rapiers' in weapon_prof:
            damage_type = f'1d8 {check_damage()} Piercing'
            new_list = ['Rapier',vers_prof,damage_type,'Finesse']
            weapon_list.append(new_list)           

        elif martial not in weapon_prof and 'rapiers' not in weapon_prof:
            damage_type = f'1d8 {check_damage()} Piercing'
            new_list = ['Rapier',vers_not_prof,damage_type,'Finesse']
            weapon_list.append(new_list)           


    if 'scimitar' in weapons:
        if martial in weapon_prof or 'scimitars' in weapon_prof:
            damage_type = f'1d6 {check_damage()} Slashing'
            new_list = ['Scimitar',vers_prof,damage_type,'Finesse, light']
            weapon_list.append(new_list)           

        elif martial not in weapon_prof and 'scimitars' not in weapon_prof:
            damage_type = f'1d6 {check_damage()} Slashing'
            new_list = ['Scimitar',vers_not_prof,damage_type,'Finesse, light']
            weapon_list.append(new_list)           


    if 'shortsword' in weapons:
        if martial in weapon_prof or 'shortswords' in weapon_prof:
            damage_type = f'1d6 {check_damage()} Piercing'
            new_list = ['Shortsword',vers_prof,damage_type,'Finesse, light']
            weapon_list.append(new_list)           

        elif martial not in weapon_prof and 'shortswords' not in weapon_prof:
            damage_type = f'1d6 {check_damage()} Piercing'
            new_list = ['Shortsword',vers_not_prof,damage_type,'Finesse, light']
            weapon_list.append(new_list)           


    if 'trident' in weapons:
        if martial in weapon_prof or 'tridents' in weapon_prof:
            damage_type = f'1d6 {str_prof} Piercing'
            new_list = ['Trident',check_positive_prof(strength,prof),damage_type,'Thrown (range 20/60), versatile (1d8)']
            weapon_list.append(new_list)           

        elif martial not in weapon_prof and 'tridents' not in weapon_prof:
            damage_type = f'1d6 {str_not_prof} Piercing'
            new_list = ['Trident',str_damage,damage_type,'Thrown (range 20/60), versatile (1d8)']
            weapon_list.append(new_list)           


    if 'warpick' in weapons:
        if martial in weapon_prof or 'warpicks' in weapon_prof:
            damage_type = f'1d8 {str_prof} Piercing'
            new_list = ['Warpick',check_positive_prof(strength,prof),damage_type,'None']
            weapon_list.append(new_list)           

        elif martial not in weapon_prof and 'warpick' not in weapon_prof:
            damage_type = f'1d8 {str_not_prof} Piercing'
            new_list = ['Warpick',str_damage,damage_type,'None']
            weapon_list.append(new_list)           


    if 'warhammer' in weapons:
        if martial in weapon_prof or 'warhammers' in weapon_prof:
            damage_type = f'1d8 {str_prof} Bludgeoning'
            new_list = ['Warhammer',check_positive_prof(strength,prof),damage_type,'Versatile (1d10)']
            weapon_list.append(new_list)           

        elif martial not in weapon_prof and 'warhammers' not in weapon_prof:
            damage_type = f'1d8 {str_not_prof} Bludgeoning'
            new_list = ['Warhammer',str_damage,damage_type,'Versatile (1d10)']
            weapon_list.append(new_list)           


    if 'whip' in weapons:
        if martial in weapon_prof or 'whips' in weapon_prof:
            damage_type = f'1d4 {check_damage()} Slashing'
            new_list = ['Whip',vers_prof,damage_type,'Finesse, reach']
            weapon_list.append(new_list)           

        elif martial not in weapon_prof and 'whips' not in weapon_prof:
            damage_type = f'1d4 {check_damage()} Slashing'
            new_list = ['Whip',vers_not_prof,damage_type,'Finesse, reach']
            weapon_list.append(new_list)           


# Martial Ranged Weapons
    if 'blowgun' in weapons:
        if martial in weapon_prof or 'blowguns' in weapon_prof:
            damage_type = f'1 {dex_prof} Piercing'
            new_list = ['Blowgun',check_positive_prof(dexterity,prof),damage_type,'Ammunition (range 25/100), loading']
            weapon_list.append(new_list)           

        elif martial not in weapon_prof and 'blowguns' not in weapon_prof:
            damage_type = f'1 {dex_not_prof} Piercing'
            new_list = ['Blowgun',dex_damage,damage_type,'Ammunition (range 20/100), loading']
            weapon_list.append(new_list)           


    if 'hand_crossbow' in weapons:
        if martial in weapon_prof or 'hand_crossbows' in weapon_prof:
            damage_type = f'1d6 {dex_prof} Piercing'
            new_list = ['Hand Crossbow',check_positive_prof(dexterity,prof),damage_type,'Ammunition (range 30/120), light, loading']
            weapon_list.append(new_list)           

        elif martial not in weapon_prof and 'hand_crossbows' not in weapon_prof:
            damage_type = f'1d6 {dex_not_prof} Piercing'
            new_list = ['Hand Crossbow',dex_damage,damage_type,'Ammunition (range 30/120), light, loading']
            weapon_list.append(new_list)           


    if 'heavy_crossbow' in weapons:
        if martial in weapon_prof or 'heavy_crossbows' in weapon_prof:
            damage_type = f'1d10 {dex_prof} Piercing'
            new_list = ['Heavy Crossbow',check_positive_prof(dexterity,prof),damage_type,'Ammunition (range 100/400), heavy, loading, two-handed']
            weapon_list.append(new_list)           

        elif martial not in weapon_prof and 'heavy_crossbows' not in weapon_prof:
            damage_type = f'1d10 {dex_not_prof} Piercing'
            new_list = ['Heavy Crossbow',dex_damage,damage_type,'Ammunition (range 100/400), heavy, loading, two-handed']
            weapon_list.append(new_list)           


    if 'longbow' in weapons:
        if martial in weapon_prof or 'longbows' in weapon_prof:
            damage_type = f'1d8 {dex_prof} Piercing'
            new_list = ['Longbow',check_positive_prof(dexterity,prof),damage_type,'Ammunition (range 150/600), heavy, two-handed']
            weapon_list.append(new_list)           

        elif martial not in weapon_prof and 'longbows' not in weapon_prof:
            damage_type = f'1d8 {dex_not_prof} Piercing'
            new_list = ['Longbow',dex_damage,damage_type,'Ammunition (range 150/600), heavy, two-handed']
            weapon_list.append(new_list)           


    if 'net' in weapons:
        if martial in weapon_prof or 'nets' in weapon_prof:
            damage_type = f'N/A'
            new_list = ['Net',check_positive_prof(dexterity,prof),damage_type,'Special, thrown (range 5/15)']
            weapon_list.append(new_list)           

        elif martial not in weapon_prof and 'nets' not in weapon_prof:
            damage_type = f'N/A'
            new_list = ['Net',dex_damage,damage_type,'Special, thrown (range 5/15)']
            weapon_list.append(new_list)           


    if 'tavern_brawler' not in dnd_dict.character_dict['features'] and 'martial_arts' not in dnd_dict.character_dict['features']:
        damage_type = f'{strength} Bludgeoning'
        new_list = ['Unarmed',str_damage,damage_type,'None']
        weapon_list.append(new_list)           

    if 'tavern_brawler' in dnd_dict.character_dict['features']:
        damage_type = f'1d4 {str_not_prof} Bludgeoning'
        new_list = ['Unarmed (Tavern Brawler)',str_damage,damage_type,'None']
        weapon_list.append(new_list)           

    if martial_arts:
        damage_type = f'{martial_arts} {dex_not_prof} Bludgeoning'
        new_list = ['Unarmed (Martial Arts)',dex_damage,damage_type,'None']
        weapon_list.append(new_list)           


    print((tabulate(weapon_list, headers = ['Weapon','Attack Bonus','Damage/Type','Properties'],tablefmt='grid')))






# Display all of the information
def char_display():

    print("Name: {}".format(dnd_dict.character_dict["name"]))
    stat_table()

# Player Class Displays
    print("Player Class:")
    dnd_class.RaceStats.class_display("Artificer",dnd_dict.character_dict['player_class']['artificer']['class_level'],dnd_dict.character_dict['player_class']['artificer']['subclass'])

    dnd_class.RaceStats.class_display("Barbarian",dnd_dict.character_dict['player_class']['barbarian']['class_level'],dnd_dict.character_dict['player_class']['barbarian']['subclass'])

    dnd_class.RaceStats.class_display("Bard",dnd_dict.character_dict['player_class']['bard']['class_level'],dnd_dict.character_dict['player_class']['bard']['subclass'])

    dnd_class.RaceStats.class_display("Cleric",dnd_dict.character_dict['player_class']['cleric']['class_level'],dnd_dict.character_dict['player_class']['cleric']['subclass'])

    dnd_class.RaceStats.class_display("Druid",dnd_dict.character_dict['player_class']['druid']['class_level'],dnd_dict.character_dict['player_class']['druid']['subclass'])

    dnd_class.RaceStats.class_display("Fighter",dnd_dict.character_dict['player_class']['fighter']['class_level'],dnd_dict.character_dict['player_class']['fighter']['subclass'])

    dnd_class.RaceStats.class_display("Monk",dnd_dict.character_dict['player_class']['monk']['class_level'],dnd_dict.character_dict['player_class']['monk']['subclass'])

    dnd_class.RaceStats.class_display("Paladin",dnd_dict.character_dict['player_class']['paladin']['class_level'],dnd_dict.character_dict['player_class']['paladin']['subclass'])

    dnd_class.RaceStats.class_display("Ranger",dnd_dict.character_dict['player_class']['ranger']['class_level'],dnd_dict.character_dict['player_class']['ranger']['subclass'])

    dnd_class.RaceStats.class_display("Rogue",dnd_dict.character_dict['player_class']['rogue']['class_level'],dnd_dict.character_dict['player_class']['rogue']['subclass'])

    dnd_class.RaceStats.class_display("Sorcerer",dnd_dict.character_dict['player_class']['sorcerer']['class_level'],dnd_dict.character_dict['player_class']['sorcerer']['subclass'])

    dnd_class.RaceStats.warlock_display(dnd_dict.character_dict['player_class']['warlock']['class_level'],dnd_dict.character_dict['player_class']['warlock']['subclass'],dnd_dict.character_dict['player_class']['warlock']['pact'])

    dnd_class.RaceStats.class_display("Wizard",dnd_dict.character_dict['player_class']['wizard']['class_level'],dnd_dict.character_dict['player_class']['wizard']['subclass'])
    print("")


    print("Background: {}".format(dnd_dict.character_dict["background"]))
    print("Race: {}".format(dnd_dict.character_dict['race']))
# Initiative bonus is the Dex mod.
    print("Initiative Bonus: {}".format(dnd_dict.character_dict['initiative']))

# Armor Classes with features included
    armor_display()
    print("Armor Class: {}".format(dnd_dict.character_dict["armor_class"]))

    if dnd_dict.character_dict['barbarian_armor_class'] > 0:
        print("Armor Class (With Barbarian Unarmored Defense): {}".format(dnd_dict.character_dict["barbarian_armor_class"]))
    if dnd_dict.character_dict['monk_armor_class'] > 0:
        print("Armor Class (With Monk Unarmored Defense): {}".format(dnd_dict.character_dict["monk_armor_class"]))
    if dnd_dict.character_dict['sorcerer_armor_class'] > 0:
        print("Armor Class (With Draconic Resilience): {}".format(dnd_dict.character_dict["sorcerer_armor_class"]))
    if dnd_dict.character_dict['spell_modifier']['ki_save'] > 0:
        print("Ki Points: {}".format(dnd_dict.character_dict['ki_points']))
    if dnd_dict.character_dict['spell_modifier']['ki_save'] > 0:
        print("Ki Saving Throw: {}".format(dnd_dict.character_dict['ki_points']))
    if dnd_dict.character_dict['rage'] == 'Unlimited':
        print("Uses of Rage: {}".format(dnd_dict.character_dict['rage']))
    elif dnd_dict.character_dict['rage'] > 0:
        print("Uses of Rage: {}".format(dnd_dict.character_dict['rage']))
    if dnd_dict.character_dict['rage_damage'] > 0:
        print("Rage Damage: {}".format(dnd_dict.character_dict['rage_damage']))
    if dnd_dict.character_dict['sneak_attack'] > 0:
        print("Sneak Attack: {}d6".format(dnd_dict.character_dict['sneak_attack']))
    if dnd_dict.character_dict['sorcery_points'] > 0:
        print("Sorcery Points: {}".format(dnd_dict.character_dict["sorcery_points"]))
    print("Passive Perception: {}".format(dnd_dict.character_dict["passive_perception"]))
    print("Hit Points: {}".format(dnd_dict.character_dict.get("hp")))
# Hit Dice List
    dnd_class.RaceStats.hit_dice_display(dnd_dict.character_dict["d6"],"d6")
    dnd_class.RaceStats.hit_dice_display(dnd_dict.character_dict["d8"],"d8")
    dnd_class.RaceStats.hit_dice_display(dnd_dict.character_dict["d10"],"d10")
    dnd_class.RaceStats.hit_dice_display(dnd_dict.character_dict["d12"],"d12")
    print("Walking Speed: {}".format(dnd_dict.character_dict["speed"]))
    if dnd_dict.character_dict['unarmored_movement_barbarian'] > 0:
        print("Walking Speed Without Heavy Armor: {}".format(dnd_dict.character_dict['unarmored_movement_barbarian']))
    if dnd_dict.character_dict['unarmored_movement_monk'] > 0:
        print("Walking Speed Without Armor: {}".format(dnd_dict.character_dict['unarmored_movement_monk']))
    if dnd_dict.character_dict['climb_speed'] > 0:
        print("Climbing Speed: {}".format(dnd_dict.character_dict['climb_speed']))
    if dnd_dict.character_dict['unarmored_movement_barbarian'] > 0 and 'roving' in dnd_dict.character_dict['features']:
        print("Climbing Speed (Without Heavy Armor): {}".format(dnd_dict.character_dict['unarmored_movement_barbarian']))
    if dnd_dict.character_dict['unarmored_movement_monk'] > 0 and 'roving' in dnd_dict.character_dict['features']:
        print("Climbing Speed (Without Armor): {}".format(dnd_dict.character_dict['unarmored_movement_monk']))
    if dnd_dict.character_dict['swim_speed'] > 0:
        print("Swimming Speed: {}".format(dnd_dict.character_dict['swim_speed']))
    if dnd_dict.character_dict['unarmored_movement_barbarian'] > 0 and 'roving' in dnd_dict.character_dict['features']:
        print("Swimming Speed (Without Heavy Armor): {}".format(dnd_dict.character_dict['unarmored_movement_barbarian']))
    if dnd_dict.character_dict['unarmored_movement_monk'] > 0 and 'roving' in dnd_dict.character_dict['features']:
        print("Swimming Speed (Without Armor): {}".format(dnd_dict.character_dict['unarmored_movement_monk']))
    if dnd_dict.character_dict['fly_speed'] > 0:
        print("Flying Speed: {}".format(dnd_dict.character_dict['fly_speed']))
    print("Size: {}".format(dnd_dict.character_dict["size"]))
    print(f"Languages Known: {', '.join(dnd_dict.character_dict['Languages'].values())}")
    if dnd_dict.character_dict["inspiration_die"]:
        print(f"Inspiration Die: {(dnd_dict.character_dict['inspiration_die'])}")
    tool_prof_display()


    if dnd_dict.character_dict["Armor_Prof"]:
        print(f"Armor Proficiencies: {', '.join(dnd_dict.character_dict['Armor_Prof'].values())}")
    else:
        print("Armor Proficiencies: N/A")

    gold_display()
    item_display()
    weapon_display()
    spell_table()




    display_magic()




    if dnd_dict.character_dict["infusions"]:
        print(f"Infusions Known: {', '.join(dnd_dict.character_dict['infusions'].values())}")

    if dnd_dict.character_dict['maneuvers']['number'] > 0 and dnd_dict.character_dict['maneuvers']['d6'] > 0:
        print("Superiority Dice: {}{} and {}d6".format(dnd_dict.character_dict['maneuvers']['number'],dnd_dict.character_dict['maneuvers']['die'],dnd_dict.character_dict['maneuvers']['d6']))
    if dnd_dict.character_dict['maneuvers']['number'] > 0 and dnd_dict.character_dict['maneuvers']['d6'] == 0:
        print("Superiority Dice: {}{}".format(dnd_dict.character_dict['maneuvers']['number'],dnd_dict.character_dict['maneuvers']['die']))
    if dnd_dict.character_dict['maneuvers']['d6'] > 0 and dnd_dict.character_dict['maneuvers']['number'] == 0:
        print("Superiority Dice: {}d6".format(dnd_dict.character_dict['maneuvers']['d6']))
    if dnd_dict.character_dict['favored_enemies']:
        print(f"Favored Enemies: {', '.join(dnd_dict.character_dict['favored_enemies'].values())}")
    if dnd_dict.character_dict['favored_terrain']:
        print(f"Favored Terrain: {', '.join(dnd_dict.character_dict['favored_terrain'].values())}")

    print(f"Racial Features: {' '.join(dnd_dict.character_dict['racial_features'].values())}")
    print(f"Features: {' '.join(dnd_dict.character_dict['features'].values())}")


    print("Proficiency Bonus: {}".format(dnd_dict.character_dict['prof_bonus']))
#Displays the skills. If the character has proficieny or expertise,
# it puts a (*) or (*)(E) before the number
    skill_table()

    spell_slot_display()

    return





