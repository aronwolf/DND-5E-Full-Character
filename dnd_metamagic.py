import dnd_dict, dnd_features, dnd_skills



def metamagic():
    dict = dnd_dict.character_dict['features']
    meta_dict = dnd_dict.character_dict['metamagic']
    while True:
        choice = input("""Select the Metamagic option you want:
1) Careful Spell
2) Distant Spell
3) Empowered Spell
4) Extended Spell
5) Heightened Spell
6) Quickened Spell
7) Seeking Spell
8) Subtle Spell
9) Transmuted Spell
10) Twinned Spell
Enter your selection: """)
        if choice == '1':
            if 'careful_spell' in dict:
                print("Metamagic option already known.")
                continue
            else:
                dnd_features.careful_spell()
                meta_dict['careful_spell'] = 'Careful Spell'
                break

        elif choice == '2':
            if 'distant_spell' in dict:
                print("Metamagic option already known.")
                continue
            else:
                dnd_features.distant_spell()
                meta_dict['distant_spell'] = 'Distant Spell'
                break

        elif choice == '3':
            if 'empowered_spell' in dict:
                print("Metamagic option already known.")
                continue
            else:
                dnd_features.empowered_spell()
                meta_dict['empowered_spell'] = 'Empowered Spell'
                break


        elif choice == '4':
            if 'extended_spell' in dict:
                print("Metamagic option already known.")
                continue
            else:
                dnd_features.extended_spell()
                meta_dict['extended_spell'] = 'Extended Spell'
                break

        elif choice == '5':
            if 'heightened_spell' in dict:
                print("Metamagic option already known.")
                continue
            else:
                dnd_features.heightened_spell()
                meta_dict['heightened_spell'] = 'Heightened Spell'
                break

        elif choice == '6':
            if 'quickened_spell' in dict:
                print("Metamagic option already known.")
                continue
            else:
                dnd_features.quickened_spell()
                meta_dict['quickened_spell'] = 'Quickened Spell'
                break

        elif choice == '7':
            if 'seeking_spell' in dict:
                print("Metamagic option already known.")
                continue
            else:
                dnd_features.seeking_spell()
                meta_dict['seeking_spell'] = 'Seeking Spell'
                break

        elif choice == '8':
            if 'subtle_spell' in dict:
                print("Metamagic option already known.")
                continue
            else:
                dnd_features.subtle_spell()
                meta_dict['subtle_spell'] = 'Subtle Spell'
                break

        elif choice == '9':
            if 'transmuted_spell' in dict:
                print("Metamagic option already known.")
                continue
            else:
                dnd_features.transmuted_spell()
                meta_dict['transmuted_spell'] = 'Transmuted Spell'
                break

        elif choice == '10':
            if 'twinned_spell' in dict:
                print("Metamagic option already known.")
                continue
            else:
                dnd_features.twinned_spell()
                meta_dict['twinned_spell'] = 'Twinned Spell'
                break

        else:
            print("Error: Invalid Input")
            continue

def metamagic_adept_choice():
    dict = dnd_dict.character_dict['features']
    meta_dict = dnd_dict.character_dict['metamagic_adept']
    while True:
        choice = input("""Select the Metamagic option you want:
1) Careful Spell
2) Distant Spell
3) Empowered Spell
4) Extended Spell
5) Heightened Spell
6) Quickened Spell
7) Seeking Spell
8) Subtle Spell
9) Transmuted Spell
10) Twinned Spell
Enter your selection: """)
        if choice == '1':
            if 'careful_spell' in dict:
                print("Metamagic option already known.")
                continue
            else:
                dnd_features.careful_spell()
                meta_dict['careful_spell'] = 'Careful Spell'
                break

        elif choice == '2':
            if 'distant_spell' in dict:
                print("Metamagic option already known.")
                continue
            else:
                dnd_features.distant_spell()
                meta_dict['distant_spell'] = 'Distant Spell'
                break

        elif choice == '3':
            if 'empowered_spell' in dict:
                print("Metamagic option already known.")
                continue
            else:
                dnd_features.empowered_spell()
                meta_dict['empowered_spell'] = 'Empowered Spell'
                break


        elif choice == '4':
            if 'extended_spell' in dict:
                print("Metamagic option already known.")
                continue
            else:
                dnd_features.extended_spell()
                meta_dict['extended_spell'] = 'Extended Spell'
                break

        elif choice == '5':
            if 'heightened_spell' in dict:
                print("Metamagic option already known.")
                continue
            else:
                dnd_features.heightened_spell()
                meta_dict['heightened_spell'] = 'Heightened Spell'
                break

        elif choice == '6':
            if 'quickened_spell' in dict:
                print("Metamagic option already known.")
                continue
            else:
                dnd_features.quickened_spell()
                meta_dict['quickened_spell'] = 'Quickened Spell'
                break

        elif choice == '7':
            if 'seeking_spell' in dict:
                print("Metamagic option already known.")
                continue
            else:
                dnd_features.seeking_spell()
                meta_dict['seeking_spell'] = 'Seeking Spell'
                break

        elif choice == '8':
            if 'subtle_spell' in dict:
                print("Metamagic option already known.")
                continue
            else:
                dnd_features.subtle_spell()
                meta_dict['subtle_spell'] = 'Subtle Spell'
                break

        elif choice == '9':
            if 'transmuted_spell' in dict:
                print("Metamagic option already known.")
                continue
            else:
                dnd_features.transmuted_spell()
                meta_dict['transmuted_spell'] = 'Transmuted Spell'
                break

        elif choice == '10':
            if 'twinned_spell' in dict:
                print("Metamagic option already known.")
                continue
            else:
                dnd_features.twinned_spell()
                meta_dict['twinned_spell'] = 'Twinned Spell'
                break

        else:
            print("Error: Invalid Input")
            continue


def first_metamagic():
    x = 1
    for x in range (x,3):
        if x < 3:
            print(f'{x}/2')
            metamagic()
            x+=1
            continue

        elif x == 3:
            break

# Used for changing Metamagic Adept options
def metamagic_adept_swap():
    if 'metamagic_adept' in dnd_dict.character_dict['feats']:
        while True:
            choice = input("""Do you want to replace a Metamagic Option:
1) Yes
2) No
Enter your selection: """)
            if choice == '1':
                dnd_skills.maneuver_swap(dnd_dict.character_dict['metamagic_adept'],dnd_dict.character_dict['features'])
                dnd_metamagic.metamagic_adept_choice()
                break

            elif choice == '2':
                break
    
            else:
                print("Error: Invalid Input")
                continue







