#!/usr/bin/python3
from __future__ import print_function
import os, math, re

class Character:
    def __init__(self, stat,skill,bonus):
        self.stat = stat
        self.bonus = bonus
        self.skill = skill
        self.dict1 = dict1
        self.dict2 = dict2


# Determines the initial stats of the character.
# Only accepts integers
# Must be between 3 and 18
    def initial_stat(stat_type):
        while True:
            try:
                stat = int(input(f'Enter your {stat_type}: '))
                if stat > 2 and stat < 19:
                    break
                else:
                    print("Invalid Input. Must Be An Integer Between 3 and 18")
            except ValueError:
                print("Invalid Input Enter an Integer")
        return stat

# Used to determine the modifiers, +1 for every even above 10, -1 for every odd below 10. A score of 10 is a +0 modifier.
    def mod(stat):
        count = 0
        if stat == 10:
            count = 0
            return count

#Add 1 to the modifier for every even number above 10
        elif stat > 10:
            stat_range = range(11, stat, 2)
            count += len(stat_range)
            return count

#Subtract 1 from the modifier for every odd number below 10.
        elif stat < 10:
            stat_range = range(11, stat, -2)
            count -= len(stat_range)
            return count


# Used to determine skill proficiency. If you are already proficient, then it
# does not add the bonus again
    def skill_prof(skill,bonus, stat):
        if skill == (stat+bonus):
            print(f'You are already proficient with {skill}')
            return False
        else:
            skill == (stat+bonus)
            return



# Used to display skill scores.
# If you are proficient in a skill, put a (*) before it.
# If you have expertise because of the Rogue feature, put an E before that as well
# Otherwise, just put the modifier.
#    def show_prof(skill, bonus, stat):
#        if skill == (stat+bonus):
#            vals = f"(*) {skill}"
#            return vals
#        elif skill == (stat + bonus + bonus):
#            vals = f"(E)(*) {skill}"
#            return vals
#        else:
#            return skill

# Used to display skill scores.
# If you are proficient in a skill, put a (*) before it.
# If you have expertise because of the Rogue feature, put an E before that as well
    def show_prof(value, skill, dict1, dict2):
        if skill in dict1:
            vals = f"(E)(*) {value}"
            return vals

        elif skill in dict2:
            vals = f"(*) {value}"
            return vals
        else:
            return value

#Determines the stat bonuses the different races give.
class RaceStats:
    def __init__(self, race, speed, size, stat, language, bonus, skill, base, full_dict, chosen_class, dice):
        self.race = race
        self.speed = speed
        self.size = size
        self.stat = stat
        self.language = language
        self.bonus = bonus
        self.skill = skill
        self.base = base
        self.full_dict = full_dict
        self.chosen_class = chosen_class
        self.dice = dice

#Prints the race name, speed, size, and language.
    def racial_choice(race, speed, size):
        print(f'Race: {race}')
        print(f'Speed: {speed} feet')
        print(f'Your size is: {size}')



#Method for calculating the stat bonuses
    def stat_bonus(stat, bonus):
        return (stat + bonus)


# Used to display Hit Dice. If there are none, then do not display them
# Tabbed for ease of reading in case more are ever added.
    def hit_dice_display(full_dict,stat):
        if full_dict > 0:
            return print(f'Hit Dice: {full_dict}{stat}')

# Select the stat you want, from 8-15.
    def point_buy_selection(stat):
        while True:
            choice = int(input(f"{stat} Selection, please input the number you want (from 8-15): "))
            if choice >=8 and choice <=15:
                return choice
            else:
                print("Choice must be an integer between 8-15")
                continue

# Point Buy stat selection, where you have 27 points to distribute between the stats, which can be from 8-15 for all of them. The stat and cost are: 8:0, 9:1, 10:2, 11:3, 12:4, 13:5, 14:7, 15:9.
    def point_buy_cost(stat,base):
        if stat == 8:
            base = base-0
            return base

        elif stat == 9:
            base = base-1
            return base

        elif stat == 10:
            base = base-2
            return base

        elif stat == 11:
            base = base-3
            return base

        elif stat == 12:
            base = base-4
            return base

        elif stat == 13:
            base = base-5
            return base

        elif stat == 14:
            base = base-7
            return base

        elif stat == 15:
            base = base-9
            return base


# Determines and displays the Spell Spell Attack (Proficiency Bonus + Stat Modifier)
    def spell_attack(bonus, stat):
        return (bonus+stat)

# Determines and displays the Spell Save DC (8 + Proficiency Bonus + Stat Modifier) 
    def spell_save(bonus,stat):
        return (8+bonus+stat)

# If the person has a level in a class, display it. If they have a subclass, display that as well. If they don't have either, do not display anything.
    def class_display(chosen_class, stat, full_dict):
        if full_dict and stat > 0:
#            display = f"{stat}, {chosen_class}, {dict}"
            display = print("{} ({}), {}".format(chosen_class,full_dict,stat))
            return display
        elif stat > 0:
#            display = f"{stat}, {chosen_class}"
            display = print("{}, {}".format(chosen_class, stat))
            return display
        else:
            return

# If the warlock has a pact, print the class, patron, pact, and level.
# If the warlock is below level 3, just print the class, patron, and level.
# Otherwise, do not print anything
    def warlock_display(stat, full_dict, bonus):
        if bonus and stat > 0:
#            display = f"{stat}, {chosen_class}, {dict}"
            display = print("Warlock, {}, ({}) (Pact of the {})".format(stat,full_dict,bonus))
            return display
        elif stat > 0:
#            display = f"{stat}, {chosen_class}"
            display = print("Warlock, {}, {}".format(stat, full_dict))
            return display
        else:
            return



class EquipMod:
    def __init__(self, full_dict,key,value,count):
        self.full_dict = full_dict
        self.key = key
        self.value = value
        self.count = count

#    def add_equip(dict,key,value,count):
    def add_equip(full_dict,key,value):
#        if re.search('\d+$',key) in dict:
# Finds the key in the dictionary if it ends with integers, meaning there are more than 1.

#        new_key = re.findall(r'\d+$',key)
        split_key = re.split('(\d+$)',key)
#        if split_key[0] in dict:
        first_key = str(split_key[0])
#        if first_key in dict:
        x = re.compile(r'\w')
        m = x.match(first_key)
#        if m:
#        if re.match('\w*',first_key):
        for key in full_dict:
            if key in first_key:
                return print("Yes")
            else:
                return print("No")

#        if first_key in dict.keys():
#            return print("Yes")
#        else:
#            return print("No")


        return print(first_key)
#        matching_keys = [k for k in dict if re.match(r'\d+$',split_key[0])]
#        return print(matching_keys)
#        return print(matching_keys)
        if matching_keys:
            return print("Already in the dictionary")
        else:
            if int(split_key[1]) > 1:
                new_value = f'{value} (x{split_key[1]})'
                full_dict[key] = new_value
            else:
                full_dict[key] = value
##                new_int = str((int(split_key[1]) + 1))
#                new_int = str((int(split_key[1]) + count))
#    #            new_int = split_key[1]
#                key = split_key[0]
#                updated_key = f'{key}{new_int}'
## Makes the value the same as the digit on the end of the key. For example, three javelins would be javelin3: Javelin (x3)
#                new_value = f'{value} (x{new_int})'
#                dict[updated_key] = new_value
#
#            if new_key not in dict:
##                dict[key]=value
#                new_value = f'{value} (x{count})'
#                dict[key] = new_value
#
#
#
##        new_key = re.findall(r'\d+$',key)
#        regex = '\d+$'
#        new_key = [k for k in dict if re.findall(regex,k)]
##        return print(new_key)
## If they key ends in a digit, separate the digits, add 1 to it.
#        if new_key:
#            for new_thing in new_key:
#                split_key = re.split('(\d+$)',key)
##                new_int = str((int(split_key[1]) + 1))
#                new_int = str((int(split_key[1]) + count))
#    #            new_int = split_key[1]
#                key = split_key[0]
#                updated_key = f'{key}{new_int}'
## Makes the value the same as the digit on the end of the key. For example, three javelins would be javelin3: Javelin (x3)
#                new_value = f'{value} (x{new_int})'
#                dict[updated_key] = new_value
##                return print("FIRST")
##                return dict[updated_key] = new_value
#
#
## If there are not digits after the key in the dictionary, put '2' after the key and put (x2) after the value.
#        if not new_key:
##            split_key = re.split('(\d+$)',key)
##            new_int = str((split_key[1]))
#
##            new_key = str(key+'2')
##            new_value = f'{value} (x2)'
#
#            if count == 1:
#                dict[key]=value
#            else:
#                new_key = str(key+str(count))
#                new_value = f'{value} (x{count})'
#                dict[new_key] = new_value

#            new_key = str(key+str(count))
#            new_value = f'{value} (x{count})'
#            dict[new_key] = new_value

#            return dict[new_key] = new_value
#            return print("SECOND")

# If the key is not in the dictionary, put that and the value into it.
#        if key not in dict:
#            dict[key] = value



#            return dict[key] = value
#            return print("THIRD")
#        else:
#            new_dict = dict[key] = value
#            return print("FOURTH")
#            return new_dict



##        if re.search('\d+$',key) in dict:
#        new_key = re.findall(r'\d+$',key)
#        if new_key:
#            for new_thing in new_key:
#                split_key = re.split('(\d+$)',key)
#                new_int = str((int(split_key[1]) + 1))
#    #            new_int = split_key[1]
#                key = split_key[0]
#                updated_key = f'{key}{new_int}'
#                new_value = f'{value} (x{new_int})'
#                dict[updated_key] = new_value
##                return print("FIRST")
##                return dict[updated_key] = new_value
#        if not new_key:
#            split_key = re.split('(\d+$)',key)
##            new_int = str((split_key[1]))
#
#            new_key = str(key+'2')
#            new_value = f'{value} (x2)'
#            dict[new_key] = new_value
##            return dict[new_key] = new_value
##            return print("SECOND")
#        if key not in dict:
#            dict[key] = value
##            return dict[key] = value
##            return print("THIRD")
#        else:
#            new_dict = dict[key] = value
##            return print("FOURTH")
#            return new_dict


# Used for spell level ups
class Spells:
    def __init__(self,cantrip,first,second,third,fourth,fifth,sixth,seventh,eighth,ninth,artificer,bard,cleric,druid,paladin,ranger,sorcerer,warlock,wizard):
        self.cantrip = cantrip
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth
        self.fifth = fifth
        self.sixth = sixth
        self.seventh = seventh
        self.eighth = eighth
        self.ninthth = ninth
        self.artificer = artificer
        self.bard = bard
        self.cleric = cleric
        self.druid = druid
        self.paladin = paladin
        self.ranger = ranger
        self.sorcerer = sorcerer
        self.warlock = warlock
        self.wizard = wizard



# Used to choose what level spell a character wants
    def second_level(first,second):
        while True:
            choice = input("What level do you want to select from?\n1) First\n2) Second\nEnter your Selection: ")
            if choice == '1':
                return first
#                break
    
            elif choice == '2':
                return second
#                break
    
            else:
                print("Error: Invalid Input")
                continue
    
    def third_level(first,second,third):
        while True:
            choice = input("What level do you want to select from?\n1) First\n2) Second\n3) Third\nEnter your Selection: ")
            if choice == '1':
                first
                break
    
            elif choice == '2':
                second
                break
    
            elif choice == '3':
                third
                break
    
            else:
                print("Error: Invalid Input")
                continue
    
    def fourth_level(first,second,third,fourth):
        while True:
            choice = input("What level do you want to select from?\n1) First\n2) Second\n3) Third\n4) Fourth\nEnter your Selection: ")
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
    
            else:
                print("Error: Invalid Input")
                continue
    
    def fifth_level(first,second,third,fourth,fifth):
        while True:
            choice = input("What level do you want to select from?\n1) First\n2) Second\n3) Third\n4) Fourth\n5) Fifth\nEnter your Selection: ")
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
    
            else:
                print("Error: Invalid Input")
                continue
    
    def sixth_level(first,second,third,fourth,fifth,sixth):
        while True:
            choice = input("What level do you want to select from?\n1) First\n2) Second\n3) Third\n4) Fourth\n5) Fifth\n6) Sixth\nEnter your Selection: ")
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
    
            else:
                print("Error: Invalid Input")
                continue
    
    def seventh_level(first,second,third,fourth,fifth,sixth,seventh):
        while True:
            choice = input("What level do you want to select from?\n1) First\n2) Second\n3) Third\n4) Fourth\n5) Fifth\n6) Sixth\n7) Seventh\nEnter your Selection: ")
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
    
            else:
                print("Error: Invalid Input")
                continue
    
    def eighth_level(first,second,third,fourth,fifth,sixth,seventh,eighth):
        while True:
            choice = input("What level do you want to select from?\n1) First\n2) Second\n3) Third\n4) Fourth\n5) Fifth\n6) Sixth\n7) Seventh\n8) Eighth\nEnter your Selection: ")
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
    
            else:
                print("Error: Invalid Input")
                continue
    
    def ninth_level(first,second,third,fourth,fifth,sixth,seventh,eighth,ninth):
        while True:
            choice = input("What level do you want to select from?\n1) First\n2) Second\n3) Third\n4) Fourth\n5) Fifth\n6) Sixth\n7) Seventh\n8) Eighth\n9) Ninth\nEnter your Selection: ")
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
    
            else:
                print("Error: Invalid Input")
                continue
    
    
    # Used for magical secrets at 18, including cantrips
    def magical_secrets_18(first,second,third,fourth,fifth,sixth,seventh,eighth,ninth,cantrip):
        while True:
            choice = input("What level do you want to select from?\n1) First\n2) Second\n3) Third\n4) Fourth\n5) Fifth\n6) Sixth\n7) Seventh\n8) Eighth\n9) Ninth\n10) Cantrip\nEnter your Selection: ")
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
    
    
    # Used to select spells for Magical Secrets from the Bard class
    def magical_secrets(artificer,bard,cleric,druid,paladin,ranger,sorcerer,warlock,wizard):
        x = 1
        for x in range(x,3):
            while True:
                if x < 3:
                    print(f'{x}/2')
                    choice = input("Select the class would you like to learn a spell from:\n1) Artificer\n2) Bard\n3) Cleric\n4) Druid\n5) Paladin\n6) Ranger\n7) Sorcerer\n8) Warlock\n9) Wizard\nEnter your selection: ")
                    if choice == '1':
                        artificer
                        x+=1
                        continue
    
                    elif choice == '2':
                        bard
                        x+=1
                        continue
    
                    elif choice == '3':
                        cleric
                        x+=1
                        continue
    
                    elif choice == '4':
                        druid
                        x+=1
                        continue
    
                    elif choice == '5':
                        paladin
                        x+=1
                        continue
    
                    elif choice == '6':
                        ranger
                        x+=1
                        continue
    
                    elif choice == '7':
                        sorcerer
                        x+=1
                        continue
    
                    elif choice == '8':
                        warlock
                        x+=1
                        continue
    
                    elif choice == '9':
                        wizard
                        x+=1
                        continue
    
                    else:
                        print("Error: Invalid Input")
                        continue
    
                elif x == 3:
                    break























    













