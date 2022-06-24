#!/usr/bin/python3
import os, math, json, dnd_features, dnd_language, dnd_tools, dnd_dict, dnd_skills, dnd_race, dnd_class, dnd_pack, dnd_weapon, dnd_magic, random,collections,dnd_sorcerer,dnd_warlock,dnd_fighting_styles,dnd_feats


#Player classes
def artificer():

# Set the HP here, add the HP from the race to the hit points determined above
    hp_mod = (dnd_dict.character_dict["hp"] + 8)
    dnd_dict.character_dict['hp'] = hp_mod
# Set Hit Dice
    dnd_dict.character_dict["d8"] = 1

    print("Hit Points: ",hp_mod)
    print("Hit Dice: 1d8 per artificer level")

    armor_prof = {'light_armor':'Light Armor', 'medium_armor':'Medium Armor', 'shields':'Shields'}
    dnd_dict.character_dict['Armor_Prof'].update(armor_prof)

# Setting the armor and weapon proficiencies

    weapon_prof = {'simple_weapons':'Simple Weapons'}
    dnd_dict.character_dict["Weapon_Prof"].update(weapon_prof)
# If you are already proficient in Thieve's Tools or Tinker's Tools, pass
    dnd_dict.character_dict["Kits"]['thieves_tools'] = 'Thieves\' Tools'
    dnd_dict.character_dict["Tools"]['tinker_tools'] = 'Tinker\'s Tools'

    dnd_dict.character_dict['player_class']['artificer']['class_level'] = 1

    dnd_tools.artisan_tools()

#Selecting the skills
#If the player is already proficient, loop back to the start and ask again.
#If they are not, then procede as normal
    i = 1
    while i < 3:
        while True:
            check_prof = dnd_dict.character_dict['skill_prof']
            print(f'{i}/2')
            skill_list = ['Arcana','History','Investigation','Medicine','Nature','Perception','Sleight of Hand']
            dnd_skills.skill_addition(skill_list,dnd_dict.character_dict['skill_prof'])
            i+=1
            break


# Setting the saving throws.
    dnd_dict.character_dict['saving_throws']['constitution'] = 'Constitution'
    dnd_dict.character_dict['saving_throws']['intelligence'] = 'Intelligence'
    dnd_skills.saving_throw_calc()


# Getting equipment
    dnd_weapon.double_simple()
    dnd_skills.equip_mod('light_crossbow1','Light Crossbow')
    dnd_dict.character_dict['weapons']['light_crossbow'] = 'Light Crossbow'
    dnd_skills.equip_mod('bolts20','Bolts')
    dnd_skills.equip_mod('thieves_tools1','Thieve\'s Tools')
    dnd_pack.dungeoneer_pack()


# Choose the type of armor you get
    while True:
        armor_choice = input("""Choose which armor you will take:
1) Studded Leather Armor
2) Scale Mail
Enter your selection: """)
        if armor_choice == '1':
            dnd_skills.equip_mod('studded_leather1','Studded Leather Armor')
            dnd_dict.character_dict['chest_equip_armor']['studded_leather'] = 'Studded Leather Armor'
            dnd_dict.character_dict['chest_armor'] = 'Studded Leather Armor'
            dnd_weapon.light_armor(12)
            print("Armor Class: ",dnd_dict.character_dict['armor_class'])
            break

        elif armor_choice == '2':
            dnd_skills.equip_mod('scale_mail1','Scale Mail')
            dnd_dict.character_dict['chest_equip_armor']['scale_mail'] = 'Scale Mail'
            dnd_dict.character_dict['chest_armor'] = 'Scale Mail'
            dnd_skills.med_armor(14)
            print("Armor Class: ",dnd_dict.character_dict['armor_class'])
            break
    
        else:
            print("Invalid Selection")
            continue

# Only done if the character does not have a natural armor class
    if dnd_dict.character_dict['natural_armor_class'] == 0:
        dnd_dict.character_dict['base_armor_class'] = 10 + dnd_dict.character_dict['Stats']['dexterity']['mod']
# Setting the Spell Save DC and Spell Attack Modifiers
    spell_attack = ((dnd_dict.character_dict["Stats"]["intelligence"]['mod']) + dnd_dict.character_dict['prof_bonus'])
    print("Spell Attack Modifier: {}".format(spell_attack))
    dnd_dict.character_dict["spell_modifier"]['intelligence']['attack'] = spell_attack

    spell_save = ((dnd_dict.character_dict["Stats"]["intelligence"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
    print("Spell DC: {}".format(spell_save))
    dnd_dict.character_dict["spell_modifier"]['intelligence']['save'] = spell_save


    dnd_magic.artificer_magic()
#     Passive perception = 10 + Perception score
    passive_perception = (dnd_dict.character_dict["perception"] + 10)
    print("Passive Perception: ",passive_perception)
    dnd_dict.character_dict["passive_perception"] = passive_perception
    dnd_dict.character_dict['half_caster_level'] += 2

    dnd_dict.character_dict['initial_class'] = 'Artificer'

    dnd_skills.spell_slot_selection()
    dnd_skills.skill_calculation()
    dnd_features.artificer_features()
    dnd_features.firearm_proficiency()

# If you pick Variant Human or Custom Lineage, pick a feat just in case you need to satisfy a prerequisite
    if dnd_dict.character_dict['race'] == 'Variant Human' or dnd_dict.character_dict['race'] == 'Custom Lineage':
        dnd_feats.choose_feat()

    return


def barbarian():

# Set the HP here, add the HP from the race to the hit points determined above
    hp_mod = (dnd_dict.character_dict["hp"] + 12)
    dnd_dict.character_dict['hp'] = hp_mod
# Set Hit Dice
    dnd_dict.character_dict["d12"] = 1

    print("Hit Points: ",hp_mod)
    print("Hit Dice: 1d12 per barbarian level")

    dnd_dict.character_dict["player_class"]["barbarian"]["class_level"] = 1

# Setting the Armor Class
#Armor Class = 10 + Dexterity Modifier + Constitution Modifier
    AC= (10 + dnd_dict.character_dict['Stats']['dexterity']['mod'] + (dnd_dict.character_dict['Stats']['constitution']['mod']))
    print("Armor Class: ",AC)
    dnd_dict.character_dict["barbarian_armor_class"] = AC

    armor_class = ((dnd_dict.character_dict["Stats"]["dexterity"]["mod"]) + 10)
    dnd_dict.character_dict["armor_class"] = armor_class
# Only done if the character does not have a natural armor class
    if dnd_dict.character_dict['natural_armor_class'] == 0:
        dnd_dict.character_dict['base_armor_class'] = 10 + dnd_dict.character_dict['Stats']['dexterity']['mod']

# Setting the armor and weapon proficiencies


    armor_prof = {'light_armor':'Light Armor','medium_armor':'Medium Armor','shields':'Shields'}
    dnd_dict.character_dict['Armor_Prof'].update(armor_prof)

    weapon_prof = {'simple_weapons':'Simple Weapons', 'martial_weapons':'Martial Weapons'}
    dnd_dict.character_dict['Weapon_Prof'].update(weapon_prof)



#Selecting the skills
    i = 1
    while i < 3:
        while True:
            check_prof = dnd_dict.character_dict['skill_prof']
            print(f'{i}/2')
            skill_list = ['Animal Handling','Athletics','Intimidation','Nature','Perception','Survival']
            dnd_skills.skill_addition(skill_list,dnd_dict.character_dict['skill_prof'])
            i+=1
            break


# Setting the saving throws.
    dnd_dict.character_dict['saving_throws']['strength'] = 'Strength'
    dnd_dict.character_dict['saving_throws']['constitution'] = 'Constutution'
    dnd_skills.saving_throw_calc()


# Selecting Equipment
    while True:
        choice1 = input("""Choose which primary weapon you will take
1) A greataxe
2) Any martial melee weapon
Choose your selection: """)
        if choice1 == '1':
            dnd_skills.equip_mod('greataxe1','Greataxe')
            dnd_dict.character_dict['weapons']['greataxe'] = 'Greataxe'
            break
    
        elif choice1 == '2':
           dnd_weapon.martial_melee()
           break

        else:
            print("Invalid Selection")
            continue

    while True:
        choice2 = input("""Choose which secondary weapon you will take
1) Two Handaxes
2) Any simple weapon
Enter your selection: """)
    
        if choice2 == '1':
            dnd_skills.equip_mod('handaxe2','Handaxe')
            dnd_dict.character_dict['weapons']['handaxe'] = ['Handaxe']
            break
 
        elif choice2 == '2':
            dnd_weapon.simple_weapon()
            break
    
        else:
            print("Invalid Selection")
            continue


    dnd_pack.explorer_pack()
    dnd_skills.equip_mod('javelin3','Javelin')
    dnd_dict.character_dict['weapons']['javelin'] = 'Javelin'
    dnd_dict.character_dict['initial_class'] = 'Barbarian'

#     Passive perception = 10 + Perception score
    passive_perception = (dnd_dict.character_dict["perception"] + 10)
    print("Passive Perception: ",passive_perception)
    dnd_dict.character_dict["passive_perception"] = passive_perception

    dnd_dict.character_dict['rage'] += 2
    dnd_dict.character_dict['rage_damage'] += 2
    dnd_skills.skill_calculation()
    dnd_features.barbarian_features()

# If you pick Variant Human or Custom Lineage, pick a feat just in case you need to satisfy a prerequisite
    if dnd_dict.character_dict['race'] == 'Variant Human' or dnd_dict.character_dict['race'] == 'Custom Lineage':
        dnd_feats.choose_feat()
    return


def bard():

    hp_mod = (dnd_dict.character_dict["hp"] + 8)
    dnd_dict.character_dict['hp'] = hp_mod
# Set Hit Dice
    dnd_dict.character_dict["d8"] = 1

    print("Hit Points: ",hp_mod)
    print("Hit Dice: 1d8 per bard level")

    dnd_dict.character_dict["player_class"]["bard"]["class_level"] = 1

# Setting the armor and weapon proficiencies


    weapon_prof = {'simple_weapons':'Simple Weapons', 'hand_crossbows':'Hand Crossbows', 'rapiers':'Rapiers', 'longswords':'Longswords','shortswords':'Shortswords'}
    dnd_dict.character_dict["Weapon_Prof"].update(weapon_prof)

    armor_prof = {'light_armor':'Light Armor'}
    dnd_dict.character_dict['Armor_Prof'].update(armor_prof)

    dnd_tools.musical_instrument()
    dnd_tools.musical_instrument()
    dnd_tools.musical_instrument()



# Setting the skill proficiencies
    dnd_skills.bard_skills()

# Setting the saving throws.
    dnd_dict.character_dict['saving_throws']['dexterity'] = 'Dexterity'
    dnd_dict.character_dict['saving_throws']['charisma'] = 'Charisma'
    dnd_skills.saving_throw_calc()

# Getting equipment

    while True:
        choice1 = input("""Choose which primary weapon you will take
1) A rapier
2) A longsword
3) Any simple weapon
Choose your selection: """)
        if choice1 == '1':
            dnd_skills.equip_mod('rapier1','Rapier')
            dnd_dict.character_dict['weapons']['rapier'] = 'Rapier'
            break

        elif choice1 == '2':
            dnd_skills.equip_mod('longsword1','Longsword')
            dnd_dict.character_dict['weapons']['longsword'] = 'Longsword'
            break

        elif choice1 == '3':
            dnd_weapon.simple_weapon()
            break

        else:
            print("Invalid Selection")
            continue

    while True:
        choice2 = input("""Choose which pack you will take
1) A diplomat's pack
2) An entertainer's pack
Enter your selection: """)

        if choice2 == '1':
            dnd_pack.diplomat_pack()
            break

        elif choice2 == '2':
            dnd_pack.entertainer_pack()
            break

        else:
            print("Invalid Selection")
            continue

    while True:
        choice3 = input("""Choose which instrument you will take
1) A lute
2) Any other musical instrument
Enter your selection: """)

        if choice3 == '1':
            dnd_skills.equip_mod('lute1','Lute')
            break

        elif choice3 == '2':
            musical_equip = input("Which instrument do you want to take? ")
            musical_key = musical_equip + str(1)
            dnd_dict.character_dict['Equipment'][musical_key] = musical_equip
            break

        else:
            print("Invalid Selection")
            continue

#Leather armor is 11 + Dex Mod
    dnd_skills.equip_mod('leather_armor1','Leather Armor')
    dnd_dict.character_dict['chest_equip_armor']['leather_armor'] = 'Leather Armor'
    dnd_dict.character_dict['chest_armor'] = 'Leather Armor'
    dnd_skills.equip_mod('dagger1','Dagger')
    dnd_dict.character_dict['weapons']['dagger'] = 'Dagger'

    dnd_weapon.light_armor(11)
    print("Armor Class: ",dnd_dict.character_dict['armor_class'])
# Only done if the character does not have a natural armor class
    if dnd_dict.character_dict['natural_armor_class'] == 0:
        dnd_dict.character_dict['base_armor_class'] = 10 + dnd_dict.character_dict['Stats']['dexterity']['mod']

    dnd_magic.bard_magic()

# Setting the Spell Save DC and Spell Attack Modifiers
    spell_attack = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'])
    print("Spell Attack Modifier: {}".format(spell_attack))
    dnd_dict.character_dict["spell_modifier"]['charisma']['attack'] = spell_attack

    spell_save = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
    print("Spell DC: {}".format(spell_save))
    dnd_dict.character_dict["spell_modifier"]['charisma']['save'] = spell_save

    dnd_dict.character_dict['initial_class'] = 'Bard'

#     Passive perception = 10 + Perception score
    dnd_features.bard1()
    passive_perception = (dnd_dict.character_dict["perception"] + 10)
    print("Passive Perception: ",passive_perception)
    dnd_dict.character_dict["passive_perception"] = passive_perception
    dnd_dict.character_dict['caster_level'] = 1
    dnd_skills.spell_slot_selection()
    dnd_skills.skill_calculation()

# If you pick Variant Human or Custom Lineage, pick a feat just in case you need to satisfy a prerequisite
    if dnd_dict.character_dict['race'] == 'Variant Human' or dnd_dict.character_dict['race'] == 'Custom Lineage':
        dnd_feats.choose_feat()

    return

def cleric():

    hp_mod = (dnd_dict.character_dict["hp"] + 8)
    dnd_dict.character_dict['hp'] = hp_mod
# Set Hit Dice
    dnd_dict.character_dict["d8"] = 1

    print("Hit Points: ",hp_mod)
    print("Hit Dice: 1d8 per cleric level")

    dnd_dict.character_dict["player_class"]["cleric"]["class_level"] = 1

# Setting the armor and weapon proficiencies
    armor_prof = {'light_armor':'Light Armor', 'medium_armor':'Medium Armor', 'shields':'Shields'}
    dnd_dict.character_dict['Armor_Prof'].update(armor_prof)
    weapon_prof = {'simple_weapons':'Simple Weapons'}
    dnd_dict.character_dict['Weapon_Prof'].update(weapon_prof)

#Selecting the skills
    cleric_skills = ['History','Insight','Medicine','Persuasion','Religion']
    i = 1
    while i < 3:
        check_prof = dnd_dict.character_dict['skill_prof']
        if 'history' in check_prof and 'insight' in check_prof and 'medicine' in check_prof and 'persuasion' in check_prof and 'religion' in check_prof:
            i+=2
            break
        else:
            print(f'{i}/2')
            dnd_skills.skill_addition(cleric_skills,check_prof)
            i+=1


# Setting the saving throws.
    dnd_dict.character_dict['saving_throws']['wisdom'] = 'Wisdom'
    dnd_dict.character_dict['saving_throws']['charisma'] = 'Charisma'
    dnd_skills.saving_throw_calc()

# Getting equipment

    while True:
        weapon_choice1 = input("""What primary weapon do you want?
1) A Mace
2) A warhammer
Enter your selection: """)
        if weapon_choice1 == '1':
            dnd_skills.equip_mod('mace1','Mace')
            dnd_dict.character_dict['weapons']['mace'] = 'Mace'
            break

        elif weapon_choice1 == '2':
            dnd_skills.equip_mod('warhammer1','Warhammer')
            dnd_dict.character_dict['weapons']['warhammer'] = 'Warhammer'
            break

        else:
            print("Invalid Selection")
            continue


# Choose the type of armor you get
    while True:
        armor_choice = input("""Choose which armor you will take:
1) Leather Armor
2) Scale Mail
3) Chain Mail
Enter your selection: """)

#Leather Armor = 11 + Dex mod +2 from shield(given below)
        if armor_choice == '1':
            dnd_skills.equip_mod('leather_armor1','Leather Armor')
            dnd_dict.character_dict['chest_equip_armor']['leather_armor'] = 'Leather Armor'
            dnd_dict.character_dict['chest_armor'] = 'Leather Armor'

            dnd_weapon.light_armor(11)
            dnd_dict.character_dict['armor_class'] += 2
            print("Armor Class: ",dnd_dict.character_dict['armor_class'])
            break

#Scale Mail = 14 + Dex mod (maximum of +2) + 2 from the shield (given below)
        elif armor_choice == '2':
            dnd_skills.equip_mod('scale_mail1','Scale Mail')
            dnd_dict.character_dict['chest_equip_armor']['scale_mail'] = 'Scale Mail'
            dnd_dict.character_dict['chest_armor'] = 'Scale Mail'
            dnd_skills.med_armor(16)
            print("Armor Class: ",dnd_dict.character_dict['armor_class'])
            break

#Chain Mail is a flat AC of 16+2 from shield (given below)
        elif armor_choice == '3':
            dnd_skills.equip_mod('chain_mail1','Chain Mail')
            dnd_dict.character_dict['chest_equip_armor']['chain_mail'] = 'Chail Mail'
            dnd_dict.character_dict['chest_armor'] = 'Chain Mail'
            print("Armor Class: 18")
            dnd_dict.character_dict["armor_class"] = 18
            break

        else:
            print("Invalid Selection")
            continue

    while True:
        weapon_choice2 = input("""What secondary weapon do you want?
1) A Light Crossbow with 20 bolts
2) Any simple weapon
Enter your selection: """)
        if weapon_choice2 == '1':
            dnd_skills.equip_mod('light_crossbow1','Light Crossbow')
            dnd_dict.character_dict['weapons']['light_crossbow'] = 'Light Crossbow'
            dnd_skills.equip_mod('bolts20','Bolts')
            break

        elif weapon_choice2 == '2':
            dnd_weapon.simple_weapon()
            break

        else:
            print("Invalid Selection")
            continue

    while True:
        pack_choice = input("""What pack do you want?
1) A priest's pack
2) An explorer's pack
Enter your selection: """)
        if pack_choice == '1':
            dnd_pack.priest_pack()
            break
 
        elif pack_choice == '2':
            dnd_pack.explorer_pack()
            break

        else:
            print("Invalid Selection")
            continue

    dnd_skills.equip_mod('shield1','Shield')
    dnd_dict.character_dict['shield_equip_armor']['shield'] = 'Shield'
    dnd_dict.character_dict['shield'] = 'Shield'
    dnd_skills.equip_mod('holy_symbol1','Holy Symbol')
# Only done if the character does not have a natural armor class
    if dnd_dict.character_dict['natural_armor_class'] == 0:
        dnd_dict.character_dict['base_armor_class'] = 10 + dnd_dict.character_dict['Stats']['dexterity']['mod']



    dnd_magic.cleric_magic()

# Choose the subclass
    while True:
        subclass_choice = input("""Select your Domain:
1) Knowledge Domain
2) Life Domain
3) Light Domain
4) Nature Domain
5) Tempest Domain
6) Trickery Domain
7) War Domain
Enter your Selection: """)
        if subclass_choice=='1':
            dnd_features.knowledge_cleric1()
            break

        elif subclass_choice=='2':
            dnd_features.life_cleric1()
            break

        elif subclass_choice=='3':
            dnd_features.light_cleric1()
            break

        elif subclass_choice=='4':
            dnd_features.nature_cleric1()
            break

        elif subclass_choice=='5':
            dnd_features.tempest_cleric1()
            break

        elif subclass_choice=='6':
            dnd_features.trickery_cleric1()
            break

        elif subclass_choice=='7':
            dnd_features.war_cleric1()
            break

        else:
            print("Invalid Selection")
            continue
# Setting the Spell Save DC and Spell Attack Modifiers
    spell_attack = ((dnd_dict.character_dict["Stats"]["wisdom"]['mod']) + dnd_dict.character_dict['prof_bonus'])
    print("Spell Attack Modifier: {}".format(spell_attack))
    dnd_dict.character_dict["spell_modifier"]['wisdom']['attack'] = spell_attack

    spell_save = ((dnd_dict.character_dict["Stats"]["wisdom"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
    print("Spell DC: {}".format(spell_save))
    dnd_dict.character_dict["spell_modifier"]['wisdom']['save'] = spell_save

    dnd_dict.character_dict['initial_class'] = 'Cleric'

#     Passive perception = 10 + Perception score
    passive_perception = (dnd_dict.character_dict["perception"] + 10)
    print("Passive Perception: ",passive_perception)
    dnd_dict.character_dict["passive_perception"] = passive_perception
    dnd_dict.character_dict['caster_level'] = 1
    dnd_skills.spell_slot_selection()
    dnd_skills.skill_calculation()

# If you pick Variant Human or Custom Lineage, pick a feat just in case you need to satisfy a prerequisite
    if dnd_dict.character_dict['race'] == 'Variant Human' or dnd_dict.character_dict['race'] == 'Custom Lineage':
        dnd_feats.choose_feat()

    return

def druid():

    hp_mod = (dnd_dict.character_dict["hp"] + 8)
    dnd_dict.character_dict['hp'] = hp_mod
# Set Hit Dice
    dnd_dict.character_dict["d8"] = 1

    print("Hit Points: ",hp_mod)
    print("Hit Dice: 1d8 per druid level")

    dnd_dict.character_dict["player_class"]["druid"]["class_level"] = 1

# Setting the armor and weapon proficiencies
# Druids also know the Druidic Language


    armor_prof={'light_armor':'Light Armor', 'medium_armor':'Medium Armor', 'shields':'Shields'}
    dnd_dict.character_dict['Armor_Prof'].update(armor_prof)
    dnd_dict.character_dict["Languages"]['Druidic'] = 'Druidic'
    weapon_prof={'clubs':'Clubs', 'daggers':'Daggers', 'darts':'Darts', 'javelins':'Javelins', 'maces':'Maces', 'quarterstaffs':'Quarterstaffs', 'scimitars':'Scimitars', 'sickles':'Sickles', 'slings':'Slings', 'spears':'Spears'}
    dnd_dict.character_dict['Weapon_Prof'].update(weapon_prof)
    dnd_dict.character_dict["Kits"]['herbalism_kit'] = 'Herbalism Kit'



#Selecting the skills
    i = 1
    while i < 3:
        while True:
            check_prof = dnd_dict.character_dict['skill_prof']
            print(f'{i}/2')
            skill_list = ['Arcana','Animal Handling','Insight','Medicine','Nature','Perception','Religion','Sleight of Hand']
            dnd_skills.skill_addition(skill_list,dnd_dict.character_dict['skill_prof'])
            i+=1
            break


# Setting the saving throws.
    dnd_dict.character_dict['saving_throws']['constitution'] = 'Constitution'
    dnd_dict.character_dict['saving_throws']['intelligence'] = 'Intelligence'
    dnd_skills.saving_throw_calc()

# Getting equipment


    dnd_weapon.double_simple()
    dnd_skills.equip_mod('light_crossbow1','Light Crossbow')
    dnd_dict.character_dict['weapons']['light_crossbow'] = 'Light Crossbow'
    dnd_skills.equip_mod('bolts20','Bolts')
    dnd_pack.dungeoneer_pack()

    while True:
        weapon_choice1 = input("""Choose what your primary weapon will be:
1) A wooden shield
2) Any simple weapon
Enter your selection: """)
        if weapon_choice1 == '1':
            dnd_skills.equip_mod('wooden_shield1','Wooden Shield')
            dnd_dict.character_dict['shield_equip_armor']['wooden_shield'] = 'Wooden Shield'
            dnd_dict.character_dict['shield'] = 'Shield'
# Shields give an armor class of +2, and leather armor (given later) gives an AC of 11 + Dex mod
            armor_class = ((dnd_dict.character_dict["Stats"]["dexterity"]["mod"]) +13)
            print("Armor Class: ",armor_class)
            dnd_dict.character_dict["armor_class"] = armor_class
            break

        elif weapon_choice1 == '2':
            dnd_weapon.simple_weapon()

# Leather armor (given later) gives an AC of 11 + Dex mod
            dnd_weapon.light_armor(11)
            print("Armor Class: ",dnd_dict.character_dict['armor_class'])
            break

        else:
            print("Invalid Selection")
            continue

    while True:
        weapon_choice2 = input("""Choose what your secondary weapon will be:
1) A scimitar
2) Any simple melee weapon
Enter your selection: """)
        if weapon_choice2 == '1':
            dnd_skills.equip_mod('scimitar1','Scimitar')
            dnd_dict.character_dict['weapons']['scimitar'] = 'Scimitar'
            break
 
        elif weapon_choice2 == '2':
            dnd_weapon.simple_melee()
            break

        else:
            print("Invalid Selection")
            continue

# Only done if the character does not have a natural armor class
    if dnd_dict.character_dict['natural_armor_class'] == 0:
        dnd_dict.character_dict['base_armor_class'] = 10 + dnd_dict.character_dict['Stats']['dexterity']['mod']

    dnd_skills.equip_mod('leather_armor1','Leather Armor')
    dnd_skills.equip_mod('druidic_focus1','Druidic Focus')

    dnd_pack.explorer_pack()

    dnd_magic.druid_magic()

# Setting the Spell Save DC and Spell Attack Modifiers
    spell_attack = ((dnd_dict.character_dict["Stats"]["wisdom"]['mod']) + dnd_dict.character_dict['prof_bonus'])
    print("Spell Attack Modifier: {}".format(spell_attack))
    dnd_dict.character_dict["spell_modifier"]['wisdom']['attack'] = spell_attack

    spell_save = ((dnd_dict.character_dict["Stats"]["wisdom"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
    print("Spell DC: {}".format(spell_save))
    dnd_dict.character_dict["spell_modifier"]['wisdom']['save'] = spell_save

    dnd_dict.character_dict['initial_class'] = 'Druid'

#     Passive perception = 10 + Perception score
    passive_perception = (dnd_dict.character_dict["perception"] + 10)
    print("Passive Perception: ",passive_perception)
    dnd_dict.character_dict["passive_perception"] = passive_perception
    dnd_skills.skill_calculation()
    dnd_dict.character_dict['caster_level'] = 1
    dnd_skills.spell_slot_selection()

    dnd_features.druid_features()

# If you pick Variant Human or Custom Lineage, pick a feat just in case you need to satisfy a prerequisite
    if dnd_dict.character_dict['race'] == 'Variant Human' or dnd_dict.character_dict['race'] == 'Custom Lineage':
        dnd_feats.choose_feat()
    return


def fighter():

    hp_mod = (dnd_dict.character_dict["hp"] + 10)
    dnd_dict.character_dict['hp'] = hp_mod
# Set Hit Dice
    dnd_dict.character_dict["d10"] = 1

    print("Hit Points: ",hp_mod)
    print("Hit Dice: 1d10 per fighter level")

    dnd_dict.character_dict["player_class"]["fighter"]["class_level"] = 1

# Setting the armor and weapon proficiencies
    armor_prof={'light_armor':'Light Armor', 'medium_armor':'Medium Armor', 'heavy_armor':'Heavy Armor', 'shields':'Shields'}
    dnd_dict.character_dict['Armor_Prof'].update(armor_prof)
    weapon_prof={'simple_weapons':'Simple Weapons', 'martial_weapons':'Martial Weapons'}
    dnd_dict.character_dict['Weapon_Prof'].update(weapon_prof)


#Selecting the skills
    i = 1
    while i < 3:
        while True:
            check_prof = dnd_dict.character_dict['skill_prof']
            print(f'{i}/2')
            skill_list = ['Acrobatics','Animal Handling','Athletics','History','Insight','Intimidation','Perception','Survival']
            dnd_skills.skill_addition(skill_list,dnd_dict.character_dict['skill_prof'])
            i+=1
            break


# Setting the saving throws.
    dnd_dict.character_dict['saving_throws']['strength'] = 'Strength'
    dnd_dict.character_dict['saving_throws']['constitution'] = 'Constitution'
    dnd_skills.saving_throw_calc()

# Getting equipment

    while True:
        weapon_choice1 = input("""Choose what your first set of equipment will be:
1) Chain Mail
2) Leather Armor, Longbow, and 20 arrows
Enter your selection: """)
        if weapon_choice1 == '1':
            dnd_skills.equip_mod('chain_mail1','Chain Mail')
            dnd_dict.character_dict['chest_equip_armor']['chain_mail'] = 'Chain Mail'
            dnd_dict.character_dict['chest_armor'] = 'Chain Mail'
#Chain mail gives an AC of 16
            dnd_dict.character_dict['armor_class'] = 16
            break

        elif weapon_choice1 == '2':
            dnd_skills.equip_mod('leather_armor1','Leather Armor')
            dnd_dict.character_dict['chest_equip_armor']['leather_armor'] = 'Leather Armor'
            dnd_dict.character_dict['chest_armor'] = 'Leather Armor'
            dnd_skills.equip_mod('longbow1','Longbow')
            dnd_dict.character_dict['weapons']['longbow'] = 'Longbow'
            dnd_skills.equip_mod('arrows20','Arrows')

# Leather armor (given later) gives an AC of 11 + Dex mod
            dnd_weapon.light_armor(11)
            print("Armor Class: ",dnd_dict.character_dict['armor_class'])
# Do not print the AC here, since it might be boosted in the next choice with the shield
            break

        else:
            print("Invalid Selection")
            continue

    while True:
        weapon_choice2 = input("""Choose what your secondary weapon will be:
1) A martial weapon and a shield
2) Two martial weapons
Enter your selection: """)
        if weapon_choice2 == '1':
            dnd_weapon.martial_weapon()
            dnd_skills.equip_mod('shield1','Shield')
            dnd_dict.character_dict['shield_equip_armor'] = 'Shield'
            dnd_dict.character_dict['shield'] = 'Shield'
# Shields give +2 to AC
            dnd_dict.character_dict['armor_class'] += 2
            print("Armor Class: ",dnd_dict.character_dict['armor_class'])
            break
 
        elif weapon_choice2 == '2':
            dnd_weapon.double_martial()
# Since there is no bonus, put the regular armor class here
            print("Armor Class: ",dnd_dict.character_dict['armor_class'])
            break

        else:
            print("Invalid Selection")
            continue

    while True:
        weapon_choice3 = input("""Choose what your ranged weapon will be:
1) A light crossbow and 20 bolts
2) Two handaxes
Enter your selection: """)
        if weapon_choice3 == '1':
            dnd_skills.equip_mod('light_crossbow1','Light Crossbow')
            dnd_dict.character_dict['weapons']['light_crossbow'] = 'Light Crossbow'
            dnd_skills.equip_mod('bolts20','Bolts')
            break

        elif weapon_choice3 == '2':
            dnd_skills.equip_mod('handaxe2','Handaxe')
            dnd_dict.character_dict['weapons']['handaxe'] = 'Handaxe'
            break

        else:
            print("Invalid Selection")
            continue

    while True:
        pack_choice = input("""Choose what your pack will be:
1) A dungeoneer\'s pack
2) An explorer\'s pack
Enter your selection: """)
        if pack_choice == '1':
            dnd_pack.dungeoneer_pack()
            break

        elif pack_choice == '2':
            dnd_pack.explorer_pack()
            break

        else:
            print("Invalid Selection")
            continue

    dnd_dict.character_dict['initial_class'] = 'Fighter'
# Only done if the character does not have a natural armor class
    if dnd_dict.character_dict['natural_armor_class'] == 0:
        dnd_dict.character_dict['base_armor_class'] = 10 + dnd_dict.character_dict['Stats']['dexterity']['mod']

# Select Fighting Style
    dnd_features.fighter1()
#     Passive perception = 10 + Perception score
    passive_perception = (dnd_dict.character_dict["perception"] + 10)
    print("Passive Perception: ",passive_perception)
    dnd_dict.character_dict["passive_perception"] = passive_perception
    dnd_skills.skill_calculation()



# If you pick Variant Human or Custom Lineage, pick a feat just in case you need to satisfy a prerequisite
    if dnd_dict.character_dict['race'] == 'Variant Human' or dnd_dict.character_dict['race'] == 'Custom Lineage':
        dnd_feats.choose_feat()
    return


def monk():

    hp_mod = (dnd_dict.character_dict["hp"] + 8)
    dnd_dict.character_dict['hp'] = hp_mod
# Set Hit Dice
    dnd_dict.character_dict["d8"] = 1

    print("Hit Points: ",hp_mod)
    print("Hit Dice: 1d8 per monk level")

    dnd_dict.character_dict["player_class"]["monk"]["class_level"] = 1

    while True:
        tool_choice = input("""Select which tool you will be proficient with:
1) One type of artisan's tools
2) One musical instrument
Enter your selection: """)
        if tool_choice == '1':
            dnd_tools.artisan_tools()
            break
 
        elif tool_choice == '2':
            dnd_tools.musical_instrument()
            break

        else:
            print("Invalid Selection")
            continue

# Setting the armor and weapon proficiencies


    weapon_prof = {'shortswords':'Shortswords', 'simple_weapons':'Simple Weapons'}
    dnd_dict.character_dict['Weapon_Prof'].update(weapon_prof)

#Selecting the skills
    i = 1
    while i < 3:
        while True:
            check_prof = dnd_dict.character_dict['skill_prof']
            print(f'{i}/2')
            skill_list = ['Acrobatics','Athletics','History','Insight','Religion','Stealth']
            dnd_skills.skill_addition(skill_list,dnd_dict.character_dict['skill_prof'])
            i+=1
            break





# Setting the saving throws.
    dnd_dict.character_dict['saving_throws']['strength'] = 'Strength'
    dnd_dict.character_dict['saving_throws']['dexterity'] = 'Dexterity'
    dnd_skills.saving_throw_calc()

# Getting equipment

    while True:
        weapon_choice = input("""Choose your primary weapon:
1) A Shortsword
2) Any Simple Weapon
Enter your selection: """)
        if weapon_choice == '1':
            dnd_skills.equip_mod('shortsword1','Shortsword')
            dnd_dict.character_dict['weapons']['shortsword'] = 'Shortsword'
            break

        elif weapon_choice == '2':
            dnd_weapon.simple_weapon()
            break

        else:
            print("Invalid Selection")
            continue



    while True:
        pack_choice = input("""Choose what your pack will be:
1) A dungeoneer's pack
2) An explorer's pack
Enter your selection: """)
        if pack_choice == '1':
            dnd_pack.dungeoneer_pack()
            break
 
        elif pack_choice == '2':
            dnd_pack.explorer_pack()
            break

        else:
            print("Invalid Selection")
            continue

    dnd_skills.equip_mod('dart10','Dart')

    dnd_features.monk_features()


#Armor Class = 10 + Dexterity Modifier + Wisdom Modifier
    AC= (10 + dnd_dict.character_dict['Stats']['dexterity']['mod'] + (dnd_dict.character_dict['Stats']['wisdom']['mod']))
    print("Armor Class: ",AC)
    dnd_dict.character_dict["monk_armor_class"] = AC
# Only done if the character does not have a natural armor class
    if dnd_dict.character_dict['natural_armor_class'] == 0:
        dnd_dict.character_dict['base_armor_class'] = 10 + dnd_dict.character_dict['Stats']['dexterity']['mod']

    armor_class = ((dnd_dict.character_dict["Stats"]["dexterity"]["mod"]) + 10)
    dnd_dict.character_dict["armor_class"] = armor_class

    dnd_dict.character_dict['initial_class'] = 'Monk'

#     Passive perception = 10 + Perception score
    passive_perception = (dnd_dict.character_dict["perception"] + 10)
    print("Passive Perception: ",passive_perception)
    dnd_dict.character_dict["passive_perception"] = passive_perception
    dnd_skills.skill_calculation()


# If you pick Variant Human or Custom Lineage, pick a feat just in case you need to satisfy a prerequisite
    if dnd_dict.character_dict['race'] == 'Variant Human' or dnd_dict.character_dict['race'] == 'Custom Lineage':
        dnd_feats.choose_feat()
    return


def paladin():

    hp_mod = (dnd_dict.character_dict["hp"] + 10)
    dnd_dict.character_dict['hp'] = hp_mod
# Set Hit Dice
    dnd_dict.character_dict["d10"] = 1

    print("Hit Points: ",hp_mod)
    print("Hit Dice: 1d10 per paladin level")

    dnd_dict.character_dict["player_class"]["paladin"]["class_level"] = 1

# Setting the armor and weapon proficiencies
    armor_prof={'light_armor':'Light Armor', 'medium_armor':'Medium Armor', 'heavy_armor':'Heavy Armor', 'shields':'Shields'}
    dnd_dict.character_dict['Armor_Prof'].update(armor_prof)
    weapon_prof={'simple_weapons':'Simple Weapons', 'martial_weapons':'Martial Weapons'}
    dnd_dict.character_dict['Weapon_Prof'].update(weapon_prof)

#Selecting the skills
    i = 1
    while i < 3:
        while True:
            check_prof = dnd_dict.character_dict['skill_prof']
            print(f'{i}/2')
            skill_list = ['Athletics','Insight','Intimidation','Medicine','Persuasion','Religion']
            dnd_skills.skill_addition(skill_list,dnd_dict.character_dict['skill_prof'])
            i+=1
            break






# Setting the saving throws.
    dnd_dict.character_dict['saving_throws']['wisdom'] = 'Wisdom'
    dnd_dict.character_dict['saving_throws']['charisma'] = 'Charisma'
    dnd_skills.saving_throw_calc()

# Getting equipment
    print("Equipment given: chain mail, a holy symbol")

# Chain mail gives a base armor class of 16
    dnd_skills.equip_mod('chain_mail1','Chain Mail')
    dnd_dict.character_dict['chest_equip_armor']['chain_mail'] = 'Chain Mail'
    dnd_dict.character_dict['chest_armor'] = 'Chain Mail'
    dnd_skills.equip_mod('holy_symbol1','Holy Symbol')
    dnd_dict.character_dict["armor_class"] = 16
# Only done if the character does not have a natural armor class
    if dnd_dict.character_dict['natural_armor_class'] == 0:
        dnd_dict.character_dict['base_armor_class'] = 10 + dnd_dict.character_dict['Stats']['dexterity']['mod']

    while True:
        weapon_choice1 = input("""What primary weapon do you want?
1) A martial weapon and a shield
2) Two martial weapons
Enter your selection: """)
        if weapon_choice1 == '1':
            dnd_weapon.martial_weapon()
# Shield gives +2 to armor class
#            dnd_dict.character_dict["armor_class"] = 16
            dnd_dict.character_dict['shield_equip_armor']['shield'] = 'Shield'
            dnd_dict.character_dict['shield'] = 'Shield'
            armor_class = (dnd_dict.character_dict["armor_class"] + 2)
            print("Armor Class: 18")
            dnd_dict.character_dict["armor_class"] = armor_class
            break

        elif weapon_choice1 == '2':
            dnd_weapon.double_martial()
            print("Armor Class: 16")
            break
        else:
            print("Invalid Selection")
            continue

    while True:
        weapon_choice2 = input("""What secondary weapon do you want?
1) Five Javelins
2) Any simple weapon
Enter your selection: """)
        if weapon_choice2 == '1':
            dnd_skills.equip_mod('javelin5','Javelin')
            dnd_dict.character_dict['weapons']['javelin'] = 'Javelin'
            break
 
        elif weapon_choice2 == '2':
            dnd_weapon.simple_weapon()
            break

        else:
            print("Invalid Selection")
            continue

    while True:
        pack_choice = input("""What pack do you want?
1) A priest's pack
2) An explorer's pack
Enter your selection: """)
        if pack_choice == '1':
            dnd_pack.priest_pack()
            break
 
        elif pack_choice == '2':
            dnd_pack.explorer_pack()
            break

        else:
            print("Invalid Selection")
            continue

# Setting the Spell Save DC and Spell Attack Modifiers
    spell_attack = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'])
    print("Spell Attack Modifier: {}".format(spell_attack))
    dnd_dict.character_dict["spell_modifier"]['charisma']['attack'] = spell_attack

    spell_save = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
    print("Spell DC: {}".format(spell_save))
    dnd_dict.character_dict["spell_modifier"]['charisma']['save'] = spell_save

    dnd_dict.character_dict['initial_class'] = 'Paladin'

#     Passive perception = 10 + Perception score
    passive_perception = (dnd_dict.character_dict["perception"] + 10)
    print("Passive Perception: ",passive_perception)
    dnd_dict.character_dict["passive_perception"] = passive_perception
    dnd_skills.spell_slot_selection()

    dnd_skills.skill_calculation()
    dnd_features.paladin_features()

# If you pick Variant Human or Custom Lineage, pick a feat just in case you need to satisfy a prerequisite
    if dnd_dict.character_dict['race'] == 'Variant Human' or dnd_dict.character_dict['race'] == 'Custom Lineage':
        dnd_feats.choose_feat()
    return


def ranger():

    hp_mod = (dnd_dict.character_dict["hp"] + 10)
    dnd_dict.character_dict['hp'] = hp_mod
# Set Hit Dice
    dnd_dict.character_dict["d10"] = 1

    print("Hit Points: ",hp_mod)
    print("Hit Dice: 1d10 per ranger level")

    dnd_dict.character_dict["player_class"]["ranger"]["class_level"] = 1

# Setting the armor and weapon proficiencies

    armor_prof={'light_armor':'Light Armor', 'medium_armor':'Medium Armor', 'shields':'Shields'}
    dnd_dict.character_dict['Armor_Prof'].update(armor_prof)
    weapon_prof={'simple_weapons':'Simple Weapons', 'martial_weapons':'Martial Weapons'}
    dnd_dict.character_dict['Weapon_Prof'].update(weapon_prof)

#Selecting the skills
    i = 1
    while i < 4:
        while True:
            check_prof = dnd_dict.character_dict['skill_prof']
            print(f'{i}/3')
            skill_list = ['Animal Handling','Athletics','Insight','Investigation','Nature','Perception','Stealth','Survival']
            dnd_skills.skill_addition(skill_list,dnd_dict.character_dict['skill_prof'])
            i+=1
            break


# Setting the saving throws.
    dnd_dict.character_dict['saving_throws']['strength'] = 'Strength'
    dnd_dict.character_dict['saving_throws']['dexterity'] = 'Dexterity'
    dnd_skills.saving_throw_calc()

# Getting equipment
# Choose your armor: Leather is 11 + Dex mod.
    while True:
        armor_choice = input("""Choose which armor you will take:
1) Leather Armor
2) Scale Mail
Enter your selection: """)
        if armor_choice == '1':
            dnd_skills.equip_mod('leather_armor1','Leather Armor')
            dnd_dict.character_dict['chest_equip_armor']['leather_armor'] = 'Leather Armor'
            dnd_dict.character_dict['chest_armor'] = 'Leather Armor'
            dnd_weapon.light_armor(11)
            print("Armor Class: ",dnd_dict.character_dict['armor_class'])
            break
 
        elif armor_choice == '2':
            dnd_skills.equip_mod('scale_mail1','Scale Mail')
            dnd_dict.character_dict['chest_equip_armor']['scale_mail'] = 'Scale Mail'
            dnd_dict.character_dict['chest_armor'] = 'Scale Mail'
            dnd_skills.med_armor(14)
            print("Armor Class: ",dnd_dict.character_dict['armor_class'])
            break

        else:
            print("Invalid Selection")
            continue

    while True:
        weapon_choice = input("""Choose what your secondary weapon will be:
1) Two shortswords
2) Two simple melee weapons
Enter your selection: """)
        if weapon_choice == '1':
            dnd_skills.equip_mod('shortsword2','Shortsword')
            dnd_dict.character_dict['weapons']['shortsword'] = 'Shortsword'
            break
 
        elif weapon_choice == '2':
            dnd_weapon.double_simple_melee()
            break

        else:
            print("Invalid Selection")
            continue

    while True:
        pack_choice = input("""Choose what your pack will be:
1) A dungeoneer\'s pack
2) An explorer\'s pack
Enter your selection: """)
        if pack_choice == '1':
            dnd_pack.dungeoneer_pack()
            break
 
        elif pack_choice == '2':
            dnd_pack.explorer_pack()
            break

        else:
            print("Invalid Selection")
            continue
# Only done if the character does not have a natural armor class
    if dnd_dict.character_dict['natural_armor_class'] == 0:
        dnd_dict.character_dict['base_armor_class'] = 10 + dnd_dict.character_dict['Stats']['dexterity']['mod']

    dnd_skills.equip_mod('longbow1','Longbow')
    dnd_dict.character_dict['weapons']['longbow'] = 'Longbow'
    dnd_skills.equip_mod('arrows20','Arrows')

# Setting the Spell Save DC and Spell Attack Modifiers
    spell_attack = ((dnd_dict.character_dict["Stats"]["wisdom"]['mod']) + dnd_dict.character_dict['prof_bonus'])
    print("Spell Attack Modifier: {}".format(spell_attack))
    dnd_dict.character_dict["spell_modifier"]['wisdom']['attack'] = spell_attack

    spell_save = ((dnd_dict.character_dict["Stats"]["wisdom"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
    print("Spell DC: {}".format(spell_save))
    dnd_dict.character_dict["spell_modifier"]['wisdom']['save'] = spell_save

#     Passive perception = 10 + Perception score
    passive_perception = (dnd_dict.character_dict["perception"] + 10)
    print("Passive Perception: ",passive_perception)
    dnd_dict.character_dict["passive_perception"] = passive_perception


    dnd_dict.character_dict['initial_class'] = 'Ranger'

    dnd_language.language()

    dnd_skills.spell_slot_selection()
    dnd_skills.skill_calculation()
    dnd_features.ranger_features()

# If you pick Variant Human or Custom Lineage, pick a feat just in case you need to satisfy a prerequisite
    if dnd_dict.character_dict['race'] == 'Variant Human' or dnd_dict.character_dict['race'] == 'Custom Lineage':
        dnd_feats.choose_feat()
    return


def rogue():

    hp_mod = (dnd_dict.character_dict["hp"] + 8)
    dnd_dict.character_dict['hp'] = hp_mod
# Set Hit Dice
    dnd_dict.character_dict["d8"] = 1

    print("Hit Points: ",hp_mod)
    print("Hit Dice: 1d8 per rogue level")

    dnd_dict.character_dict["player_class"]["rogue"]["class_level"] = 1

# Setting the armor and weapon proficiencies

    weapon_prof = {'simple_weapons':'Simple Weapons', 'hand_crossbows':'Hand Crossbows', 'rapiers':'Rapiers', 'longswords':'Longswords','shortswords':'Shortswords'}
    dnd_dict.character_dict['Weapon_Prof'].update(weapon_prof)

    armor_prof = {'light_armor':'Light Armor'}
    dnd_dict.character_dict['Armor_Prof'].update(armor_prof)
    dnd_dict.character_dict["Kits"]['thieves_tools'] = 'Thieves\' Tools'

#Selecting the skills
    dnd_skills.rogue_skill_choice()


# Setting the saving throws.
    dnd_dict.character_dict['saving_throws']['dexterity'] = 'Dexterity'
    dnd_dict.character_dict['saving_throws']['intelligence'] = 'Intelligence'
    dnd_skills.saving_throw_calc()

# Getting equipment
    while True:
        weapon_choice1 = input("""Choose what your primary weapon will be:
1) A Rapier
2) A Shortsword
Enter your selection: """)
        if weapon_choice1 == '1':
            dnd_skills.equip_mod('rapier1','Rapier')
            dnd_dict.character_dict['weapons']['rapier'] = 'Rapier'
            break
 
        elif weapon_choice1 == '2':
            dnd_skills.equip_mod('shortsword1','Shortsword')
            dnd_dict.character_dict['weapons']['shortsword'] = 'Shortsword'
            break

        else:
            print("Invalid Selection")
            continue

    while True:
        weapon_choice2 = input("""Choose what your secondary weapon will be:
1) A Shortbow and a quiver of 20 arrows
2) A Shortsword
Enter your selection: """)
        if weapon_choice2 == '1':
            dnd_skills.equip_mod('shortbow1','Shortbow')
            dnd_dict.character_dict['weapons']['shortbow'] = 'Shortbow'
            dnd_skills.equip_mod('arrows20','Arrows')
            break
 
        elif weapon_choice2 == '2':
            dnd_skills.equip_mod('shortsword1','Shortsword')
            dnd_dict.character_dict['weapons']['shortsword'] = 'Shortsword'
            break

        else:
            print("Invalid Selection")
            continue

    while True:
        pack_choice = input("""Choose what your pack will be:
1) A burgler\'s pack
2) An dungeoneer\'s pack
3) An explorer\'s pack
Enter your selection: """)
        if pack_choice == '1':
            dnd_pack.burgler_pack()
            break
 
        elif pack_choice == '2':
            dnd_pack.dungeoneer_pack()
            break

        elif pack_choice == '3':
            dnd_pack.explorer_pack()
            break

        else:
            print("Invalid Selection")
            continue

    dnd_skills.equip_mod('leather_armor1','Leather Armor')
    dnd_dict.character_dict['chest_equip_armor']['leather_armor'] = 'Leather Armor'
    dnd_dict.character_dict['chest_armor'] = 'Leather Armor'
    dnd_skills.equip_mod('dagger2','Dagger')
    dnd_dict.character_dict['weapons']['dagger'] = 'Dagger'
    dnd_skills.equip_mod('thieves_tools1','Thieve\'s Tools')

# Leather armor AC is 11 + Dex mod
    dnd_weapon.light_armor(11)
    print("Armor Class: ",dnd_dict.character_dict['armor_class'])
# Only done if the character does not have a natural armor class
    if dnd_dict.character_dict['natural_armor_class'] == 0:
        dnd_dict.character_dict['base_armor_class'] = 10 + dnd_dict.character_dict['Stats']['dexterity']['mod']

    dnd_dict.character_dict['initial_class'] = 'Rogue'

#     Passive perception = 10 + Perception score
    passive_perception = (dnd_dict.character_dict["perception"] + 10)
    print("Passive Perception: ",passive_perception)
    dnd_dict.character_dict["passive_perception"] = passive_perception

    dnd_skills.skill_calculation()
    dnd_features.rogue_features()

# If you pick Variant Human or Custom Lineage, pick a feat just in case you need to satisfy a prerequisite
    if dnd_dict.character_dict['race'] == 'Variant Human' or dnd_dict.character_dict['race'] == 'Custom Lineage':
        dnd_feats.choose_feat()
    return


def sorcerer():

    hp_mod = (dnd_dict.character_dict["hp"] + 6)
    dnd_dict.character_dict['hp'] = hp_mod
# Set Hit Dice
    dnd_dict.character_dict["d6"] = 1

    print("Hit Points: ",hp_mod)
    print("Hit Dice: 1d6 per sorcerer level")

    dnd_dict.character_dict["player_class"]["sorcerer"]["class_level"] = 1

# Setting the armor and weapon proficiencies
    weapon_prof={'daggers':'Daggers', 'darts':'Darts', 'slings':'Slings', 'quarterstaffs':'Quarterstaffs', 'light_crossbows':'Light Crossbows'}
    dnd_dict.character_dict['Weapon_Prof'].update(weapon_prof)

#Selecting the skills
    i = 1
    while i < 3:
        while True:
            check_prof = dnd_dict.character_dict['skill_prof']
            print(f'{i}/2')
            skill_list = ['Arcana','Deception','Insight','Intimidation','Persuasion','Religion']
            dnd_skills.skill_addition(skill_list,dnd_dict.character_dict['skill_prof'])
            i+=1
            break



# Setting the saving throws.
    dnd_dict.character_dict['saving_throws']['constitution'] = 'Constitution'
    dnd_dict.character_dict['saving_throws']['charisma'] = 'Charisma'
    dnd_skills.saving_throw_calc()


# Getting equipment
    while True:
        weapon_choice = input("""What primary weapon do you want?
1) A light crossbow with 20 bolts
2) Any simple weapon
Enter your selection: """)
        if weapon_choice == '1':
            dnd_skills.equip_mod('light_crossbow1','Light Crossbow')
            dnd_dict.character_dict['weapons']['light_crossbow'] = 'Light Crossbow'
            dnd_skills.equip_mod('bolts20','Bolts')
            break
 
        elif weapon_choice == '2':
            dnd_weapon.simple_weapon()
            break

        else:
            print("Invalid Selection")
            continue

    while True:
        focus_choice = input("""What tool will you use to cast your spells?
1) A component pouch
2) An arcana focus
Enter your selection: """)
        if focus_choice == '1':
            dnd_skills.equip_mod('component_pouch1','Component Pouch')
            break
 
        elif focus_choice == '2':
            dnd_skills.equip_mod('arcane_focus1','Arcane Focus')
            break

        else:
            print("Invalid Selection")
            continue

    while True:
        pack_choice = input("""What pack do you want?
1) A dungeoneer's pack
2) An explorer's pack
Enter your selection: """)
        if pack_choice == '1':
            dnd_pack.dungeoneer_pack()
            break
 
        elif pack_choice == '2':
            dnd_pack.explorer_pack()
            break

        else:
            print("Invalid Selection")
            continue

    dnd_skills.equip_mod('dagger2','Dagger')
    dnd_dict.character_dict['weapons']['dagger'] = 'Dagger'


    dnd_magic.sorcerer_magic()

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

    armor_class = ((dnd_dict.character_dict["Stats"]["dexterity"]["mod"]) + 10)
    dnd_dict.character_dict["armor_class"] = armor_class
    print("Armor Class: ",armor_class)
# Only done if the character does not have a natural armor class
    if dnd_dict.character_dict['natural_armor_class'] == 0:
        dnd_dict.character_dict['base_armor_class'] = 10 + dnd_dict.character_dict['Stats']['dexterity']['mod']

# Setting the Spell Save DC and Spell Attack Modifiers
    spell_attack = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'])
    print("Spell Attack Modifier: {}".format(spell_attack))
    dnd_dict.character_dict["spell_modifier"]['charisma']['attack'] = spell_attack

    spell_save = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
    print("Spell DC: {}".format(spell_save))
    dnd_dict.character_dict["spell_modifier"]['charisma']['save'] = spell_save

    dnd_dict.character_dict['initial_class'] = 'Sorcerer'

#     Passive perception = 10 + Perception score
    passive_perception = (dnd_dict.character_dict["perception"] + 10)
    print("Passive Perception: ",passive_perception)
    dnd_dict.character_dict["passive_perception"] = passive_perception
    dnd_skills.skill_calculation()
    dnd_dict.character_dict['caster_level'] = 1
    dnd_skills.spell_slot_selection()


# If you pick Variant Human or Custom Lineage, pick a feat just in case you need to satisfy a prerequisite
    if dnd_dict.character_dict['race'] == 'Variant Human' or dnd_dict.character_dict['race'] == 'Custom Lineage':
        dnd_feats.choose_feat()
    return


def warlock():

    hp_mod = (dnd_dict.character_dict["hp"] + 8)
    dnd_dict.character_dict['hp'] = hp_mod
# Set Hit Dice
    dnd_dict.character_dict["d8"] = 1

    print("Hit Points: ",hp_mod)
    print("Hit Dice: 1d8 per warlock level")

    dnd_dict.character_dict["player_class"]["warlock"]["class_level"] = 1

# Setting the armor and weapon proficiencies

    armor_prof = {'light_armor':'Light Armor'}
    dnd_dict.character_dict['Armor_Prof'].update(armor_prof)

    weapon_prof = {'simple_weapons':'Simple Weapons'}
    dnd_dict.character_dict['Weapon_Prof'].update(weapon_prof)

#Selecting the skills
    i = 1
    while i < 3:
        while True:
            check_prof = dnd_dict.character_dict['skill_prof']
            print(f'{i}/2')
            skill_list = ['Arcana','Deception','History','Intimidation','Investigation','Nature','Religion']
            dnd_skills.skill_addition(skill_list,dnd_dict.character_dict['skill_prof'])
            i+=1
            break




# Setting the saving throws.
    dnd_dict.character_dict['saving_throws']['wisdom'] = 'Wisdom'
    dnd_dict.character_dict['saving_throws']['charisma'] = 'Charisma'
    dnd_skills.saving_throw_calc()

# Getting equipment
    while True:
        weapon_choice = input("""What primary weapon do you want?
1) A light crossbow with 20 bolts
2) Any simple weapon
Enter your selection: """)
        if weapon_choice == '1':
            dnd_skills.equip_mod('light_crossbow1','Light Crossbow')
            dnd_dict.character_dict['weapons']['light_crossbow'] = 'Light Crossbow'
            dnd_skills.equip_mod('bolts20','Bolts')
            break

        elif weapon_choice == '2':
            dnd_weapon.simple_weapon()
            break

        else:
            print("Invalid Selection")
            continue

    while True:
        focus_choice = input("""What tool will you use to cast your spells?
1) A component pouch
2) An arcana focus
Enter your selection: """)
        if focus_choice == '1':
            dnd_skills.equip_mod('component_pouch1','Component Pouch')
            break
 
        elif focus_choice == '2':
            dnd_skills.equip_mod('arcane_focus1','Arcane Focus')
            break

        else:
            print("Invalid Selection")
            continue

    while True:
        pack_choice = input("""What pack do you want?
1) A scholar's pack
2) A dungeoneer's pack
Enter your selection: """)
        if pack_choice == '1':
            dnd_pack.scholar_pack()
            break
 
        elif pack_choice == '2':
            dnd_pack.dungeoneer_pack()
            break

        else:
            print("Invalid Selection")
            continue

    dnd_skills.equip_mod('leather_armor1','Leather Armor')
    dnd_dict.character_dict['chest_equip_armor']['leather_armor'] = 'Leather Armor'
    dnd_dict.character_dict['chest_armor'] = 'Leather Armor'
    dnd_skills.equip_mod('dagger2','Dagger')
    dnd_dict.character_dict['weapons']['dagger'] = 'Dagger'
    dnd_weapon.simple_weapon()
# Leather armor is 11 + Dex mod

    dnd_weapon.light_armor(11)
    print("Armor Class: ",dnd_dict.character_dict['armor_class'])

# Only done if the character does not have a natural armor class
    if dnd_dict.character_dict['natural_armor_class'] == 0:
        dnd_dict.character_dict['base_armor_class'] = 10 + dnd_dict.character_dict['Stats']['dexterity']['mod']


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

# Setting the Spell Save DC and Spell Attack Modifiers
    spell_attack = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'])
    print("Spell Attack Modifier: {}".format(spell_attack))
    dnd_dict.character_dict["spell_modifier"]['charisma']['attack'] = spell_attack

    spell_save = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
    print("Spell DC: {}".format(spell_save))
    dnd_dict.character_dict["spell_modifier"]['charisma']['save'] = spell_save

    dnd_dict.character_dict['initial_class'] = 'Warlock'

#     Passive perception = 10 + Perception score
    passive_perception = (dnd_dict.character_dict["perception"] + 10)
    print("Passive Perception: ",passive_perception)
    dnd_dict.character_dict["passive_perception"] = passive_perception
    dnd_skills.skill_calculation()

    dnd_dict.character_dict['pact_magic']['first'] = 1


# If you pick Variant Human or Custom Lineage, pick a feat just in case you need to satisfy a prerequisite
    if dnd_dict.character_dict['race'] == 'Variant Human' or dnd_dict.character_dict['race'] == 'Custom Lineage':
        dnd_feats.choose_feat()
    return


def wizard():

    hp_mod = (dnd_dict.character_dict["hp"] + 6)
    dnd_dict.character_dict['hp'] = hp_mod
# Set Hit Dice
    dnd_dict.character_dict["d6"] = 1


    print("Hit Points: ",hp_mod)
    print("Hit Dice: 1d6 per wizard level")


    dnd_dict.character_dict["player_class"]["wizard"]["class_level"] = 1

# Setting the armor and weapon proficiencies

    weapon_prof={'daggers':'Daggers', 'darts':'Darts', 'slings':'Slings', 'quarterstaffs':'Quarterstaffs', 'light_crossbows':'Light Crossbows'}
    dnd_dict.character_dict['Weapon_Prof'].update(weapon_prof)

#Selecting the skills
    i = 1
    while i < 3:
        while True:
            check_prof = dnd_dict.character_dict['skill_prof']
            print(f'{i}/2')
            skill_list = ['Arcana','History','Insight','Investigation','Medicine','Religion']
            dnd_skills.skill_addition(skill_list,dnd_dict.character_dict['skill_prof'])
            i+=1
            break



# Setting the saving throws.
    dnd_dict.character_dict['saving_throws']['intelligence'] = 'Intelligence'
    dnd_dict.character_dict['saving_throws']['wisdom'] = 'Wisdom'
    dnd_skills.saving_throw_calc()

# Getting equipment
    while True:
        weapon_choice = input("""What primary weapon do you want?
1) A quarterstaff
2) A dagger
Enter your selection: """)
        if weapon_choice == '1':
            dnd_skills.equip_mod('quarterstaff1','Quarterstaff')
            dnd_dict.character_dict['weapons']['quarterstaff'] = 'Quarterstaff'
            break
 
        elif weapon_choice == '2':
            dnd_skills.equip_mod('dagger1','Dagger')
            dnd_dict.character_dict['weapons']['dagger'] = 'Dagger'
            break

        else:
            print("Invalid Selection")
            continue

    while True:
        focus_choice = input("""What tool will you use to cast your spells?
1) A component pouch
2) An arcana focus
Enter your selection: """)
        if focus_choice == '1':
            dnd_skills.equip_mod('component_pouch1','Component Pouch')
            break
 
        elif focus_choice == '2':
            dnd_skills.equip_mod('arcane_focus1','Arcane Focus')
            break

        else:
            print("Invalid Selection")
            continue

    while True:
        pack_choice = input("""What pack do you want?
1) A scholar's pack
2) An explorer's pack
Enter your selection: """)
        if pack_choice == '1':
            dnd_pack.scholar_pack()
            break
 
        elif pack_choice == '2':
            dnd_pack.explorer_pack()
            break

        else:
            print("Invalid Selection")
            continue

    dnd_skills.equip_mod('spellbook1','Spellbook')

#Armor Class = 10 + Dex mod
    armor_class = ((dnd_dict.character_dict["Stats"]["dexterity"]["mod"]) + 10)

    print("Armor Class: ",armor_class)
    dnd_dict.character_dict["armor_class"] = armor_class
# Only done if the character does not have a natural armor class
    if dnd_dict.character_dict['natural_armor_class'] == 0:
        dnd_dict.character_dict['base_armor_class'] = 10 + dnd_dict.character_dict['Stats']['dexterity']['mod']

    dnd_features.wizard1()
    dnd_magic.wizard_magic()

# Setting the Spell Save DC and Spell Attack Modifiers
    spell_attack = ((dnd_dict.character_dict["Stats"]["intelligence"]['mod']) + dnd_dict.character_dict['prof_bonus'])
    print("Spell Attack Modifier: {}".format(spell_attack))
    dnd_dict.character_dict["spell_modifier"]['intelligence']['attack'] = spell_attack

    spell_save = ((dnd_dict.character_dict["Stats"]["intelligence"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
    print("Spell DC: {}".format(spell_save))
    dnd_dict.character_dict["spell_modifier"]['intelligence']['save'] = spell_save

    dnd_dict.character_dict['initial_class'] = 'Wizard'

#     Passive perception = 10 + Perception score
    passive_perception = (dnd_dict.character_dict["perception"] + 10)
    print("Passive Perception: ",passive_perception)
    dnd_dict.character_dict["passive_perception"] = passive_perception
    dnd_skills.skill_calculation()

    dnd_dict.character_dict['caster_level'] = 1

    dnd_skills.spell_slot_selection()

# If you pick Variant Human or Custom Lineage, pick a feat just in case you need to satisfy a prerequisite
    if dnd_dict.character_dict['race'] == 'Variant Human' or dnd_dict.character_dict['race'] == 'Custom Lineage':
        dnd_feats.choose_feat()
    return

def player_class():
    while True:
        character_class = input("""Choose your class:
1) Artificer
2) Barbarian
3) Bard
4) Cleric
5) Druid
6) Fighter
7) Monk
8) Paladin
9) Ranger
10) Rogue
11) Sorcerer
12) Warlock
13) Wizard
Enter your selection: """)

        if character_class=='1':
            artificer()
            break

        elif character_class=='2':
            barbarian()
            break

        elif character_class=='3':
            bard()
            break

        elif character_class=='4':
            cleric()
            break

        elif character_class=='5':
            druid()
            break

        elif character_class=='6':
            fighter()
            break

        elif character_class=='7':
            monk()
            break

        elif character_class=='8':
            paladin()
            break

        elif character_class=='9':
            ranger()
            break

        elif character_class=='10':
            rogue()
            break

        elif character_class=='11':
            sorcerer()
            break

        elif character_class=='12':
            warlock()
            break

        elif character_class=='13':
            wizard()
            break

        else:
            print("Invalid input")
            continue
