import dnd_dict, dnd_skills, dnd_features, random


def boon_selection():
    boon_dict = dnd_dict.character_dict['boon']
    while True:
        choice = input("""Select the boon you want:
1) Boon of Combat Prowess
2) Boon of Dimensional Travel
3) Boon of Fate
4) Boon of Fortitude
5) Boon of High Magic
6) Boon of Immortality
7) Boon of Invincibility
8) Boon of Irresistible Offense
9) Boon of Luck
10) Boon of Magic Resistance
11) Boon of Peerless Aim
12) Boon of Perfect Health
13) Boon of Planar Travel
14) Boon of Quick Casting
15) Boon of Recovery
16) Boon of Resilience
17) Boon of Skill Proficiency
18) Boon of Speed
19) Boon of Spell Mastery
20) Boon of Spell Recall
21) Boon of the Fire Soul
22) Boon of the Night Spirit
23) Boon of the Stormborn
24) Boon of the Unfettered
25) Boon of Truesight
26) Boon of Undetectability
Enter your selection: """)
        if choice == '1':
            if 'boon_of_combat_prowess' in boon_dict:
                print("Boon already known")
                continue
            else:
                dnd_features.boon_of_combat_prowess()
                break

        elif choice == '2':
            if 'boon_of_dimensional_travel' in boon_dict:
                print("Boon already known")
                continue
            else:
                dnd_features.boon_of_dimensional_travel()
                break

        elif choice == '3':
            if 'boon_of_fate' in boon_dict:
                print("Boon already known")
                continue
            else:
                dnd_features.boon_of_fate()
                break

        elif choice == '4':
            if 'boon_of_fortitude' in boon_dict:
                print("Boon already known")
                continue
            else:
                dnd_features.boon_of_fortitude()
                break

        elif choice == '5':
            if 'boon_of_high_magic' in boon_dict:
                print("Boon already known")
                continue
            elif dnd_dict.character_dict['spell_slots']['ninth'] == 0:
                print("You must have a 9th level spell slot")
                continue
            else:
                dnd_features.boon_of_high_magic()
                break

        elif choice == '6':
            if 'boon_of_immortality' in boon_dict:
                print("Boon already known")
                continue
            else:
                dnd_features.boon_of_immortality()
                break

        elif choice == '7':
            if 'boon_of_invincibility' in boon_dict:
                print("Boon already known")
                continue
            else:
                dnd_features.boon_of_invincibility()
                break

        elif choice == '8':
            if 'boon_of_irresistible_offense' in boon_dict:
                print("Boon already known")
                continue
            else:
                dnd_features.boon_of_irresistible_offense()
                break

        elif choice == '9':
            if 'boon_of_luck' in boon_dict:
                print("Boon already known")
                continue
            else:
                dnd_features.boon_of_luck()
                break

        elif choice == '10':
            if 'boon_of_magic_resistance' in boon_dict:
                print("Boon already known")
                continue
            else:
                dnd_features.boon_of_magic_resistance()
                break

        elif choice == '11':
            if 'boon_of_peerless_aim' in boon_dict:
                print("Boon already known")
                continue
            else:
                dnd_features.boon_of_peerless_aim()
                break

        elif choice == '12':
            if 'boon_of_perfect_health' in boon_dict:
                print("Boon already known")
                continue
            else:
                dnd_features.boon_of_perfect_health()
                break

        elif choice == '13':
            if 'boon_of_planar_travel' in boon_dict:
                print("Boon already known")
                continue
            else:
                dnd_features.boon_of_planar_travel()
                break

        elif choice == '14':
            if 'boon_of_quick_casting' in boon_dict:
                print("Boon already known")
                continue
            else:
                dnd_features.boon_of_quick_casting()
                break

        elif choice == '15':
            if 'boon_of_recovery' in boon_dict:
                print("Boon already known")
                continue
            else:
                dnd_features.boon_of_recovery()
                break

        elif choice == '16':
            if 'boon_of_resilience' in boon_dict:
                print("Boon already known")
                continue
            else:
                dnd_features.boon_of_resilience()
                break

        elif choice == '17':
            if 'boon_of_skill_proficiency' in boon_dict:
                print("Boon already known")
                continue
            else:
                dnd_features.boon_of_skill_proficiency()
                break

        elif choice == '18':
            if 'boon_of_speed' in boon_dict:
                print("Boon already known")
                continue
            else:
                dnd_features.boon_of_speed()
                break

        elif choice == '19':
            if 'boon_of_spell_mastery' in boon_dict:
                print("Boon already known")
                continue
            else:
                dnd_features.boon_of_spell_mastery()
                break

        elif choice == '20':
            if 'boon_of_spell_recall' in boon_dict:
                print("Boon already known")
                continue
            else:
                dnd_features.boon_of_spell_recall()
                break

        elif choice == '21':
            if 'boon_of_the_fire_soul' in boon_dict:
                print("Boon already known")
                continue
            else:
                dnd_features.boon_of_the_fire_soul()
                break

        elif choice == '22':
            if 'boon_of_the_night_spirit' in boon_dict:
                print("Boon already known")
                continue
            else:
                dnd_features.boon_of_the_night_spirit()
                break

        elif choice == '23':
            if 'boon_of_the_stormborn' in boon_dict:
                print("Boon already known")
                continue
            else:
                dnd_features.boon_of_the_stormborn()
                break

        elif choice == '24':
            if 'boon_of_the_unfettered' in boon_dict:
                print("Boon already known")
                continue
            else:
                dnd_features.boon_of_the_unfettered()
                break

        elif choice == '25':
            if 'boon_of_truesight' in boon_dict:
                print("Boon already known")
                continue
            else:
                dnd_features.boon_of_truesight()
                break

        elif choice == '26':
            if 'boon_of_undetectability' in boon_dict:
                print("Boon already known")
                continue
            else:
                dnd_features.boon_of_undetectability()
                break

        else:
            print("Error: Invalid Input")
            continue



# Used for Aberrant Dragonmark
# You have a 10% chance of getting a single boon from level 10 on
def aberrant_boon():
    if 'aberrant_dragonmark' in dnd_dict.character_dict['feats']:
        if dnd_dict.character_dict['total_level'] < 10 or dnd_dict.character_dict['aberrant_check'] == 'Yes':
            pass
        else:
            random_number = random.randint(1,10)
            if random_number == 10:
                boon_selection()
                dnd_dict.character_dict['aberrant_check'] = 'Yes'
# Lose 1 Hit Die
# Set up a list to determine which die will be lost
# Total HP will be reduced by a random roll of that die
                res = []
                if dnd_dict.character_dict['d6'] > 0:
                    res.append('d6')
                if dnd_dict.character_dict['d8'] > 0:
                    res.append('d8')
                if dnd_dict.character_dict['d10'] > 0:
                    res.append('d10')
                if dnd_dict.character_dict['d12'] > 0:
                    res.append('d12')
    
                tmp_dict = {}
                counter = 1
                for value in res:
                    print(f'{counter}) {value}')
                    tmp_dict[counter] = value
                    counter+=1
                while True:
                    try:
                        choice = int(input("Select the Hit Die you want to reduce by 1: "))
                    except ValueError as e:
                        print("Error: Invalid Input")
                        continue
                    if tmp_dict.get(choice,{}):
                        to_delete = tmp_dict[choice]
                        if to_delete == 'd6':
                            dnd_dict.character_dict['d6'] -= 1
                            new_random_number = random.randint(1,6)
                            dnd_dict.character_dict['hp'] -= new_random_number
                            print(f'Hit Points reduced by {new_random_number}')
                            break
                        if to_delete == 'd8':
                            dnd_dict.character_dict['d8'] -= 1
                            new_random_number = random.randint(1,8)
                            dnd_dict.character_dict['hp'] -= new_random_number
                            print(f'Hit Points reduced by {new_random_number}')
                            break
                        if to_delete == 'd10':
                            dnd_dict.character_dict['d10'] -= 1
                            new_random_number = random.randint(1,10)
                            dnd_dict.character_dict['hp'] -= new_random_number
                            print(f'Hit Points reduced by {new_random_number}')
                            break
                        if to_delete == 'd12':
                            dnd_dict.character_dict['d12'] -= 1
                            new_random_number = random.randint(1,12)
                            dnd_dict.character_dict['hp'] -= new_random_number
                            print(f'Hit Points reduced by {new_random_number}')
                        break

# Subtract your Constitution Modifier (minimum of 1) from your total hp
                if dnd_dict.character_dict['Stats']['constitution']['mod'] < 1:
                    con_mod = dnd_dict.character_dict['Stats']['constitution']['mod']
                    dnd_dict.character_dict['hp'] -= 1 
                    print(f'Hit Points reduced by an additional {con_mod}')
                else:
                    dnd_dict.character_dict['hp'] -= dnd_dict.character_dict['Stats']['constitution']['mod']
                    print("Hit Points reduced by an additional 1")
















































































