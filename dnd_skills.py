#!/usr/bin/python3
import dnd_dict, dnd_class, math, re, copy, dnd_weapon
from tabulate import tabulate

def prof_modifier():
    if dnd_dict.character_dict['total_level'] == 1:
        dnd_dict.character_dict['prof_bonus'] = 2

    elif dnd_dict.character_dict['total_level'] == 5:
        dnd_dict.character_dict['prof_bonus'] = 3

    elif dnd_dict.character_dict['total_level'] == 9:
        dnd_dict.character_dict['prof_bonus'] = 4

    elif dnd_dict.character_dict['total_level'] == 13:
        dnd_dict.character_dict['prof_bonus'] = 5

    elif dnd_dict.character_dict['total_level'] == 18:
        dnd_dict.character_dict['prof_bonus'] = 6


def set_skill():
    dnd_dict.character_dict['acrobatics']=dnd_dict.character_dict['Stats']['dexterity']['mod']
    dnd_dict.character_dict['animal_handling']=dnd_dict.character_dict['Stats']['wisdom']['mod']
    dnd_dict.character_dict['arcana']=dnd_dict.character_dict['Stats']['intelligence']['mod']
    dnd_dict.character_dict['athletics']=dnd_dict.character_dict['Stats']['strength']['mod']
    dnd_dict.character_dict['deception']=dnd_dict.character_dict['Stats']['charisma']['mod']
    dnd_dict.character_dict['history']=dnd_dict.character_dict['Stats']['intelligence']['mod']
    dnd_dict.character_dict['insight']=dnd_dict.character_dict['Stats']['wisdom']['mod']
    dnd_dict.character_dict['intimidation']=dnd_dict.character_dict['Stats']['charisma']['mod']
    dnd_dict.character_dict['investigation']=dnd_dict.character_dict['Stats']['intelligence']['mod']
    dnd_dict.character_dict['medicine']=dnd_dict.character_dict['Stats']['wisdom']['mod']
    dnd_dict.character_dict['nature']=dnd_dict.character_dict['Stats']['intelligence']['mod']
    dnd_dict.character_dict['perception']=dnd_dict.character_dict['Stats']['wisdom']['mod']
    dnd_dict.character_dict['performance']=dnd_dict.character_dict['Stats']['charisma']['mod']
    dnd_dict.character_dict['persuasion']=dnd_dict.character_dict['Stats']['charisma']['mod']
    dnd_dict.character_dict['religion']=dnd_dict.character_dict['Stats']['intelligence']['mod']
    dnd_dict.character_dict['sleight_of_hand']=dnd_dict.character_dict['Stats']['dexterity']['mod']
    dnd_dict.character_dict['stealth']=dnd_dict.character_dict['Stats']['dexterity']['mod']
    dnd_dict.character_dict['survival']=dnd_dict.character_dict['Stats']['wisdom']['mod']


skill_list = ['Acrobatics','Animal Handling','Arcana','Athletics','Deception','History','Insight','Intimidation','Investigation','Medicine','Nature','Perception','Performance','Persuasion','Religion','Sleight of Hand','Stealth','Survival']

def skill_choice():
    if 'acrobatics' in dnd_dict.character_dict['skill_prof'] and 'animal_handling' in dnd_dict.character_dict['skill_prof'] and 'arcana' in dnd_dict.character_dict['skill_prof'] and 'athletics' in dnd_dict.character_dict['skill_prof'] and 'deception' in dnd_dict.character_dict['skill_prof'] and 'history' in dnd_dict.character_dict['skill_prof'] and 'insight' in dnd_dict.character_dict['skill_prof'] and 'intimidation' in dnd_dict.character_dict['skill_prof'] and 'investigation' in dnd_dict.character_dict['skill_prof'] and 'medicine' in dnd_dict.character_dict['skill_prof'] and 'nature' in dnd_dict.character_dict['skill_prof'] and 'perception' in dnd_dict.character_dict['skill_prof'] and 'performance' in dnd_dict.character_dict['skill_prof'] and 'persuasion' in dnd_dict.character_dict['skill_prof'] and 'religion' in dnd_dict.character_dict['skill_prof'] and 'sleight_of_hand' in dnd_dict.character_dict['skill_prof'] and 'stealth' in dnd_dict.character_dict['skill_prof'] and 'survival' in dnd_dict.character_dict['skill_prof']:
        pass
    else:
        skill_addition(skill_list,dnd_dict.character_dict['skill_prof'])




# Double the proficiency for a stat that already has proficiency
def expertise():
    tmp_dict = {}
    counter = 1
# Display the spells and their values
    for key, value in dnd_dict.character_dict['skill_prof'].items():
        print(f'{counter}) {value}')
        tmp_dict[counter] = value
        counter +=1

    while True:
        try:
            choice = int(input("Select what you want to add: "))
        except ValueError as e:
            print("Invalid Input")
            continue


        if tmp_dict.get(choice,{}) in dnd_dict.character_dict['expertise'].values():
            print(f'{tmp_dict.get(choice,{})} already known')
            continue

        elif tmp_dict.get(choice,{}):
            to_delete = tmp_dict[choice]
# Makes the spell lowercase and turns all spaces into underscores
            new_value = to_delete.lower().replace(' ','_')
            dnd_dict.character_dict['expertise'][new_value]=to_delete
            break
        else:
            print("Error: Invalid Input")






# Skill list for rogue. Will be repeated 4 times in the Rogue function.
rogue_skill_list = ['Acrobatics','Athletics','Deception','Insight','Intimidation','Investigation','Perception','Performance','Persuasion','Sleight of Hand','Stealth']

def rogue_skills():
    if 'acrobatics' in dnd_dict.character_dict['skill_prof'] and 'athletics' in dnd_dict.character_dict['skill_prof'] and 'deception' in dnd_dict.character_dict['skill_prof'] and 'insight' in dnd_dict.character_dict['skill_prof'] and 'intimidation' in dnd_dict.character_dict['skill_prof'] and 'investigation' in dnd_dict.character_dict['skill_prof'] and 'perception' in dnd_dict.character_dict['skill_prof'] and 'performance' in dnd_dict.character_dict['skill_prof'] and 'persuasion' in dnd_dict.character_dict['skill_prof'] and 'sleight_of_hand' in dnd_dict.character_dict['skill_prof'] and 'stealth' in dnd_dict.character_dict['skill_prof']:
        pass
    else:
        skill_addition(rogue_skill_list,dnd_dict.character_dict['skill_prof'])


def expertise_choice():
    if 'thieves_tools' in dnd_dict.character_dict['tool_expertise']:
        i = 1
        for i in range(i,3):
            if i < 3:
                print(f'{i}/2')
                expertise()
                i +=1
                continue
            if i == 3:
                break

    else:
        while True:
            choice = input("""Do you want to gain expertise with two skills or expertise with Thieves Tools and a single skill?
1) Expertise with two skills
2) Expertise with Thieves Tools and one skill
Enter your selection: """)
            if choice == '1':
# Run expertise 2 times.
                i = 1
                for i in range(i,3):
                    if i < 3:
                        print(f'{i}/2')
                        expertise()
                        i +=1
                        continue
                    if i == 3:
                        break
                break

            elif choice == '2':
                if 'thieves_tools' in dnd_dict.character_dict['tool_expertise']:
                    print("You already have expertise with Thieves' Tools")
                    continue
                else:
                    dnd_dict.character_dict['tool_expertise']['thieves_tools'] = 'Thieves\' Tools'
                    expertise()
                    break
            else:
                print("Error: Invalid Selection")
                continue



# Used for Half-Elf Skills
def half_elf_skills():
    x = 1
    for x in range(x,3):
        if x < 3:
            print(f'{x}/2')
            skill_choice()
            x += 1
            continue

        elif x == 3:
            break


# Used for Bard Skills
def bard_skills():
    x = 1
    for x in range(x,5):
        if x < 5:
            print(f'{x}/4')
            skill_choice()
            x += 1
            continue

        elif x == 5:
            break


def rogue_skill_choice():
    x = 1
    for x in range(x,5):
        if x < 5:
            print(f'{x}/4')
            rogue_skills()
            x += 1
            continue

        elif x == 5:
            break

#If a skill is in saving_throws, add the proficiency bonus
# Otherwise, the saving throw is the stat modifier

def saving_throw_calc():
    prof_bonus = dnd_dict.character_dict['prof_bonus']
    save_dict = dnd_dict.character_dict['saving_throws']
    stats_dict = dnd_dict.character_dict['Stats']
    if 'strength' in save_dict:
        saving_throw = (stats_dict['strength']['mod'] + prof_bonus)
        stats_dict['strength']['save'] = saving_throw
    else:
        stats_dict['strength']['save'] = stats_dict['strength']['mod']

    if 'dexterity' in save_dict:
        saving_throw = (stats_dict['dexterity']['mod'] + prof_bonus)
        stats_dict['dexterity']['save'] = saving_throw
    else:
        stats_dict['dexterity']['save'] = stats_dict['dexterity']['mod']
        
    if 'constitution' in save_dict:
        saving_throw = (stats_dict['constitution']['mod'] + prof_bonus)
        stats_dict['constitution']['save'] = saving_throw
    else:
        stats_dict['constitution']['save'] = stats_dict['constitution']['mod']

    if 'intelligence' in save_dict:
        saving_throw = (stats_dict['intelligence']['mod'] + prof_bonus)
        stats_dict['intelligence']['save'] = saving_throw
    else:
        stats_dict['intelligence']['save'] = stats_dict['intelligence']['mod']

    if 'wisdom' in save_dict:
        saving_throw = (stats_dict['wisdom']['mod'] + prof_bonus)
        stats_dict['wisdom']['save'] = saving_throw
    else:
        stats_dict['wisdom']['save'] = stats_dict['wisdom']['mod']

    if 'charisma' in save_dict:
        saving_throw = (stats_dict['charisma']['mod'] + prof_bonus)
        stats_dict['charisma']['save'] = saving_throw
    else:
        stats_dict['charisma']['save'] = stats_dict['charisma']['mod']


#If a skill is in skill_prof, add the proficiency bonus
def skill_calculation():
    prof_bonus = dnd_dict.character_dict['prof_bonus']
# Use if the player gets Jack of All Trades from the Bard class.
# If the player is not proficient with the skill, add half of the proficiency modifier, rounded down
    new_prof_bonus = (prof_bonus // 2)
    if 'acrobatics' in dnd_dict.character_dict['expertise']:
        acr_mod = dnd_dict.character_dict['Stats']['dexterity']['mod']
        new_prof = (prof_bonus * 2)
        updated_acr = (acr_mod + new_prof)
        dnd_dict.character_dict['acrobatics']=updated_acr
    elif 'acrobatics' in dnd_dict.character_dict['skill_prof']:
        acr_mod = dnd_dict.character_dict['Stats']['dexterity']['mod']
        updated_acr = (acr_mod + prof_bonus)
        dnd_dict.character_dict['acrobatics'] = updated_acr
    elif 'jack_of_all_trades' in dnd_dict.character_dict['features'] or 'remarkable_athlete' in dnd_dict.character_dict['features']:
        acr_mod = dnd_dict.character_dict['Stats']['dexterity']['mod']
        updated_acr = (acr_mod + new_prof_bonus)
        dnd_dict.character_dict['acrobatics'] = updated_acr
    else:
        dnd_dict.character_dict['acrobatics'] = dnd_dict.character_dict['Stats']['dexterity']['mod']

    if 'animal_handling' in dnd_dict.character_dict['expertise']:
        anm_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
        new_prof = (prof_bonus * 2)
        updated_anm = (anm_mod + new_prof)
        dnd_dict.character_dict['animal_handling']=updated_anm
    elif 'animal_handling' in dnd_dict.character_dict['skill_prof']:
        anm_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
        updated_anm = (anm_mod +  prof_bonus)
        dnd_dict.character_dict['animal_handling'] = updated_anm


    elif 'jack_of_all_trades' in dnd_dict.character_dict['features']:
        anm_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
        updated_anm = (anm_mod +  new_prof_bonus)
        dnd_dict.character_dict['animal_handling'] = updated_acr
    else:
        dnd_dict.character_dict['animal_handling'] = dnd_dict.character_dict['Stats']['wisdom']['mod']

    if 'arcana' in dnd_dict.character_dict['expertise']:
        arc_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
        new_prof = (prof_bonus * 2)
        updated_arc = (arc_mod + new_prof)
        dnd_dict.character_dict['arcana']=updated_arc
    elif 'arcana' in dnd_dict.character_dict['skill_prof']:
        arc_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
        updated_arc = (arc_mod + prof_bonus)
        dnd_dict.character_dict['arcana'] = updated_arc


    elif 'jack_of_all_trades' in dnd_dict.character_dict['features']:
        arc_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
        updated_arc = (arc_mod + new_prof_bonus)
        dnd_dict.character_dict['arcana'] = updated_arc
    else:
        dnd_dict.character_dict['arcana'] = dnd_dict.character_dict['Stats']['intelligence']['mod']

    if 'athletics' in dnd_dict.character_dict['expertise']:
        ath_mod = dnd_dict.character_dict['Stats']['strength']['mod']
        new_prof = (prof_bonus * 2)
        updated_ath = (ath_mod + new_prof)
        dnd_dict.character_dict['athletics']=updated_ath
    elif 'athletics' in dnd_dict.character_dict['skill_prof']:
        ath_mod = dnd_dict.character_dict['Stats']['strength']['mod']
        updated_ath = (ath_mod +  prof_bonus)
        dnd_dict.character_dict['athletics'] = updated_ath
    elif 'jack_of_all_trades' in dnd_dict.character_dict['features'] or 'remarkable_athlete' in dnd_dict.character_dict['features']:
        ath_mod = dnd_dict.character_dict['Stats']['strength']['mod']
        updated_ath = (ath_mod +  new_prof_bonus)
        dnd_dict.character_dict['athletics'] = updated_ath
    else:
        dnd_dict.character_dict['athletics'] = dnd_dict.character_dict['Stats']['strength']['mod']

    if 'deception' in dnd_dict.character_dict['expertise']:
        dec_mod = dnd_dict.character_dict['Stats']['charisma']['mod']
        new_prof = (prof_bonus * 2)
        updated_dec = (dec_mod + new_prof)
        dnd_dict.character_dict['deception']=updated_dec
    elif 'deception' in dnd_dict.character_dict['skill_prof']:
        dec_mod = dnd_dict.character_dict['Stats']['charisma']['mod']
        updated_dec = (dec_mod + prof_bonus)
        dnd_dict.character_dict['deception'] = updated_dec
    elif 'jack_of_all_trades' in dnd_dict.character_dict['features']:
        dec_mod = dnd_dict.character_dict['Stats']['charisma']['mod']
        updated_dec = (dec_mod + new_prof_bonus)
        dnd_dict.character_dict['deception'] = updated_dec
    else:
        dnd_dict.character_dict['deception'] = dnd_dict.character_dict['Stats']['charisma']['mod']

    if 'history' in dnd_dict.character_dict['expertise']:
        his_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
        new_prof = (prof_bonus * 2)
        updated_his = (his_mod + new_prof)
        dnd_dict.character_dict['history']=updated_his
    elif 'history' in dnd_dict.character_dict['skill_prof']:
        his_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
        updated_his = (his_mod +  prof_bonus)
        dnd_dict.character_dict['history'] = updated_his
    elif 'jack_of_all_trades' in dnd_dict.character_dict['features']:
        his_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
        updated_his = (his_mod +  new_prof_bonus)
        dnd_dict.character_dict['history'] = updated_his
    else:
        dnd_dict.character_dict['history'] = dnd_dict.character_dict['Stats']['intelligence']['mod']

    if 'insight' in dnd_dict.character_dict['expertise']:
        ins_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
        new_prof = (prof_bonus * 2)
        updated_ins = (ins_mod + new_prof)
        dnd_dict.character_dict['insight']=updated_ins
    elif 'insight' in dnd_dict.character_dict['skill_prof']:
        ins_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
        updated_ins = (ins_mod + prof_bonus)
        dnd_dict.character_dict['insight'] = updated_ins
    elif 'jack_of_all_trades' in dnd_dict.character_dict['features']:
        ins_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
        updated_ins = (ins_mod + new_prof_bonus)
        dnd_dict.character_dict['insight'] = updated_ins
    else:
        dnd_dict.character_dict['insight'] = dnd_dict.character_dict['Stats']['wisdom']['mod']

    if 'intimidation' in dnd_dict.character_dict['expertise']:
        itd_mod = dnd_dict.character_dict['Stats']['charisma']['mod']
        new_prof = (prof_bonus * 2)
        updated_itd = (itd_mod + new_prof)
        dnd_dict.character_dict['intimidation']=updated_itd
    elif 'intimidation' in dnd_dict.character_dict['skill_prof']:
        itd_mod = dnd_dict.character_dict['Stats']['charisma']['mod']
        updated_itd = (itd_mod + prof_bonus)
        dnd_dict.character_dict['intimidation'] = updated_itd
    elif 'jack_of_all_trades' in dnd_dict.character_dict['features']:
        itd_mod = dnd_dict.character_dict['Stats']['charisma']['mod']
        updated_itd = (itd_mod + new_prof_bonus)
        dnd_dict.character_dict['intimidation'] = updated_itd
    else:
        dnd_dict.character_dict['intimidation'] = dnd_dict.character_dict['Stats']['charisma']['mod']

    if 'investigation' in dnd_dict.character_dict['expertise']:
        inv_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
        new_prof = (prof_bonus * 2)
        updated_inv = (inv_mod + new_prof)
        dnd_dict.character_dict['investigation']=updated_inv
    elif 'investigation' in dnd_dict.character_dict['skill_prof']:
        inv_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
        updated_inv = (inv_mod + prof_bonus)
        dnd_dict.character_dict['investigation'] = updated_inv
    elif 'jack_of_all_trades' in dnd_dict.character_dict['features']:
        inv_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
        updated_inv = (inv_mod + new_prof_bonus)
        dnd_dict.character_dict['investigation'] = updated_inv
    else:
        dnd_dict.character_dict['investigation'] = dnd_dict.character_dict['Stats']['intelligence']['mod']

    if 'medicine' in dnd_dict.character_dict['expertise']:
        med_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
        new_prof = (prof_bonus * 2)
        updated_med = (med_mod + new_prof)
        dnd_dict.character_dict['medicine']=updated_med
    elif 'medicine' in dnd_dict.character_dict['skill_prof']:
        med_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
        updated_med = (med_mod + prof_bonus)
        dnd_dict.character_dict['medicine'] = updated_med
    elif 'jack_of_all_trades' in dnd_dict.character_dict['features']:
        med_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
        updated_med = (med_mod + new_prof_bonus)
        dnd_dict.character_dict['medicine'] = updated_med
    else:
        dnd_dict.character_dict['medicine'] = dnd_dict.character_dict['Stats']['wisdom']['mod']

    if 'nature' in dnd_dict.character_dict['expertise']:
        nat_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
        new_prof = (prof_bonus * 2)
        updated_nat = (nat_mod + new_prof)
        dnd_dict.character_dict['nature']=updated_nat
    elif 'nature' in dnd_dict.character_dict['skill_prof']:
        nat_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
        updated_nat = (nat_mod + prof_bonus)
        dnd_dict.character_dict['nature'] = updated_nat
    elif 'jack_of_all_trades' in dnd_dict.character_dict['features']:
        nat_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
        updated_nat = (nat_mod + new_prof_bonus)
        dnd_dict.character_dict['nature'] = updated_nat
    else:
        dnd_dict.character_dict['nature'] = dnd_dict.character_dict['Stats']['intelligence']['mod']

    if 'perception' in dnd_dict.character_dict['expertise']:
        prc_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
        new_prof = (prof_bonus * 2)
        updated_prc = (prc_mod + new_prof)
        dnd_dict.character_dict['perception']=updated_prc
    elif 'perception' in dnd_dict.character_dict['skill_prof']:
        prc_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
        updated_prc = (prc_mod + prof_bonus)
        dnd_dict.character_dict['perception'] = updated_prc
    elif 'jack_of_all_trades' in dnd_dict.character_dict['features']:
        prc_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
        updated_prc = (prc_mod + new_prof_bonus)
        dnd_dict.character_dict['perception'] = updated_prc
    else:
        dnd_dict.character_dict['perception'] = dnd_dict.character_dict['Stats']['wisdom']['mod']

    if 'performance' in dnd_dict.character_dict['expertise']:
        prf_mod = dnd_dict.character_dict['Stats']['charisma']['mod']
        new_prof = (prof_bonus * 2)
        updated_prf = (prf_mod +new_prof)
        dnd_dict.character_dict['performance']=updated_prf
    elif 'performance' in dnd_dict.character_dict['skill_prof']:
        prf_mod = dnd_dict.character_dict['Stats']['charisma']['mod']
        updated_prf = (prf_mod + prof_bonus)
        dnd_dict.character_dict['performance'] = updated_prf
    elif 'jack_of_all_trades' in dnd_dict.character_dict['features']:
        prf_mod = dnd_dict.character_dict['Stats']['charisma']['mod']
        updated_prf = (prf_mod + new_prof_bonus)
        dnd_dict.character_dict['performance'] = updated_prf
    else:
        dnd_dict.character_dict['performance'] = dnd_dict.character_dict['Stats']['charisma']['mod']

    if 'persuasion' in dnd_dict.character_dict['expertise']:
        per_mod = dnd_dict.character_dict['Stats']['charisma']['mod']
        new_prof = (prof_bonus * 2)
        updated_per = (per_mod + new_prof)
        dnd_dict.character_dict['persuasion']=updated_per
    elif 'persuasion' in dnd_dict.character_dict['skill_prof']:
        per_mod = dnd_dict.character_dict['Stats']['charisma']['mod']
        updated_per = (per_mod + prof_bonus)
        dnd_dict.character_dict['persuasion'] = updated_per
    elif 'jack_of_all_trades' in dnd_dict.character_dict['features']:
        per_mod = dnd_dict.character_dict['Stats']['charisma']['mod']
        updated_per = (per_mod + new_prof_bonus)
        dnd_dict.character_dict['persuasion'] = updated_per
    else:
        dnd_dict.character_dict['persuasion'] = dnd_dict.character_dict['Stats']['charisma']['mod']

    if 'religion' in dnd_dict.character_dict['expertise']:
        rel_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
        new_prof = (prof_bonus * 2)
        updated_rel = (rel_mod + new_prof)
        dnd_dict.character_dict['religion']=updated_rel
    elif 'religion' in dnd_dict.character_dict['skill_prof']:
        rel_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
        updated_rel = (rel_mod + prof_bonus)
        dnd_dict.character_dict['religion'] = updated_rel
    elif 'jack_of_all_trades' in dnd_dict.character_dict['features']:
        rel_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
        updated_rel = (rel_mod + new_prof_bonus)
        dnd_dict.character_dict['religion'] = updated_rel
    else:
        dnd_dict.character_dict['religion'] = dnd_dict.character_dict['Stats']['intelligence']['mod']

    if 'sleight_of_hand' in dnd_dict.character_dict['expertise']:
        soh_mod = dnd_dict.character_dict['Stats']['dexterity']['mod']
        new_prof = (prof_bonus * 2)
        updated_soh = (soh_mod + new_prof)
        dnd_dict.character_dict['sleight_of_hand']=updated_soh
    elif 'sleight_of_hand' in dnd_dict.character_dict['skill_prof']:
        soh_mod = dnd_dict.character_dict['Stats']['dexterity']['mod']
        updated_soh = (soh_mod + prof_bonus)
        dnd_dict.character_dict['sleight_of_hand'] = updated_soh
    elif 'jack_of_all_trades' in dnd_dict.character_dict['features'] or 'remarkable_athlete' in dnd_dict.character_dict['features']:
        soh_mod = dnd_dict.character_dict['Stats']['dexterity']['mod']
        updated_soh = (soh_mod + new_prof_bonus)
        dnd_dict.character_dict['sleight_of_hand'] = updated_soh
    else:
        dnd_dict.character_dict['sleight_of_hand'] = dnd_dict.character_dict['Stats']['dexterity']['mod']

    if 'stealth' in dnd_dict.character_dict['expertise']:
        stl_mod = dnd_dict.character_dict['Stats']['dexterity']['mod']
        new_prof = (prof_bonus * 2)
        updated_stl = (stl_mod + new_prof)
        dnd_dict.character_dict['stealth']=updated_stl
    elif 'stealth' in dnd_dict.character_dict['skill_prof']:
        stl_mod = dnd_dict.character_dict['Stats']['dexterity']['mod']
        updated_stl = (stl_mod + prof_bonus)
        dnd_dict.character_dict['stealth'] = updated_stl
    elif 'jack_of_all_trades' in dnd_dict.character_dict['features'] or 'remarkable_athlete' in dnd_dict.character_dict['features']:
        soh_mod = dnd_dict.character_dict['Stats']['dexterity']['mod']
        updated_soh = (soh_mod + new_prof_bonus)
        dnd_dict.character_dict['stealth'] = updated_soh
    else:
        dnd_dict.character_dict['stealth'] = dnd_dict.character_dict['Stats']['dexterity']['mod']
    if 'boon_of_undetectability' in dnd_dict.character_dict['boon']:
        dnd_dict.character_dict['stealth'] += 10

    if 'survival' in dnd_dict.character_dict['expertise']:
        sur_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
        new_prof = (prof_bonus * 2)
        updated_sur = (sur_mod + new_prof)
        dnd_dict.character_dict['survival']=updated_sur
    elif 'survival' in dnd_dict.character_dict['skill_prof']:
        sur_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
        updated_sur = (sur_mod + prof_bonus)
        dnd_dict.character_dict['survival'] = updated_sur
    elif 'jack_of_all_trades' in dnd_dict.character_dict['features']:
        sur_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
        updated_sur = (sur_mod + new_prof_bonus)
        dnd_dict.character_dict['survival'] = updated_sur
    else:
        dnd_dict.character_dict['survival'] = dnd_dict.character_dict['Stats']['wisdom']['mod']

    if 'initiative' in dnd_dict.character_dict['expertise']:
        int_mod = dnd_dict.character_dict['Stats']['dexterity']['mod']
        new_prof = (prof_bonus * 2)
        updated_int = (int_mod + new_prof)
        dnd_dict.character_dict['initiative']=updated_int
    elif 'initiative' in dnd_dict.character_dict['skill_prof']:
        int_mod = dnd_dict.character_dict['Stats']['dexterity']['mod']
        updated_int = (int_mod + prof_bonus)
        dnd_dict.character_dict['initiative'] = updated_int
    elif 'jack_of_all_trades' in dnd_dict.character_dict['features'] or 'remarkable_athlete' in dnd_dict.character_dict['features']:
        int_mod = dnd_dict.character_dict['Stats']['dexterity']['mod']
        updated_int = (int_mod + new_prof_bonus)
        dnd_dict.character_dict['initiative'] = updated_int
    else:
        dnd_dict.character_dict['initiative'] = dnd_dict.character_dict['Stats']['dexterity']['mod']

# Gloomstalker Ranger Feature
    if 'dread_ambusher' in dnd_dict.character_dict['features']:
        dnd_dict.character_dict['initiative'] += dnd_dict.character_dict['Stats']['wisdom']['mod']

# Chronurgy Wizard Feature
    if 'temporal_awareness' in dnd_dict.character_dict['features']:
        dnd_dict.character_dict['initiative'] += dnd_dict.character_dict['Stats']['intelligence']['mod']

# War Magic Wizard Feature
    if 'tactical_wit' in dnd_dict.character_dict['features']:
        dnd_dict.character_dict['initiative'] += dnd_dict.character_dict['Stats']['intelligence']['mod']

# Swashbuckler Rogue Feature
    if 'rakish_audacity' in dnd_dict.character_dict['features']:
        dnd_dict.character_dict['initiative'] += dnd_dict.character_dict['Stats']['charisma']['mod']

    if 'alert' in dnd_dict.character_dict['features']:
        dnd_dict.character_dict['initiative'] += 5


    passive_perception = (dnd_dict.character_dict['perception'] + 10)
    if 'observant' in dnd_dict.character_dict['feats']:
        passive_perception += 5


"""
Displays the equipment so the amount of equipment obtained as a number after the key for the dict. If it is over 1, then it will be displayed as Value(x{number}), otherwise it will be displayed as just the value. If there is already equipment obtained, then the key will be divided into two parts, with the existing amount being the second part. That will be added to the key in the function to create a new key for the dictionary and value, with the old key:value pair being deleted.
"""
def equip_mod(key,value):
    dict = dnd_dict.character_dict['Equipment']
    split_key = re.split('(\d+$)',key)
    first_key = str(split_key[0])
    res = ' '.join([k for k in dict if k.startswith(first_key)])
    if str(res) in dict:
        split_res = re.split('(\d+$)',res)
        first_res = int(split_res[1])
        new_int = first_res + int(split_key[1])
        new_key = first_key + str(new_int)
        new_value = f'{value} (x{new_int})'
        dict[new_key]=new_value
        del dict[res]
    else:
        if int(split_key[1]) == 1:
            dict[key]=value
        elif int(split_key[1]) > 1:
            new_value = f'{value} (x{split_key[1]})'
            dict[key]=new_value
        else:
            new_key = key + str(1)
            new_value = f'{value} (x{split_key[1]})'
            dict[new_key]=new_value



"""
Displays the misc. items so the amount of equipment obtained as a number after the key for the dict. If it is over 1, then it will be displayed as Value(x{number} {whatever the measurement is}), otherwise it will be displayed as just the value and the singular measurement. If there is already equipment obtained, then the key will be divided into two parts, with the existing amount being the second part. That will be added to the key in the function to create a new key for the dictionary and value, with the old key:value pair being deleted.
"""
def misc_mod(key,value,measurement,singular_measurement):
    dict = dnd_dict.character_dict['Misc']
    split_key = re.split('(\d+$)',key)
    first_key = str(split_key[0])
    res = ' '.join([k for k in dict if k.startswith(first_key)])
    if str(res) in dict:
        split_res = re.split('(\d+$)',res)
        first_res = int(split_res[1])
        new_int = first_res + int(split_key[1])
        new_key = first_key + str(new_int)
# 'null' is to account for any potential grammatical errors in the descriptions (like for torches, pitons, etc.).
        if value == 'null':
            new_value = f'{measurement} (x{new_int})'
            dict[new_key]=new_value
            del dict[res]
        else:
            new_value = f'{value} (x{new_int} {measurement})'
            dict[new_key]=new_value
            del dict[res]

    else:
        if int(split_key[1]) == 1:
            if value == 'null':
                new_value = f'{singular_measurement} (x1)'
                dict[key]=new_value
            else:
                new_value = f'{value} (x1 {singular_measurement})'
                dict[key]=new_value
        elif int(split_key[1]) > 1:
            if value == 'null':
                new_value = f'{measurement} (x{split_key[1]})'
                dict[key]=new_value
            else:
                new_value = f'{value} (x{split_key[1]} {measurement})'
                dict[key]=new_value
        else:
            new_key = key + str(1)
            if value == 'null':
                new_value = f'{measurement} (x{split_key[1]})'
                dict[new_key]=new_value
            else:
                new_value = f'{value} ({split_key[1]} {measurement})'
                dict[new_key]=new_value


def spell_slot(level):
    if ((dnd_dict.character_dict['caster_level'])+(((((dnd_dict.character_dict['semi_caster_level'])+1)//3)))+(((dnd_dict.character_dict['half_caster_level'])//2)))==level:
        return True


# Setting the spell slots a player gets, rounding down for half-casters
def spell_slot_selection():
# If semi-casters = 4 with no other classes, the first level spell slots get up to 4.
    if dnd_dict.character_dict['semi_caster_level'] == 4 and dnd_dict.character_dict['caster_level'] == 0 and dnd_dict.character_dict['half_caster_level'] == 0:
        dnd_dict.character_dict['spell_slots']['first'] = 3
    elif spell_slot(1):
        dnd_dict.character_dict['spell_slots']['first'] = 2
    elif spell_slot(2):
        dnd_dict.character_dict['spell_slots']['first'] = 3
    elif spell_slot(3):
        dnd_dict.character_dict['spell_slots']['first'] = 4
        dnd_dict.character_dict['spell_slots']['second'] = 2
    elif spell_slot(4):
        dnd_dict.character_dict['spell_slots']['second'] = 3
    elif spell_slot(5):
        dnd_dict.character_dict['spell_slots']['third'] = 2
    elif spell_slot(6):
        dnd_dict.character_dict['spell_slots']['third'] = 3
    elif spell_slot(7):
        dnd_dict.character_dict['spell_slots']['fourth'] = 1
    elif spell_slot(8):
        dnd_dict.character_dict['spell_slots']['fourth'] = 2
    elif spell_slot(9):
        dnd_dict.character_dict['spell_slots']['fourth'] = 3
        dnd_dict.character_dict['spell_slots']['fifth'] = 1
    elif spell_slot(10):
        dnd_dict.character_dict['spell_slots']['fifth'] = 2
    elif spell_slot(11):
        dnd_dict.character_dict['spell_slots']['sixth'] = 1
    elif spell_slot(12):
        dnd_dict.character_dict['spell_slots']['sixth'] = 1
    elif spell_slot(13):
        dnd_dict.character_dict['spell_slots']['seventh'] = 1
    elif spell_slot(14):
        dnd_dict.character_dict['spell_slots']['seventh'] = 1
    elif spell_slot(15):
        dnd_dict.character_dict['spell_slots']['eighth'] = 1
    elif spell_slot(16):
        dnd_dict.character_dict['spell_slots']['eighth'] = 1
    elif spell_slot(17):
        dnd_dict.character_dict['spell_slots']['ninth'] = 1
    elif spell_slot(18):
        dnd_dict.character_dict['spell_slots']['fifth'] = 3
    elif spell_slot(19):
        dnd_dict.character_dict['spell_slots']['sixth'] = 2
    elif spell_slot(20):
        dnd_dict.character_dict['spell_slots']['seventh'] = 2
    else:
        pass

# Cycle through a dictionary, and if they keys are in the small dict, eliminate them from the med dict and full dict, before nuking the small one.
def pact_swap(small_dict,med_dict,full_dict):
    for key in small_dict.keys():
       if key in small_dict:
            full_dict.pop(key, None)
            med_dict.pop(key, None)
    small_dict.clear()
#Cycle through cantrips if you are switching out Pact of the Tome.
    if dnd_dict.character_dict['special_spells']['tome_cantrips']:
        for key in dnd_dict.character_dict['special_spells']['tome_cantrips'].keys():
           if key in dnd_dict.character_dict['special_spells']['tome_cantrips'].keys():
                dnd_dict.character_dict['spells'].pop(key, None)
        dnd_dict.character_dict['special_spells']['tome_cantrips'].clear()

#Cycle through ritual spells if you have the invocation.
    if dnd_dict.character_dict['special_spells']['tome_ritual']:
        for key in dnd_dict.character_dict['special_spells']['tome_ritual'].keys():
           if key in dnd_dict.character_dict['special_spells']['tome_ritual'].keys():
                dnd_dict.character_dict['spells'].pop(key, None)
        dnd_dict.character_dict['special_spells']['tome_ritual'].clear()
        

# Delete the spell from the class spell list, but if it is also in a "special" list that can't be swapped out of, then don't delete it from the overall available spell list.
def spell_swap(class_dict,special_dict,full_dict):

    tmp_dict = {}
    counter = 1
# Display the spells and their values
    for key, value in class_dict.items():
        print(f'{counter}) {value}')
        tmp_dict[counter] = key
        counter +=1
    while True:
        try:
            choice = int(input("Select the spell you want to delete: "))
        except ValueError as e:
            print("Invalid Input")
            continue
        if tmp_dict.get(choice,{}):
            to_delete = tmp_dict[choice]
# If the spell is in the "special" category, only delete the spell from the class list
            if to_delete in special_dict:
                class_dict.pop(to_delete,None)
# Otherwise, delete it from the full spell list
            else:
                class_dict.pop(to_delete,None)
                full_dict.pop(to_delete,None)
            break
        else:
            print("Error: Invalid Input")


# Delete the Invocation from the Invocation list, also including if it is in the pact invocation dict.
def invocation_change(class_dict,mid_dict,full_dict):
    tmp_dict = {}
    counter = 1
# Display the spells and their values
    for key, value in class_dict.items():
        print(f'{counter}) {value}')
        tmp_dict[counter] = key
        counter +=1
    while True:
        try:
            choice = int(input("Select what you want to delete: "))
        except ValueError as e:
            print("Invalid Input")
            continue
        if tmp_dict.get(choice,{}):
            to_delete = tmp_dict[choice]
            class_dict.pop(to_delete,None)
            full_dict.pop(to_delete,None)
            if to_delete in mid_dict:
                mid_dict.pop(to_delete,None)
            break
        else:
            print("Error: Invalid Input")

# Delete the Battle Master Manuever from the Manuever list.
def maneuver_swap(class_dict,full_dict):
    tmp_dict = {}
    counter = 1
# Display the spells and their values
    for key, value in class_dict.items():
        print(f'{counter}) {value}')
        tmp_dict[counter] = key
        counter +=1
    while True:
        try:
            choice = int(input("Select the spell you want to delete: "))
        except ValueError as e:
            print("Invalid Input")
            continue
        if tmp_dict.get(choice,{}):
            to_delete = tmp_dict[choice]
            class_dict.pop(to_delete,None)
            full_dict.pop(to_delete,None)
            break
        else:
            print("Error: Invalid Input")



# Delete the skill from the skill list.
def skill_swap(class_dict):

    tmp_dict = {}
    counter = 1
# Display the spells and their values
    for key, value in class_dict.items():
        print(f'{counter}) {value}')
        tmp_dict[counter] = key
        counter +=1
    while True:
        try:
            choice = int(input("Select what you want to delete: "))
        except ValueError as e:
            print("Invalid Input")
            continue
        if tmp_dict.get(choice,{}):
            to_delete = tmp_dict[choice]
# Delete it from the full spell list
            class_dict.pop(to_delete,None)
            break
        else:
            print("Error: Invalid Input")



def spell_add(spells,full_dict,class_dict):
    tmp_dict = {}
    counter = 1
# Display the spells and their values
    for value in spells:
        print(f'{counter}) {value}')
        tmp_dict[counter] = value
        counter +=1

    while True:
        try:
            choice = int(input("Select the spell you want to add: "))
        except ValueError as e:
            print("Invalid Input")
            continue
        if tmp_dict.get(choice,{}) in full_dict.values():
            print(f'{tmp_dict.get(choice,{})} already known')
            continue
        elif tmp_dict.get(choice,{}):
            to_delete = tmp_dict[choice]
# Makes the spell lowercase and turns all spaces into underscores
            new_value = to_delete.lower().replace(' ','_')
            full_dict[new_value]=to_delete
            class_dict[new_value]=to_delete
            break
        else:
            print("Error: Invalid Input")

# Used for Book of Ancient Secrets. Only adds spells to the specific dictionary as opposed to that and the full spell list.
def book_spell_add(spells,full_dict,class_dict):
    tmp_dict = {}
    counter = 1
# Display the spells and their values
    for value in spells:
        print(f'{counter}) {value}')
        tmp_dict[counter] = value
        counter +=1

    while True:
        try:
            choice = int(input("Select the spell you want to add: "))
        except ValueError as e:
            print("Invalid Input")
            continue
        if tmp_dict.get(choice,{}) in full_dict.values():
            print(f'{tmp_dict.get(choice,{})} already known')
            continue
        elif tmp_dict.get(choice,{}):
            to_delete = tmp_dict[choice]
# Makes the spell lowercase and turns all spaces into underscores
            new_value = to_delete.lower().replace(' ','_')
            class_dict[new_value]=to_delete
            break
        else:
            print("Error: Invalid Input")



# Used to choose if you want to swap a spell
def spell_swap_choice(spell_list,full_dict,special_dict,class_dict):
    while True:
        choice = input("""Do you want to replace a spell?
1) Yes
2) No
Enter your selection: """)
        if choice == '1':
            spell_swap(class_dict,special_dict,full_dict)
            spell_add(spell_list,full_dict,class_dict)
            break

        elif choice == '2':
            break

        else:
            print("Error: Invalid Selection")
            continue


# Like spell_add, except you only need to worry about a single dictionary as opposed to putting it in multiple. For example, Infusions, skills, Invocations, etc.
def skill_addition(spells,full_dict):
    tmp_dict = {}
    counter = 1
# Display the spells and their values
    for value in spells:
        print(f'{counter}) {value}')
        tmp_dict[counter] = value
        counter +=1

    while True:
        try:
            choice = int(input("Select what you want to add: "))
        except ValueError as e:
            print("Invalid Input")
            continue

        if tmp_dict.get(choice,{}) in full_dict.values():
            print(f'{tmp_dict.get(choice,{})} already known')
            continue

        elif tmp_dict.get(choice,{}):
            to_delete = tmp_dict[choice]
# Makes the spell lowercase and turns all spaces into underscores
            new_value = to_delete.lower().replace(' ','_')
            full_dict[new_value]=to_delete
            break
        else:
            print("Error: Invalid Input")

# Used for the Strixhaven Initiate spell choices
def strixhaven_spells(spell_list):
    tmp_dict = {}
    counter = 1
    for value in spell_list:
        print(f'{counter}) {value}')
        tmp_dict[counter] = value
        counter +=1

    while True:
        try:
            choice = int(input("Select what you want to add: "))
        except ValueError as e:
            print("Invalid Input")
            continue

        if counter == 1:
            break

        elif tmp_dict.get(choice,{}) in dnd_dict.character_dict['spells'].values():
            print(f'{tmp_dict.get(choice,{})} already known')
            continue

        elif tmp_dict.get(choice,{}):
            to_delete = tmp_dict[choice]
# Makes the spell lowercase and turns all spaces into underscores
            new_value = to_delete.lower().replace(' ','_')
            dnd_dict.character_dict['spells'][new_value]=to_delete
            break
        else:
            print("Error: Invalid Input")




# Delete the Fighting Style from the Fighting Style list.
def fighting_style_swap(class_dict,full_dict):

    tmp_dict = {}
    counter = 1
# Display the spells and their values
    for key, value in class_dict.items():
        print(f'{counter}) {value}')
        tmp_dict[counter] = key
        counter +=1
    while True:
        try:
            choice = int(input("Select the spell you want to delete: "))
        except ValueError as e:
            print("Invalid Input")
            continue
        if tmp_dict.get(choice,{}):
            to_delete = tmp_dict[choice]
            class_dict.pop(to_delete,None)
            full_dict.pop(to_delete,None)

## If you delete the Blessed Warrior fighting style, delete the cantrips learned from that feature
            if to_delete == 'blessed_warrior_fighting_style':
                if key in dnd_dict.character_dict['special_spells']['fighting_cleric']:
                    for key in dnd_dict.character_dict['special_spells']['fighting_cleric'].keys():
                       if key in dnd_dict.character_dict['special_spells']['fighting_cleric'].keys():
                            dnd_dict.character_dict['spells'].pop(key, None)
                    dnd_dict.character_dict['special_spells']['fighiting_cleric'].clear()

## If you delete the Druidic Warrior fighting style, delete the cantrips learned from that feature
            if to_delete == 'druidic_warrior_fighting_style':
                if key in dnd_dict.character_dict['special_spells']['fighting_cleric']:
                    for key in dnd_dict.character_dict['special_spells']['fighting_druid'].keys():
                       if key in dnd_dict.character_dict['special_spells']['fighting_druid'].keys():
                            dnd_dict.character_dict['spells'].pop(key, None)
                    dnd_dict.character_dict['special_spells']['fighting_druid'].clear()

# If you delete the Superior Technique Fighting Style, subtract 1d6 Superiority Dice and change the maneuver
            if to_delete == 'superior_technique_fighting_style':
                dnd_dict.character_dict['maneuvers']['d6'] -= 1
                maneuver_swap(dnd_dict.character_dict['maneuvers']['types'],dnd_dict.character_dict['features'])
            break
        else:
            print("Error: Invalid Input")


# Used to choose what level spell a character wants
def second_level(first_spell,second_spell,first_dict,second_dict):
    while True:
        choice = input("""What level do you want to select from?
1) First
2) Second
Enter your Selection: """)
        if choice == '1':
            spell_add(first_spell,dnd_dict.character_dict['spells']['first'],first_dict)
            break

        elif choice == '2':
            spell_add(second_spell,dnd_dict.character_dict['spells']['second'],second_dict)
            break

        else:
            print("Error: Invalid Input")
            continue

def third_level(first_spell,second_spell,third_spell,first_dict,second_dict,third_dict):
    while True:
        choice = input("""What level do you want to select from?
1) First
2) Second
3) Third
Enter your Selection: """)

        if choice == '1':
            spell_add(first_spell,dnd_dict.character_dict['spells']['first'],first_dict)
            break

        elif choice == '2':
            spell_add(second_spell,dnd_dict.character_dict['spells']['second'],second_dict)
            break

        elif choice == '3':
            spell_add(third_spell,dnd_dict.character_dict['spells']['third'],third_dict)
            break

        else:
            print("Error: Invalid Input")
            continue

def fourth_level(first_spell,second_spell,third_spell,fourth_spell,first_dict,second_dict,third_dict,fourth_dict):
    while True:
        choice = input("""What level do you want to select from?
1) First
2) Second
3) Third
4) Fourth
Enter your Selection: """)

        if choice == '1':
            spell_add(first_spell,dnd_dict.character_dict['spells']['first'],first_dict)
            break

        elif choice == '2':
            spell_add(second_spell,dnd_dict.character_dict['spells']['second'],second_dict)
            break

        elif choice == '3':
            spell_add(third_spell,dnd_dict.character_dict['spells']['third'],third_dict)
            break

        elif choice == '4':
            spell_add(fourth_spell,dnd_dict.character_dict['spells']['fourth'],fourth_dict)
            break

        else:
            print("Error: Invalid Input")
            continue

def fifth_level(first_spell,second_spell,third_spell,fourth_spell,fifth_spell,first_dict,second_dict,third_dict,fourth_dict,fifth_dict):
    while True:
        choice = input("""What level do you want to select from?
1) First
2) Second
3) Third
4) Fourth
5) Fifth
Enter your Selection: """)

        if choice == '1':
            spell_add(first_spell,dnd_dict.character_dict['spells']['first'],first_dict)
            break

        elif choice == '2':
            spell_add(second_spell,dnd_dict.character_dict['spells']['second'],second_dict)
            break

        elif choice == '3':
            spell_add(third_spell,dnd_dict.character_dict['spells']['third'],third_dict)
            break

        elif choice == '4':
            spell_add(fourth_spell,dnd_dict.character_dict['spells']['fourth'],fourth_dict)
            break

        elif choice == '5':
            spell_add(fifth_spell,dnd_dict.character_dict['spells']['fifth'],fifth_dict)
            break

        else:
            print("Error: Invalid Input")
            continue

def sixth_level(first_spell,second_spell,third_spell,fourth_spell,fifth_spell,sixth_spell,first_dict,second_dict,third_dict,fourth_dict,fifth_dict,sixth_dict):
    while True:
        choice = input("""What level do you want to select from?
1) First
2) Second
3) Third
4) Fourth
5) Fifth
6) Sixth
Enter your Selection: """)

        if choice == '1':
            spell_add(first_spell,dnd_dict.character_dict['spells']['first'],first_dict)
            break

        elif choice == '2':
            spell_add(second_spell,dnd_dict.character_dict['spells']['second'],second_dict)
            break

        elif choice == '3':
            spell_add(third_spell,dnd_dict.character_dict['spells']['third'],third_dict)
            break

        elif choice == '4':
            spell_add(fourth_spell,dnd_dict.character_dict['spells']['fourth'],fourth_dict)
            break

        elif choice == '5':
            spell_add(fifth_spell,dnd_dict.character_dict['spells']['fifth'],fifth_dict)
            break

        elif choice == '6':
            spell_add(sixth_spell,dnd_dict.character_dict['spells']['sixth'],sixth_dict)
            break

        else:
            print("Error: Invalid Input")
            continue


def seventh_level(first_spell,second_spell,third_spell,fourth_spell,fifth_spell,sixth_spell,seventh_spell,first_dict,second_dict,third_dict,fourth_dict,fifth_dict,sixth_dict,seventh_dict):
    while True:
        choice = input("""What level do you want to select from?
1) First
2) Second
3) Third
4) Fourth
5) Fifth
6) Sixth
7) Seventh
Enter your Selection: """)

        if choice == '1':
            spell_add(first_spell,dnd_dict.character_dict['spells']['first'],first_dict)
            break

        elif choice == '2':
            spell_add(second_spell,dnd_dict.character_dict['spells']['second'],second_dict)
            break

        elif choice == '3':
            spell_add(third_spell,dnd_dict.character_dict['spells']['third'],third_dict)
            break

        elif choice == '4':
            spell_add(fourth_spell,dnd_dict.character_dict['spells']['fourth'],fourth_dict)
            break

        elif choice == '5':
            spell_add(fifth_spell,dnd_dict.character_dict['spells']['fifth'],fifth_dict)
            break

        elif choice == '6':
            spell_add(sixth_spell,dnd_dict.character_dict['spells']['sixth'],sixth_dict)
            break

        elif choice == '7':
            spell_add(seventh_spell,dnd_dict.character_dict['spells']['seventh'],seventh_dict)
            break

        else:
            print("Error: Invalid Input")
            continue


def eighth_level(first_spell,second_spell,third_spell,fourth_spell,fifth_spell,sixth_spell,seventh_spell,eighth_spell,first_dict,second_dict,third_dict,fourth_dict,fifth_dict,sixth_dict,seventh_dict,eighth_dict):
    while True:
        choice = input("""What level do you want to select from?
1) First
2) Second
3) Third
4) Fourth
5) Fifth
6) Sixth
7) Seventh
8) Eighth
Enter your Selection: """)

        if choice == '1':
            spell_add(first_spell,dnd_dict.character_dict['spells']['first'],first_dict)
            break

        elif choice == '2':
            spell_add(second_spell,dnd_dict.character_dict['spells']['second'],second_dict)
            break

        elif choice == '3':
            spell_add(third_spell,dnd_dict.character_dict['spells']['third'],third_dict)
            break

        elif choice == '4':
            spell_add(fourth_spell,dnd_dict.character_dict['spells']['fourth'],fourth_dict)
            break

        elif choice == '5':
            spell_add(fifth_spell,dnd_dict.character_dict['spells']['fifth'],fifth_dict)
            break

        elif choice == '6':
            spell_add(sixth_spell,dnd_dict.character_dict['spells']['sixth'],sixth_dict)
            break

        elif choice == '7':
            spell_add(seventh_spell,dnd_dict.character_dict['spells']['seventh'],seventh_dict)
            break

        elif choice == '8':
            spell_add(eighth_spell,dnd_dict.character_dict['spells']['eighth'],eighth_dict)
            break

        else:
            print("Error: Invalid Input")
            continue


def ninth_level(first_spell,second_spell,third_spell,fourth_spell,fifth_spell,sixth_spell,seventh_spell,eighth_spell,ninth_spell,first_dict,second_dict,third_dict,fourth_dict,fifth_dict,sixth_dict,seventh_dict,eighth_dict,ninth_dict):
    while True:
        choice = input("""What level do you want to select from?
1) First
2) Second
3) Third
4) Fourth
5) Fifth
6) Sixth
7) Seventh
8) Eighth
9) Ninth
Enter your Selection: """)
        if choice == '1':
            spell_add(first_spell,dnd_dict.character_dict['spells']['first'],first_dict)
            break

        elif choice == '2':
            spell_add(second_spell,dnd_dict.character_dict['spells']['second'],second_dict)
            break

        elif choice == '3':
            spell_add(third_spell,dnd_dict.character_dict['spells']['third'],third_dict)
            break

        elif choice == '4':
            spell_add(fourth_spell,dnd_dict.character_dict['spells']['fourth'],fourth_dict)
            break

        elif choice == '5':
            spell_add(fifth_spell,dnd_dict.character_dict['spells']['fifth'],fifth_dict)
            break

        elif choice == '6':
            spell_add(sixth_spell,dnd_dict.character_dict['spells']['sixth'],sixth_dict)
            break

        elif choice == '7':
            spell_add(seventh_spell,dnd_dict.character_dict['spells']['seventh'],seventh_dict)
            break

        elif choice == '8':
            spell_add(eighth_spell,dnd_dict.character_dict['spells']['eighth'],eighth_dict)
            break

        elif choice == '9':
            spell_add(ninth_spell,dnd_dict.character_dict['spells']['ninth'],ninth_dict)
            break

        else:
            print("Error: Invalid Input")
            continue

def cantrip_swap(spell_list,spell_dict):
    spell_swap(spell_dict,dnd_dict.character_dict['special_spells']['cantrips'],dnd_dict.character_dict['spells']['cantrips'])
    spell_add(spell_list,dnd_dict.character_dict['spells']['cantrips'],spell_dict)


# Used to swap out spells (while giving the option not to at all)
def first_swap(first_spell,first_dict):
    while True:
        choice = input("""What level do you want to select from?
1) First
0) Do Not Swap
Enter your Selection: """)
        if choice == '1':
            if not first_dict:
                print("Error: You Do Not Know Any Spells of This Level in This Class.")
                continue
            else:
                spell_swap(first_dict,dnd_dict.character_dict['special_spells']['first'],dnd_dict.character_dict['spells']['first'])
                spell_add(first_spell,dnd_dict.character_dict['spells']['first'],first_dict)
                break

        elif choice == '0':
            break

        else:
            print("Error: Invalid Input")
            continue


def second_swap(first_spell,second_spell,first_dict,second_dict):
    while True:
        choice = input("""What level do you want to select from?
1) First
2) Second
0) Do Not Swap
Enter your Selection: """)
        if choice == '1':
            if not first_dict:
                print("Error: You Do Not Know Any Spells of This Level in This Class.")
                continue
            else:
                spell_swap(first_dict,dnd_dict.character_dict['special_spells']['first'],dnd_dict.character_dict['spells']['first'])
                spell_add(first_spell,dnd_dict.character_dict['spells']['first'],first_dict)
                break

        elif choice == '2':
            if not second_dict:
                print("Error: You Do Not Know Any Spells of This Level in This Class.")
                continue
            else:
                spell_swap(second_dict,dnd_dict.character_dict['special_spells']['second'],dnd_dict.character_dict['spells']['second'])
                spell_add(second_spell,dnd_dict.character_dict['spells']['second'],second_dict)
                break

        elif choice == '0':
            break

        else:
            print("Error: Invalid Input")
            continue

def third_swap(first_spell,second_spell,third_spell,first_dict,second_dict,third_dict):
    while True:
        choice = input("""What level do you want to select from?
1) First
2) Second
3) Third
0) Do Not Swap
Enter your Selection: """)
        if choice == '1':
            if not first_dict:
                print("Error: You Do Not Know Any Spells of This Level in This Class.")
                continue
            else:
                spell_swap(first_dict,dnd_dict.character_dict['special_spells']['first'],dnd_dict.character_dict['spells']['first'])
                spell_add(first_spell,dnd_dict.character_dict['spells']['first'],first_dict)
                break

        elif choice == '2':
            if not second_dict:
                print("Error: You Do Not Know Any Spells of This Level in This Class.")
                continue
            else:
                spell_swap(second_dict,dnd_dict.character_dict['special_spells']['second'],dnd_dict.character_dict['spells']['second'])
                spell_add(second_spell,dnd_dict.character_dict['spells']['second'],second_dict)
                break

        elif choice == '3':
            if not third_dict:
                print("Error: You Do Not Know Any Spells of This Level in This Class.")
                continue
            else:
                spell_swap(third_dict,dnd_dict.character_dict['special_spells']['third'],dnd_dict.character_dict['spells']['third'])
                spell_add(third_spell,dnd_dict.character_dict['spells']['third'],third_dict)
                break

        elif choice == '0':
            break

        else:
            print("Error: Invalid Input")
            continue



def fourth_swap(first_spell,second_spell,third_spell,fourth_spell,first_dict,second_dict,third_dict,fourth_dict):
    while True:
        choice = input("""What level do you want to select from?
1) First
2) Second
3) Third
4) Fourth
0) Do Not Swap
Enter your Selection: """)
        if choice == '1':
            if not first_dict:
                print("Error: You Do Not Know Any Spells of This Level in This Class.")
                continue
            else:
                spell_swap(first_dict,dnd_dict.character_dict['special_spells']['first'],dnd_dict.character_dict['spells']['first'])
                spell_add(first_spell,dnd_dict.character_dict['spells']['first'],first_dict)
                break

        elif choice == '2':
            if not second_dict:
                print("Error: You Do Not Know Any Spells of This Level in This Class.")
                continue
            else:
                spell_swap(second_dict,dnd_dict.character_dict['special_spells']['second'],dnd_dict.character_dict['spells']['second'])
                spell_add(second_spell,dnd_dict.character_dict['spells']['second'],second_dict)
                break

        elif choice == '3':
            if not third_dict:
                print("Error: You Do Not Know Any Spells of This Level in This Class.")
                continue
            else:
                spell_swap(third_dict,dnd_dict.character_dict['special_spells']['third'],dnd_dict.character_dict['spells']['third'])
                spell_add(third_spell,dnd_dict.character_dict['spells']['third'],third_dict)
                break

        elif choice == '4':
            if not fourth_dict:
                print("Error: You Do Not Know Any Spells of This Level in This Class.")
                continue
            else:
                spell_swap(fourth_dict,dnd_dict.character_dict['special_spells']['fourth'],dnd_dict.character_dict['spells']['fourth'])
                spell_add(fourth_spell,dnd_dict.character_dict['spells']['fourth'],fourth_dict)
                break

        elif choice == '0':
            break

        else:
            print("Error: Invalid Input")
            continue

def fifth_swap(first_spell,second_spell,third_spell,fourth_spell,fifth_spell,first_dict,second_dict,third_dict,fourth_dict,fifth_dict):
    while True:
        choice = input("""What level do you want to select from?
1) First
2) Second
3) Third
4) Fourth
5) Fifth
0) Do Not Swap
Enter your Selection: """)
        if choice == '1':
            if not first_dict:
                print("Error: You Do Not Know Any Spells of This Level in This Class.")
                continue
            else:
                spell_swap(first_dict,dnd_dict.character_dict['special_spells']['first'],dnd_dict.character_dict['spells']['first'])
                spell_add(first_spell,dnd_dict.character_dict['spells']['first'],first_dict)
                break

        elif choice == '2':
            if not second_dict:
                print("Error: You Do Not Know Any Spells of This Level in This Class.")
                continue
            else:
                spell_swap(second_dict,dnd_dict.character_dict['special_spells']['second'],dnd_dict.character_dict['spells']['second'])
                spell_add(second_spell,dnd_dict.character_dict['spells']['second'],second_dict)
                break

        elif choice == '3':
            if not third_dict:
                print("Error: You Do Not Know Any Spells of This Level in This Class.")
                continue
            else:
                spell_swap(third_dict,dnd_dict.character_dict['special_spells']['third'],dnd_dict.character_dict['spells']['third'])
                spell_add(third_spell,dnd_dict.character_dict['spells']['third'],third_dict)
                break

        elif choice == '4':
            if not fourth_dict:
                print("Error: You Do Not Know Any Spells of This Level in This Class.")
                continue
            else:
                spell_swap(fourth_dict,dnd_dict.character_dict['special_spells']['fourth'],dnd_dict.character_dict['spells']['fourth'])
                spell_add(fourth_spell,dnd_dict.character_dict['spells']['fourth'],fourth_dict)
                break

        elif choice == '5':
            if not fifth_dict:
                print("Error: You Do Not Know Any Spells of This Level in This Class.")
                continue
            else:
                spell_swap(fifth_dict,dnd_dict.character_dict['special_spells']['fifth'],dnd_dict.character_dict['spells']['fifth'])
                spell_add(fifth_spell,dnd_dict.character_dict['spells']['fifth'],fifth_dict)
                break

        elif choice == '0':
            break

        else:
            print("Error: Invalid Input")
            continue

def sixth_swap(first_spell,second_spell,third_spell,fourth_spell,fifth_spell,sixth_spell,first_dict,second_dict,third_dict,fourth_dict,fifth_dict,sixth_dict):
    while True:
        choice = input("""What level do you want to select from?
1) First
2) Second
3) Third
4) Fourth
5) Fifth
6) Sixth
0) Do Not Swap
Enter your Selection: """)
        if choice == '1':
            if not first_dict:
                print("Error: You Do Not Know Any Spells of This Level in This Class.")
                continue
            else:
                spell_swap(first_dict,dnd_dict.character_dict['special_spells']['first'],dnd_dict.character_dict['spells']['first'])
                spell_add(first_spell,dnd_dict.character_dict['spells']['first'],first_dict)
                break

        elif choice == '2':
            if not second_dict:
                print("Error: You Do Not Know Any Spells of This Level in This Class.")
                continue
            else:
                spell_swap(second_dict,dnd_dict.character_dict['special_spells']['second'],dnd_dict.character_dict['spells']['second'])
                spell_add(second_spell,dnd_dict.character_dict['spells']['second'],second_dict)
                break

        elif choice == '3':
            if not third_dict:
                print("Error: You Do Not Know Any Spells of This Level in This Class.")
                continue
            else:
                spell_swap(third_dict,dnd_dict.character_dict['special_spells']['third'],dnd_dict.character_dict['spells']['third'])
                spell_add(third_spell,dnd_dict.character_dict['spells']['third'],third_dict)
                break

        elif choice == '4':
            if not fourth_dict:
                print("Error: You Do Not Know Any Spells of This Level in This Class.")
                continue
            else:
                spell_swap(fourth_dict,dnd_dict.character_dict['special_spells']['fourth'],dnd_dict.character_dict['spells']['fourth'])
                spell_add(fourth_spell,dnd_dict.character_dict['spells']['fourth'],fourth_dict)
                break

        elif choice == '5':
            if not fifth_dict:
                print("Error: You Do Not Know Any Spells of This Level in This Class.")
                continue
            else:
                spell_swap(fifth_dict,dnd_dict.character_dict['special_spells']['fifth'],dnd_dict.character_dict['spells']['fifth'])
                spell_add(fifth_spell,dnd_dict.character_dict['spells']['fifth'],fifth_dict)
                break

        elif choice == '6':
            if not sixth_dict:
                print("Error: You Do Not Know Any Spells of This Level in This Class.")
                continue
            else:
                spell_swap(sixth_dict,dnd_dict.character_dict['special_spells']['sixth'],dnd_dict.character_dict['spells']['sixth'])
                spell_add(sixth_spell,dnd_dict.character_dict['spells']['sixth'],sixth_dict)
                break

        elif choice == '0':
            break

        else:
            print("Error: Invalid Input")
            continue

def seventh_swap(first_spell,second_spell,third_spell,fourth_spell,fifth_spell,sixth_spell,seventh_spell,first_dict,second_dict,third_dict,fourth_dict,fifth_dict,sixth_dict,seventh_dict):
    while True:
        choice = input("""What level do you want to select from?
1) First
2) Second
3) Third
4) Fourth
5) Fifth
6) Sixth
7) Seventh
0) Do Not Swap
Enter your Selection: """)
        if choice == '1':
            if not first_dict:
                print("Error: You Do Not Know Any Spells of This Level in This Class.")
                continue
            else:
                spell_swap(first_dict,dnd_dict.character_dict['special_spells']['first'],dnd_dict.character_dict['spells']['first'])
                spell_add(first_spell,dnd_dict.character_dict['spells']['first'],first_dict)
                break

        elif choice == '2':
            if not second_dict:
                print("Error: You Do Not Know Any Spells of This Level in This Class.")
                continue
            else:
                spell_swap(second_dict,dnd_dict.character_dict['special_spells']['second'],dnd_dict.character_dict['spells']['second'])
                spell_add(second_spell,dnd_dict.character_dict['spells']['second'],second_dict)
                break

        elif choice == '3':
            if not third_dict:
                print("Error: You Do Not Know Any Spells of This Level in This Class.")
                continue
            else:
                spell_swap(third_dict,dnd_dict.character_dict['special_spells']['third'],dnd_dict.character_dict['spells']['third'])
                spell_add(third_spell,dnd_dict.character_dict['spells']['third'],third_dict)
                break

        elif choice == '4':
            if not fourth_dict:
                print("Error: You Do Not Know Any Spells of This Level in This Class.")
                continue
            else:
                spell_swap(fourth_dict,dnd_dict.character_dict['special_spells']['fourth'],dnd_dict.character_dict['spells']['fourth'])
                spell_add(fourth_spell,dnd_dict.character_dict['spells']['fourth'],fourth_dict)
                break

        elif choice == '5':
            if not fifth_dict:
                print("Error: You Do Not Know Any Spells of This Level in This Class.")
                continue
            else:
                spell_swap(fifth_dict,dnd_dict.character_dict['special_spells']['fifth'],dnd_dict.character_dict['spells']['fifth'])
                spell_add(fifth_spell,dnd_dict.character_dict['spells']['fifth'],fifth_dict)
                break

        elif choice == '6':
            if not sixth_dict:
                print("Error: You Do Not Know Any Spells of This Level in This Class.")
                continue
            else:
                spell_swap(sixth_dict,dnd_dict.character_dict['special_spells']['sixth'],dnd_dict.character_dict['spells']['sixth'])
                spell_add(sixth_spell,dnd_dict.character_dict['spells']['sixth'],sixth_dict)
                break

        elif choice == '7':
            if not seventh_dict:
                print("Error: You Do Not Know Any Spells of This Level in This Class.")
                continue
            else:
                spell_swap(seventh_dict,dnd_dict.character_dict['special_spells']['seventh'],dnd_dict.character_dict['spells']['seventh'])
                spell_add(seventh_spell,dnd_dict.character_dict['spells']['seventh'],seventh_dict)
                break

        elif choice == '0':
            break

        else:
            print("Error: Invalid Input")
            continue

def eighth_swap(first_spell,second_spell,third_spell,fourth_spell,fifth_spell,sixth_spell,seventh_spell,eighth_spell,first_dict,second_dict,third_dict,fourth_dict,fifth_dict,sixth_dict,seventh_dict,eighth_dict):
    while True:
        choice = input("""What level do you want to select from?
1) First
2) Second
3) Third
4) Fourth
5) Fifth
6) Sixth
7) Seventh
8) Eighth
0) Do Not Swap
Enter your Selection: """)
        if choice == '1':
            if not first_dict:
                print("Error: You Do Not Know Any Spells of This Level in This Class.")
                continue
            else:
                spell_swap(first_dict,dnd_dict.character_dict['special_spells']['first'],dnd_dict.character_dict['spells']['first'])
                spell_add(first_spell,dnd_dict.character_dict['spells']['first'],first_dict)
                break

        elif choice == '2':
            if not second_dict:
                print("Error: You Do Not Know Any Spells of This Level in This Class.")
                continue
            else:
                spell_swap(second_dict,dnd_dict.character_dict['special_spells']['second'],dnd_dict.character_dict['spells']['second'])
                spell_add(second_spell,dnd_dict.character_dict['spells']['second'],second_dict)
                break

        elif choice == '3':
            if not third_dict:
                print("Error: You Do Not Know Any Spells of This Level in This Class.")
                continue
            else:
                spell_swap(third_dict,dnd_dict.character_dict['special_spells']['third'],dnd_dict.character_dict['spells']['third'])
                spell_add(third_spell,dnd_dict.character_dict['spells']['third'],third_dict)
                break

        elif choice == '4':
            if not fourth_dict:
                print("Error: You Do Not Know Any Spells of This Level in This Class.")
                continue
            else:
                spell_swap(fourth_dict,dnd_dict.character_dict['special_spells']['fourth'],dnd_dict.character_dict['spells']['fourth'])
                spell_add(fourth_spell,dnd_dict.character_dict['spells']['fourth'],fourth_dict)
                break

        elif choice == '5':
            if not fifth_dict:
                print("Error: You Do Not Know Any Spells of This Level in This Class.")
                continue
            else:
                spell_swap(fifth_dict,dnd_dict.character_dict['special_spells']['fifth'],dnd_dict.character_dict['spells']['fifth'])
                spell_add(fifth_spell,dnd_dict.character_dict['spells']['fifth'],fifth_dict)
                break

        elif choice == '6':
            if not sixth_dict:
                print("Error: You Do Not Know Any Spells of This Level in This Class.")
                continue
            else:
                spell_swap(sixth_dict,dnd_dict.character_dict['special_spells']['sixth'],dnd_dict.character_dict['spells']['sixth'])
                spell_add(sixth_spell,dnd_dict.character_dict['spells']['sixth'],sixth_dict)
                break

        elif choice == '7':
            if not seventh_dict:
                print("Error: You Do Not Know Any Spells of This Level in This Class.")
                continue
            else:
                spell_swap(seventh_dict,dnd_dict.character_dict['special_spells']['seventh'],dnd_dict.character_dict['spells']['seventh'])
                spell_add(seventh_spell,dnd_dict.character_dict['spells']['seventh'],seventh_dict)
                break

        elif choice == '8':
            if not eighth_dict:
                print("Error: You Do Not Know Any Spells of This Level in This Class.")
                continue
            else:
                spell_swap(eighth_dict,dnd_dict.character_dict['special_spells']['eighth'],dnd_dict.character_dict['spells']['eighth'])
                spell_add(eighth_spell,dnd_dict.character_dict['spells']['eighth'],eighth_dict)
                break

        elif choice == '0':
            break

        else:
            print("Error: Invalid Input")
            continue


def ninth_swap(first_spell,second_spell,third_spell,fourth_spell,fifth_spell,sixth_spell,seventh_spell,eighth_spell,ninth_spell,first_dict,second_dict,third_dict,fourth_dict,fifth_dict,sixth_dict,seventh_dict,eighth_dict,ninth_dict):
    while True:
        choice = input("""What level do you want to select from?
1) First
2) Second
3) Third
4) Fourth
5) Fifth
6) Sixth
7) Seventh
8) Eighth
9) Ninth
0) Do Not Swap
Enter your Selection: """)
        if choice == '1':
            if not first_dict:
                print("Error: You Do Not Know Any Spells of This Level in This Class.")
                continue
            else:
                spell_swap(first_dict,dnd_dict.character_dict['special_spells']['first'],dnd_dict.character_dict['spells']['first'])
                spell_add(first_spell,dnd_dict.character_dict['spells']['first'],first_dict)
                break

        elif choice == '2':
            if not second_dict:
                print("Error: You Do Not Know Any Spells of This Level in This Class.")
                continue
            else:
                spell_swap(second_dict,dnd_dict.character_dict['special_spells']['second'],dnd_dict.character_dict['spells']['second'])
                spell_add(second_spell,dnd_dict.character_dict['spells']['second'],second_dict)
                break

        elif choice == '3':
            if not third_dict:
                print("Error: You Do Not Know Any Spells of This Level in This Class.")
                continue
            else:
                spell_swap(third_dict,dnd_dict.character_dict['special_spells']['third'],dnd_dict.character_dict['spells']['third'])
                spell_add(third_spell,dnd_dict.character_dict['spells']['third'],third_dict)
                break

        elif choice == '4':
            if not fourth_dict:
                print("Error: You Do Not Know Any Spells of This Level in This Class.")
                continue
            else:
                spell_swap(fourth_dict,dnd_dict.character_dict['special_spells']['fourth'],dnd_dict.character_dict['spells']['fourth'])
                spell_add(fourth_spell,dnd_dict.character_dict['spells']['fourth'],fourth_dict)
                break

        elif choice == '5':
            if not fifth_dict:
                print("Error: You Do Not Know Any Spells of This Level in This Class.")
                continue
            else:
                spell_swap(fifth_dict,dnd_dict.character_dict['special_spells']['fifth'],dnd_dict.character_dict['spells']['fifth'])
                spell_add(fifth_spell,dnd_dict.character_dict['spells']['fifth'],fifth_dict)
                break

        elif choice == '6':
            if not sixth_dict:
                print("Error: You Do Not Know Any Spells of This Level in This Class.")
                continue
            else:
                spell_swap(sixth_dict,dnd_dict.character_dict['special_spells']['sixth'],dnd_dict.character_dict['spells']['sixth'])
                spell_add(sixth_spell,dnd_dict.character_dict['spells']['sixth'],sixth_dict)
                break

        elif choice == '7':
            if not seventh_dict:
                print("Error: You Do Not Know Any Spells of This Level in This Class.")
                continue
            else:
                spell_swap(seventh_dict,dnd_dict.character_dict['special_spells']['seventh'],dnd_dict.character_dict['spells']['seventh'])
                spell_add(seventh_spell,dnd_dict.character_dict['spells']['seventh'],seventh_dict)
                break

        elif choice == '8':
            if not eighth_dict:
                print("Error: You Do Not Know Any Spells of This Level in This Class.")
                continue
            else:
                spell_swap(eighth_dict,dnd_dict.character_dict['special_spells']['eighth'],dnd_dict.character_dict['spells']['eighth'])
                spell_add(eighth_spell,dnd_dict.character_dict['spells']['eighth'],eighth_dict)
                break

        elif choice == '9':
            if not ninth_dict:
                print("Error: You Do Not Know Any Spells of This Level in This Class.")
                continue
            else:
                spell_swap(ninth_dict,dnd_dict.character_dict['special_spells']['ninth'],dnd_dict.character_dict['spells']['ninth'])
                spell_add(ninth_spell,dnd_dict.character_dict['spells']['ninth'],ninth_dict)
                break

        elif choice == '0':
            break

        else:
            print("Error: Invalid Input")
            continue



# Used for magical secrets at 18, including cantrips
def magical_secrets_18(first,second,third,fourth,fifth,sixth,seventh,eighth,ninth,cantrip):
    while True:
        choice = input("""What level do you want to select from?
1) First
2) Second
3) Third
4) Fourth
5) Fifth
6) Sixth
7) Seventh
8) Eighth
9) Ninth
10) Cantrip
Enter your Selection: """)
        if choice == '1':
            first
            break

        elif choice == '2':
            second
            break

        elif choice == '3':
            third
            break

        elif choice == '4':
            fourth
            break

        elif choice == '5':
            fifth
            break

        elif choice == '6':
            sixth
            break

        elif choice == '7':
            seventh
            break

        elif choice == '8':
            eighth
            break

        elif choice == '9':
            ninth
            break

        elif choice == '10':
            cantrip
            break

        else:
            print("Error: Invalid Input")
            continue



# Used to determine the Monk's Ki Saving Throw
def ki_save():
    if dnd_dict.character_dict['player_class']['monk']['class_level'] > 1:
        ki_save = 8 + dnd_dict.character_dict['prof_bonus'] + dnd_dict.character_dict['Stats']['wisdom']['mod']
        dnd_dict.character_dict['spell_modifier']['ki_save'] = ki_save


# Used to updating spell attack and saving throw modifiers
def save_modifier_update():
    if dnd_dict.character_dict['spell_modifier']['ki_save'] > 0:
        ki_save = 8 + dnd_dict.character_dict['prof_bonus'] + dnd_dict.character_dict['Stats']['wisdom']['mod']
        dnd_dict.character_dict['spell_modifier']['ki_save'] = ki_save
        
    if dnd_dict.character_dict['spell_modifier']['intelligence']['attack'] > 0:
        spell_attack = ((dnd_dict.character_dict['Stats']['intelligence']['mod']) + dnd_dict.character_dict['prof_bonus'])
        dnd_dict.character_dict['spell_modifier']['intelligence']['attack'] = spell_attack

    if dnd_dict.character_dict['spell_modifier']['intelligence']['save'] > 0:
        spell_save = ((dnd_dict.character_dict['Stats']['intelligence']['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
        dnd_dict.character_dict['spell_modifier']['intelligence']['save'] = spell_save

    if dnd_dict.character_dict['spell_modifier']['wisdom']['attack'] > 0:
        spell_attack = ((dnd_dict.character_dict['Stats']['wisdom']['mod']) + dnd_dict.character_dict['prof_bonus'])
        dnd_dict.character_dict['spell_modifier']['wisdom']['attack'] = spell_attack

    if dnd_dict.character_dict['spell_modifier']['wisdom']['save'] > 0:
        spell_save = ((dnd_dict.character_dict['Stats']['wisdom']['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
        dnd_dict.character_dict['spell_modifier']['wisdom']['save'] = spell_save

    if dnd_dict.character_dict['spell_modifier']['charisma']['attack'] > 0:
        spell_attack = ((dnd_dict.character_dict['Stats']['charisma']['mod']) + dnd_dict.character_dict['prof_bonus'])
        dnd_dict.character_dict['spell_modifier']['charisma']['attack'] = spell_attack

    if dnd_dict.character_dict['spell_modifier']['charisma']['save'] > 0:
        spell_save = ((dnd_dict.character_dict['Stats']['charisma']['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
        dnd_dict.character_dict['spell_modifier']['charisma']['save'] = spell_save

# Used for determining Medium Armor Class. The Dex Mod can only be a maximum of 2.
def med_armor(value):
    if dnd_dict.character_dict['Stats']['dexterity']['mod'] > 2:
        dnd_dict.character_dict['armor_class'] = 2 + value
    else:
        dnd_dict.character_dict['armor_class'] = dnd_dict.character_dict['Stats']['dexterity']['mod'] + value

# Used to update armor class. Add armor as needed.
def armor_check():
    dexterity = dnd_dict.character_dict['Stats']['dexterity']['mod']
    chest = dnd_dict.character_dict['chest_armor']
    shield = dnd_dict.character_dict['shield']
    leather = dnd_weapon.light_armor(11)
    studded_leather = dnd_weapon.light_armor(12)
    armor_class = dnd_dict.character_dict['armor_class']

    if dnd_dict.character_dict['barbarian_armor_class'] > 0:
        dnd_dict.character_dict['barbarian_armor_class'] = 10 + dexterity + dnd_dict.character_dict['Stats']['constitution']['mod']

    if dnd_dict.character_dict['monk_armor_class'] > 0:
        dnd_dict.character_dict['monk_armor_class'] = 10 + dexterity + dnd_dict.character_dict['Stats']['wisdom']['mod']

    if dnd_dict.character_dict['sorcerer_armor_class'] > 0:
        dnd_dict.character_dict['sorcerer_armor_class'] = 13 + dexterity

    if dnd_dict.character_dict['natural_armor_class'] == 0:
        dnd_dict.character_dict['base_armor_class'] = 10 + dexterity

    if chest == 'Leather Armor':
        armor_class = leather

    if chest == 'Studded Leather Armor':
        armor_class = studded_leather

    if chest == 'Scale Mail':
        med_armor(14)

    if chest == 'Chain Mail':
        armor_class = 16
        dnd_dict.character_dict['armor_class'] = 16

    if shield == 'Shield':
        dnd_dict.character_dict['armor_class'] += 2

    if shield == 'Wooden Shield':
        dnd_dict.character_dict['armor_class'] += 2

    if 'defense_fighting_style' in dnd_dict.character_dict['features'] and chest:
        dnd_dict.character_dict['armor_class'] += 1

# If you don't have chest armor, the armor class is just the base armor class
    if not chest:
        dnd_dict.character_dict['armor_class'] = dnd_dict.character_dict['base_armor_class']









































































































































