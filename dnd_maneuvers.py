import dnd_dict, dnd_skills,dnd_features


def maneuvers():
    dict = dnd_dict.character_dict['maneuvers']['types']
    while True:
        choice = input("""Select the Maneuver you want:
1) Ambush
2) Bait and Switch
3) Brace
4) Commander's Strike
5) Commanding Presence
6) Disarming Attack
7) Distracting Strike
8) Evasive Footwork
9) Feinting Attack
10) Goading Attack
11) Grappling Strike
12) Lunging Attack
13) Manuevering Attack
14) Menacing Attack
15) Parry
16) Precision Attack
17) Pushing Attack
18) Quick Toss
19) Rally
20) Riposte
21) Sweeping Attack
22) Tactical Assessment
23) Trip Attack
Enter your selection: """)
        if choice == '1':
            if 'ambush' in dict:
                print("Manuever already known")
                continue
            else:
                dnd_features.ambush()
                break

        elif choice == '2':
            if 'bait_and_switch' in dict:
                print("Manuever already known")
                continue
            else:
                dnd_features.bait_and_switch()
                break

        elif choice == '3':
            if 'brace' in dict:
                print("Manuever already known")
                continue
            else:
                dnd_features.brace()
                break

        elif choice == '4':
            if 'commanders_strike' in dict:
                print("Manuever already known")
                continue
            else:
                dnd_features.commanders_strike()
                break

        elif choice == '5':
            if 'commanding_presence' in dict:
                print("Manuever already known")
                continue
            else:
                dnd_features.commanding_presence()
                break

        elif choice == '6':
            if 'disarming_attack' in dict:
                print("Manuever already known")
                continue
            else:
                dnd_features.disarming_attack()
                break

        elif choice == '7':
            if 'distracting_strike' in dict:
                print("Manuever already known")
                continue
            else:
                dnd_features.distracting_strike()
                break

        elif choice == '8':
            if 'evasive_footwork' in dict:
                print("Manuever already known")
                continue
            else:
                dnd_features.evasive_footwork()
                break

        elif choice == '9':
            if 'feinting_attack' in dict:
                print("Manuever already known")
                continue
            else:
                dnd_features.feinting_attack()
                break

        elif choice == '10':
            if 'goading_attack' in dict:
                print("Manuever already known")
                continue
            else:
                dnd_features.goading_attack()
                break

        elif choice == '11':
            if 'grappling_strike' in dict:
                print("Manuever already known")
                continue
            else:
                dnd_features.grappling_strike()
                break

        elif choice == '12':
            if 'lunging_attack' in dict:
                print("Manuever already known")
                continue
            else:
                dnd_features.lunging_attack()
                break

        elif choice == '13':
            if 'maneuvering_attack' in dict:
                print("Manuever already known")
                continue
            else:
                dnd_features.maneuvering_attack()
                break

        elif choice == '14':
            if 'menacing_attack' in dict:
                print("Manuever already known")
                continue
            else:
                dnd_features.menacing_attack()
                break

        elif choice == '15':
            if 'parry' in dict:
                print("Manuever already known")
                continue
            else:
                dnd_features.parry()
                break

        elif choice == '16':
            if 'precision_attack' in dict:
                print("Manuever already known")
                continue
            else:
                dnd_features.precision_attack()
                break

        elif choice == '17':
            if 'pushing_attack' in dict:
                print("Manuever already known")
                continue
            else:
                dnd_features.pushing_attack()
                break

        elif choice == '18':
            if 'quick_toss' in dict:
                print("Manuever already known")
                continue
            else:
                dnd_features.quick_toss()
                break

        elif choice == '19':
            if 'rally' in dict:
                print("Manuever already known")
                continue
            else:
                dnd_features.rally()
                break

        elif choice == '20':
            if 'riposte' in dict:
                print("Manuever already known")
                continue
            else:
                dnd_features.riposte()
                break

        elif choice == '21':
            if 'sweeping_attack' in dict:
                print("Manuever already known")
                continue
            else:
                dnd_features.sweeping_attack()
                break

        elif choice == '22':
            if 'tactical_assessment' in dict:
                print("Manuever already known")
                continue
            else:
                dnd_features.tactical_assessment()
                break

        elif choice == '23':
            if 'trip_attack' in dict:
                print("Manuever already known")
                continue
            else:
                dnd_features.trip_attack()
                break

        else:
            print("Error: Invalid Input")
            continue


def maneuver_choice():
    while True:
        choice = input("""Do you want to swap out a maneuver?
1) Yes
2) No
Enter your selection: """)
        if choice == '1':
            dnd_skills.maneuver_swap(dnd_dict.character_dict['maneuvers']['types'],dnd_dict.character_dict['features'])
            maneuvers()
            break
        elif choice == '2':
            break
        else:
            print("Error: Invalid Input")
            continue












