#!/usr/bin/python3
import random, os, math, json, dnd_features, dnd_tools, dnd_dict, dnd_skills, dnd_race, dnd_class,dnd_language,dnd_pack,re


def acolyte():
    print("Skill Proficiencies: Insight, Religion")
    dnd_language.double_language()
    dnd_dict.character_dict["background"] = 'Acolyte'

    print("Equipment: A holy symbol (a gift to you when you entered the priesthood), a prayer book or prayer wheel, 5 sticks of incense, vestments, a set of common clothes, and a belt pouch containing 15 gp")

# Update skill proficiencies
    dnd_dict.character_dict['skill_prof']['insight'] = 'Insight'
    dnd_dict.character_dict['skill_prof']['religion'] = 'Religion'

    dnd_dict.character_dict["gold"] = 15

    misc_items = {'prayer_book_wheel1':'A prayer book or prayer wheel','vestments1':'Vestments','common_clothes1':'Common Clothes'}
    dnd_skills.misc_mod('incense5','Incense','sticks','stick')
    dnd_skills.equip_mod('holy_symbol1','Holy Symbol')

    dnd_dict.character_dict["Misc"].update(misc_items)

    dnd_features.acolyte_features()
    return

def anthropologist():
    dnd_language.double_language()

    print("Skill Proficiencies: Insight, Religion")

    dnd_dict.character_dict['background']= 'Anthropologist'

    print("Equipment: A leather-bound diary, a bottle of ink, an ink pen, a set of traveler's clothes, one trinket of special significance, and a pouch containing 10 gp")

# Update skill proficiencies
    dnd_dict.character_dict['skill_prof']['insight'] = 'Insight'
    dnd_dict.character_dict['skill_prof']['religion'] = 'Religion'



    misc_items = {'diary1':'A leather-bound diary','ink1':'A bottle of ink','pen1':'An ink pen','traveler_clothes1':'A set of traveler\'s clothes','trinket1':'One trinket of special significance'}

    dnd_dict.character_dict["Misc"].update(misc_items)

    dnd_dict.character_dict["gold"] = 10

    dnd_features.anthropologist_features()

    return

def archeologist():
    print("Skill Proficiencies: History, Survival")
    print("Tool Proficiencies: Cartographer's Tools or Navigator's Tools")

    dnd_dict.character_dict['background']= "Archeologist"
    while True:
        choice = input("Choose your tool proficiency:\n1) Cartographer's Tools\n2) Navigator's Tools\nEnter your selection: ")
        if choice == '1':
            print("Cartographer's Tools Chosen")
            dnd_dict.character_dict["Tools"]['cartographer_tools'] = "Cartographer's Tools"
            break
 
        elif choice == '2':
            print("Navigator's Tools Chosen")
            dnd_dict.character_dict["Tools"]['navigator_tools'] = "Navigator's Tools"
            break

        else:
            print("Invalid entry.")
            continue

    dnd_language.language()

# Update skill proficiencies
    dnd_dict.character_dict['skill_prof']['history'] = 'History'
    dnd_dict.character_dict['skill_prof']['survival'] = 'Survival'


    print("Equipment: A wooden case containing a map to a ruin or dungeon, a bullseye lantern, a miner's pick, a set of traveler's clothes, a shovel, a two-person tent, a trinket recovered from a dig site, and a pouch containing 25 gp")


    misc_items = {'dungeon_map1':'A wooden case containing a map to a ruin or dungeon','lantern1':'A bullseye lantern','miner_pick1':'A miner\'s pick','traveler_clothes1':'A set of traveler\'s clothes','shovel1':'A shovel','tent1':'A two person tent','trinket1':'A trinket recovered from a digsite'}

    dnd_dict.character_dict["Misc"].update(misc_items)
    dnd_dict.character_dict["gold"] = 25


    dnd_features.archeologist_features()

    return

def charlatan():
    print("Skill Proficiencies: Deception, Sleight of Hand")
    print("Tool Proficiencies: Disguise Kit, Forgery Kit")

    dnd_dict.character_dict['background']= 'Charlatan'
    dnd_dict.character_dict["Kits"]['disguise_kit'] = 'Disguise Kit'
    dnd_dict.character_dict["Kits"]['forgery_kit'] = 'Forgery Kit'

# Update skill proficiencies

    dnd_dict.character_dict['skill_prof']['deception'] = 'Deception'
    dnd_dict.character_dict['skill_prof']['sleight_of_hand'] = 'Sleight of Hand'

    print("Equipment A set of fine clothes, a disguise kit, tools of the con of your choice (ten stoppered bottles filled with colored liquid, a set of weighted dice, a deck of marked cards, or a signet ring of an imaginary duke), and a belt pouch containing 15 gp")


    misc_items = {'fine_clothes1':'A fine set of clothes','con_tools1':'Tools of the con of your choice (ten stoppered bottles filled with colored liquid, a set of weighted dice, a deck of marked cards, or a signet ring of an imaginary duke)'}
    dnd_dict.character_dict["Misc"].update(misc_items)
    dnd_dict.character_dict['Equipment']['disguise_kit1'] = 'Disguise Kit'


    dnd_dict.character_dict["gold"] = 15

    dnd_features.charlatan_features()

    return

def city_watch():
    print("Skill Proficiencies: Athletics, Insight")

    dnd_dict.character_dict['background']= 'City Watch'
    dnd_language.double_language()

# Update skill proficiencies

    dnd_dict.character_dict['skill_prof']['athletics'] = 'Athletics'
    dnd_dict.character_dict['skill_prof']['insight'] = 'Insight'

    print("Equipment: A uniform in the style of your unit and indicative of your rank, a horn with which to summon help, a set of manacles, and a pouch containing 10 gp")


    misc_items = {'unit_uniform1':'A uniform in the style of your unit and indicative of your rank','help_horn1':'A horn with which to summon help','manacles1':'A set of manacles'}
    dnd_dict.character_dict["Misc"].update(misc_items)

    dnd_dict.character_dict["gold"] = 10


    dnd_features.city_watch_features()

    return

def cloistered_scholar():
    print("Skill Proficiencies: History, 1 from Arcana, Nature, or Religion")

    dnd_dict.character_dict['background']= 'Cloistered Scholar'
    dnd_language.double_language()


    dnd_dict.character_dict['skill_prof']['history'] = 'History'

    skill_list = ['Arcana','Nature','Religion']
    dnd_skills.skill_addition(skill_list,dnd_dict.character_dict['skill_prof'])


    print("Equipment: The scholar's robes of your cloister, a writing kit (small pouch with a quill, ink, folded parchment, and a small penknife), a borrowed book on the subject of your current study, and a pouch containing 10 gp")


    misc_items = {'scholar_robes1':'The scholar\'s robes of your cloister','writing_kit1':'A writing kit (small pouch with a quill, ink, folded parchment, and a small penknife','borrowed_book1':'A borrowed book on the subject of your current study'}
    dnd_dict.character_dict["Misc"].update(misc_items)

    dnd_dict.character_dict["gold"] = 10


    dnd_features.cloistered_scholar_features()

    return

def criminal():
    print("Skill Proficiencies: Deception, Stealth")
    print("Tool Proficiencies: One Type of Gaming Set, Thieves' Tools")
    print("Equipment: A crowbar, a set of dark common clothes including a hood, and a belt pouch containing 15 gp")

    dnd_dict.character_dict['background']= 'Criminal'
    dnd_dict.character_dict["Kits"]['thieves_tools'] = 'Thieves\' Tools'
    dnd_tools.gaming_set()

# Update skill proficiencies
    dnd_dict.character_dict['skill_prof']['deception'] = 'Deception'
    dnd_dict.character_dict['skill_prof']['stealth'] = 'Stealth'


    misc_items = {'crowbar1':'A crowbar','dark_clothes1':'A set of dark clothes, including a hood'}
    dnd_dict.character_dict["Misc"].update(misc_items)
    dnd_dict.character_dict["gold"] = 15


    dnd_features.criminal_features()

    return

def entertainer():
    print("Skill Proficiencies: Acrobatics, Performance")
    print("Tool Proficiencies: Disguise kit, One Type of Musical Instument")
    print("Equipment: A musical instrument (one of your choice), the favor of an admirer (love letter, lock of hair, or trinket), a costume, and a belt pouch containing 15 gp")


    dnd_dict.character_dict['background']= 'Entertainer'
    dnd_dict.character_dict["Kits"]['disguise_kit'] = 'Disguise Kit'
 

# Update skill proficiencies
    dnd_dict.character_dict['skill_prof']['acrobatics'] = 'Acrobatics'
    dnd_dict.character_dict['skill_prof']['performance'] = 'Performance'

    dnd_tools.musical_instrument()
    while True:
        musical_equip = input("What instrument do you want to take? ")
        regex = re.compile(r'[a-zA-Z\']')
        if regex.search(musical_equip) == None:
            print("Do not use numbers or special characters. Please pick again.")
            continue
        else:
            dnd_dict.character_dict["Equipment"][musical_equip] = musical_equip
            break

    misc_items = {'favor1':'The favor of an admirer (love letter, a lock of hair, or a trinket)','costume1':'A costume'}
    dnd_dict.character_dict["Misc"].update(misc_items)
    dnd_dict.character_dict["gold"] = 15


    dnd_features.entertainer_features()

    return

def far_traveler():
    print("Skill Proficiencies: Insight, Perception")
    print("Tool Proficiencies: One Instrument and One Gaming Set")

    dnd_dict.character_dict['background']= 'Far Traveler'
    dnd_language.language()
    gaming_set = dnd_tools.gaming_set()


    print("Equipment: One set of traveler's clothes, any one musical instrument or gaming set you are proficient with, poorly wrought maps from your homeland that depict where you are in the world, a small piece of jewelry worth 10 gp in the style of your homeland's craftsmanship, and a pouch containing 5 gp")

# Update skill proficiencies
    dnd_dict.character_dict['skill_prof']['insight'] = 'Insight'
    dnd_dict.character_dict['skill_prof']['perception'] = 'Perception'

    musical_equip = dnd_tools.musical_instrument()

    misc_items = {'traveler_clothes1':'One set of traveler\'s clothes','poor_map1':'Poorly wrought maps from your homeland that depicts where you are in the world','home_jewlery1':'A small piece of jewlery worth 10 gp in the style of your homeland\'s craftsmanship'}
    dnd_dict.character_dict["Misc"].update(misc_items)
    dnd_dict.character_dict["gold"] = 5

    dnd_features.far_traveler_features()
    return

def folk_hero():
    print("Skill Proficiencies: Animal Handling, Survival")
    print("Tool Proficiencies: One Type of Artisan's Tools, Vehicles(Land)")
    print("Equipment: A shovel, an iron pot, a set of common clothes, and a belt pouch containing 10 gp")

    dnd_dict.character_dict['background']= 'Folk Hero'
    dnd_tools.artisan_tools()

# Update skill proficiencies
    dnd_dict.character_dict['skill_prof']['animal_handling'] = 'Animal Handling'
    dnd_dict.character_dict['skill_prof']['survival'] = 'Survival'


    dnd_dict.character_dict["Vehicles"]['land'] = 'Land'

    misc_items = {'common_clothes1':'One set of common clothes','shovel1':'A shovel','iron_pot1':'An iron pot'}
    dnd_dict.character_dict["Misc"].update(misc_items)
    dnd_dict.character_dict["gold"] = 10

    dnd_features.folk_hero_features()
    return

def gladiator():
    print("Skill Proficiencies: Acrobatics, Performance")
    print("Tool Proficiencies: Disguise kit, One Type of Musical Instument")
    print("Equipment: A musical instrument (one of your choice), the favor of an admirer (love letter, lock of hair, or trinket), a costume, and a belt pouch containing 15 gp")

    dnd_dict.character_dict['background']= 'Gladiator'

# Update skill proficiencies
    dnd_dict.character_dict['skill_prof']['acrobatics'] = 'Acrobatics'
    dnd_dict.character_dict['skill_prof']['performance'] = 'Performance'


    dnd_dict.character_dict["Kits"]['disguise_kit'] = 'Disguise Kit'
    dnd_tools.musical_instrument()

    dnd_dict.character_dict["gold"] = 15

    while True:
        musical_equip = input("What instrument do you want to take? ")
        regex = re.compile(r'[a-zA-Z\']')
        if regex.search(musical_equip) == None:
            print("Do not use numbers or special characters. Please pick again.")
            continue
        else:
            dnd_dict.character_dict["Equipment"][musical_equip] = musical_equip
            break

    misc_items = {'favor1':'The favor of an admirer (love letter, a lock of hair, or a trinket)','costume1':'A costume'}
    dnd_dict.character_dict["Misc"].update(misc_items)

    dnd_features.gladiator_features()
    return

def guild_artisan():
    print("Skill Proficiencies: Insight, Persuasion")
    dnd_language.language()

    dnd_dict.character_dict['background']= 'Guild Artisan'

# Update skill proficiencies
    dnd_dict.character_dict['skill_prof']['insight'] = 'Insight'
    dnd_dict.character_dict['skill_prof']['persuasion'] = 'Persuasion'


    print("Equipment: A set of artisan's tools (one of your choice), a letter of introduction from your guild, a set of traveler's clothes, and a belt pouch containing 15 gp")


    dnd_tools.artisan_tools_equip()

    misc_items = {'traveler_clothes1':'A set of traveler\'s clothes','intro_letter1':'A letter of introduction from your guild'}
    dnd_dict.character_dict["Misc"].update(misc_items)
    dnd_dict.character_dict["gold"] = 15


    dnd_features.guild_artisan_features()
    return

def guild_merchant():
    print("Skill Proficiencies: Insight, Persuasion")
    print("Tool Proficiency: navigator's tools")
    dnd_language.double_language()

    dnd_dict.character_dict['background']= 'Guild Merchant'
    dnd_dict.character_dict["Tools"]['navigator_tools'] = "Navigator's Tools"

# Update skill proficiencies
    dnd_dict.character_dict['skill_prof']['insight'] = 'Insight'
    dnd_dict.character_dict['skill_prof']['persuasion'] = 'Persuasion'

    print("Equipment A mule and a cart, a letter of introduction from your guild, a set of traveler's clothes, and a belt pouch containing 15 gp")


    misc_items = {'mule_cart1':'A mule and a cart','traveler_clothes1':'A set of traveler\'s clothes','intro_letter1':'A letter of introduction from your guild'}
    dnd_dict.character_dict["Misc"].update(misc_items)
    dnd_dict.character_dict["gold"] = 15

    dnd_features.guild_artisan_features()
    return

def haunted_one():
    print("Skill Proficiencies: Two of Arcana, Investigation, Religion, or Survival")
    print("Equipment: Monster hunter’s pack, a set of common clothes, one trinket of special significance")
 
    dnd_dict.character_dict['background']= 'Haunted One'

    dnd_pack.monster_hunter_pack()
    misc_items = {'common_clothes1':'A set of common clothes','special_trinket1':'One trinket of special significance'}

    dnd_dict.character_dict["Misc"].update(misc_items)

    skill_list = ['Arcana','Investigation','Religion','Survival']
    i = 1
    for i in range (i,3):
        if i < 3:
            print(f'{i}/2')
            dnd_skills.skill_addition(skill_list,dnd_dict.character_dict['skill_prof'])
            i+=1
            continue

        elif i == 3:
            break



    dnd_language.exotic_language()
    dnd_dict.character_dict["gold"] = 0

    dnd_features.haunted_one_features()
    return

def hermit():
    print("Skill Proficiencies: Medicine, Religion")
    print("Tool Proficiency: Herbalism Kit")
    print("Equipment: A scroll case stuffed full of notes from your studies or prayers, a winter blanket, a set of common clothes, an herbalism kit, and 5 gp")

    dnd_dict.character_dict['background']= 'Hermit'
    dnd_dict.character_dict["Kits"]['herbalism_kit'] = 'Herbalism Kit'


# Update skill proficiencies
    dnd_dict.character_dict['skill_prof']['medicine'] = 'Medicine'
    dnd_dict.character_dict['skill_prof']['religion'] = 'Religion'

    dnd_dict.character_dict["Equipment"]['herbalism_kit1'] = 'Herbalism Kit'
    misc_items = {'scroll_case1':'A scroll case stuffed full of notes from your studies or prayers','common_clothes1':'A set of common clothes','blanket1':'A winter blanket'}
    dnd_dict.character_dict["Misc"].update(misc_items)
    dnd_dict.character_dict["gold"] = 5

    dnd_language.language()

    dnd_features.hermit_features()
    return


def inquisitor():
    print("Skill Proficiencies: Investigation, Religion")
    print("Tool Proficiencies: Thieves' Tools, one set of artisan's tools of your choice")
    print("Equipment: A holy symbol, a set of traveler’s clothes, and a belt pouch containing 15 gp")

    dnd_dict.character_dict['background']= 'Inquisitor'
    dnd_tools. artisan_tools()
    dnd_dict.character_dict["Kits"]['thieves_tools'] = 'Thieves\' Tools'

# Update skill proficiencies
    dnd_dict.character_dict['skill_prof']['investigation'] = 'Investigation'
    dnd_dict.character_dict['skill_prof']['religion'] = 'Religion'

    misc_items = {'traveler_clothes1':'A set of traveler\'s clothes'}
    dnd_skills.equip_mod('holy_symbol1','Holy Symbol')
    dnd_dict.character_dict["Misc"].update(misc_items)
    dnd_dict.character_dict["gold"] = 15


    dnd_features.inquisitor_features()
    return

def investigator():
    print("Skill Proficiencies: Athletics, Insight")
    print("Equipment: A uniform in the style of your unit and indicative of your rank, a horn with which to summon help, a set of manacles, and a pouch containing 10 gp")

    dnd_language.double_language()

    dnd_dict.character_dict['background']= 'Investigator'

# Update skill proficiencies
    dnd_dict.character_dict['skill_prof']['athletics'] = 'Athletics'
    dnd_dict.character_dict['skill_prof']['insight'] = 'Insight'

    misc_items = {'unit_uniform1':'A uniform in the style of your unit and indicative of your rank','help_horn1':'A horn with which to summon help','manacles1':'A set of manacles'}
    dnd_dict.character_dict["Misc"].update(misc_items)
    dnd_dict.character_dict["gold"] = 10


    dnd_features.investigator_features()
    return

def knight():
    print("Skill Proficiencies: History, Persuasion")
    print("Tool Proficiencies: One Type of Gaming Set")
    print("Equipment: A set of fine clothes, a signet ring, a scroll of pedigree, and a purse containing 25 gp")

    dnd_language.language()
    dnd_dict.character_dict['background']= 'Knight'

# Update skill proficiencies
    dnd_dict.character_dict['skill_prof']['history'] = 'History'
    dnd_dict.character_dict['skill_prof']['persuasion'] = 'Persuasion'


    dnd_tools.gaming_set()


    misc_items = {'fine_clothes1':'A set of fine clothes','signit_ring1':'A signit ring','pedigree_scroll1':'A scroll of pedigree'}
    dnd_dict.character_dict["Misc"].update(misc_items)
    dnd_dict.character_dict["gold"] = 25

    dnd_features.knight_features()
    return

def marine():
    print("Skill Proficiencies: Athletics, Survival")
    print("Tool Proficiencies: Vehicles (Land & Water)")
    print("Equipment: A dagger that belonged to a fallen comrade, a folded rag emblazoned with the symbol of your ship or company, a set of traveler's clothes, and a belt pouch containing 10 gp")

    dnd_dict.character_dict['background']= 'Marine'
# Update skill proficiencies
    dnd_dict.character_dict['skill_prof']['athletics'] = 'Athletics'
    dnd_dict.character_dict['skill_prof']['survival'] = 'Survival'


    dnd_dict.character_dict["Vehicles"]['land'] = 'Land'
    dnd_dict.character_dict["Vehicles"]['water'] = 'Water'


    misc_items = {'fallen_dagger1':'A dagger that belonged to a fallen comrade','company_symbol1':'A folded rag emblazoned with the symbol of your ship or company','traveler_clothes1':'A set of traveler\'s clothes'}
    dnd_dict.character_dict["Misc"].update(misc_items)
    dnd_dict.character_dict["gold"] = 10

    dnd_features.marine_features()
    return

def mercenary():
    print("Skill Proficiencies: Athletics, Persuasion")
    print("Tool Proficiencies: One Type of Gaming Set, Vehicles(Land)")
    print("Equipment: A uniform of your company (traveler's clothes in quality), an insignia of your rank, a gaming set of your choice, and a pouch containing the remainder of your last wages (10 gp)")

    dnd_dict.character_dict['background']= 'Mercenary'
    dnd_tools.gaming_set()

# Update skill proficiencies
    dnd_dict.character_dict['skill_prof']['athletics'] = 'Athletics'
    dnd_dict.character_dict['skill_prof']['persuasion'] = 'Persuasion'


    misc_items = {'company_uniform1':'A uniform of your company (traveler\'s clothes in quality','rank_insignia1':'An insignia of your rank'}
    dnd_dict.character_dict["Misc"].update(misc_items)

    dnd_dict.character_dict["gold"] = 10

    dnd_features.mercenary_features()
    return

def noble():

    print("Skill Proficiencies: History, Persuasion")
    print("Tool Proficiencies: One Type of Gaming Set")
    print("Equipment: A set of fine clothes, a signet ring, a scroll of pedigree, and a purse containing 25 gp")

    dnd_language.language()
    dnd_tools.gaming_set()
    dnd_dict.character_dict['background']= 'Noble'

# Update skill proficiencies
    dnd_dict.character_dict['skill_prof']['history'] = 'History'
    dnd_dict.character_dict['skill_prof']['persuasion'] = 'Persuasion'

    misc_items = {'fine_clothes1':'A set of fine clothes','signit_ring1':'A signit ring','pedigree_scroll1':'A scroll of pedigree'}
    dnd_dict.character_dict["Misc"].update(misc_items)
    dnd_dict.character_dict["gold"] = 25

    dnd_features.noble_features()
    return

def outlander():
    print("Skill Proficiencies: Athletics, Survival")
    print("Tool Proficiencies: One Type of Musical Instrument")
    print("Equipment: A staff, a hunting trap, a trophy from an animal you killed, a set of traveler's clothes, and a belt pouch containing 10 gp")

    dnd_language.language()
    dnd_tools.musical_instrument()
    dnd_dict.character_dict['background']= 'Outlander'

# Update skill proficiencies
    dnd_dict.character_dict['skill_prof']['athletics'] = 'Athletics'
    dnd_dict.character_dict['skill_prof']['survival'] = 'Survival'


    misc_items = {'staff1':'A staff','hunting_trap1':'A hunting trap','hunting_trophy1':'A trophy from an animal you killed','traveler_clothes1':'A set of traveler\'s clothes'}
    dnd_dict.character_dict["Misc"].update(misc_items)
    dnd_dict.character_dict["gold"] = 10

    dnd_features.outlander_features()
    return

def pirate():
    print("Skill Proficiencies: Athletics, Perception")
    print("Tool Proficiencies: Navigator's Tools, Vehicles(Water)")
    print("Equipment: A belaying pin (club), 50 feet of silk rope, a lucky charm such as a rabbit foot or a small stone with a hole in the center (or you may roll for a random trinket on the Trinkets table in chapter 5), a set of common clothes, and a belt pouch containing 10 gp")

    dnd_dict.character_dict['background']= 'Pirate'

# Update skill proficiencies
    dnd_dict.character_dict['skill_prof']['athletics'] = 'Athletics'
    dnd_dict.character_dict['skill_prof']['perception'] = 'Perception'

    dnd_dict.character_dict["Tools"]['navigator_tools'] = "Navigator's Tools"
    dnd_dict.character_dict["Vehicles"]['water'] = 'Water'


    misc_items = {'belay_pin1':'A belaying pin(club)','lucky_charm1':'A lucky charm such as a rabbit foot or a small stone with a hole in the center (or you may roll for a random trinket on the Trinkets table in chapter 5)','common_clothes1':'A set of common clothes'}
    dnd_skills.misc_mod('silk_rope50','Silk Rope','Feet','Foot')
    dnd_dict.character_dict["Misc"].update(misc_items)
    dnd_dict.character_dict["gold"] = 10

    dnd_features.pirate_features()
    return

def sage():
    print("Skill Proficiencies: Arcana, History")

    dnd_language.double_language()
    dnd_dict.character_dict['background']= 'Sage'

# Update skill proficiencies
    dnd_dict.character_dict['skill_prof']['arcana'] = 'Arcana'
    dnd_dict.character_dict['skill_prof']['history'] = 'History'

    print("Equipment: A bottle of black ink, a quill, a small knife, a letter from a dead colleague posing a question you have not yet been able to answer, a set of common clothes, and a belt pouch containing 10 gp")

    misc_items = {'ink1':'A bottle of black ink','quill1':'A quill','dead_letter1':'A letter from a dead colleague posing a question you have not yet been able to answer','common_clothes1':'A set of common clothes'}
    dnd_dict.character_dict["Misc"].update(misc_items)
    dnd_dict.character_dict["gold"] = 10

    dnd_features.sage_features()
    return

def sailor():
    print("Skill Proficiencies: Athletics, Perception")
    print("Tool Proficiencies: Navigator's Tools, Vehicles(Water)")
    print("Equipment: A belaying pin (club), 50 feet of silk rope, a lucky charm such as a rabbit foot or a small stone with a hole in the center (or you may roll for a random trinket on the Trinkets table in chapter 5), a set of common clothes, and a belt pouch containing 10 gp")

    dnd_dict.character_dict['background']= 'Sailor'
# Update skill proficiencies
    dnd_dict.character_dict['skill_prof']['athletics'] = 'Athletics'
    dnd_dict.character_dict['skill_prof']['perception'] = 'Perception'

    dnd_dict.character_dict["Tools"]['navigator_tools'] = "Navigator's Tools"
    dnd_dict.character_dict["Vehicles"]['water'] = 'Water'

    misc_items = {'belay_pin1':'A belaying pin(club)','lucky_charm1':'A lucky charm such as a rabbit foot or a small stone with a hole in the center (or you may roll for a random trinket on the Trinkets table in chapter 5)','common_clothes1':'A set of common clothes'}
    dnd_skills.misc_mod('silk_rope50','Silk Rope','Feet','Foot')
    dnd_dict.character_dict["Misc"].update(misc_items)
    dnd_dict.character_dict["gold"] = 10

    dnd_features.sailor_features()
    return

def soldier():
    print("Skill Proficiencies: Athletics, Intimidation")
    print("Tool Proficiencies: One Type of Gaming Set, Vehicles (Land)")
    print("Equipment: An insignia of rank, a trophy taken from a fallen enemy (a dagger, broken blade, or piece of a banner), a set of bone dice or deck of cards, a set of common clothes, and a belt pouch containing 10 gp")

    dnd_tools.gaming_set()
    dnd_dict.character_dict['background']= 'Soldier'

# Update skill proficiencies
    dnd_dict.character_dict['skill_prof']['athletics'] = 'Athletics'
    dnd_dict.character_dict['skill_prof']['intimidation'] = 'Intimidation'

    dnd_dict.character_dict["Vehicles"]['land'] = 'Land'



    misc_items = {'rank_insignia1':'An insignia of rank','fallen_trophy1':'A trophy taken from a fallen enemy (a dagger, broken blade, or a piece of a banner)','common_clothes1':'A set of common clothes'}
    dnd_dict.character_dict["Misc"].update(misc_items)


    dnd_dict.character_dict["gold"] = 10

    dnd_features.soldier_features()
    return

def spy():
    print("Proficiencies: Deception, Stealth")
    print("Tools: One Type of Gaming Set, Thieves' Tools")
    print("Equipment: A crowbar, a set of dark common clothes including a hood, and a belt pouch containing 15 gp")

    dnd_tools.gaming_set()
    dnd_dict.character_dict["Kits"]['thieves_tools'] = 'Thieves\' Tools'
    dnd_dict.character_dict['background']= 'Spy'

# Update skill proficiencies
    dnd_dict.character_dict['skill_prof']['deception'] = 'Deception'
    dnd_dict.character_dict['skill_prof']['stealth'] = 'Stealth'

    dnd_dict.character_dict["gold"] = 15

    misc_items = {'crowbar1':'A crowbar','dark_clothes1':'A set of dark clothes, including a hood'}
    dnd_dict.character_dict["Misc"].update(misc_items)

    dnd_features.spy_features()
    return


def urban_bounty_hunter():
    print("Skill Proficiencies: Choose Two From Deception, Persuasion, and Stealth")
    print("Tool Proficiencies: Two From Among One Type of Gaming Set, One Musical Instrument, and Thieves' Tools")
    print("Equipment: A set of clothes appropriate to your duties and a pouch containing 20 gp")

    dnd_dict.character_dict['background']= 'Urban Bounty Hunter'
#Choosing the Tool Proficiencies
    while True:
       choice1 =input("Select your first choice:\n1) One Instrument\n2) One Type of Gaming Set\n3) Thieves' Tools\nEnter your selection: ")
       if choice1=='1':
           dnd_tools.musical_instrument()
           break

       elif choice1=='2':
           dnd_tools.gaming_set()
           break

       elif choice1=='3':
           print("Thieves\' Tools selected")
           dnd_dict.character_dict["Kits"]['thieves_tools'] = 'Thieves\' Tools'
           break

       else:
           print("Invalid Selection")
           continue

    while True:
        choice2 =input("Select your second choice:\n1) One Musical Instrument\n2) One Gaming Set\n3) Thieves' Tools\nEnter your selection: ")
        if choice2=='1':
            if choice1=='1':
                print("Already Selected")
                continue
            else: 
                dnd_tools.musical_instrument()
                break

        elif choice2=='2':
            if choice1=='2':
                print("Already Selected")
                continue
            else:
                dnd_tools.gaming_set()
                break

        elif choice2=='3':
            if choice1=='3':
                print("Already Selected")
                continue
            else:
                print("Thieves\' Tools selected")
                dnd_dict.character_dict["Kits"]['thieves_tools'] = 'Thieves\' Tools'
                break

        else:
            print("Invalid Selection")
            continue

#Choose your skills, if proficient with all three skills, then continue with the program.


    skill_list = ['Deception','Persuasion','Stealth']
    i = 1
    for i in range (i,3):
        check_prof = dnd_dict.character_dict['skill_prof']
        if 'deception' in check_prof and 'persuasion' in check_prof and 'stealth' in check_prof:
            i+=2
            break
        elif i < 3:
            print(f'{i}/2')
            dnd_skills.skill_addition(skill_list,dnd_dict.character_dict['skill_prof'])
            i+=1
            continue

        elif i >= 3:
            break







    misc_items = {'duty_clothes1':'A set of clothes appropriate to your duties'}
    dnd_dict.character_dict["Misc"].update(misc_items)
    dnd_dict.character_dict["gold"] = 20

    dnd_features.urban_bounty_hunter_features()
    return

def urchin():
    print("Skill Proficiencies: Sleight of Hand, Stealth")
    print("Tool Proficiencies: Disguise Kit, Thieves' Tools")
    print("Equipment: A small knife, a map of the city you grew up in, a pet mouse, a token to remember your parents by, a set of common clothes, and a belt pouch containing 10 gp")

    dnd_dict.character_dict['background']= "Urchin"
# Update skill proficiencies
    dnd_dict.character_dict['skill_prof']['sleight_of_hand'] = 'Sleight of Hand'
    dnd_dict.character_dict['skill_prof']['stealth'] = 'Stealth'

    dnd_dict.character_dict["Kits"]['disguise_kit'] = "Disguise Kit"
    dnd_dict.character_dict["Kits"]['thieves_tools'] = "Thieves' Tools"

    misc_items = {'small_knife1':'A small knife','city_map1':'A map of the city you grew up in','pet_mouse1':'A pet mouse','parent_token1':'A token to remember your parents by','common_clothes1':'A set of common clothes'}
    dnd_dict.character_dict["Misc"].update(misc_items)
    dnd_dict.character_dict["gold"] = 10

    dnd_features.urchin_features()
    return

def player_background():
    while True:
        background_choice = input("""Choose your background:
1) Acolyte
2) Anthropologist
3) Archeologist
4) Charlatan
5) City Watch
6) Cloistered Scholar
7) Criminal
8) Entertainer
9) Far Traveler
10) Folk Hero
11) Gladiator
12) Guild Artisan
13) Guild Merchant
14) Haunted One
15) Hermit
16) Inquisitor
17) Investigator
18) Knight
19) Marine
20) Mercenary
21) Noble
22) Outlander
23) Pirate
24) Sage
25) Sailor
26) Soldier
27) Spy
28) Urban Bounty Hunter
29) Urchin
Enter your selection: """)

        if background_choice == '1':
            acolyte()
            break

        elif background_choice == '2':
            anthropologist()
            break

        elif background_choice == '3':
            archeologist()
            break

        elif background_choice == '4':
            charlatan()
            break

        elif background_choice == '5':
            city_watch()
            break

        elif background_choice == '6':
            cloistered_scholar()
            break

        elif background_choice == '7':
            criminal()
            break

        elif background_choice == '8':
            entertainer()
            break

        elif background_choice == '9':
            far_traveler()
            break

        elif background_choice == '10':
            folk_hero()
            break

        elif background_choice == '11':
            gladiator()
            break

        elif background_choice == '12':
            guild_artisan()
            break

        elif background_choice == '13':
            guild_merchant()
            break

        elif background_choice == '14':
            haunted_one()
            break

        elif background_choice == '15':
            hermit()
            break

        elif background_choice == '16':
            inquisitor()
            break

        elif background_choice == '17':
            investigator()
            break

        elif background_choice == '18':
            knight()
            break

        elif background_choice == '19':
            marine()
            break

        elif background_choice == '20':
            mercenary()
            break

        elif background_choice == '21':
            noble()
            break

        elif background_choice == '22':
            outlander()
            break

        elif background_choice == '23':
            pirate()
            break

        elif background_choice == '24':
            sage()
            break

        elif background_choice == '25':
            sailor()
            break

        elif background_choice == '26':
            soldier()
            break

        elif background_choice == '27':
            spy()
            break

        elif background_choice == '28':
            urban_bounty_hunter()
            break

        elif background_choice == '29':
            urchin()
            break

        else:
            print("Invalid input")
            continue
