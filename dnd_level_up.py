#!/usr/bin/python3
import dnd_skills, dnd_dict, dnd_class,random,dnd_artificer,dnd_barbarian,dnd_bard,dnd_cleric,dnd_druid,dnd_fighter,dnd_monk,dnd_paladin,dnd_ranger,dnd_rogue,dnd_sorcerer,dnd_warlock,dnd_wizard,dnd_feats, dnd_metamagic, dnd_invocations, dnd_fighting_styles, dnd_boons

# Used to level up a player's class. If they already have a level in it, proceed as normally. If they don't, they need to have at least a certain amount in one or two stats to multiclass into it.

def level_up(die):
    dnd_boons.aberrant_boon()
    dnd_skills.saving_throw_calc()
    dnd_skills.skill_calculation()
    dnd_skills.prof_modifier()
    dnd_skills.save_modifier_update()
# If the player has the Tough feat, increase hp by 2
    if 'tough' in dnd_dict.character_dict['features']:
        new_hp = (dnd_dict.character_dict['hp'] + 2)
        dnd_dict.character_dict['hp'] += new_hp
# If the player has Dwarven Toughness, increase hp by 1
    if 'dwarven_toughness' in dnd_dict.character_dict['features']:
        new_hp = (dnd_dict.character_dict['hp'] + 1)
        dnd_dict.character_dict['hp'] = new_hp

# Increases the hp
    hp_roll = random.randint(1,die)
    print("Your suggested Hit Point (as determined by a random roll) increase is {}. Bonuses from any additional features will automatically be added.".format(hp_roll))
    while True:
        try:
            choice = int(input("Enter your Hit Point increase: "))
        except ValueError as e:
            print("Error: Input must be an integer between 1 and {}.".format(die))
            continue
        if int(choice) > 0 and int(choice) <= die:
            dnd_dict.character_dict["hp"] += int(choice)
            break
        elif int(choice) < 1 or int(choice) > die:
            print("Error: Your selection must be between 1 and {}.".format(die))
            continue


    if dnd_dict.character_dict['total_level'] == 5 and dnd_dict.character_dict['race'] == 'Tiefling':
        dnd_dict.character_dict['special_spells']['racial_spells']['darkness'] = 'Darkness'
        dnd_dict.character_dict['spells']['second']['darkness'] = 'Darkness'
    dnd_skills.ki_save()
    dnd_metamagic.metamagic_adept_swap()
    dnd_invocations.eldritch_adept_swap()

# Ability Score Improvement
def asi():
    x=1
    while x < 4:
        if x<3:
            while True:
                dict = dnd_dict.character_dict['Stats']
                print(f'{x}/2')
                choice = input("""Choose the Ability Score you want to raise (to a maximum of 20):
1) Strength
2) Dexterity
3) Constitution
4) Intelligence
5) Wisdom
6) Charisma
Enter your selection: """)
                if choice=='1':
# If the AS is at 20 or below, increase it. Otherwise, reject it.
                    if dict['strength']['base'] < 20:
                        stat = dict['strength']['base']+1
                        dict['strength']['base'] = stat
                        mod = dnd_class.Character.mod(dict['strength']['base'])
                        dict['strength']['mod'] = mod
                        x+=1
                        break
                    else:
                        print("Stat cannot be raised over 20")
                        continue
                elif choice=='2':
                    if dict['dexterity']['base'] < 20:
                        stat = dict['dexterity']['base']+1
                        dict['dexterity']['base'] = stat
                        mod = dnd_class.Character.mod(dict['dexterity']['base'])
                        dict['dexterity']['mod'] = mod
                        x+=1
                        break
                    else:
                        print("Stat cannot be raised over 20")
                        continue

                elif choice=='3':
                    if dict['constitution']['base'] < 20:
                        stat = dict['constitution']['base']+1
                        dict['constitution']['base'] = stat
                        mod = dnd_class.Character.mod(dict['constitution']['base'])
# If the modifier is positive and is raised, then increase you hp by your total level.
                        if mod > dict['constitution']['mod'] and mod > 0:
                            new_hp = dnd_dict.character_dict['hp'] + dnd_dict.character_dict['total_level']
                            dnd_dict.character_dict['hp'] = new_hp
                        dict['constitution']['mod'] = mod
                        x+=1
                        break
                    else:
                        print("Stat cannot be raised over 20")
                        continue

                elif choice=='4':
                    if dict['intelligence']['base'] < 20:
                        stat = dict['intelligence']['base']+1
                        dict['intelligence']['base'] = stat
                        mod = dnd_class.Character.mod(dict['intelligence']['base'])
                        dict['intelligence']['mod'] = mod
                        x+=1
                        break
                    else:
                        print("Stat cannot be raised over 20")
                        continue

                elif choice=='5':
                    if dict['wisdom']['base'] < 20:
                        stat = dict['wisdom']['base']+1
                        dict['wisdom']['base'] = stat
                        mod = dnd_class.Character.mod(dict['wisdom']['base'])
                        dict['wisdom']['mod'] = mod
                        x+=1
                        break
                    else:
                        print("Stat cannot be raised over 20")
                        continue

                elif choice=='6':
                    if dict['charisma']['base'] < 20:
                        stat = dict['charisma']['base']+1
                        dict['charisma']['base'] = stat
                        mod = dnd_class.Character.mod(dict['charisma']['base'])
                        dict['charisma']['mod'] = mod
                        x+=1
                        break
                    else:
                        print("Stat cannot be raised over 20")
                        continue

                else:
                    print("Invalid Selection")
        elif x==3:
            dnd_fighting_styles.martial_versatility_style_fighting_initiate()
            break



# Choose if you want an Ability Score Improvement or a feat
def asi_or_feat():
    dnd_metamagic.metamagic_adept_swap()
    dnd_fighting_styles.martial_versatility_style_fighting_initiate()
# If all stats are at 20, automatically choose a feat instead
    dict = dnd_dict.character_dict['Stats']
    if dict['strength']['base'] >= 20 and dict['dexterity']['base'] >= 20 and dict['constitution']['base'] >= 20 and dict['intelligence']['base'] >= 20 and dict['wisdom']['base'] >= 20 and dict['charisma']['base'] >= 20:
            dnd_feats.choose_feat()
    else:
        while True:
            choice = input("""Select one option:
1) Ability Score Improvement
2) Feat
Enter your selection: """)
            if choice == '1':
                asi()
                break
            elif choice == '2':
                dnd_feats.choose_feat()
                break
            else:
                print("Error: Invalid Input")
                continue




# Stat requirements to multiclass if you start with any of these classes.
# Artificer: 13 Int, Barbarian: 13 Strength, Bard: 13 Charisma, Cleric: 13 Wisdom
# Druid: 13 Wisdom, Fighter 13 Strength or 13 Dexterity, Monk: 13 Dexterity, 13 Wisdom
# Paladin: 13 Strength and 13 Charisma, Ranger: 13 Dexterity, 13 Wisdom
# Rogue: 13 Dexterity, Sorcerer: 13 Charisma, Warlock: 13 Charisma
# Wizard: 13 Intelligence
def class_reqs():
    if ("Artificer" in dnd_dict.character_dict.values() and dnd_dict.character_dict['Stats']['intelligence']['base'] >= 13) or ("Barbarian" in dnd_dict.character_dict.values() and dnd_dict.character_dict['Stats']['strength']['base'] >= 13) or ("Bard" in dnd_dict.character_dict.values() and dnd_dict.character_dict['Stats']['charisma']['base'] >= 13) or ("Cleric" in dnd_dict.character_dict.values() and dnd_dict.character_dict['Stats']['wisdom']['base'] >= 13) or ("Druid" in dnd_dict.character_dict.values() and dnd_dict.character_dict['Stats']['wisdom']['base'] >= 13) or ("Fighter" in dnd_dict.character_dict.values() and (dnd_dict.character_dict['Stats']['strength']['base'] >= 13 or dnd_dict.character_dict['Stats']['dexterity']['base'] >= 13))  or ("Monk" in dnd_dict.character_dict.values() and dnd_dict.character_dict['Stats']['dexterity']['base'] >= 13 and dnd_dict.character_dict['Stats']['wisdom']['base'] >= 13) or ("Paladin" in dnd_dict.character_dict.values() and dnd_dict.character_dict['Stats']['strength']['base'] >= 13 and dnd_dict.character_dict['Stats']['charisma']['base'] >= 13) or ("Ranger" in dnd_dict.character_dict.values() and dnd_dict.character_dict['Stats']['dexterity']['base'] >= 13 and dnd_dict.character_dict['Stats']['wisdom']['base'] >= 13) or ("Rogue" in dnd_dict.character_dict.values() and dnd_dict.character_dict['Stats']['dexterity']['base'] >= 13)  or ("Sorcerer" in dnd_dict.character_dict.values() and dnd_dict.character_dict['Stats']['charisma']['base'] >= 13) or ("Warlock" in dnd_dict.character_dict.values() and dnd_dict.character_dict['Stats']['charisma']['base'] >= 1) or ("Wizard" in dnd_dict.character_dict.values() and dnd_dict.character_dict['Stats']['intelligence']['base'] >= 13):
        return True

def class_level_up():

# Raises the new level
    new_total_level = (dnd_dict.character_dict['total_level'] + 1)
    dnd_dict.character_dict['total_level']=new_total_level
    dnd_skills.prof_modifier()
# Racial trait for Tiefling. They learn Hellish Rebuke at level 3 and
# Darkness at level 5
    if dnd_dict.character_dict['total_level'] == 3 and dnd_dict.character_dict['race'] == 'Tiefling':
        dnd_dict.character_dict['special_spells']['racial_spells']['hellish_rebuke'] = 'Hellish Rebuke'
        dnd_dict.character_dict['spells']['first']['hellish_rebuke'] = 'Hellish Rebuke'

    while True:
        choice2 = input("""Select the class you want to level up
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
        if choice2 == '1' and (("Artificer" in dnd_dict.character_dict.values()) or (dnd_dict.character_dict['Stats']['intelligence']['base'] >= 13 and class_reqs())): 
            dnd_dict.character_dict['total_level'] = new_total_level
            dnd_dict.character_dict['player_class']['artificer']['class_level'] +=1
            dnd_artificer.artificer()
            break


        elif choice2 == '2' and (("Barbarian" in dnd_dict.character_dict.values()) or (dnd_dict.character_dict['Stats']['strength']['base'] >= 13 and class_reqs())): 
            dnd_dict.character_dict['total_level'] = new_total_level
            new_class_level = (dnd_dict.character_dict['player_class']['barbarian']['class_level'] + 1)
            dnd_dict.character_dict['player_class']['barbarian']['class_level']= new_class_level
            dnd_barbarian.barbarian()
            break


        elif choice2 == '3' and (("Bard" in dnd_dict.character_dict.values()) or (dnd_dict.character_dict['Stats']['charisma']['base'] >= 13 and class_reqs())): 
            dnd_dict.character_dict['total_level'] = new_total_level
            new_class_level = (dnd_dict.character_dict['player_class']['bard']['class_level'] + 1)
            dnd_dict.character_dict['player_class']['bard']['class_level']= new_class_level
            dnd_bard.bard()
            break


        elif choice2 == '4' and (("Cleric" in dnd_dict.character_dict.values()) or (dnd_dict.character_dict['Stats']['wisdom']['base'] >= 13 and class_reqs())): 
            dnd_dict.character_dict['total_level'] = new_total_level
            new_class_level = (dnd_dict.character_dict['player_class']['cleric']['class_level'] + 1)
            dnd_dict.character_dict['player_class']['cleric']['class_level']= new_class_level
            dnd_cleric.cleric()
            break

        elif choice2 == '5' and (("Druid" in dnd_dict.character_dict.values()) or (dnd_dict.character_dict['Stats']['wisdom']['base'] >= 13 and class_reqs())): 
            dnd_dict.character_dict['total_level'] = new_total_level
            new_class_level = (dnd_dict.character_dict['player_class']['druid']['class_level'] + 1)
            dnd_dict.character_dict['player_class']['druid']['class_level']= new_class_level
            dnd_druid.druid()
            break

        elif choice2 == '6' and (("Fighter" in dnd_dict.character_dict.values()) or ((dnd_dict.character_dict['Stats']['strength']['base'] >= 13 or dnd_dict.character_dict['Stats']['dexterity']['base'] >= 13) and class_reqs())): 
            dnd_dict.character_dict['total_level'] = new_total_level
            new_class_level = (dnd_dict.character_dict['player_class']['fighter']['class_level'] + 1)
            dnd_dict.character_dict['player_class']['fighter']['class_level']= new_class_level
            dnd_fighter.fighter()
            break

        elif choice2 == '7' and (("Monk" in dnd_dict.character_dict.values()) or ((dnd_dict.character_dict['Stats']['dexterity']['base'] >= 13 and dnd_dict.character_dict['Stats']['wisdom']['base'] >= 13) and class_reqs())): 
            dnd_dict.character_dict['total_level'] = new_total_level
            new_class_level = (dnd_dict.character_dict['player_class']['monk']['class_level'] + 1)
            dnd_dict.character_dict['player_class']['monk']['class_level']= new_class_level
            dnd_monk.monk()
            break

        elif choice2 == '8' and (("Paladin" in dnd_dict.character_dict.values()) or ((dnd_dict.character_dict['Stats']['strength']['base'] >= 13 and dnd_dict.character_dict['Stats']['charisma']['base'] >= 13) and class_reqs())): 
            dnd_dict.character_dict['total_level'] = new_total_level
            new_class_level = (dnd_dict.character_dict['player_class']['paladin']['class_level'] + 1)
            dnd_dict.character_dict['player_class']['paladin']['class_level']= new_class_level
            dnd_paladin.paladin()
            break

        elif choice2 == '9' and (("Ranger" in dnd_dict.character_dict.values()) or ((dnd_dict.character_dict['Stats']['dexterity']['base'] >= 13 and dnd_dict.character_dict['Stats']['wisdom']['base'] >= 13) and class_reqs())): 
            dnd_dict.character_dict['total_level'] = new_total_level
            new_class_level = (dnd_dict.character_dict['player_class']['ranger']['class_level'] + 1)
            dnd_dict.character_dict['player_class']['ranger']['class_level']= new_class_level
            dnd_ranger.ranger()
            break

        elif choice2 == '10' and (("Rogue" in dnd_dict.character_dict.values()) or (dnd_dict.character_dict['Stats']['dexterity']['base'] >= 13  and class_reqs())): 
            dnd_dict.character_dict['total_level'] = new_total_level
            new_class_level = (dnd_dict.character_dict['player_class']['rogue']['class_level'] + 1)
            dnd_dict.character_dict['player_class']['rogue']['class_level']= new_class_level
            dnd_rogue.rogue()
            break

        elif choice2 == '11' and (("Sorcerer" in dnd_dict.character_dict.values()) or (dnd_dict.character_dict['Stats']['charisma']['base'] >= 13  and class_reqs())): 
            dnd_dict.character_dict['total_level'] = new_total_level
            new_class_level = (dnd_dict.character_dict['player_class']['sorcerer']['class_level'] + 1)
            dnd_dict.character_dict['player_class']['sorcerer']['class_level']= new_class_level
            dnd_sorcerer.sorcerer()
            break

        elif choice2 == '12' and (("Warlock" in dnd_dict.character_dict.values()) or (dnd_dict.character_dict['Stats']['charisma']['base'] >= 13  and class_reqs())): 
            dnd_dict.character_dict['total_level'] = new_total_level
            new_class_level = (dnd_dict.character_dict['player_class']['warlock']['class_level'] + 1)
            dnd_dict.character_dict['player_class']['warlock']['class_level']= new_class_level
            dnd_warlock.warlock()
            break

        elif choice2 == '13' and (("Wizard" in dnd_dict.character_dict.values()) or (dnd_dict.character_dict['Stats']['intelligence']['base'] >= 13  and class_reqs())): 
            dnd_dict.character_dict['total_level'] = new_total_level
            new_class_level = (dnd_dict.character_dict['player_class']['wizard']['class_level'] + 1)
            dnd_dict.character_dict['player_class']['wizard']['class_level']= new_class_level
            dnd_wizard.wizard()
            break

        else:
            print("Error: Invalid Input")
            continue




























