import dnd_dict, dnd_features, dnd_skills

def level_req(level):
    if dnd_dict.character_dict['total_level'] >= level:
        return True

def elemental_discipline():
    dict = dnd_dict.character_dict['elemental_disciplines']
    while True:
        choice = input("""Select the elemental discipline you want:
1) Breath of Winter (must be at least level 17)
2) Clench of the North Wind (must be at least level 6)
3) Elemental Attunement
4) Eternal Mountain Defense (must be at least level 17)
5) Fangs of the Fire Snake
6) Fist of Four Thunders
7) Fist of Unbroken Air
8) Flames of the Phoenix (must be at least level 11)
9) Gong of the Summit (must be at least level 6)
10) Mist Stance (must be at least level 11)
11) Ride the Wind (must be at least level 11)
12) River of Hungry Flame (must be at least level 17)
13) Rush of the Gale Spirits
14) Shape of Flowing River
15) Sweeping Cinder Strike
16) Water Whip
17) Wave of Rolling Earth (must be at least level 17)
Enter your selection: """)
        if choice == '1':
            if 'breath_of_winter' in dict:
                print("Elemental Discipline already known")
                continue
            elif level_req(17):
                dnd_features.breath_of_winter()
                break
            else:
                print("Error: You must be at least level 17 to learn this Elemental Discipline")
                continue

        elif choice == '2':
            if 'clench_of_the_north_wind' in dict:
                print("Elemental Discipline already known")
                continue
            elif level_req(6):
                dnd_features.clench_of_the_north_wind()
                break
            else:
                print("Error: You must be at least level 6 to learn this Elemental Discipline")
                continue

        elif choice == '3':
            if 'elemental_attunement' in dict:
                print("Elemental Discipline already known")
                continue
            elif level_req(1):
                dnd_features.elemental_attunement()
                break
            else:
                print("Error: You must be at least level 1 to learn this Elemental Discipline")
                continue

        elif choice == '4':
            if 'eternal_mountain_defense' in dict:
                print("Elemental Discipline already known")
                continue
            elif level_req(17):
                dnd_features.eternal_mountain_defense()
                break
            else:
                print("Error: You must be at least level 17 to learn this Elemental Discipline")
                continue

        elif choice == '5':
            if 'fangs_of_the_fire_snake' in dict:
                print("Elemental Discipline already known")
                continue
            elif level_req(1):
                dnd_features.fangs_of_the_fire_snake()
                break
            else:
                print("Error: You must be at least level 1 to learn this Elemental Discipline")
                continue

        elif choice == '6':
            if 'fist_of_four_thunders' in dict:
                print("Elemental Discipline already known")
                continue
            elif level_req(1):
                dnd_features.fist_of_four_thunders()
                break
            else:
                print("Error: You must be at least level 1 to learn this Elemental Discipline")
                continue

        elif choice == '7':
            if 'fist_of_unbroken_air' in dict:
                print("Elemental Discipline already known")
                continue
            elif level_req(1):
                dnd_features.fist_of_unbroken_air()
                break
            else:
                print("Error: You must be at least level 1 to learn this Elemental Discipline")
                continue

        elif choice == '8':
            if 'flames_of_the_phoenix' in dict:
                print("Elemental Discipline already known")
                continue
            elif level_req(11):
                dnd_features.flames_of_the_phoenix()
                break
            else:
                print("Error: You must be at least level 11 to learn this Elemental Discipline")
                continue

        elif choice == '9':
            if 'gong_of_the_summit' in dict:
                print("Elemental Discipline already known")
                continue
            elif level_req(6):
                dnd_features.gong_of_the_summit()
                break
            else:
                print("Error: You must be at least level 6 to learn this Elemental Discipline")
                continue

        elif choice == '10':
            if 'mist_stance' in dict:
                print("Elemental Discipline already known")
                continue
            elif level_req(11):
                dnd_features.mist_stance()
                break
            else:
                print("Error: You must be at least level 11 to learn this Elemental Discipline")
                continue

        elif choice == '11':
            if 'ride_the_wind' in dict:
                print("Elemental Discipline already known")
                continue
            elif level_req(11):
                dnd_features.ride_the_wind()
                break
            else:
                print("Error: You must be at least level 11 to learn this Elemental Discipline")
                continue

        elif choice == '12':
            if 'river_of_hungry_flame' in dict:
                print("Elemental Discipline already known")
                continue
            elif level_req(17):
                dnd_features.river_of_hungry_flame()
                break
            else:
                print("Error: You must be at least level 17 to learn this Elemental Discipline")
                continue

        elif choice == '13':
            if 'rush_of_the_gale_spirits' in dict:
                print("Elemental Discipline already known")
                continue
            elif level_req(1):
                dnd_features.rush_of_the_gale_spirits()
                break
            else:
                print("Error: You must be at least level 1 to learn this Elemental Discipline")
                continue

        elif choice == '14':
            if 'shape_the_flowing_river' in dict:
                print("Elemental Discipline already known")
                continue
            elif level_req(1):
                dnd_features.shape_the_flowing_river()
                break
            else:
                print("Error: You must be at least level 1 to learn this Elemental Discipline")
                continue

        elif choice == '15':
            if 'sweeping_cinder_strike' in dict:
                print("Elemental Discipline already known")
                continue
            elif level_req(1):
                dnd_features.sweeping_cinder_strike()
                break
            else:
                print("Error: You must be at least level 1 to learn this Elemental Discipline")
                continue

        elif choice == '16':
            if 'water_whip' in dict:
                print("Elemental Discipline already known")
                continue
            elif level_req(1):
                dnd_features.water_whip()
                break
            else:
                print("Error: You must be at least level 1 to learn this Elemental Discipline")
                continue

        elif choice == '17':
            if 'wave_of_rolling_earth' in dict:
                print("Elemental Discipline already known")
                continue
            elif level_req(17):
                dnd_features.wave_of_rolling_earth()
                break
            else:
                print("Error: You must be at least level 17 to learn this Elemental Discipline")
                continue

        else:
            print("Error: Invalid Input")
            continue


def discipline_swap():
    if dnd_dict.character_dict['player_class']['monk']['subclass'] == 'Way of the Four Elements':
        while True:
            choice = input("""Do you want to swap an Elemental Discipline?
1) Yes
2) No
Enter your selection: """)
            if choice == '1':
                dnd_skills.maneuver_swap(dnd_dict.character_dict['elemental_disciplines'],dnd_dict.character_dict['features'])
                elemental_discipline()
                break 

            elif choice == '2':
                break 

            else:
                print("Error: Invalid Input")
                continue
















