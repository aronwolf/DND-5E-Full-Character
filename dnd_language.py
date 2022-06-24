#!/usr/bin/python3
import dnd_dict, dnd_skills

elf_lang_list = ['Abyssal','Celestial','Deep Speech','Draconic','Dwarvish','Giant','Gnomish','Goblin','Infernal','Halfling','Orc','Primordial','Sylvan','Undercommon']

full_lang_list = ['Abyssal','Celestial','Deep Speech','Draconic','Dwarvish','Elven','Giant','Gnomish','Goblin','Infernal','Halfling','Orc','Primordial','Sylvan','Undercommon']

exotic_lang_list = ['Abyssal','Celestial','Deep Speech','Draconic','Infernal','Primordial','Sylvan','Undercommon']

def elf_lang():
    dnd_skills.skill_addition(elf_lang_list,dnd_dict.character_dict['Languages'])

def language():
    dnd_skills.skill_addition(full_lang_list,dnd_dict.character_dict['Languages'])

#Used for Haunted One background
def exotic_language():
    dnd_skills.skill_addition(exotic_lang_list,dnd_dict.character_dict['Languages'])


#Used for backgrounds that give two new languages.
def double_language():
    y = 1
    for y in range (y,3):
        if y < 3:
            print(f'{y}/2')
            language()
            y+=1
            continue

        elif y == 3:
            break


