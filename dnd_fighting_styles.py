import dnd_dict, dnd_skills, dnd_features, dnd_maneuvers


def fighter_fighting_styles():
    while True:
        choice = input("""Select the fighting style you want to learn:
Fighting Style

You adopt a particular style of fighting as your specialty. Choose one of the following options. You can't take a Fighting Style option more than once, even if you later get to choose again. Make your selection:

1) Archery. You gain a +2 bonus to attack rolls you make with ranged weapons.

2) Blind Fighting. You have blindsight with a range of 10 feet. Within that range, you can effectively see anything that isn't behind total cover, even if you're blinded or in darkness. Moreover, you can see an invisible creature within that range, unless the creature successfully hides from you.

3) Defense. While you are wearing armor, you gain a +1 bonus to AC.

4) Dueling. When you are wielding a melee weapon in one hand and no other weapons, you gain a +2 bonus to damage rolls with that weapon.

5) Great Weapon Fighting. When you roll a 1 or 2 on a damage die for an attack you make with a melee weapon that you are wielding with two hands, you can reroll the die and must use the new roll, even if the new roll is a 1 or a 2. The weapon must have the two-handed or versatile property for you to gain this benefit.

6) Interception. When a creature you can see hits a target, other than you, within 5 feet of you with an attack, you can use your reaction to reduce the damage the target takes by 1d10 + your proficiency bonus (to a minimum of 0 damage). You must be wielding a shield or a simple or martial weapon to use this reaction.

7) Protection. When a creature you can see attacks a target other than you that is within 5 feet of you, you can use your reaction to impose disadvantage on the attack roll. You must be wielding a shield.

8) Superior Technique. You learn one maneuver of your choice from among those available to the Battle Master archetype. If a maneuver you use requires your target to make a saving throw to resist the maneuver's effects, the saving throw DC equals 8 + your proficiency bonus + your Strength or Dexterity modifier (your choice.)
    You gain one superiority die, which is a d6 (this die is added to any superiority dice you have from another source). This die is used to fuel your maneuvers. A superiority die is expended when you use it. You regain your expended superiority dice when you finish a short or long rest.

9) Thrown Weapon Fighting. You can draw a weapon that has the thrown property as part of the attack you make with the weapon.
    In addition, when you hit with a ranged attack using a thrown weapon, you gain a +2 bonus to the damage roll.

10) Two-Weapon Fighting. When you engage in two-weapon fighting, you can add your ability modifier to the damage of the second attack.

11) Unarmed Fighting. Your unarmed strikes can deal bludgeoning damage equal to 1d6 + your Strength modifier on a hit. If you aren't wielding any weapons or a shield when you make the attack roll, the d6 becomes a d8.
    At the start of each of your turns, you can deal 1d4 bludgeoning damage to one creature grappled by you.
Enter your selection: """)

        if choice == '1':
            if 'archery_fighting_style' in dnd_dict.character_dict['features']:
                print("Fighting Style already known")
                continue
            else:
                dnd_features.archery(dnd_dict.character_dict['fighter_fighting_styles'])
                break

        elif choice == '2':
            if 'blind_fighting_fighting_style' in dnd_dict.character_dict['features']:
                print("Fighting Style already known")
                continue
            else:
                dnd_features.blind_fighting(dnd_dict.character_dict['fighter_fighting_styles'])
                break

        elif choice == '3':
            if 'defense_fighting_style' in dnd_dict.character_dict['features']:
                print("Fighting Style already known")
                continue
            else:
                dnd_features.defense(dnd_dict.character_dict['fighter_fighting_styles'])
                break

        elif choice == '4':
            if 'dueling_fighting_style' in dnd_dict.character_dict['features']:
                print("Fighting Style already known")
                continue
            else:
                dnd_features.dueling(dnd_dict.character_dict['fighter_fighting_styles'])
                break

        elif choice == '5':
            if 'great_weapon_fighting_fighting_style' in dnd_dict.character_dict['features']:
                print("Fighting Style already known")
                continue
            else:
                dnd_features.great_weapon_fighting(dnd_dict.character_dict['fighter_fighting_styles'])
                break

        elif choice == '6':
            if 'interception_fighting_style' in dnd_dict.character_dict['features']:
                print("Fighting Style already known")
                continue
            else:
                dnd_features.interception(dnd_dict.character_dict['fighter_fighting_styles'])
                break

        elif choice == '7':
            if 'protection_fighting_style' in dnd_dict.character_dict['features']:
                print("Fighting Style already known")
                continue
            else:
                dnd_features.protection(dnd_dict.character_dict['fighter_fighting_styles'])
                break

        elif choice == '8':
            if 'superior_technique_fighting_style' in dnd_dict.character_dict['features']:
                print("Fighting Style already known")
                continue
            else:
                dnd_features.superior_technique(dnd_dict.character_dict['fighter_fighting_styles'])
                break

        elif choice == '9':
            if 'thrown_weapon_fighting_fighting_style' in dnd_dict.character_dict['features']:
                print("Fighting Style already known")
                continue
            else:
                dnd_features.thrown_weapon_fighting(dnd_dict.character_dict['fighter_fighting_styles'])
                break

        elif choice == '10':
            if 'two_weapon_fighting_style' in dnd_dict.character_dict['features']:
                print("Fighting Style already known")
                continue
            else:
                dnd_features.two_weapon_fighting(dnd_dict.character_dict['fighter_fighting_styles'])
                break

        elif choice == '11':
            if 'unarmed_fighting_fighting_style' in dnd_dict.character_dict['features']:
                print("Fighting Style already known")
                continue
            else:
                dnd_features.unarmed_fighting(dnd_dict.character_dict['fighter_fighting_styles'])
                break

        else:
            print("Error: Invalid Input")
            continue


def paladin_fighting_styles():
    while True:
        choice = input("""Fighting Style

Starting at 2nd level, you adopt a particular style of fighting as your specialty. Choose one of the following options. You can't take a Fighting Style option more than once, even if you later get to choose again.

1) Blessed Warrior. You learn two cantrips of your choice from the cleric spell list. They count as paladin spells for you, and Charisma is your spellcasting ability for them. Whenever you gain a level in this class, you can replace one of these cantrips with another cantrip from the cleric spell list.

2) Blind Fighting. You have blindsight with a range of 10 feet. Within that range, you can effectively see anything that isn't behind total cover, even if you're blinded or in darkness. Moreover, you can see an invisible creature within that range, unless the creature successfully hides from you.

3) Defense. While you are wearing armor, you gain a +1 bonus to AC.

4) Dueling. When you are wielding a melee weapon in one hand and no other weapons, you gain a +2 bonus to damage rolls with that weapon.

5) Great Weapon Fighting. When you roll a 1 or 2 on a damage die for an attack you make with a melee weapon that you are wielding with two hands, you can reroll the die and must use the new roll, even if the new roll is a 1 or a 2. The weapon must have the two-handed or versatile property for you to gain this benefit.

6) Interception. When a creature you can see hits a target, other than you, within 5 feet of you with an attack, you can use your reaction to reduce the damage the target takes by 1d10 + your proficiency bonus (to a minimum of 0 damage). You must be wielding a shield or a simple or martial weapon to use this reaction.

7) Protection. When a creature you can see attacks a target other than you that is within 5 feet of you, you can use your reaction to impose disadvantage on the attack roll. You must be wielding a shield.
Enter your selection: """)

        if choice == '1':
            if 'blessed_warrior_fighting_style' in dnd_dict.character_dict['features']:
                print("Fighting Style already known")
                continue
            else:
                dnd_features.blessed_warrior(dnd_dict.character_dict['paladin_fighting_styles'])
                break

        elif choice == '2':
            if 'blind_fighting_fighting_style' in dnd_dict.character_dict['features']:
                print("Fighting Style already known")
                continue
            else:
                dnd_features.blind_fighting(dnd_dict.character_dict['paladin_fighting_styles'])
                break

        elif choice == '3':
            if 'defense_fighting_style' in dnd_dict.character_dict['features']:
                print("Fighting Style already known")
                continue
            else:
                dnd_features.defense(dnd_dict.character_dict['paladin_fighting_styles'])
                break

        elif choice == '4':
            if 'dueling_fighting_style' in dnd_dict.character_dict['features']:
                print("Fighting Style already known")
                continue
            else:
                dnd_features.dueling(dnd_dict.character_dict['paladin_fighting_styles'])
                break

        elif choice == '5':
            if 'great_weapon_fighting_fighting_style' in dnd_dict.character_dict['features']:
                print("Fighting Style already known")
                continue
            else:
                dnd_features.great_weapon_fighting(dnd_dict.character_dict['paladin_fighting_styles'])
                break

        elif choice == '6':
            if 'interception_fighting_style' in dnd_dict.character_dict['features']:
                print("Fighting Style already known")
                continue
            else:
                dnd_features.interception(dnd_dict.character_dict['paladin_fighting_styles'])
                break

        elif choice == '7':
            if 'protection_fighting_style' in dnd_dict.character_dict['features']:
                print("Fighting Style already known")
                continue
            else:
                dnd_features.protection(dnd_dict.character_dict['paladin_fighting_styles'])
                break

        else:
            print("Error: Invalid Input")
            continue

def ranger_fighting_styles():
    while True:
        choice = input("""Fighting Style

At 2nd level, you adopt a particular style of fighting as your specialty. Choose one of the following options. You can't take a Fighting Style option more than once, even if you later get to choose again.

1) Archery. You gain a +2 bonus to attack rolls you make with ranged weapons.

2) Blind Fighting. You have blind sight with a range of 10 feet. Within that range, you can effectively see anything that isn't behind total cover, even if you're blinded or in darkness. Moreover, you can see an invisible creature within that range, unless the creature successfully hides from you.

3) Defense. While you are wearing armor, you gain a +1 bonus to AC.

4) Druidic Warrior. You learn two cantrips of your choice from the Druid spell list. They count as ranger spells for you, and Wisdom is your spellcasting ability for them. Whenever you gain a level in this class, you can replace one of these cantrips with another cantrip from the Druid spell list.

5) Dueling. When you are wielding a melee weapon in one hand and no other weapons, you gain a +2 bonus to damage rolls with that weapon.

6) Thrown Weapon Fighting. You can draw a weapon that has the thrown property as part of the attack you make with the weapon.
    In addition, when you hit with a ranged attack using a thrown weapon, you gain a +2 bonus to the damage roll.

7) Two-Weapon Fighting. When you engage in two-weapon fighting, you can add your ability modifier to the damage of the second attack.
Enter your selection: """)


        if choice == '1':
            if 'archery_fighting_style' in dnd_dict.character_dict['features']:
                print("Fighting Style already known")
                continue
            else:
                dnd_features.archery(dnd_dict.character_dict['ranger_fighting_styles'])
                break

        elif choice == '2':
            if 'blind_fighting_fighting_style' in dnd_dict.character_dict['features']:
                print("Fighting Style already known")
                continue
            else:
                dnd_features.blind_fighting(dnd_dict.character_dict['ranger_fighting_styles'])
                break

        elif choice == '3':
            if 'defense_fighting_style' in dnd_dict.character_dict['features']:
                print("Fighting Style already known")
                continue
            else:
                dnd_features.defense(dnd_dict.character_dict['ranger_fighting_styles'])
                break

        elif choice == '4':
            if 'druidic_warrior_fighting_style' in dnd_dict.character_dict['features']:
                print("Fighting Style already known")
                continue
            else:
                dnd_features.druidic_warrior(dnd_dict.character_dict['ranger_fighting_styles'])
                break

        elif choice == '5':
            if 'dueling_fighting_style' in dnd_dict.character_dict['features']:
                print("Fighting Style already known")
                continue
            else:
                dnd_features.dueling(dnd_dict.character_dict['ranger_fighting_styles'])
                break

        elif choice == '6':
            if 'thrown_weapon_fighting_fighting_style' in dnd_dict.character_dict['features']:
                print("Fighting Style already known")
                continue
            else:
                dnd_features.thrown_weapon_fighting(dnd_dict.character_dict['ranger_fighting_styles'])
                break

        elif choice == '7':
            if 'two_weapon_fighting_style' in dnd_dict.character_dict['features']:
                print("Fighting Style already known")
                continue
            else:
                dnd_features.two_weapon_fighting(dnd_dict.character_dict['ranger_fighting_styles'])
                break

        else:
            print("Error: Invalid Input")
            continue

def fighting_initiate_fighting_styles():
    while True:
        choice = input("""Select the fighting style you want to learn:
Fighting Style

You adopt a particular style of fighting as your specialty. Choose one of the following options. You can't take a Fighting Style option more than once, even if you later get to choose again. Make your selection:

1) Archery. You gain a +2 bonus to attack rolls you make with ranged weapons.

2) Blind Fighting. You have blindsight with a range of 10 feet. Within that range, you can effectively see anything that isn't behind total cover, even if you're blinded or in darkness. Moreover, you can see an invisible creature within that range, unless the creature successfully hides from you.

3) Defense. While you are wearing armor, you gain a +1 bonus to AC.

4) Dueling. When you are wielding a melee weapon in one hand and no other weapons, you gain a +2 bonus to damage rolls with that weapon.

5) Great Weapon Fighting. When you roll a 1 or 2 on a damage die for an attack you make with a melee weapon that you are wielding with two hands, you can reroll the die and must use the new roll, even if the new roll is a 1 or a 2. The weapon must have the two-handed or versatile property for you to gain this benefit.

6) Interception. When a creature you can see hits a target, other than you, within 5 feet of you with an attack, you can use your reaction to reduce the damage the target takes by 1d10 + your proficiency bonus (to a minimum of 0 damage). You must be wielding a shield or a simple or martial weapon to use this reaction.

7) Protection. When a creature you can see attacks a target other than you that is within 5 feet of you, you can use your reaction to impose disadvantage on the attack roll. You must be wielding a shield.

8) Superior Technique. You learn one maneuver of your choice from among those available to the Battle Master archetype. If a maneuver you use requires your target to make a saving throw to resist the maneuver's effects, the saving throw DC equals 8 + your proficiency bonus + your Strength or Dexterity modifier (your choice.)
    You gain one superiority die, which is a d6 (this die is added to any superiority dice you have from another source). This die is used to fuel your maneuvers. A superiority die is expended when you use it. You regain your expended superiority dice when you finish a short or long rest.

9) Thrown Weapon Fighting. You can draw a weapon that has the thrown property as part of the attack you make with the weapon.
    In addition, when you hit with a ranged attack using a thrown weapon, you gain a +2 bonus to the damage roll.

10) Two-Weapon Fighting. When you engage in two-weapon fighting, you can add your ability modifier to the damage of the second attack.

11) Unarmed Fighting. Your unarmed strikes can deal bludgeoning damage equal to 1d6 + your Strength modifier on a hit. If you aren't wielding any weapons or a shield when you make the attack roll, the d6 becomes a d8.
    At the start of each of your turns, you can deal 1d4 bludgeoning damage to one creature grappled by you.
Enter your selection: """)

        if choice == '1':
            if 'archery_fighting_style' in dnd_dict.character_dict['features']:
                print("Fighting Style already known")
                continue
            else:
                dnd_features.archery(dnd_dict.character_dict['special_fighting_styles'])
                break

        elif choice == '2':
            if 'blind_fighting_fighting_style' in dnd_dict.character_dict['features']:
                print("Fighting Style already known")
                continue
            else:
                dnd_features.blind_fighting(dnd_dict.character_dict['special_fighting_styles'])
                break

        elif choice == '3':
            if 'defense_fighting_style' in dnd_dict.character_dict['features']:
                print("Fighting Style already known")
                continue
            else:
                dnd_features.defense(dnd_dict.character_dict['special_fighting_styles'])
                break

        elif choice == '4':
            if 'dueling_fighting_style' in dnd_dict.character_dict['features']:
                print("Fighting Style already known")
                continue
            else:
                dnd_features.dueling(dnd_dict.character_dict['special_fighting_styles'])
                break

        elif choice == '5':
            if 'great_weapon_fighting_fighting_style' in dnd_dict.character_dict['features']:
                print("Fighting Style already known")
                continue
            else:
                dnd_features.great_weapon_fighting(dnd_dict.character_dict['special_fighting_styles'])
                break

        elif choice == '6':
            if 'interception_fighting_style' in dnd_dict.character_dict['features']:
                print("Fighting Style already known")
                continue
            else:
                dnd_features.interception(dnd_dict.character_dict['special_fighting_styles'])
                break

        elif choice == '7':
            if 'protection_fighting_style' in dnd_dict.character_dict['features']:
                print("Fighting Style already known")
                continue
            else:
                dnd_features.protection(dnd_dict.character_dict['special_fighting_styles'])
                break

        elif choice == '8':
            if 'superior_technique_fighting_style' in dnd_dict.character_dict['features']:
                print("Fighting Style already known")
                continue
            else:
                dnd_features.superior_technique(dnd_dict.character_dict['special_fighting_styles'])
                break

        elif choice == '9':
            if 'thrown_weapon_fighting_fighting_style' in dnd_dict.character_dict['features']:
                print("Fighting Style already known")
                continue
            else:
                dnd_features.thrown_weapon_fighting(dnd_dict.character_dict['special_fighting_styles'])
                break

        elif choice == '10':
            if 'two_weapon_fighting_style' in dnd_dict.character_dict['features']:
                print("Fighting Style already known")
                continue
            else:
                dnd_features.two_weapon_fighting(dnd_dict.character_dict['special_fighting_styles'])
                break

        elif choice == '11':
            if 'unarmed_fighting_fighting_style' in dnd_dict.character_dict['features']:
                print("Fighting Style already known")
                continue
            else:
                dnd_features.unarmed_fighting(dnd_dict.character_dict['special_fighting_styles'])
                break

        else:
            print("Error: Invalid Input")
            continue


# Used for Paladin or Ranger's Martial Versatility
def martial_versatility_style_paladin():
    while True:
        choice = input("""Do you want to swap out a Fighting Style:
1) Yes
2) No
Enter your selection: """)
        if choice == '1':
            dnd_skills.fighting_style_swap(dnd_dict.character_dict['paladin_fighting_styles'],dnd_dict.character_dict['features'])
            paladin_fighting_styles()
            break

        elif choice == '2':
            break

        else:
            print("Error: Invalid Selection")
            continue


# Used for  Ranger's Martial Versatility
def martial_versatility_style_ranger():
    while True:
        choice = input("""Do you want to swap out a Fighting Style:
1) Yes
2) No
Enter your selection: """)
        if choice == '1':
            dnd_skills.fighting_style_swap(dnd_dict.character_dict['ranger_fighting_styles'],dnd_dict.character_dict['features'])
            ranger_fighting_styles()
            break

        elif choice == '2':
            break

        else:
            print("Error: Invalid Selection")
            continue



# Used for Fighter's Martial Versatility
def martial_versatility_style_fighter():
    while True:
        choice = input("""Do you want to swap out a Fighting Style or (if possible) a Manuever?
1) Fighting Style
2) Manuever
0) No
Enter your choice: """)
        if choice == '1':
            dnd_skills.fighting_style_swap(dnd_dict.character_dict['fighter_fighting_styles'],dnd_dict.character_dict['features'])
            fighter_fighting_styles()
            break
        elif choice == '2':
            if dnd_dict.character_dict['maneuvers']['types']:
                dnd_skills.maneuver_swap(dnd_dict.character_dict['maneuvers']['types'],features)
                dnd_maneuvers.maneuvers()
                break
            else:
                print("Error: You do not have any maneuvers.")
                continue
        elif choice == '0':
            break
        else:
            print("Error: Invalid Input")
            continue


# Used for Fighter Initiate's Martial Versatility
def martial_versatility_style_fighting_initiate():
    if 'fighting_initiate' in dnd_dict.character_dict['feats']:
        while True:
            choice = input("""Do you want to swap out a Fighting Style or (if possible) a Manuever?
1) Fighting Style
2) No
Enter your choice: """)
            if choice == '1':
                dnd_skills.fighting_style_swap(dnd_dict.character_dict['fighter_fighting_styles'],dnd_dict.character_dict['features'])
                fighting_initiate_fighting_styles()
                break
            elif choice == '2':
                break
            else:
                print("Error: Invalid Input")
                continue

