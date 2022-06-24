#!/usr/bin/python3
import dnd_dict, dnd_skills


# Artificer Cantrips
artificer_cantrip = ['Acid Splash','Booming Blade', 'Create Bonfire', 'Dancing Lights','Fire Bolt','Frostbite','Green-Flame Blade','Guidance','Light','Lightning Lure','Mage Hand','Magic Stone','Mending','Message','Poison Spray','Prestidigitation','Ray of Frost','Resistance','Shocking Grasp','Spare the Dying','Sword Burst','Thorn Whip','Thunderclap']


# Used for learning from other classes, like the Bard's Magical Secrets Feature
artificer_first_classless = ['Absorb Elements','Alarm','Catapult','Cure Wounds','Detect Magic','Disguise Self','Expeditious Retreat','Faerie Fire','False Life','Feather Fall','Grease','Identify','Jump','Longstrider','Purify Food and Drink','Sanctuary','Snare','Tasha\'s Caustic Brew']
artificer_second_classless = ['Aid','Alter Self','Arcane Lock','Blur','Continual Flame','Darkvision','Enhance Ability','Enlarge/Reduce','Heat Metal','Invisibility','Lesser Restoration','Levitate','Magic Mouth','Magic Weapon','Protection from Poison','Pyrotechnics','Rope Trick','See Invisibility','Skywrite','Spider Climb','Web']
artificer_third_classless = ['Ashardalon\'s Stride','Blink','Catnap','Create Food and Water','Dispel Magic','Elemental Weapon','Flame Arrows','Fly','Glyph of Warding','Haste','Intellect Fortress','Protection from Energy','Revivify','Tiny Servant','Water Breathing','Water Walk']
artificer_fourth_classless = ['Arcane Eye','Elemental Bane','Fabricate','Freedom of Movement','Leomond\'s Secret Chest','Mordenkainen\'s Faithful Hound','Otiluke\'s Resilient Sphere','Stone Shape','Stoneskin','Summon Construct']
artificer_fifth_classless = ['Animate Objects','Bigby\'s Hand','Creation','Greater Restoration','Skill Empowerment','Transmute Rock','Wall of Stone']


def artificer_first():
        art_magic={'absorb_elements':'Absorb Elements', 'alarm':'Alarm', 'catapult':'Catapult', 'cure_wounds':'Cure Wounds', 'detect_magic':'Detect Magic', 'disguise_self':'Disguise Self', 'expeditious_retreat':'Expeditious Retreat', 'faerie_fire':'Faerie Fire', 'false_life':'False Life', 'feather_fall':'Feather Fall', 'grease':'Grease', 'identify':'Identify', 'jump':'Jump', 'longstrider':'Longstrider', 'purify_food_and_drink':'Purify Food and Drink', 'sanctuary':'Sanctuary', 'snare':'Snare', 'tasha\'s_caustic_brew':'Tasha\'s Caustic Brew'}
        dnd_dict.character_dict['spells']['first'].update(art_magic)
        dnd_dict.character_dict['class_spells']['artificer']['first'].update(art_magic)
        dnd_dict.character_dict['special_spells']['first'].update(art_magic)

def artificer_second():
        art_magic = {'aid':'Aid','alter_self':'Alter Self','arcane_lock':'Arcane Lock','blur':'Blur','continual_flame':'Continual Flame','darkvision':'Darkvision','enhance_ability':'Enhance Ability','enlarge/reduce':'Enlarge/Reduce','heat_metal':'Heat Metal','invisibility':'Invisibility','lesser_restoration':'Lesser Restoration','levitate':'Levitate','magic_mouth':'Magic Mouth','magic_weapon':'Magic Weapon','protection_from_poison':'Protection from Poison','pyrotechnics':'Pyrotechnics','rope_trick':'Rope Trick','see_invisibility':'See Invisibility','skywrite':'Skywrite','spider_climb':'Spider Climb','web':'Web'}
        dnd_dict.character_dict['spells']['second'].update(art_magic)
        dnd_dict.character_dict['class_spells']['artificer']['second'].update(art_magic)
        dnd_dict.character_dict['special_spells']['second'].update(art_magic)

def artificer_third():
        art_magic = {'ashardalon\'s_stride':'Ashardalon\'s Stride','blink':'Blink','catnap':'Catnap','create_food_and_water':'Create Food and Water','dispel_magic':'Dispel Magic','elemental_weapon':'Elemental Weapon','flame_arrows':'Flame Arrows','fly':'Fly','glyph_of_warding':'Glyph of Warding','haste':'Haste','intellect_fortress':'Intellect Fortress','protection_from_energy':'Protection from Energy','revivify':'Revivify','tiny_servant':'Tiny Servant','water_breathing':'Water Breathing','water_walk':'Water Walk'}
        dnd_dict.character_dict['spells']['third'].update(art_magic)
        dnd_dict.character_dict['class_spells']['artificer']['third'].update(art_magic)
        dnd_dict.character_dict['special_spells']['third'].update(art_magic)

def artificer_fourth():
        art_magic = {'arcane_eye':'Arcane Eye','elemental_bane':'Elemental Bane','fabricate':'Fabricate','freedom_of_movement':'Freedom of Movement','leomond\'s_secret_chest':'Leomond\'s Secret Chest','mordenkainen\'s_faithful_hound':'Mordenkainen\'s Faithful Hound','otiluke\'s_resilient_sphere':'Otiluke\'s Resilient Sphere','stone_shape':'Stone Shape','stoneskin':'Stoneskin','summon_construct':'Summon Construct'}
        dnd_dict.character_dict['spells']['fourth'].update(art_magic)
        dnd_dict.character_dict['class_spells']['artificer']['fourth'].update(art_magic)
        dnd_dict.character_dict['special_spells']['fourth'].update(art_magic)

def artificer_fifth():
        art_magic = {'animate_objects':'Animate Objects','bigby\'s_hand':'Bigby\'s Hand','creation':'Creation','greater_restoration':'Greater Restoration','skill_empowerment':'Skill Empowerment','transmute_rock':'Transmute Rock','wall_of_stone':'Wall of Stone'}
        dnd_dict.character_dict['spells']['fifth'].update(art_magic)
        dnd_dict.character_dict['class_spells']['artificer']['fifth'].update(art_magic)
        dnd_dict.character_dict['special_spells']['fifth'].update(art_magic)





# Select two artificer cantrips and get all 1st level spells\
def artificer_magic():
    x=1
    while x < 4:
        if x<3:
            print(f'{x}/2')
            dnd_skills.spell_add(artificer_cantrip,dnd_dict.character_dict['spells']['cantrips'],dnd_dict.character_dict['class_spells']['artificer']['artificer_cantrips'])
            x+=1
        elif x == 3:
            dnd_dict.character_dict['special_spells']['first'].update(dnd_dict.character_dict['class_spells']['artificer']['first'])
            artificer_first()
            x+=1
            break

########################################################################

bard_cantrip=['Blade Ward','Dancing Lights','Friends','Light','Mage Hand','Mending','Message','Minor Illusion','Prestidigitation','Thunderclap','True Strike','Vicious Mockery']
bard_first = ['Animal Friendship','Bane','Charm Person','Comprehend Languages','Cure Wounds','Detect Magic','Disguise Self','Dissonant Whispers','Distort Value','Earth Tremor','Faerie Fire','Feather Fall','Healing Word','Heroism','Hideous Laughter','Identify','Illusory Script','Longstrider','Silent Image','Silvery Barbs','Sleep','Speak with Animals','Tasha\'s Hideous Laughter','Thunderwave','Unseen Servant']
bard_second = ['Aid', 'Animal Messenger','Blindness/Deafness','Borrowed Knowledge','Calm Emotions','Cloud of Daggers','Crown of Madness','Detect Thoughts','Enhance Ability','Enlarge/Reduce','Enthrall','Gift of Gab','Heat Metal','Hold Person','Invisibility','Kinetic Jaunt','Knock','Lesser Restoration','Locate Animals or Plants','Locate Object','Magic Mouth','Mirror Image','Nathair\'s Mischief','Phantasmal Force','Pyrotechnics','See Invisibility','Shatter','Silence','Skywrite','Suggestion','Warding Wind','Zone of Truth']
bard_third = ['Bestow Curse','Catnap','Clairvoyance','Dispel Magic','Enemies Abound','Fast Friends','Fear','Feign Death','Glyph of Warding','Hypnotic Pattern','Intellect Fortress','Leomund\'s Tiny Hut','Major Image','Mass Healing Word','Motivational Speech','Nondetection','Plant Growth','Sending','Slow','Speak with Dead','Speak with Plants','Stinking Cloud','Tongues']
bard_fourth = ['Charm Monster','Compulsion','Confusion','Dimension Door','Freedom of Movement','Greater Invisibility','Hallucinatory Terrain','Locate Creature','Phantasmal Killer','Polymorph','Raulothim\'s Psychic Lance']
bard_fifth = ['Animate Objects','Awaken','Dominate Person','Dream','Geas','Greater Restoration','Hold Monster','Legend Lore','Mass Cure Wounds','Mislead','Modify Memory','Planar Binding','Raise Dead','Rary\'s Telepathic Bond','Scrying','Seeming','Skill Empowerment','Synaptic Static','Teleportation Circle']
bard_sixth = ['Eyebite','Find the Path','Guards and Wards','Heroes\' Feast','Mass Suggestion','Otto\'s Irresistible Dance','Programmed Illusion','True Seeing']
bard_seventh = ['Dream of the Blue Veil','Etherealness','Forcecage','Mirage Arcane','Mordenkainen\'s Magnificent Mansion','Mordenkainen\'s Sword','Prismatic Spray','Project Image','Regenerate','Resurrection','Symbol','Teleport']
bard_eighth = ['Antipathy/Sympathy','Dominate Monster','Feeblemind','Glibness','Mind Blank','Power Word: Stun']
bard_ninth = ['Foresight','Mass Polymorph','Power Word: Heal','Power Word: Kill','Prismatic Wall','Psychic Scream','True Polymorph']
bard_ritual_first = ['Comprehend Languages','Detect Magic','Identify','Illusory Script','Speak with Animals','Unseen Servant']


# Select two bard cantrips and get four 1st level spells
def bard_magic():
    x=1
    y=1
    while x < 4:
        if x<3:
            print(f'{x}/2')
            dnd_skills.spell_add(bard_cantrip,dnd_dict.character_dict['spells']['cantrips'],dnd_dict.character_dict['class_spells']['bard_cantrips'])
            x+=1
        elif x == 3:
            while y < 6:
                if y < 5:
                    print(f'{y}/4')
                    dnd_skills.spell_add(bard_first,dnd_dict.character_dict['spells']['first'],dnd_dict.character_dict['class_spells']['bard']['first'])
                    y+=1
                elif y ==5:
                    y+=1
                    x+=1
                    break


# Magical Secrets function. Select two of the spells that you will use.
# Put cantrips and leveled spells as separate choices, since you can switch out the latter
def magical_secrets6():
    x = 1
    while x < 3:
        while True:
            print(f'{x}/2')
            choice = input("""What level do you want to select from?
1) Cantrip
2) First
3) Second
4) Third
Enter your Selection: """)
    
            if choice == '1':
# Put in if you want the Dunamancy Cantrips.
                new_cantrip = artificer_cantrip + bard_cantrip + cleric_cantrip + druid_cantrip + sorcerer_cantrip + warlock_cantrip + all_wizard_cantrip

                cantrips = []
# Remove duplicates
                [cantrips.append(x) for x in new_cantrip if x not in cantrips]
# Put in alphabetical order
                cantrips.sort()
                dnd_skills.spell_add(cantrips,dnd_dict.character_dict['spells']['cantrips'],dnd_dict.character_dict['class_spells']['bard_cantrips'])
                x+=1
                break

            elif choice == '2':
# Combine all of the leveled spells into a single list
                new_spells = artificer_first_classless + bard_first + cleric_first_classless + druid_first_classless + paladin_first_classless + ranger_first + sorcerer_first + warlock_first + all_wizard_first
                first_spell = []
# Remove duplicates
                [first_spell.append(x) for x in new_spells if x not in first_spell]
# Put in alphabetical order
                first_spell.sort()
                dnd_skills.spell_add(first_spell,dnd_dict.character_dict['spells']['first'],dnd_dict.character_dict['class_spells']['bard']['first'])
                x+=1
                break

            elif choice == '3':
                new_spells = artificer_second_classless + bard_second + cleric_second_classless + druid_second_classless + paladin_second_classless + ranger_second + sorcerer_second + warlock_second + all_wizard_second
                second_spell = []
                [second_spell.append(x) for x in new_spells if x not in second_spell]
                second_spell.sort()
                dnd_skills.spell_add(second_spell,dnd_dict.character_dict['spells']['second'],dnd_dict.character_dict['class_spells']['bard']['second'])
                x+=1
                break

            elif choice == '4':
                new_spells = artificer_third_classless + bard_third + cleric_third_classless + druid_third_classless + paladin_third_classless + ranger_third + sorcerer_third + warlock_third + all_wizard_third
                third_spell = []
                [third_spell.append(x) for x in new_spells if x not in third_spell]
                third_spell.sort()
                dnd_skills.spell_add(third_spell,dnd_dict.character_dict['spells']['third'],dnd_dict.character_dict['class_spells']['bard']['third'])
                x+=1
                break

            else:
                print("Error: Invalid Input")
                continue


def magical_secrets10():
    x = 1
    while x < 3:
        while True:
            print(f'{x}/2')
            choice = input("""What level do you want to select from?
1) Cantrip
2) First
3) Second
4) Third
5) Fourth
6) Fifth
Enter your Selection: """)
    
            if choice == '1':
# Put in if you want the Dunamancy Cantrips.
                new_cantrip = artificer_cantrip + bard_cantrip + cleric_cantrip + druid_cantrip + sorcerer_cantrip + warlock_cantrip + all_wizard_cantrip

                cantrips = []
# Remove duplicates
                [cantrips.append(x) for x in new_cantrip if x not in cantrips]
# Put in alphabetical order
                cantrips.sort()
                dnd_skills.spell_add(cantrips,dnd_dict.character_dict['spells']['cantrips'],dnd_dict.character_dict['class_spells']['bard_cantrips'])
                x+=1
                break

            elif choice == '2':
# Combine all of the leveled spells into a single list
                new_spells = artificer_first_classless + bard_first + cleric_first_classless + druid_first_classless + paladin_first_classless + ranger_first + sorcerer_first + warlock_first + all_wizard_first
                first_spell = []
# Remove duplicates
                [first_spell.append(x) for x in new_spells if x not in first_spell]
# Put in alphabetical order
                first_spell.sort()
                dnd_skills.spell_add(first_spell,dnd_dict.character_dict['spells']['first'],dnd_dict.character_dict['class_spells']['bard']['first'])
                x+=1
                break

            elif choice == '3':
                new_spells = artificer_second_classless + bard_second + cleric_second_classless + druid_second_classless + paladin_second_classless + ranger_second + sorcerer_second + warlock_second + all_wizard_second
                second_spell = []
                [second_spell.append(x) for x in new_spells if x not in second_spell]
                second_spell.sort()
                dnd_skills.spell_add(second_spell,dnd_dict.character_dict['spells']['second'],dnd_dict.character_dict['class_spells']['bard']['second'])
                x+=1
                break

            elif choice == '4':
                new_spells = artificer_third_classless + bard_third + cleric_third_classless + druid_third_classless + paladin_third_classless + ranger_third + sorcerer_third + warlock_third + all_wizard_third
                third_spell = []
                [third_spell.append(x) for x in new_spells if x not in third_spell]
                third_spell.sort()
                dnd_skills.spell_add(third_spell,dnd_dict.character_dict['spells']['third'],dnd_dict.character_dict['class_spells']['bard']['third'])
                x+=1
                break

            elif choice == '5':
                new_spells = artificer_fourth_classless + bard_fourth + cleric_fourth_classless + druid_fourth_classless + paladin_fourth_classless + ranger_fourth + sorcerer_fourth + warlock_fourth + all_wizard_fourth
                fourth_spell = []
                [fourth_spell.append(x) for x in new_spells if x not in fourth_spell]
                fourth_spell.sort()
                dnd_skills.spell_add(fourth_spell,dnd_dict.character_dict['spells']['fourth'],dnd_dict.character_dict['class_spells']['bard']['fourth'])
                x+=1
                break

            elif choice == '6':
                new_spells = artificer_fifth_classless + bard_fifth + cleric_fifth_classless + druid_fifth_classless + paladin_fifth_classless + ranger_fifth + sorcerer_fifth + warlock_fifth + all_wizard_fifth
                fifth_spell = []
                [fifth_spell.append(x) for x in new_spells if x not in fifth_spell]
                fifth_spell.sort()
                dnd_skills.spell_add(fifth_spell,dnd_dict.character_dict['spells']['fifth'],dnd_dict.character_dict['class_spells']['bard']['fifth'])
                x+=1
                break

            else:
                print("Error: Invalid Input")
                continue


def magical_secrets14():
    x = 1
    while x < 3:
        while True:
            print(f'{x}/2')
            choice = input("""What level do you want to select from?
1) Cantrip
2) First
3) Second
4) Third
5) Fourth
6) Fifth
7) Sixth
8) Seventh
Enter your Selection: """)
    
            if choice == '1':
# Put in if you want the Dunamancy Cantrips.
                new_cantrip = artificer_cantrip + bard_cantrip + cleric_cantrip + druid_cantrip + sorcerer_cantrip + warlock_cantrip + all_wizard_cantrip

                cantrips = []
# Remove duplicates
                [cantrips.append(x) for x in new_cantrip if x not in cantrips]
# Put in alphabetical order
                cantrips.sort()
                dnd_skills.spell_add(cantrips,dnd_dict.character_dict['spells']['cantrips'],dnd_dict.character_dict['class_spells']['bard_cantrips'])
                x+=1
                break

            elif choice == '2':
# Combine all of the leveled spells into a single list
                new_spells = artificer_first_classless + bard_first + cleric_first_classless + druid_first_classless + paladin_first_classless + ranger_first + sorcerer_first + warlock_first + all_wizard_first
                first_spell = []
# Remove duplicates
                [first_spell.append(x) for x in new_spells if x not in first_spell]
# Put in alphabetical order
                first_spell.sort()
                dnd_skills.spell_add(first_spell,dnd_dict.character_dict['spells']['first'],dnd_dict.character_dict['class_spells']['bard']['first'])
                x+=1
                break

            elif choice == '3':
                new_spells = artificer_second_classless + bard_second + cleric_second_classless + druid_second_classless + paladin_second_classless + ranger_second + sorcerer_second + warlock_second + all_wizard_second
                second_spell = []
                [second_spell.append(x) for x in new_spells if x not in second_spell]
                second_spell.sort()
                dnd_skills.spell_add(second_spell,dnd_dict.character_dict['spells']['second'],dnd_dict.character_dict['class_spells']['bard']['second'])
                x+=1
                break

            elif choice == '4':
                new_spells = artificer_third_classless + bard_third + cleric_third_classless + druid_third_classless + paladin_third_classless + ranger_third + sorcerer_third + warlock_third + all_wizard_third
                third_spell = []
                [third_spell.append(x) for x in new_spells if x not in third_spell]
                third_spell.sort()
                dnd_skills.spell_add(third_spell,dnd_dict.character_dict['spells']['third'],dnd_dict.character_dict['class_spells']['bard']['third'])
                x+=1
                break

            elif choice == '5':
                new_spells = artificer_fourth_classless + bard_fourth + cleric_fourth_classless + druid_fourth_classless + paladin_fourth_classless + ranger_fourth + sorcerer_fourth + warlock_fourth + all_wizard_fourth
                fourth_spell = []
                [fourth_spell.append(x) for x in new_spells if x not in fourth_spell]
                fourth_spell.sort()
                dnd_skills.spell_add(fourth_spell,dnd_dict.character_dict['spells']['fourth'],dnd_dict.character_dict['class_spells']['bard']['fourth'])
                x+=1
                break

            elif choice == '6':
                new_spells = artificer_fifth_classless + bard_fifth + cleric_fifth_classless + druid_fifth_classless + paladin_fifth_classless + ranger_fifth + sorcerer_fifth + warlock_fifth + all_wizard_fifth
                fifth_spell = []
                [fifth_spell.append(x) for x in new_spells if x not in fifth_spell]
                fifth_spell.sort()
                dnd_skills.spell_add(fifth_spell,dnd_dict.character_dict['spells']['fifth'],dnd_dict.character_dict['class_spells']['bard']['fifth'])
                x+=1
                break

            elif choice == '7':
                new_spells = bard_sixth + cleric_sixth_classless + druid_sixth_classless + sorcerer_sixth + warlock_sixth + all_wizard_sixth
                sixth_spell = []
                [sixth_spell.append(x) for x in new_spells if x not in sixth_spell]
                sixth_spell.sort()
                dnd_skills.spell_add(sixth_spell,dnd_dict.character_dict['spells']['sixth'],dnd_dict.character_dict['class_spells']['bard']['sixth'])
                x+=1
                break

            elif choice == '8':
                new_spells = bard_seventh + cleric_seventh_classless + druid_seventh_classless + sorcerer_seventh + warlock_seventh + all_wizard_seventh
                seventh_spell = []
                [seventh_spell.append(x) for x in new_spells if x not in seventh_spell]
                seventh_spell.sort()
                dnd_skills.spell_add(seventh_spell,dnd_dict.character_dict['spells']['seventh'],dnd_dict.character_dict['class_spells']['bard']['seventh'])
                x+=1
                break

            else:
                print("Error: Invalid Input")
                continue


def magical_secrets18():
    x = 1
    while x < 3:
        while True:
            print(f'{x}/2')
            choice = input("""What level do you want to select from?
1) Cantrip
2) First
3) Second
4) Third
5) Fourth
6) Fifth
7) Sixth
8) Seventh
9) Eighth
10) Ninth
Enter your Selection: """)
    
            if choice == '1':
# Put in if you want the Dunamancy Cantrips.
                new_cantrip = artificer_cantrip + bard_cantrip + cleric_cantrip + druid_cantrip + sorcerer_cantrip + warlock_cantrip + all_wizard_cantrip

                cantrips = []
# Remove duplicates
                [cantrips.append(x) for x in new_cantrip if x not in cantrips]
# Put in alphabetical order
                cantrips.sort()
                dnd_skills.spell_add(cantrips,dnd_dict.character_dict['spells']['cantrips'],dnd_dict.character_dict['class_spells']['bard_cantrips'])
                x+=1
                break

            elif choice == '2':
# Combine all of the leveled spells into a single list
                new_spells = artificer_first_classless + bard_first + cleric_first_classless + druid_first_classless + paladin_first_classless + ranger_first + sorcerer_first + warlock_first + all_wizard_first
                first_spell = []
# Remove duplicates
                [first_spell.append(x) for x in new_spells if x not in first_spell]
# Put in alphabetical order
                first_spell.sort()
                dnd_skills.spell_add(first_spell,dnd_dict.character_dict['spells']['first'],dnd_dict.character_dict['class_spells']['bard']['first'])
                x+=1
                break

            elif choice == '3':
                new_spells = artificer_second_classless + bard_second + cleric_second_classless + druid_second_classless + paladin_second_classless + ranger_second + sorcerer_second + warlock_second + all_wizard_second
                second_spell = []
                [second_spell.append(x) for x in new_spells if x not in second_spell]
                second_spell.sort()
                dnd_skills.spell_add(second_spell,dnd_dict.character_dict['spells']['second'],dnd_dict.character_dict['class_spells']['bard']['second'])
                x+=1
                break

            elif choice == '4':
                new_spells = artificer_third_classless + bard_third + cleric_third_classless + druid_third_classless + paladin_third_classless + ranger_third + sorcerer_third + warlock_third + all_wizard_third
                third_spell = []
                [third_spell.append(x) for x in new_spells if x not in third_spell]
                third_spell.sort()
                dnd_skills.spell_add(third_spell,dnd_dict.character_dict['spells']['third'],dnd_dict.character_dict['class_spells']['bard']['third'])
                x+=1
                break

            elif choice == '5':
                new_spells = artificer_fourth_classless + bard_fourth + cleric_fourth_classless + druid_fourth_classless + paladin_fourth_classless + ranger_fourth + sorcerer_fourth + warlock_fourth + all_wizard_fourth
                fourth_spell = []
                [fourth_spell.append(x) for x in new_spells if x not in fourth_spell]
                fourth_spell.sort()
                dnd_skills.spell_add(fourth_spell,dnd_dict.character_dict['spells']['fourth'],dnd_dict.character_dict['class_spells']['bard']['fourth'])
                x+=1
                break

            elif choice == '6':
                new_spells = artificer_fifth_classless + bard_fifth + cleric_fifth_classless + druid_fifth_classless + paladin_fifth_classless + ranger_fifth + sorcerer_fifth + warlock_fifth + all_wizard_fifth
                fifth_spell = []
                [fifth_spell.append(x) for x in new_spells if x not in fifth_spell]
                fifth_spell.sort()
                dnd_skills.spell_add(fifth_spell,dnd_dict.character_dict['spells']['fifth'],dnd_dict.character_dict['class_spells']['bard']['fifth'])
                x+=1
                break

            elif choice == '7':
                new_spells = bard_sixth + cleric_sixth_classless + druid_sixth_classless + sorcerer_sixth + warlock_sixth + all_wizard_sixth
                sixth_spell = []
                [sixth_spell.append(x) for x in new_spells if x not in sixth_spell]
                sixth_spell.sort()
                dnd_skills.spell_add(sixth_spell,dnd_dict.character_dict['spells']['sixth'],dnd_dict.character_dict['class_spells']['bard']['sixth'])
                x+=1
                break

            elif choice == '8':
                new_spells = bard_seventh + cleric_seventh_classless + druid_seventh_classless + sorcerer_seventh + warlock_seventh + all_wizard_seventh
                seventh_spell = []
                [seventh_spell.append(x) for x in new_spells if x not in seventh_spell]
                seventh_spell.sort()
                dnd_skills.spell_add(seventh_spell,dnd_dict.character_dict['spells']['seventh'],dnd_dict.character_dict['class_spells']['bard']['seventh'])
                x+=1
                break

            elif choice == '9':
                new_spells = bard_eighth + cleric_eighth_classless + druid_eighth_classless + sorcerer_eighth + warlock_eighth + all_wizard_eighth
                eighth_spell = []
                [eighth_spell.append(x) for x in new_spells if x not in eighth_spell]
                eighth_spell.sort()
                dnd_skills.spell_add(eighth_spell,dnd_dict.character_dict['spells']['eighth'],dnd_dict.character_dict['class_spells']['bard']['eighth'])
                x+=1
                break

            elif choice == '10':
                new_spells = bard_ninth + cleric_ninth_classless + druid_ninth_classless + sorcerer_ninth + warlock_ninth + all_wizard_ninth
                ninth_spell = []
                [ninth_spell.append(x) for x in new_spells if x not in ninth_spell]
                ninth_spell.sort()
                dnd_skills.spell_add(ninth_spell,dnd_dict.character_dict['spells']['ninth'],dnd_dict.character_dict['class_spells']['bard']['ninth'])
                x+=1
                break

            else:
                print("Error: Invalid Input")
                continue





#####################################################################

# Cleric Cantrips
cleric_cantrip = ['Guidance','Light','Mending','Resistance','Sacred Flame','Spare the Dying','Thaumaturgy','Toll the Dead','Word of Radiance']

# Used for learning from other classes, like the Bard's Magical Secrets Feature
cleric_first_classless = ['Bane','Bless','Ceremony','Command','Create or Destroy Water','Cure Wounds','Detect Evil and Good','Detect Poison and Disease','Guiding Bolt','Healing Word','Inflict Wounds','Protection from Evil and Good','Purify Food and Drink','Sanctuary','Shield of Faith'] 

cleric_second_classless = ['Aid','Augury','Blindness/Deafness','Borrowed Knowledge','Calm Emotions','Continual Flame','Enhance Ability','Find Traps','Gentle Repose','Hold Person','Lesser Restoration','Locate Object','Prayer of Healing','Protection from Poison','Silence','Spiritual Weapon','Warding Bond','Zone of Truth']

cleric_third_classless = ['Animate Dead','Aura of Vitality','Beacon of Hope','Bestow Curse','Clairvoyance','Create Food and Water','Daylight','Dispel Magic','Fast Friends','Feign Death','Glyph of Warding','Incite Greed','Life Transference','Magic Circle','Mass Healing Word','Meld into Stone','Motivational Speech','Protection from Energy','Remove Curse','Revivify','Sending','Speak with Dead','Spirit Guardians','Spirit Shroud','Tongues','Water Walk']

cleric_fourth_classless = ['Aura of Life','Aura of Purity','Banishment','Control Water','Death Ward','Divination','Freedom of Movement','Guardian of Faith','Locate Creature','Stone Shape']

cleric_fifth_classless = ['Commune','Contagion','Dawn','Dispel Good and Evil','Flame Strike','Geas','Greater Restoration','Hallow','Holy Weapon','Insect Plague','Legend Lore','Mass Cure Wounds','Planar Binding','Raise Dead','Scrying','Summon Celestial']

cleric_sixth_classless = ['Blade Barrier','Create Undead','Find the Path','Forbiddance','Harm','Heal','Heroes\' Feast','Planar Ally','Sunbeam','True Seeing','Word of Recall']

cleric_seventh_classless = ['Conjure Celestial','Divine Word','Etherealness','Fire Storm','Plane Shift','Regenerate','Resurrection','Symbol','Temple of the Gods']

cleric_eighth_classless = ['Antimagic Field','Control Weather','Earthquake','Holy Aura','Sunburst']

cleric_ninth_classless = ['Astral Projection','Gate','Mass Heal','Power Word: Heal','True Resurrection']

cleric_ritual_first = ['Ceremony','Detect Magic','Detect Poison and Disease','Purify Food and Drink']

def cleric_first():
        cleric_spell = {'bane':'Bane', 'bless':'Bless', 'ceremony':'Ceremony', 'command':'Command', 'create_or_destroy_water':'Create or Destroy Water', 'cure_wounds':'Cure Wounds', 'detect_evil_and_good':'Detect Evil and Good', 'detect_poison_and_disease':'Detect Poison and Disease', 'guiding_bolt':'Guiding Bolt', 'healing_word':'Healing Word', 'inflict_wounds':'Inflict Wounds', 'protection_from_evil_and_good':'Protection from Evil and Good', 'purify_food_and_drink':'Purify Food and Drink', 'sanctuary':'Sanctuary', 'shield_of_faith':'Shield of Faith'}
        dnd_dict.character_dict['class_spells']['cleric']['first'].update(cleric_spell)
        dnd_dict.character_dict['spells']['first'].update(cleric_spell)
        dnd_dict.character_dict['special_spells']['first'].update(cleric_spell)

def cleric_second():
        cleric_spell = {'aid':'Aid','augury':'Augury','blindness/deafness':'Blindness/Deafness','borrowed_knowledge':'Borrowed Knowledge','calm_emotions':'Calm Emotions','continual_flame':'Continual Flame','enhance_ability':'Enhance Ability','find_traps':'Find Traps','gentle_repose':'Gentle Repose','hold_person':'Hold Person','lesser_restoration':'Lesser Restoration','locate_object':'Locate Object','prayer_of_healing':'Prayer of Healing','protection_from_poison':'Protection from Poison','silence':'Silence','spiritual_weapon':'Spiritual Weapon','warding_bond':'Warding Bond','zone_of_truth':'Zone of Truth'}
        dnd_dict.character_dict['class_spells']['cleric']['second'].update(cleric_spell)
        dnd_dict.character_dict['spells']['second'].update(cleric_spell)
        dnd_dict.character_dict['special_spells']['second'].update(cleric_spell)

def cleric_third():
        cleric_spell = {'animate_dead':'Animate Dead','aura_of_vitality':'Aura of Vitality','beacon_of_hope':'Beacon of Hope','bestow_curse':'Bestow Curse','clairvoyance':'Clairvoyance','create_food_and_water':'Create Food and Water','daylight':'Daylight','dispel_magic':'Dispel Magic','fast_friends':'Fast Friends','feign_death':'Feign Death','glyph_of_warding':'Glyph of Warding','incite_greed':'Incite Greed','life_transference':'Life Transference','magic_circle':'Magic Circle','mass_healing_word':'Mass Healing Word','meld_into_stone':'Meld into Stone','motivational_speech':'Motivational Speech','protection_from_energy':'Protection from Energy','remove_curse':'Remove Curse','revivify':'Revivify','sending':'Sending','speak_with_dead':'Speak with Dead','spirit_guardians':'Spirit Guardians','spirit_shroud':'Spirit Shroud','tongues':'Tongues','water_walk':'Water Walk'}
        dnd_dict.character_dict['class_spells']['cleric']['third'].update(cleric_spell)
        dnd_dict.character_dict['spells']['third'].update(cleric_spell)
        dnd_dict.character_dict['special_spells']['third'].update(cleric_spell)

def cleric_fourth():
        cleric_spell = {'aura_of_life':'Aura of Life','aura_of_purity':'Aura of Purity','banishment':'Banishment','control_water':'Control Water','death_ward':'Death Ward','divination':'Divination','freedom_of_movement':'Freedom of Movement','guardian_of_faith':'Guardian of Faith','locate_creature':'Locate Creature','stone_shape':'Stone Shape'}
        dnd_dict.character_dict['class_spells']['cleric']['fourth'].update(cleric_spell)
        dnd_dict.character_dict['spells']['fourth'].update(cleric_spell)
        dnd_dict.character_dict['special_spells']['fourth'].update(cleric_spell)

def cleric_fifth():
        cleric_spell = {'commune':'Commune','contagion':'Contagion','dawn':'Dawn','dispel_good_and_evil':'Dispel Good and Evil','flame_strike':'Flame Strike','geas':'Geas','greater_restoration':'Greater Restoration','hallow':'Hallow','holy_weapon':'Holy Weapon','insect_plague':'Insect Plague','legend_lore':'Legend Lore','mass_cure_wounds':'Mass Cure Wounds','planar_binding':'Planar Binding','raise_dead':'Raise Dead','scrying':'Scrying','summon_celestial':'Summon Celestial'}
        dnd_dict.character_dict['class_spells']['cleric']['fifth'].update(cleric_spell)
        dnd_dict.character_dict['spells']['fifth'].update(cleric_spell)
        dnd_dict.character_dict['special_spells']['fifth'].update(cleric_spell)

def cleric_sixth():
        cleric_spell = {'blade_barrier':'Blade Barrier','create_undead':'Create Undead','find_the_path':'Find the Path','forbiddance':'Forbiddance','harm':'Harm','heal':'Heal','heroes\'_feast':'Heroes\' Feast','planar_ally':'Planar Ally','sunbeam':'Sunbeam','true_seeing':'True Seeing','word_of_recall':'Word of Recall'}
        dnd_dict.character_dict['class_spells']['cleric']['sixth'].update(cleric_spell)
        dnd_dict.character_dict['spells']['sixth'].update(cleric_spell)
        dnd_dict.character_dict['special_spells']['sixth'].update(cleric_spell)

def cleric_seventh():
        cleric_spell = {'conjure_celestial':'Conjure Celestial','divine_word':'Divine Word','etherealness':'Etherealness','fire_storm':'Fire Storm','plane_shift':'Plane Shift','regenerate':'Regenerate','resurrection':'Resurrection','symbol':'Symbol','temple_of_the_gods':'Temple of the Gods'}
        dnd_dict.character_dict['class_spells']['cleric']['seventh'].update(cleric_spell)
        dnd_dict.character_dict['spells']['seventh'].update(cleric_spell)
        dnd_dict.character_dict['special_spells']['seventh'].update(cleric_spell)

def cleric_eighth():
        cleric_spell = {'antimagic_field':'Antimagic Field','control_weather':'Control Weather','earthquake':'Earthquake','holy_aura':'Holy Aura','sunburst':'Sunburst'}
        dnd_dict.character_dict['class_spells']['cleric']['eighth'].update(cleric_spell)
        dnd_dict.character_dict['spells']['eighth'].update(cleric_spell)
        dnd_dict.character_dict['special_spells']['eighth'].update(cleric_spell)

def cleric_ninth():
        cleric_spell = {'astral_projection':'Astral Projection','gate':'Gate','mass_heal':'Mass Heal','power_word:_heal':'Power Word: Heal','true_resurrection':'True Resurrection'}
        dnd_dict.character_dict['class_spells']['cleric']['ninth'].update(cleric_spell)
        dnd_dict.character_dict['spells']['ninth'].update(cleric_spell)
        dnd_dict.character_dict['special_spells']['ninth'].update(cleric_spell)




def cleric_magic():
    x=1
    while x < 5:
        if x<4:
            print(f'{x}/3')
            dnd_skills.spell_add(cleric_cantrip,dnd_dict.character_dict['spells']['cantrips'],dnd_dict.character_dict['class_spells']['cleric_cantrips'])
            x+=1
        elif x == 4:
            cleric_first()
            x+=1
            break

########################################################################

druid_cantrip = ['Control Flames','Create Bonfire','Druidcraft','Frostbite','Guidance','Gust','Infestation','Magic Stone','Mending','Mold Earth','Poison Spray','Primal Savagery','Produce Flame','Resistance','Shape Water','Shillelagh','Thornwhip','Thunderclap']

druid_first_classless = ['Absorb Elements','Animal Friendship','Beast Bond','Charm Person','Create or Destroy Water','Cure Wounds','Detect Magic','Detect Poison and Disease','Earth Tremor','Entangle','Faerie Fire','Fog Cloud','Goodberry','Healing Word','Ice Knife','Jump','Longstrider','Purify Food and Drink','Snare','Speak with Animals','Thunderwave']

druid_second_classless = ['Animal Messenger','Augury','Barkskin','Beast Sense','Continual Flame','Darkvision','Dust Devil','Earthbind','Enhance Ability','Enlarge/Reduce','Find Traps','Flame Blade','Flaming Sphere','Gust of Wind','Healing Spirit','Heat Metal','Hold Person','Lesser Restoration','Locate Animals or Plants','Locate Object','Moonbeam','Pass Without Trace','Protection from Poison','Skywrite','Spike Growth','Summon Beast','Warding Wind','Wither and Bloom']

druid_third_classless = ['Aura of Vitality','Call Lightning','Conjure Animals','Daylight','Dispel Magic','Elemental Weapon','Erupting Earth','Feign Death','Flame Arrows','Meld into Stone','Plant Growth','Protection from Energy','Revivify','Sleet Storm','Speak with Plants','Summon Fey','Tidal Wave','Wall of Water','Water Breathing','Water Walk','Wind Wall']

druid_fourth_classless = ['Blight','Charm Monster','Confusion','Conjure Minor Elementals','Conjure Woodland Beings','Control Water','Divination','Dominate Beast','Elemental Bane','Fire Shield','Freedom of Movement','Giant Insect','Grasping Vine','Guardian of Nature','Hallucinatory Terrain','Ice Storm','Locate Creature','Polymorph','Stone Shape','Stoneskin','Summon Elemental','Wall of Fire','Watery Sphere']

druid_fifth_classless = ['Antilife Shell','Awaken','Commune with Nature','Cone of Cold','Conjure Elemental','Contagion','Control Winds','Geas','Greater Restoration','Insect Plague','Maelstrom','Mass Cure Wounds','Planar Binding','Reincarnate','Scrying','Summon Draconic Spirit','Transmute Rock','Tree Stride','Wall of Stone','Wrath of Nature']

druid_sixth_classless = ['Bones of the Earth','Conjure Fey','Druid Grove','Find the Path','Flesh to Stone','Heal','Heroes\' Feast','Investiture of Flame','Investiture of Ice','Investiture of Stone','Investiture of Wind','Move Earth','Primordial Ward','Sunbeam','Transport via Plants','Wall of Thorns','Wind Walk']

druid_seventh_classless = ['Draconic Transformation','Fire Storm','Mirage Arcane','Plane Shift','Regenerate','Reverse Gravity','Symbol','Whirlwind']

druid_eighth_classless = ['Animal Shapes','Antipathy/Sympathy','Control Weather','Earthquake','Feeblemind','Incendiary Cloud','Sunburst','Tsunami']

druid_ninth_classless = ['Foresight','Shapechange','Storm of Vengeance','True Resurrection']

druid_ritual_first = ['Detect Magic','Detect Poison and Disease','Purify Food and Drink','Speak with Animals']

def druid_first():
        druid_spell = {'absorb_elements':'Absorb Elements', 'animal_friendship':'Animal Friendship', 'beast_bond':'Beast Bond', 'charm_person':'Charm Person', 'create_or_destroy_water':'Create or Destroy Water', 'cure_wounds':'Cure Wounds', 'detect_magic':'Detect Magic', 'detect_poison_and_disease':'Detect Poison and Disease', 'earth_tremor':'Earth Tremor', 'entangle':'Entangle', 'faerie_fire':'Faerie Fire', 'fog_cloud':'Fog Cloud', 'goodberry':'Goodberry', 'healing_word':'Healing Word', 'ice_knife':'Ice Knife', 'jump':'Jump', 'longstrider':'Longstrider', 'purify_food_and_drink':'Purify Food and Drink', 'snare':'Snare', 'speak_with_animals':'Speak with Animals', 'thunderwave':'Thunderwave'}
        dnd_dict.character_dict['class_spells']['druid']['first'].update(druid_spell)
        dnd_dict.character_dict['spells']['first'].update(druid_spell)
        dnd_dict.character_dict['special_spells']['first'].update(druid_spell)

def druid_second():
        druid_spell = {'animal_messenger':'Animal Messenger','augury':'Augury','barkskin':'Barkskin','beast_sense':'Beast Sense','continual_flame':'Continual Flame','darkvision':'Darkvision','dust_devil':'Dust Devil','earthbind':'Earthbind','enhance_ability':'Enhance Ability','enlarge/reduce':'Enlarge/Reduce','find_traps':'Find Traps','flame_blade':'Flame Blade','flaming_sphere':'Flaming Sphere','gust_of_wind':'Gust of Wind','healing_spirit':'Healing Spirit','heat_metal':'Heat Metal','hold_person':'Hold Person','lesser_restoration':'Lesser Restoration','locate_animals_or_plants':'Locate Animals or Plants','locate_object':'Locate Object','moonbeam':'Moonbeam','pass_without_trace':'Pass Without Trace','protection_from_poison':'Protection from Poison','skywrite':'Skywrite','spike_growth':'Spike Growth','summon_beast':'Summon Beast','warding_wind':'Warding Wind','wither_and_bloom':'Wither and Bloom'}
        dnd_dict.character_dict['class_spells']['druid']['second'].update(druid_spell)
        dnd_dict.character_dict['spells']['second'].update(druid_spell)
        dnd_dict.character_dict['special_spells']['second'].update(druid_spell)

def druid_third():
        druid_spell = {'aura_of_vitality':'Aura of Vitality','call_lightning':'Call Lightning','conjure_animals':'Conjure Animals','daylight':'Daylight','dispel_magic':'Dispel Magic','elemental_weapon':'Elemental Weapon','erupting_earth':'Erupting Earth','feign_death':'Feign Death','flame_arrows':'Flame Arrows','meld_into_stone':'Meld into Stone','plant_growth':'Plant Growth','protection_from_energy':'Protection from Energy','revivify':'Revivify','sleet_storm':'Sleet Storm','speak_with_plants':'Speak with Plants','summon_fey':'Summon Fey','tidal_wave':'Tidal Wave','wall_of_water':'Wall of Water','water_breathing':'Water Breathing','water_walk':'Water Walk','wind_walk':'Wind Walk'}
        dnd_dict.character_dict['class_spells']['druid']['third'].update(druid_spell)
        dnd_dict.character_dict['spells']['third'].update(druid_spell)
        dnd_dict.character_dict['special_spells']['third'].update(druid_spell)

def druid_fourth():
        druid_spell = {'blight':'Blight','charm_monster':'Charm Monster','confusion':'Confusion','conjure_minor_elementals':'Conjure Minor Elementals','conjure_woodland_beings':'Conjure Woodland Beings','control_water':'Control Water','divination':'Divination','dominate_beast':'Dominate Beast','elemental_bane':'Elemental Bane','fire_shield':'Fire Shield','freedom_of_movement':'Freedom of Movement','giant_insect':'Giant Insect','grasping_vine':'Grasping Vine','guardian_of_nature':'Guardian of Nature','hallucinatory_terrain':'Hallucinatory Terrain','ice_storm':'Ice Storm','locate_creature':'Locate Creature','polymorph':'Polymorph','stone_shape':'Stone Shape','stoneskin':'Stoneskin','summon_elemental':'Summon Elemental','wall_of_fire':'Wall of Fire','watery_sphere':'Watery Sphere'}
        dnd_dict.character_dict['class_spells']['druid']['fourth'].update(druid_spell)
        dnd_dict.character_dict['spells']['fourth'].update(druid_spell)
        dnd_dict.character_dict['special_spells']['fourth'].update(druid_spell)

def druid_fifth():
        druid_spell = {'antilife_shell':'Antilife Shell','awaken':'Awaken','commune_with_nature':'Commune with Nature','cone_of_cold':'Cone of Cold','conjure_elemental':'Conjure Elemental','contagion':'Contagion','control_winds':'Control Winds','geas':'Geas','greater_restoration':'Greater Restoration','insect_plague':'Insect Plague','maelstrom':'Maelstrom','mass_cure_wounds':'Mass Cure Wounds','planar_binding':'Planar Binding','reincarnate':'Reincarnate','scrying':'Scrying','summon_draconic_spirit':'Summon Draconic Spirit','transmute_rock':'Transmute Rock','tree_stride':'Tree Stride','wall_of_stone':'Wall of Stone','wrath_of_nature':'Wrath of Nature'}
        dnd_dict.character_dict['class_spells']['druid']['fifth'].update(druid_spell)
        dnd_dict.character_dict['spells']['fifth'].update(druid_spell)
        dnd_dict.character_dict['special_spells']['fifth'].update(druid_spell)

def druid_sixth():
        druid_spell = {'bones_of_the_earth':'Bones of the Earth','conjure_fey':'Conjure Fey','druid_grove':'Druid Grove','find_the_path':'Find the Path','flesh_to_stone':'Flesh to Stone','heal':'Heal','heroes\'_feast':'Heroes\' Feast','investiture_of_flame':'Investiture of Flame','investiture_of_ice':'Investiture of Ice','investiture_of_stone':'Investiture of Stone','investiture_of_wind':'Investiture of Wind','move_earth':'Move Earth','primordial_ward':'Primordial Ward','sunbeam':'Sunbeam','transport_via_plants':'Transport via Plants','wall_of_thorns':'Wall of Thorns','wind_walk':'Wind Walk'}
        dnd_dict.character_dict['class_spells']['druid']['sixth'].update(druid_spell)
        dnd_dict.character_dict['spells']['sixth'].update(druid_spell)
        dnd_dict.character_dict['special_spells']['sixth'].update(druid_spell)

def druid_seventh():
        druid_spell = {'draconic_transformation':'Draconic Transformation','fire_storm':'Fire Storm','mirage_arcane':'Mirage Arcane','plane_shift':'Plane Shift','regenerate':'Regenerate','reverse_gravity':'Reverse Gravity','symbol':'Symbol','whirlwind':'Whirlwind'}
        dnd_dict.character_dict['class_spells']['druid']['seventh'].update(druid_spell)
        dnd_dict.character_dict['spells']['seventh'].update(druid_spell)
        dnd_dict.character_dict['special_spells']['seventh'].update(druid_spell)

def druid_eighth():
        druid_spell = {'animal_shapes':'Animal Shapes','antipathy/sympathy':'Antipathy/Sympathy','control_weather':'Control Weather','earthquake':'Earthquake','feeblemind':'Feeblemind','incendiary_cloud':'Incendiary Cloud','sunburst':'Sunburst','tsunami':'Tsunami'}
        dnd_dict.character_dict['class_spells']['druid']['eighth'].update(druid_spell)
        dnd_dict.character_dict['spells']['eighth'].update(druid_spell)
        dnd_dict.character_dict['special_spells']['eighth'].update(druid_spell)

def druid_ninth():
        druid_spell = {'foresight':'Foresight','shapechange':'Shapechange','storm_of_vengeance':'Storm of Vengeance','true_resurrection':'True Resurrection'}
        dnd_dict.character_dict['class_spells']['druid']['ninth'].update(druid_spell)
        dnd_dict.character_dict['spells']['ninth'].update(druid_spell)
        dnd_dict.character_dict['special_spells']['ninth'].update(druid_spell)




# Used for learning from other classes, like the Bard's Magical Secrets Feature

def druid_magic():
    x=1
    while x < 4:
        if x<3:
            print(f'{x}/2')
            dnd_skills.spell_add(druid_cantrip,dnd_dict.character_dict['spells']['cantrips'],dnd_dict.character_dict['class_spells']['druid_cantrips'])
            x+=1
        elif x == 3:
            druid_first()
            x+=1
            break
################################################################

paladin_first_classless = ['Bless','Ceremony','Command','Compelled Duel','Cure Wounds','Detect Evil and Good','Detect Magic','Detect Poison and Disease','Divine Favor','Heroism','Protection from Evil and Good','Purify Food and Drink','Searing Smite','Shield of Faith','Thunderous Smite','Wrathful Smite']

paladin_second_classless = ['Aid','Branding Smite','Find Steed','Gentle Repose','Lesser Restoration','Locate Object','Magic Weapon','Prayer of Healing','Protection from Poison','Warding Bond','Zone of Truth']

paladin_third_classless = ['Aura of Vitality','Blinding Smite','Create Food and Water','Crusader\'s Mantle','Daylight','Dispel Magic','Elemental Weapon','Magic Circle','Remove Curse','Revivify','Spirit Shroud']

paladin_fourth_classless = ['Aura of Life','Aura of Purity','Banishment','Death Ward','Find Greater Steed','Locate Creature','Staggering Smite']

paladin_fifth_classless = ['Banishing Smite','Circle of Power','Destructive Wave','Dispel Evil and Good','Geas','Holy Weapon','Raise Dead','Summon Celestial']


def paladin_first():
        paladin_spell = {'bless':'Bless','ceremony':'Ceremony','command':'Command','compelled_duel':'Compelled Duel','cure_wounds':'Cure Wounds','detect_evil_and_good':'Detect Evil and Good','detect_magic':'Detect Magic','detect_poison_and_disease':'Detect Poison and Disease','divine_favor':'Divine Favor','heroism':'Heroism','protection_from_evil_and_good':'Protection from Evil and Good','purify_food_and_drink':'Purify Food and Drink','searing_smite':'Searing Smite','shield_of_faith':'Shield of Faith','thunderous_smite':'Thunderous Smite','wrathful_smite':'Wrathful Smite'}
        dnd_dict.character_dict['class_spells']['paladin']['first'].update(paladin_spell)
        dnd_dict.character_dict['spells']['first'].update(paladin_spell)
        dnd_dict.character_dict['special_spells']['first'].update(paladin_spell)

def paladin_second():
        paladin_spell = {'aid':'Aid','branding_smite':'Branding Smite','find_steed':'Find Steed','gentle_repose':'Gentle Repose','lesser_restoration':'Lesser Restoration','locate_object':'Locate Object','magic_weapon':'Magic Weapon','prayer_of_healing':'Prayer of Healing','protection_from_poison':'Protection from Poison','warding_bond':'Warding Bond','zone_of_truth':'Zone of Truth'}
        dnd_dict.character_dict['class_spells']['paladin']['second'].update(paladin_spell)
        dnd_dict.character_dict['spells']['second'].update(paladin_spell)
        dnd_dict.character_dict['special_spells']['second'].update(paladin_spell)

def paladin_third():
        paladin_spell = {'aura_of_vitality':'Aura of Vitality','blinding_smite':'Blinding Smite','create_food_and_water':'Create Food and Water','crusader\'s_mantle':'Crusader\'s Mantle','daylight':'Daylight','dispel_magic':'Dispel Magic','elemental_weapon':'Elemental Weapon','magic_circle':'Magic Circle','remove_curse':'Remove Curse','revivify':'Revivify','spirit_shroud':'Spirit Shroud'}
        dnd_dict.character_dict['class_spells']['paladin']['third'].update(paladin_spell)
        dnd_dict.character_dict['spells']['third'].update(paladin_spell)
        dnd_dict.character_dict['special_spells']['third'].update(paladin_spell)

def paladin_fourth():
        paladin_spell = {'aura_of_life':'Aura of Life','aura_of_purity':'Aura of Purity','banishment':'Banishment','death_ward':'Death Ward','find_greater_steed':'Find Greater Steed','locate_creature':'Locate Creature','staggering_smite':'Staggering Smite'}
        dnd_dict.character_dict['class_spells']['paladin']['fourth'].update(paladin_spell)
        dnd_dict.character_dict['spells']['fourth'].update(paladin_spell)
        dnd_dict.character_dict['special_spells']['fourth'].update(paladin_spell)

def paladin_fifth():
        paladin_spell = {'banishing_smite':'Banishing Smite','circle_of_power':'Circle of Power','destructive_wave':'Destructive Wave','dispel_evil_and_good':'Dispel Evil and Good','geas':'Geas','holy_weapon':'Holy Weapon','raise_dead':'Raise Dead','summon_celestial':'Summon Celestial'}
        dnd_dict.character_dict['class_spells']['paladin']['fifth'].update(paladin_spell)
        dnd_dict.character_dict['spells']['fifth'].update(paladin_spell)
        dnd_dict.character_dict['special_spells']['fifth'].update(paladin_spell)


#################################################################

ranger_first = ['Absorb Elements','Alarm','Animal Friendship','Beast Bond','Cure Wounds','Detect Magic','Detect Poison and Disease','Ensnaring Strike','Entangle','Fog Cloud','Goodberry','Hail of Thorns','Hunter\'s Mark','Jump','Longstrider','Searing Strike','Snare','Speak with Animals','Zephyr Strike']

ranger_second = ['Aid','Animal Messenger','Barkskin','Beast Sense','Cordon of Arrows','Darkvision','Enhance Ability','Find Traps','Gust of Wind','Healing Spirit','Lesser Restoration','Locate Animals or Plants','Locate Object','Magic Weapon','Pass Without Trace','Protection from Poison','Silence','Spike Growth','Summon Beast']

ranger_third = ['Ashardalon\'s Stride','Conjure Animals','Conjure Barrage','Daylight','Elemental Weapon','Flame Arrows','Lightning Arrow','Meld into Stone','Nondetection','Plant Growth','Protection from Energy','Revivify','Speak with Plants','Summon Fey','Water Breathing','Water Walk','Wind Wall']

ranger_fourth = ['Conjure Woodland Beings','Dominate Beast','Freedom of Movement','Grasping Vine','Guardian of Nature','Locate Creature','Stoneskin','Summon Elemental']

ranger_fifth = ['Commune with Nature','Conjure Volley','Greater Restoration','Steel Wind Strike','Swift Quiver','Tree Stride','Wrath of Nature']





##################################################################
sorcerer_cantrip =['Acid Splash','Blade Ward','Booming Blade','Chill Touch','Control Flames','Create Bonfire','Dancing Lights','Fire Bolt','Friends','Frostbite','Green-Flame Blade','Gust','Infestation','Light','Lightning Lure','Mage Hand','Mending','Message','Mind Sliver','Minor Illusion','Mold Earth','Poison Spray','Prestidigitation','Ray of Frost','Shape Water','Shocking Grasp','Sword Burst','Thunderclap','True Strike']

sorcerer_first = ['Absorb Elements','Burning Hands','Catapult','Chaos Bolt','Charm Person','Chromatic Orb','Color Spray','Comprehend Languages','Detect Magic','Disguise Self','Distort Value','Earth Tremor','Expeditious Retreat','False Life','Feather Fall','Fog Cloud','Ice Knife','Jump','Mage Armor','Magic Missile','Ray of Sickness','Shield','Silent Image','Silvery Barbs','Sleep','Tasha\'s Caustic Brew','Thunderwave','Witch Bolt']

sorcerer_second = ['Aganazzar\'s Scorcher','Alter Self','Blindness/Deafness','Blur','Cloud of Daggers','Crown of Madness','Darkness','Darkvision','Detect Thoughts','Dragon\'s Breath','Dust Devil','Earthbind','Enhance Ability','Enlarge/Reduce','Flame Blade','Flaming Sphere','Gust of Wind','Hold Person','Invisibility','Kinetic Jaunt','Knock','Levitate','Magic Weapon','Maximillian\'s Earthen Grasp','Mind Spike','Mirror Image','Misty Step','Nathair\'s Mischief','Phantasmal Force','Pyrotechnics','Rime\'s Binding Ice','Scorching Ray','See Invisibility','Shadow Blade','Shatter','Snilloc\'s Snowball Storm','Spider Climb','Suggestion','Tasha\'s Mind Whip','Vortex Warp','Warding Wind','Web','Wither and Bloom']

sorcerer_third = ['Ashardalon\'s Stride','Blink','Catnap','Clairvoyance','Conjure Lesser Demon','Counterspell','Daylight','Dispel Magic','Enemies Abound','Erupting Earth','Fear','Fireball','Flame Arrows','Fly','Gaseous Form','Haste','Hypnotic Pattern','Incite Greed','Intellect Fortress','Lightning Bolt','Major Image','Melf\'s Minute Meteors','Protection from Energy','Sleet Storm','Slow','Stinking Cloud','Thunderstep','Tongues','Vampiric Touch','Wall of Water','Water Breathing','Water Walk']

sorcerer_fourth = ['Banishment','Blight','Charm Monster','Confusion','Dimension Door','Dominate Beast','Fire Shield','Greater Invisibility','Ice Storm','Polymorph','Raulothim\'s Psychic Lance','Sickening Radiance','Stoneskin','Storm Sphere','Vitriolic Sphere','Wall of Fire','Watery Sphere']

sorcerer_fifth = ['Animate Objects','Bigby\'s Hand','Cloudkill','Cone of Cold','Control Winds','Creation','Dominate Person','Enervation','Far Step','Hold Monster','Immolation','Insect Plague','Seeming','Skill Empowerment','Summon Draconic Spirit','Synaptic Static','Telekinesis','Teleportation Circle','Wall of Light','Wall of Stone']

sorcerer_sixth = ['Arcane Gate','Chain Lightning','Circle of Death','Disintegrate','Eyebite','Fizban\'s Platinum Shield','Flesh to Stone','Globe of Invulnerability','Investiture of Flame','Investiture of Ice','Investiture of Stone','Investiture of Wind','Mass Suggestion','Mental Prison','Move Earth','Otiluke\'s Freezing Sphere','Scatter','Sunbeam','Tasha\'s Otherworldly Guise','True Seeing']

sorcerer_seventh = ['Crown of Stars','Delayed Blast Fireball','Draconic Transformation','Dream of the Blue Veil','Etherealness','Finger of Death','Fire Storm','Plane Shift','Power Word: Pain','Prismatic Spray','Reverse Gravity','Teleport']

sorcerer_eighth = ['Abi-Dalzim\'s Horrid Wilting','Dominate Monster','Earthquake','Incendiary Cloud','Power Word: Stun','Sunburst']

sorcerer_ninth = ['Blade of Disaster','Gate','Mass Polymorph','Meteor Swarm','Power Word: Kill','Psychic Scream','Time Stop','Wish']
sorcerer_ritual_first = ['Comprehend Languages','Detect Magic']




######################################################################



# Select four sorcerer cantrips and get two 1st level spells
def sorcerer_magic():
    x=1
    y=1
    while x < 6:
        if x<5:
            print(f'{x}/4')
            dnd_skills.spell_add(sorcerer_cantrip,dnd_dict.character_dict['spells']['cantrips'],dnd_dict.character_dict['class_spells']['sorcerer_cantrips'])
            x+=1
        elif x == 5:
            while y < 4:
                if y < 3:
                    print(f'{y}/2')
                    dnd_skills.spell_add(sorcerer_first,dnd_dict.character_dict['spells']['first'],dnd_dict.character_dict['class_spells']['sorcerer']['first'])
                    y+=1
                elif y ==3:
                    y+=1
                    x+=1
                    break

#########################################################

warlock_cantrip = ['Blade Ward','Booming Blade','Chill Touch','Create Bonfire','Eldritch Blast','Friends','Frostbite','Green-Flame Blade','Infestation','Lightning Lure','Mage Hand','Magic Stone','Mind Sliver','Minor Illusion','Poison Spray','Prestidigitation','Sword Burst','Thunderclap','Toll the Dead','True Strike']

warlock_first = ['Armor of Agathys','Arms of Hadar','Cause Fear','Charm Person','Comprehend Languages','Distort Value','Expeditious Retreat','Hellish Rebuke','Hex','Illusory Script','Protection from Evil and Good','Unseen Servant','Witch Bolt']

warlock_second = ['Borrowed Knowledge','Cloud of Daggers','Crown of Madness','Darkness','Earthbind','Enthrall','Flock of Familiars','Hold Person','Invisibility','Mind Spike','Mirror Image','Misty Step','Ray of Enfeeblement','Shadow Blade','Shatter','Spider Climb','Suggestion']

warlock_third = ['Counterspell','Dispel Magic','Enemies Abound','Fear','Fly','Gaseous Form','Hunger of Hadar','Hypnotic Pattern','Incite Greed','Intellect Fortress','Magic Circle','Major Image','Remove Curse','Spirit Shroud','Summon Fey','Summon Lesser Demons','Summon Shadowspawn','Summon Undead','Thunder Step','Tongues','Vampiric Touch']

warlock_fourth = ['Banishment','Blight','Charm Monster','Dimension Door','Elemental Bane','Galder\'s Speedy Courier','Hallucinatory Terrain','Raulothim\'s Psychic Lance','Shadow of Moil','Sickening Radiance','Summon Aberration','Summon Greater Demon']

warlock_fifth = ['Contact Other Plane','Danse Macabre','Dream','Enervation','Far Step','Hold Monster','Infernal Calling','Mislead','Modify Memory','Negative Energy Flood','Planar Binding','Scrying','Synaptic Static','Teleportation Circle','Wall of Light']

warlock_sixth = ['Arcane Gate','Circle of Death','Conjure Fey','Create Undead','Eyebite','Flesh to Stone','Investiture of Flame','Investiture of Ice','Investiture of Stone','Investiture of Wind','Mass Suggestion','Mental Prison','Scatter','Soul Cage','Summon Fiend','Tasha\'s Otherworldly Guise','True Seeing']

warlock_seventh = ['Crown of Stars','Dream of the Blue Veil','Etherealness','Finger of Death','Forcecage','Plane Shift','Power Word: Pain','Project Image']

warlock_eighth = ['Abi-Dalzim\'s Horrid Wilting','Demiplane','Dominate Monster','Feeblemind','Glibness','Maddening Darkness','Power Word: Stun']

warlock_ninth = ['Astral Projection','Blade of Disaster','Foresight','Imprisonment','Power Word: Kill','Psychic Scream','Shapechange','True Polymorph','Weird']

# Used for an invocation
warlock_ritual_first = ['Alarm','Comprehend Languages','Detect Poison and Disease','Find Familiar','Floating Disk','Identify','Illusory Script','Purify Food and Drink','Speak with Animals','Unseen Servant']





archfey_warlock_first = ['Armor of Agathys','Arms of Hadar','Cause Fear','Charm Person','Comprehend Languages','Distort Value','Expeditious Retreat','Hellish Rebuke','Hex','Illusory Script','Protection from Evil and Good','Unseen Servant','Witch Bolt','Faerie Fire','Sleep']

archfey_warlock_second = ['Borrowed Knowledge','Cloud of Daggers','Crown of Madness','Darkness','Earthbind','Enthrall','Flock of Familiars','Hold Person','Invisibility','Mind Spike','Mirror Image','Misty Step','Ray of Enfeeblement','Shadow Blade','Shatter','Spider Climb','Suggestion','Calm Emotions']

archfey_warlock_third = ['Counterspell','Dispel Magic','Enemies Abound','Fear','Fly','Gaseous Form','Hunger of Hadar','Hypnotic Pattern','Incite Greed','Intellect Fortress','Magic Circle','Major Image','Remove Curse','Spirit Shroud','Summon Fey','Summon Lesser Demons','Summon Shadowspawn','Summon Undead','Thunder Step','Tongues','Vampiric Touch','Blink','Plant Growth']

archfey_warlock_fourth = ['Banishment','Blight','Charm Monster','Dimension Door','Elemental Bane','Galder\'s Speedy Courier','Hallucinatory Terrain','Raulothim\'s Psychic Lance','Shadow of Moil','Sickening Radiance','Summon Aberration','Summon Greater Demon','Dominate Beast','Greater Invisibility']

archfey_warlock_fifth = ['Contact Other Plane','Danse Macabre','Dream','Enervation','Far Step','Hold Monster','Infernal Calling','Mislead','Modify Memory','Negative Energy Flood','Planar Binding','Scrying','Synaptic Static','Teleportation Circle','Wall of Light','Dominate Person','Seeming']





fiend_warlock_first = ['Armor of Agathys','Arms of Hadar','Cause Fear','Charm Person','Comprehend Languages','Distort Value','Expeditious Retreat','Hellish Rebuke','Hex','Illusory Script','Protection from Evil and Good','Unseen Servant','Witch Bolt','Burning Hands','Command']

fiend_warlock_second = ['Borrowed Knowledge','Cloud of Daggers','Crown of Madness','Darkness','Earthbind','Enthrall','Flock of Familiars','Hold Person','Invisibility','Mind Spike','Mirror Image','Misty Step','Ray of Enfeeblement','Shadow Blade','Shatter','Spider Climb','Suggestion','Blindness/Deafness','Scorching Ray']

fiend_warlock_third = ['Counterspell','Dispel Magic','Enemies Abound','Fear','Fly','Gaseous Form','Hunger of Hadar','Hypnotic Pattern','Incite Greed','Intellect Fortress','Magic Circle','Major Image','Remove Curse','Spirit Shroud','Summon Fey','Summon Lesser Demons','Summon Shadowspawn','Summon Undead','Thunder Step','Tongues','Vampiric Touch','Fireball','Stinking Cloud']

fiend_warlock_fourth = ['Banishment','Blight','Charm Monster','Dimension Door','Elemental Bane','Galder\'s Speedy Courier','Hallucinatory Terrain','Raulothim\'s Psychic Lance','Shadow of Moil','Sickening Radiance','Summon Aberration','Summon Greater Demon','Fire Shield','Wall of Fire']

fiend_warlock_fifth = ['Contact Other Plane','Danse Macabre','Dream','Enervation','Far Step','Hold Monster','Infernal Calling','Mislead','Modify Memory','Negative Energy Flood','Planar Binding','Scrying','Synaptic Static','Teleportation Circle','Wall of Light','Flame Strike','Hallow']




goo_warlock_first = ['Armor of Agathys','Arms of Hadar','Cause Fear','Charm Person','Comprehend Languages','Distort Value','Expeditious Retreat','Hellish Rebuke','Hex','Illusory Script','Protection from Evil and Good','Unseen Servant','Witch Bolt','Dissonant Whispers','Tasha\'s Hideous Laughter']

goo_warlock_second = ['Borrowed Knowledge','Cloud of Daggers','Crown of Madness','Darkness','Earthbind','Enthrall','Flock of Familiars','Hold Person','Invisibility','Mind Spike','Mirror Image','Misty Step','Ray of Enfeeblement','Shadow Blade','Shatter','Spider Climb','Suggestion','Detect Thoughts','Phantasmal Force']

goo_warlock_third = ['Counterspell','Dispel Magic','Enemies Abound','Fear','Fly','Gaseous Form','Hunger of Hadar','Hypnotic Pattern','Incite Greed','Intellect Fortress','Magic Circle','Major Image','Remove Curse','Spirit Shroud','Summon Fey','Summon Lesser Demons','Summon Shadowspawn','Summon Undead','Thunder Step','Tongues','Vampiric Touch','Clairvoyance','Sending']

goo_warlock_fourth = ['Banishment','Blight','Charm Monster','Dimension Door','Elemental Bane','Galder\'s Speedy Courier','Hallucinatory Terrain','Raulothim\'s Psychic Lance','Shadow of Moil','Sickening Radiance','Summon Aberration','Summon Greater Demon','Dominate Beast','Evard\'s Black Tentacles']

goo_warlock_fifth = ['Contact Other Plane','Danse Macabre','Dream','Enervation','Far Step','Hold Monster','Infernal Calling','Mislead','Modify Memory','Negative Energy Flood','Planar Binding','Scrying','Synaptic Static','Teleportation Circle','Wall of Light','Dominate Person','Telekinesis']






# Select two warlock cantrips and get two 1st level spells
def archfey_warlock_magic():
    x=1
    y=1
    while x < 4:
        if x<3:
            print(f'{x}/2')
            dnd_skills.spell_add(warlock_cantrip,dnd_dict.character_dict['spells']['cantrips'],dnd_dict.character_dict['class_spells']['warlock_cantrips'])
            x+=1
        elif x == 3:
            while y < 4:
                if y < 3:
                    print(f'{y}/2')
                    dnd_skills.spell_add(archfey_warlock_first,dnd_dict.character_dict['spells']['first'],dnd_dict.character_dict['class_spells']['warlock']['first'])
                    y+=1
                elif y ==3:
                    y+=1
                    x+=1
                    break

# Select two warlock cantrips and get two 1st level spells
def fiend_warlock_magic():
    x=1
    y=1
    while x < 4:
        if x<3:
            print(f'{x}/2')
            dnd_skills.spell_add(warlock_cantrip,dnd_dict.character_dict['spells']['cantrips'],dnd_dict.character_dict['class_spells']['warlock_cantrips'])
            x+=1
        elif x == 3:
            while y < 4:
                if y < 3:
                    print(f'{y}/2')
                    dnd_skills.spell_add(fiend_warlock_first,dnd_dict.character_dict['spells']['first'],dnd_dict.character_dict['class_spells']['warlock']['first'])
                    y+=1
                elif y ==3:
                    y+=1
                    x+=1
                    break

# Select two warlock cantrips and get two 1st level spells
def goo_warlock_magic():
    x=1
    y=1
    while x < 4:
        if x<3:
            print(f'{x}/2')
            dnd_skills.spell_add(warlock_cantrip,dnd_dict.character_dict['spells']['cantrips'],dnd_dict.character_dict['class_spells']['warlock_cantrips'])
            x+=1
        elif x == 3:
            while y < 4:
                if y < 3:
                    print(f'{y}/2')
                    dnd_skills.spell_add(goo_warlock_first,dnd_dict.character_dict['spells']['first'],dnd_dict.character_dict['class_spells']['warlock']['first'])
                    y+=1
                elif y ==3:
                    y+=1
                    x+=1
                    break
# Basic Warlock spell selection without patrons
def warlock_magic():
    x=1
    y=1
    while x < 4:
        if x<3:
            print(f'{x}/2')
            dnd_skills.spell_add(warlock_cantrip,dnd_dict.character_dict['spells']['cantrips'],dnd_dict.character_dict['class_spells']['warlock_cantrips'])
            x+=1
        elif x == 3:
            while y < 4:
                if y < 3:
                    print(f'{y}/2')
                    dnd_skills.spell_add(warlock_first,dnd_dict.character_dict['spells']['first'],dnd_dict.character_dict['class_spells']['warlock']['first'])
                    y+=1
                elif y ==3:
                    y+=1
                    x+=1
                    break



#####################################################################

# Wizard spell list that does not include Graviturgy or Chronurgy spells.
wizard_cantrip = ['Acid Splash','Blade Ward','Booming Blade','Chill Touch','Control Flames','Create Bonfire','Dancing Lights','Encode Thoughts','Fire Bolt','Friends','Frostbite','Green-Flame Blade','Gust','Infestation','Light','Lightning Lure','Mage Hand','Mending','Message','Mind Sliver','Minor Illusion','Mold Earth','Poison Spray','Prestidigitation','Ray of Frost','Shape Water','Shocking Grasp','Sword Burst','Thunderclap','Toll the Dead','True Strike']

wizard_first = ['Absorb Elements','Alarm','Burning Hands','Catapult','Cause Fear','Charm Person','Chromatic Orb','Color Spray','Comprehend Languages','Detect Magic','Disguise Self','Distort Value','Earth Tremor','Expeditious Retreat','False Life','Feather Fall','Find Familiar','Floating Disk','Fog Cloud','Frost Fingers','Grease','Hideous Laughter','Ice Knife','Identify','Illusory Script','Jim\'s Magic Missile','Jump','Longstrider','Mage Armor','Magic Missile','Protection from Evil and Good','Ray of Sickness','Shield','Silent Image','Silvery Barbs','Sleep','Snare','Tasha\'s Hideous Laughter','Tasha\'s Caustic Brew','Tenser\'s Floating Disk','Thunderwave','Unseen Servant','Witch Bolt']

wizard_second = ['Aganazzar\'s Scorcher','Alter Self','Arcane Lock','Augury','Blindness/Deafness','Blur','Borrowed Knowledge','Cloud of Daggers','Continual Flame','Crown of Madness','Darkness','Darkvision','Detect Thoughts','Dragon\'s Breath','Dust Devil','Earthbind','Enhance Ability','Enlarge/Reduce','Flaming Sphere','Flock of Familiars','Gentle Repose','Gift of Gab','Gust of Wind','Hold Person','Invisibility','Jim\'s Glowing Coin','Kinetic Jaunt','Knock','Levitate','Locate Object','Magic Mouth','Magic Weapon','Maximillian\'s Earthen Grasp','Melf\'s Acid Arrow','Mind Spike','Mirror Image','Misty Step','Nathair\'s Mischief','Nystul\'s Magic Aura','Phantasmal Force','Pyrotechnics','Ray of Enfeeblement','Rime\'s Binding Ice','Rope Trick','Scorching Ray','See Invisibility','Shadow Blade','Shatter','Skywrite','Snilloc\'s Snowball Storm','Spider Climb','Suggestion','Tasha\'s Mind Whip','Vortex Warp','Warding Wind','Web','Wither and Bloom']

wizard_third = ['Animate Dead','Ashardalon\'s Stride','Bestow Curse','Blink','Catnap','Clairvoyance','Conjure Lesser Demon','Counterspell','Dispel Magic','Enemies Abound','Erupting Earth','Fast Friends','Fear','Feign Death','Fireball','Flame Arrows','Fly','Galder\'s Tower','Gaseous Form','Glyph of Warding','Haste','Hypnotic Pattern','Incite Greed','Intellect Fortress','Leomund\'s Tiny Hut','Life Transference','Lightning Bolt','Magic Circle','Major Image','Melf\'s Minute Meteors','Nondetection','Phantom Steed','Protection from Energy','Remove Curse','Sending','Sleet Storm','Slow','Speak with Dead','Spirit Shroud','Stinking Cloud','Summon Fey','Summon Lesser Demons','Summon Shadowspawn','Summon Undead','Thunder Step','Tidal Wave','Tiny Servant','Tongues','Vampiric Touch','Wall of Sand','Wall of Water','Water Breathing']

wizard_fourth = ['Arcane Eye','Banishment','Blight','Charm Monster','Confusion','Conjure Minor Elementals','Control Water','Dimension Door','Divination','Elemental Bane','Evard\'s Black Tentacles','Fabricate','Fire Shield','Galder\'s Speedy Courier','Greater Invisibility','Hallucinatory Terrain','Ice Storm','Leomund\'s Secret Chest','Locate Creature','Mordenkainen\'s Faithful Hound','Mordenkainen\'s Private Sanctum','Otiluke\'s Resilient Sphere','Phantasmal Killer','Polymorph','Sickening Radiance','Stone Shape','Stoneskin','Storm Sphere','Summon Aberration','Summon Construct','Summon Elemental','Summon Greater Demon','Vitriolic Sphere','Wall of Fire','Watery Sphere']

wizard_fifth = ['Animate Objects','Bigby\'s Hand','Cloudkill','Cone of Cold','Conjure Elemental','Contact Other Plane','Control Winds','Creation','Danse Macabre','Dawn','Dominate Person','Dream','Enervation','Far Step','Geas','Hold Monster','Immolation','Infernal Calling','Legend Lore','Mislead','Modify Memory','Negative Energy Flood','Passwall','Planar Binding','Rary\'s Telepathic Bond','Scrying','Seeming','Skill Empowerment','Steel Wind Strike','Summon Draconic Spirit','Synaptic Static','Telekinesis','Teleportation Circle','Trasnmute Rock','Wall of Force','Wall of Light','Wall of Stone']

wizard_sixth = ['Arcane Gate','Chain Lightning','Circle of Death','Contingency','Create Homunculus','Create Undead','Disintegrate','Drawmij\'s Instant Summons','Eyebite','Fizban\'s Platinum Shield','Flesh to Stone','Globe of Invulnerability','Guards and Wards','Investiture of Flame','Investiture of Ice','Investiture of Stone','Investiture of Wind','Magic Jar','Mass Suggestion','Mental Prison','Move Earth','Otiluke\'s Freezing Sphere','Otto\'s Irresistible Dance','Programmed Illusion','Scatter','Soul Cage','Summon Fiend','Sunbeam','Tasha\'s Otherworldly Guise','Tenser\'s Transformation','True Seeing','Wall of Ice']

wizard_seventh = ['Create Magen','Crown of Stars','Delayed Fireball','Draconic Transformation','Dream of the Blue Veil','Etherealness','Finger of Death','Forcecage','Mirage Arcane','Mordenkainen\'s Magnificent Mansion','Mordenkainen\'s Sword','Plane Shift','Power Word: Pain','Prismatic Spray','Project Image','Reverse Gravity','Sequester','Simulacrum','Symbol','Teleport','Whirlwind']

wizard_eighth = ['Abi-Dalzim\'s Horrid Wilting','Antimagic Field','Antipathy/Sympathy','Clone','Control Weather','Demiplane','Dominate Monster','Feeblemind','Illusory Dragon','Incendiary Cloud','Maddening Darkness','Maze','Mighty Fortress','Mind Blank','Power Word: Stun','Sunburst','Telepathy']

wizard_ninth = ['Astral Projection','Blade of Disaster','Foresight','Gate','Imprisonment','Invulnerability','Mass Polymorph','Meteor Swarm','Power Word: Kill','Prismatic Wall','Psychic Scream','Shapechange','Time Stop','True Polymorph','Weird','Wish']

wizard_ritual_first = ['Alarm','Comprehend Languages','Detect Magic','Find Familiar','Identify','Illusory Script','Tenser\'s Floating Disk','Unseen Servant']





# Used for all spells

all_wizard_cantrip = ['Acid Splash','Blade Ward','Booming Blade','Chill Touch','Control Flames','Create Bonfire','Dancing Lights','Encode Thoughts','Fire Bolt','Friends','Frostbite','Green-Flame Blade','Gust','Infestation','Light','Lightning Lure','Mage Hand','Mending','Message','Mind Sliver','Minor Illusion','Mold Earth','Poison Spray','Prestidigitation','Ray of Frost','Shape Water','Shocking Grasp','Sword Burst','Thunderclap','Toll the Dead','True Strike']

all_wizard_first = ['Absorb Elements','Alarm','Burning Hands','Catapult','Cause Fear','Charm Person','Chromatic Orb','Color Spray','Comprehend Languages','Detect Magic','Disguise Self','Distort Value','Earth Tremor','Expeditious Retreat','False Life','Feather Fall','Find Familiar','Floating Disk','Fog Cloud','Frost Fingers','Gift of Alacrity','Grease','Hideous Laughter','Ice Knife','Identify','Illusory Script','Jim\'s Magic Missile','Jump','Longstrider','Mage Armor','Magic Missile','Protection from Evil and Good','Ray of Sickness','Shield','Silent Image','Silvery Barbs','Sleep','Snare','Tasha\'s Hideous Laughter','Tasha\'s Caustic Brew','Tenser\'s Floating Disk','Thunderwave','Unseen Servant','Witch Bolt']

all_wizard_second = ['Aganazzar\'s Scorcher','Alter Self','Arcane Lock','Augury','Blindness/Deafness','Blur','Borrowed Knowledge','Cloud of Daggers','Continual Flame','Crown of Madness','Darkness','Darkvision','Detect Thoughts','Dragon\'s Breath','Dust Devil','Earthbind','Enhance Ability','Enlarge/Reduce','Flaming Sphere','Flock of Familiars','Fortune\'s Favor','Gentle Repose','Gift of Gab','Gust of Wind','Hold Person','Immovable Object','Invisibility','Jim\'s Glowing Coin','Kinetic Jaunt','Knock','Levitate','Locate Object','Magic Mouth','Magic Weapon','Maximillian\'s Earthen Grasp','Melf\'s Acid Arrow','Mind Spike','Mirror Image','Misty Step','Nathair\'s Mischief','Nystul\'s Magic Aura','Phantasmal Force','Pyrotechnics','Ray of Enfeeblement','Rime\'s Binding Ice','Rope Trick','Scorching Ray','See Invisibility','Shadow Blade','Shatter','Skywrite','Snilloc\'s Snowball Storm','Spider Climb','Suggestion','Tasha\'s Mind Whip','Vortex Warp','Warding Wind','Web','Wither and Bloom','Wristpocket']

all_wizard_third = ['Animate Dead','Ashardalon\'s Stride','Bestow Curse','Blink','Catnap','Clairvoyance','Conjure Lesser Demon','Counterspell','Dispel Magic','Enemies Abound','Erupting Earth','Fast Friends','Fear','Feign Death','Fireball','Flame Arrows','Fly','Galder\'s Tower','Gaseous Form','Glyph of Warding','Haste','Hypnotic Pattern','Incite Greed','Intellect Fortress','Leomund\'s Tiny Hut','Life Transference','Lightning Bolt','Magic Circle','Major Image','Melf\'s Minute Meteors','Nondetection','Phantom Steed','Protection from Energy','Pulse Wave','Remove Curse','Sending','Sleet Storm','Slow','Speak with Dead','Spirit Shroud','Stinking Cloud','Summon Fey','Summon Lesser Demons','Summon Shadowspawn','Summon Undead','Thunder Step','Tidal Wave','Tiny Servant','Tongues','Vampiric Touch','Wall of Sand','Wall of Water','Water Breathing']

all_wizard_fourth = ['Arcane Eye','Banishment','Blight','Charm Monster','Confusion','Conjure Minor Elementals','Control Water','Dimension Door','Divination','Elemental Bane','Evard\'s Black Tentacles','Fabricate','Fire Shield','Galder\'s Speedy Courier','Gravity Sinkhole','Greater Invisibility','Hallucinatory Terrain','Ice Storm','Leomund\'s Secret Chest','Locate Creature','Mordenkainen\'s Faithful Hound','Mordenkainen\'s Private Sanctum','Otiluke\'s Resilient Sphere','Phantasmal Killer','Polymorph','Sickening Radiance','Stone Shape','Stoneskin','Storm Sphere','Summon Aberration','Summon Construct','Summon Elemental','Summon Greater Demon','Vitriolic Sphere','Wall of Fire','Watery Sphere']

all_wizard_fifth = ['Animate Objects','Bigby\'s Hand','Cloudkill','Cone of Cold','Conjure Elemental','Contact Other Plane','Control Winds','Creation','Danse Macabre','Dawn','Dominate Person','Dream','Enervation','Far Step','Geas','Hold Monster','Immolation','Infernal Calling','Legend Lore','Mislead','Modify Memory','Negative Energy Flood','Passwall','Planar Binding','Rary\'s Telepathic Bond','Scrying','Seeming','Skill Empowerment','Steel Wind Strike','Summon Draconic Spirit','Synaptic Static','Telekinesis','Teleportation Circle','Temporal Shunt','Trasnmute Rock','Wall of Force','Wall of Light','Wall of Stone']

all_wizard_sixth = ['Arcane Gate','Chain Lightning','Circle of Death','Contingency','Create Homunculus','Create Undead','Disintegrate','Drawmij\'s Instant Summons','Eyebite','Fizban\'s Platinum Shield','Flesh to Stone','Globe of Invulnerability','Gravity Fissure','Guards and Wards','Investiture of Flame','Investiture of Ice','Investiture of Stone','Investiture of Wind','Magic Jar','Mass Suggestion','Mental Prison','Move Earth','Otiluke\'s Freezing Sphere','Otto\'s Irresistible Dance','Programmed Illusion','Scatter','Soul Cage','Summon Fiend','Sunbeam','Tasha\'s Otherworldly Guise','Tenser\'s Transformation','True Seeing','Wall of Ice']

all_wizard_seventh = ['Create Magen','Crown of Stars','Delayed Fireball','Draconic Transformation','Dream of the Blue Veil','Etherealness','Finger of Death','Forcecage','Mirage Arcane','Mordenkainen\'s Magnificent Mansion','Mordenkainen\'s Sword','Plane Shift','Power Word: Pain','Prismatic Spray','Project Image','Reverse Gravity','Sequester','Simulacrum','Symbol','Teleport','Tether Essence','Whirlwind']

all_wizard_eighth = ['Abi-Dalzim\'s Horrid Wilting','Antimagic Field','Antipathy/Sympathy','Clone','Control Weather','Dark Star','Demiplane','Dominate Monster','Feeblemind','Illusory Dragon','Incendiary Cloud','Maddening Darkness','Maze','Mighty Fortress','Mind Blank','Power Word: Stun','Reality Break','Sunburst','Telepathy']

all_wizard_ninth = ['Astral Projection','Blade of Disaster','Foresight','Gate','Imprisonment','Invulnerability','Mass Polymorph','Meteor Swarm','Power Word: Kill','Prismatic Wall','Psychic Scream','Ravenous Void','Shapechange','Time Ravage','Time Stop','True Polymorph','Weird','Wish']




# Used for School of Graviturgy if I ever put it in
graviturgy_wizard_cantrip = ['Acid Splash','Blade Ward','Booming Blade','Chill Touch','Control Flames','Create Bonfire','Dancing Lights','Encode Thoughts','Fire Bolt','Friends','Frostbite','Green-Flame Blade','Gust','Infestation','Light','Lightning Lure','Mage Hand','Mending','Message','Mind Sliver','Minor Illusion','Mold Earth','Poison Spray','Prestidigitation','Ray of Frost','Shape Water','Shocking Grasp','Sword Burst','Thunderclap','Toll the Dead','True Strike']

graviturgy_wizard_first = ['Absorb Elements','Alarm','Burning Hands','Catapult','Cause Fear','Charm Person','Chromatic Orb','Color Spray','Comprehend Languages','Detect Magic','Disguise Self','Distort Value','Earth Tremor','Expeditious Retreat','False Life','Feather Fall','Find Familiar','Floating Disk','Fog Cloud','Frost Fingers','Grease','Hideous Laughter','Ice Knife','Identify','Illusory Script','Jim\'s Magic Missile','Jump','Longstrider','Mage Armor','Magic Missile','Protection from Evil and Good','Ray of Sickness','Shield','Silent Image','Silvery Barbs','Sleep','Snare','Tasha\'s Hideous Laughter','Tasha\'s Caustic Brew','Tenser\'s Floating Disk','Thunderwave','Unseen Servant','Witch Bolt']

graviturgy_wizard_second = ['Aganazzar\'s Scorcher','Alter Self','Arcane Lock','Augury','Blindness/Deafness','Blur','Borrowed Knowledge','Cloud of Daggers','Continual Flame','Crown of Madness','Darkness','Darkvision','Detect Thoughts','Dragon\'s Breath','Dust Devil','Earthbind','Enhance Ability','Enlarge/Reduce','Flaming Sphere','Flock of Familiars','Fortune\'s Favor','Gentle Repose','Gift of Gab','Gust of Wind','Hold Person','Immovable Object','Invisibility','Jim\'s Glowing Coin','Kinetic Jaunt','Knock','Levitate','Locate Object','Magic Mouth','Magic Weapon','Maximillian\'s Earthen Grasp','Melf\'s Acid Arrow','Mind Spike','Mirror Image','Misty Step','Nathair\'s Mischief','Nystul\'s Magic Aura','Phantasmal Force','Pyrotechnics','Ray of Enfeeblement','Rime\'s Binding Ice','Rope Trick','Scorching Ray','See Invisibility','Shadow Blade','Shatter','Skywrite','Snilloc\'s Snowball Storm','Spider Climb','Suggestion','Tasha\'s Mind Whip','Vortex Warp','Warding Wind','Web','Wither and Bloom','Wristpocket']

graviturgy_wizard_third = ['Animate Dead','Ashardalon\'s Stride','Bestow Curse','Blink','Catnap','Clairvoyance','Conjure Lesser Demon','Counterspell','Dispel Magic','Enemies Abound','Erupting Earth','Fast Friends','Fear','Feign Death','Fireball','Flame Arrows','Fly','Galder\'s Tower','Gaseous Form','Glyph of Warding','Haste','Hypnotic Pattern','Incite Greed','Intellect Fortress','Leomund\'s Tiny Hut','Life Transference','Lightning Bolt','Magic Circle','Major Image','Melf\'s Minute Meteors','Nondetection','Phantom Steed','Protection from Energy','Pulse Wave','Remove Curse','Sending','Sleet Storm','Slow','Speak with Dead','Spirit Shroud','Stinking Cloud','Summon Fey','Summon Lesser Demons','Summon Shadowspawn','Summon Undead','Thunder Step','Tidal Wave','Tiny Servant','Tongues','Vampiric Touch','Wall of Sand','Wall of Water','Water Breathing']

graviturgy_wizard_fourth = ['Arcane Eye','Banishment','Blight','Charm Monster','Confusion','Conjure Minor Elementals','Control Water','Dimension Door','Divination','Elemental Bane','Evard\'s Black Tentacles','Fabricate','Fire Shield','Galder\'s Speedy Courier','Gravity Sinkhole','Greater Invisibility','Hallucinatory Terrain','Ice Storm','Leomund\'s Secret Chest','Locate Creature','Mordenkainen\'s Faithful Hound','Mordenkainen\'s Private Sanctum','Otiluke\'s Resilient Sphere','Phantasmal Killer','Polymorph','Sickening Radiance','Stone Shape','Stoneskin','Storm Sphere','Summon Aberration','Summon Construct','Summon Elemental','Summon Greater Demon','Vitriolic Sphere','Wall of Fire','Watery Sphere']

graviturgy_wizard_fifth = ['Animate Objects','Bigby\'s Hand','Cloudkill','Cone of Cold','Conjure Elemental','Contact Other Plane','Control Winds','Creation','Danse Macabre','Dawn','Dominate Person','Dream','Enervation','Far Step','Geas','Hold Monster','Immolation','Infernal Calling','Legend Lore','Mislead','Modify Memory','Negative Energy Flood','Passwall','Planar Binding','Rary\'s Telepathic Bond','Scrying','Seeming','Skill Empowerment','Steel Wind Strike','Summon Draconic Spirit','Synaptic Static','Telekinesis','Teleportation Circle','Trasnmute Rock','Wall of Force','Wall of Light','Wall of Stone']

graviturgy_wizard_sixth = ['Arcane Gate','Chain Lightning','Circle of Death','Contingency','Create Homunculus','Create Undead','Disintegrate','Drawmij\'s Instant Summons','Eyebite','Fizban\'s Platinum Shield','Flesh to Stone','Globe of Invulnerability','Gravity Fissure','Guards and Wards','Investiture of Flame','Investiture of Ice','Investiture of Stone','Investiture of Wind','Magic Jar','Mass Suggestion','Mental Prison','Move Earth','Otiluke\'s Freezing Sphere','Otto\'s Irresistible Dance','Programmed Illusion','Scatter','Soul Cage','Summon Fiend','Sunbeam','Tasha\'s Otherworldly Guise','Tenser\'s Transformation','True Seeing','Wall of Ice']

graviturgy_wizard_seventh = ['Create Magen','Crown of Stars','Delayed Fireball','Draconic Transformation','Dream of the Blue Veil','Etherealness','Finger of Death','Forcecage','Mirage Arcane','Mordenkainen\'s Magnificent Mansion','Mordenkainen\'s Sword','Plane Shift','Power Word: Pain','Prismatic Spray','Project Image','Reverse Gravity','Sequester','Simulacrum','Symbol','Teleport','Tether Essence','Whirlwind']

graviturgy_wizard_eighth = ['Abi-Dalzim\'s Horrid Wilting','Antimagic Field','Antipathy/Sympathy','Clone','Control Weather','Dark Star','Demiplane','Dominate Monster','Feeblemind','Illusory Dragon','Incendiary Cloud','Maddening Darkness','Maze','Mighty Fortress','Mind Blank','Power Word: Stun','Sunburst','Telepathy']

graviturgy_wizard_ninth = ['Astral Projection','Blade of Disaster','Foresight','Gate','Imprisonment','Invulnerability','Mass Polymorph','Meteor Swarm','Power Word: Kill','Prismatic Wall','Psychic Scream','Ravenous Void','Shapechange','Time Stop','True Polymorph','Weird','Wish']


#Used for Chronurgy if I ever put it in
chronurgy_wizard_cantrip = ['Acid Splash','Blade Ward','Booming Blade','Chill Touch','Control Flames','Create Bonfire','Dancing Lights','Encode Thoughts','Fire Bolt','Friends','Frostbite','Green-Flame Blade','Gust','Infestation','Light','Lightning Lure','Mage Hand','Mending','Message','Mind Sliver','Minor Illusion','Mold Earth','Poison Spray','Prestidigitation','Ray of Frost','Shape Water','Shocking Grasp','Sword Burst','Thunderclap','Toll the Dead','True Strike']

chronurgy_wizard_first = ['Absorb Elements','Alarm','Burning Hands','Catapult','Cause Fear','Charm Person','Chromatic Orb','Color Spray','Comprehend Languages','Detect Magic','Disguise Self','Distort Value','Earth Tremor','Expeditious Retreat','False Life','Feather Fall','Find Familiar','Floating Disk','Fog Cloud','Frost Fingers','Gift of Alacrity','Grease','Hideous Laughter','Ice Knife','Identify','Illusory Script','Jim\'s Magic Missile','Jump','Longstrider','Mage Armor','Magic Missile','Protection from Evil and Good','Ray of Sickness','Shield','Silent Image','Silvery Barbs','Sleep','Snare','Tasha\'s Hideous Laughter','Tasha\'s Caustic Brew','Tenser\'s Floating Disk','Thunderwave','Unseen Servant','Witch Bolt']

chronurgy_wizard_second = ['Aganazzar\'s Scorcher','Alter Self','Arcane Lock','Augury','Blindness/Deafness','Blur','Borrowed Knowledge','Cloud of Daggers','Continual Flame','Crown of Madness','Darkness','Darkvision','Detect Thoughts','Dragon\'s Breath','Dust Devil','Earthbind','Enhance Ability','Enlarge/Reduce','Flaming Sphere','Flock of Familiars','Fortune\'s Favor','Gentle Repose','Gift of Gab','Gust of Wind','Hold Person','Immovable Object','Invisibility','Jim\'s Glowing Coin','Kinetic Jaunt','Knock','Levitate','Locate Object','Magic Mouth','Magic Weapon','Maximillian\'s Earthen Grasp','Melf\'s Acid Arrow','Mind Spike','Mirror Image','Misty Step','Nathair\'s Mischief','Nystul\'s Magic Aura','Phantasmal Force','Pyrotechnics','Ray of Enfeeblement','Rime\'s Binding Ice','Rope Trick','Scorching Ray','See Invisibility','Shadow Blade','Shatter','Skywrite','Snilloc\'s Snowball Storm','Spider Climb','Suggestion','Tasha\'s Mind Whip','Vortex Warp','Warding Wind','Web','Wither and Bloom','Wristpocket']

chronurgy_wizard_third = ['Animate Dead','Ashardalon\'s Stride','Bestow Curse','Blink','Catnap','Clairvoyance','Conjure Lesser Demon','Counterspell','Dispel Magic','Enemies Abound','Erupting Earth','Fast Friends','Fear','Feign Death','Fireball','Flame Arrows','Fly','Galder\'s Tower','Gaseous Form','Glyph of Warding','Haste','Hypnotic Pattern','Incite Greed','Intellect Fortress','Leomund\'s Tiny Hut','Life Transference','Lightning Bolt','Magic Circle','Major Image','Melf\'s Minute Meteors','Nondetection','Phantom Steed','Protection from Energy','Pulse Wave','Remove Curse','Sending','Sleet Storm','Slow','Speak with Dead','Spirit Shroud','Stinking Cloud','Summon Fey','Summon Lesser Demons','Summon Shadowspawn','Summon Undead','Thunder Step','Tidal Wave','Tiny Servant','Tongues','Vampiric Touch','Wall of Sand','Wall of Water','Water Breathing']

chronurgy_wizard_fourth = ['Arcane Eye','Banishment','Blight','Charm Monster','Confusion','Conjure Minor Elementals','Control Water','Dimension Door','Divination','Elemental Bane','Evard\'s Black Tentacles','Fabricate','Fire Shield','Galder\'s Speedy Courier','Greater Invisibility','Hallucinatory Terrain','Ice Storm','Leomund\'s Secret Chest','Locate Creature','Mordenkainen\'s Faithful Hound','Mordenkainen\'s Private Sanctum','Otiluke\'s Resilient Sphere','Phantasmal Killer','Polymorph','Sickening Radiance','Stone Shape','Stoneskin','Storm Sphere','Summon Aberration','Summon Construct','Summon Elemental','Summon Greater Demon','Vitriolic Sphere','Wall of Fire','Watery Sphere']

chronurgy_wizard_fifth = ['Animate Objects','Bigby\'s Hand','Cloudkill','Cone of Cold','Conjure Elemental','Contact Other Plane','Control Winds','Creation','Danse Macabre','Dawn','Dominate Person','Dream','Enervation','Far Step','Geas','Hold Monster','Immolation','Infernal Calling','Legend Lore','Mislead','Modify Memory','Negative Energy Flood','Passwall','Planar Binding','Rary\'s Telepathic Bond','Scrying','Seeming','Skill Empowerment','Steel Wind Strike','Summon Draconic Spirit','Synaptic Static','Telekinesis','Teleportation Circle','Temporal Shunt','Trasnmute Rock','Wall of Force','Wall of Light','Wall of Stone']

chronurgy_wizard_sixth = ['Arcane Gate','Chain Lightning','Circle of Death','Contingency','Create Homunculus','Create Undead','Disintegrate','Drawmij\'s Instant Summons','Eyebite','Fizban\'s Platinum Shield','Flesh to Stone','Globe of Invulnerability','Guards and Wards','Investiture of Flame','Investiture of Ice','Investiture of Stone','Investiture of Wind','Magic Jar','Mass Suggestion','Mental Prison','Move Earth','Otiluke\'s Freezing Sphere','Otto\'s Irresistible Dance','Programmed Illusion','Scatter','Soul Cage','Summon Fiend','Sunbeam','Tasha\'s Otherworldly Guise','Tenser\'s Transformation','True Seeing','Wall of Ice']

chronurgy_wizard_seventh = ['Create Magen','Crown of Stars','Delayed Fireball','Draconic Transformation','Dream of the Blue Veil','Etherealness','Finger of Death','Forcecage','Mirage Arcane','Mordenkainen\'s Magnificent Mansion','Mordenkainen\'s Sword','Plane Shift','Power Word: Pain','Prismatic Spray','Project Image','Reverse Gravity','Sequester','Simulacrum','Symbol','Teleport','Tether Essence','Whirlwind']

chronurgy_wizard_eighth = ['Abi-Dalzim\'s Horrid Wilting','Antimagic Field','Antipathy/Sympathy','Clone','Control Weather','Demiplane','Dominate Monster','Feeblemind','Illusory Dragon','Incendiary Cloud','Maddening Darkness','Maze','Mighty Fortress','Mind Blank','Power Word: Stun','Reality Break','Sunburst','Telepathy']

chronurgy_wizard_ninth = ['Astral Projection','Blade of Disaster','Foresight','Gate','Imprisonment','Invulnerability','Mass Polymorph','Meteor Swarm','Power Word: Kill','Prismatic Wall','Psychic Scream','Shapechange','Time Ravage','Time Stop','True Polymorph','Weird','Wish']
















# Eldritch Knights can only learn Wizard spells from Abjuration and Evocation Schools
eldritch_knight_first = ['Absorb Elements','Alarm','Burning Hands','Chromatic Orb','Earth Tremor','Frost Fingers','Jim\'s Magic Missile','Mage Armor','Magic Missile','Protection from Evil and Good','Shield','Snare','Tasha\'s Caistoc Brew','Thunderwave','Witch Bolt']

eldritch_knight_second = ['Aganazzar\'s Scorcher','Arcane Lock','Continual Flame','Darkness','Gust of Wind','Melf\'s Acid Arrow','Rime\'s Binding Frost','Scorching Ray','Shatter','Snilloc\'s Snowball Swarm','Warding Wind']

eldritch_knight_third = ['Counterspell','Dispel Magic','Fireball','Glyph of Warding','Intellect Fortress','Leomund\'s Tiny Hut','Lightning Bolt','Magic Circle','Melf\'s Minute Meteors','Nondetection','Protection from Energy','Remove Curse','Sending','Wall of Sand','Wall of Water']

eldritch_knight_fourth = ['Banishment','Fire Shield','Ice Storm','Mordenkainen\'s Private Sanctum','Otiluke\'s Resilient Sphere','Sickening Radiance','Stoneskin','Storm Sphere','Vitriolic Sphere','Wall of Fire']

eldritch_knight_fifth = ['Bigby\'s Hand','Cone of Cold','Dawn','Immolation','Planar Binding','Wall of Force','Wall of Light','Wall of Stone']

# Select two wizard cantrips and get three 1st level Evocation or Abjuration spells
def eldritch_knight_magic():
    x=1
    y=1
    while x < 4:
        if x<3:
            print(f'{x}/2')
            dnd_skills.spell_add(wizard_cantrip,dnd_dict.character_dict['spells']['cantrips'],dnd_dict.character_dict['class_spells']['fighter_cantrips'])
            x+=1
        elif x == 3:
            while y < 5:
                if y < 4:
                    print(f'{y}/3')
                    dnd_skills.spell_add(eldritch_knight_first,dnd_dict.character_dict['spells']['first'],dnd_dict.character_dict['class_spells']['fighter']['first'])
                    y+=1
                elif y ==4:
                    y+=1
                    x+=1
                    break






# Arcane Tricksters can only learn Wizard spells from Enchantment and Illusion Schools
arcane_trickster_first = ['Charm Person','Color Spray','Disguise Self','Distort Value','Illusory Script','Silent Image','Silvery Barbs','Sleep','Tasha\'s Hideous Laughter']

arcane_trickster_second = ['Blur','Crown of Madness','Gift of Gab','Hold Person','Invisibility','Jim\'s Glowing Coin','Magic Mouth','Mirror Image','Nathair\'s Mischief','Nystul\'s Magic Aura','Phantasmal Force','Shadow Blade','Suggestion','Tasha\'s Mind Whip']

arcane_trickster_third = ['Catnap','Enemies Abound','Fast Friends','Fear','Hypnotic Pattern','Incite Greed','Major Image','Phantom Steed']

arcane_trickster_fourth = ['Charm Monster','Confusion','Greater Invisibility','Hallucinatory Terrain','Phantasmal Killer','Raylothim\'s Psychic Lance']

arcane_trickster_fifth = ['Creation','Dominate Person','Dream','Geas','Hold Monster','Mislead','Modify Memory','Seeming','Synaptic Static']


def arcane_trickster_magic():
    x=1
    y=1
    while x < 4:
        if x<3:
            print(f'{x}/2')
            dnd_skills.spell_add(wizard_cantrip,dnd_dict.character_dict['spells']['cantrips'],dnd_dict.character_dict['class_spells']['rogue_cantrips'])
            x+=1
        elif x == 3:
            while y < 4:
                if y < 3:
                    print(f'{y}/3')
                    dnd_skills.spell_add(arcane_trickster_first,dnd_dict.character_dict['spells']['first'],dnd_dict.character_dict['class_spells']['rogue']['first'])
                    y+=1
                elif y ==3:
                    print('3/3')
                    dnd_skills.spell_add(wizard_first,dnd_dict.character_dict['spells']['first'],dnd_dict.character_dict['class_spells']['rogue_special']['first'])
                    y+=1
                    x+=1
                    break





# Select three wizard cantrips and get six 1st level spells
def wizard_magic():
    x=1
    y=1
    while x < 5:
        if x<4:
            print(f'{x}/3')
            dnd_skills.spell_add(wizard_cantrip,dnd_dict.character_dict['spells']['cantrips'],dnd_dict.character_dict['class_spells']['wizard_cantrips'])
            x+=1
        elif x == 4:
            while y < 8:
                if y < 5:
                    print(f'{y}/6')
                    dnd_skills.spell_add(wizard_first,dnd_dict.character_dict['spells']['first'],dnd_dict.character_dict['class_spells']['wizard']['first'])
                    y+=1
                elif y ==5:
                    y+=1
                    x+=1
                    break

# Used for when the wizard gets two spells when leveling up.
# If the Chronurgy and Gravity schools are added later, then only cycle through their spell lists. Otherwise, proceed as normal
# If you don't care about that rule, then use the function using "regular_spell" and comment out their specific list.
#def wizard_level_up(time_spells,gravity_spells,regular_spells):
def wizard_level_up(time_spells,gravity_spells,regular_spells,all_spells):
    x = 1
    for x in range (x,3):
        if x < 3:
            if dnd_dict.character_dict['player_class']['wizard']['subclass'] == 'School of Chronurgy':
                print(f'{x}/2')
                dnd_skills.spell_add(time_spells,dnd_dict.character_dict['spells'],dnd_dict.character_dict['class_spells']['wizard'])
                x+=1
                continue

            elif dnd_dict.character_dict['player_class']['wizard']['subclass'] == 'School of Gravity':
                print(f'{x}/2')
                dnd_skills.spell_add(gravity_spells,dnd_dict.character_dict['spells'],dnd_dict.character_dict['class_spells']['wizard'])
                x+=1
                continue

            else:
                print(f'{x}/2')
                dnd_skills.spell_add(regular_spells,dnd_dict.character_dict['spells'],dnd_dict.character_dict['class_spells']['wizard'])
                x+=1
                continue

# Used for all spells if you dont want to deal with the school restrictions.
# Un-comment out lines 3862-3878 in that case and comment out the ones below.
#            print(f'{x}/2')
#            dnd_skills.spell_add(all_spells,dnd_dict.character_dict['spells'],dnd_dict.character_dict['class_spells']['wizard'])
#            x+=1
#            continue

        elif x == 3:
            break


def first_wizard_level_up():
    x = 1
    for x in range (x,3):
        if x < 3:
# Un-comment this and comment out the other if statements if you want all of the spells
#            dnd_skills.spell_add(all_wizard_first,dnd_dict.character_dict['spells']['first'],dnd_dict.character_dict['class_spells']['wizard']['first'])
#                x+=1
#                continue
#        elif x == 3:
#            break

            if dnd_dict.character_dict['player_class']['wizard']['subclass'] == 'School of Chronurgy':
                print(f'{x}/2')
                dnd_skills.spell_add(chronurgy_wizard_first,dnd_dict.character_dict['spells']['first'],dnd_dict.character_dict['class_spells']['wizard']['first'])
                x+=1
                continue

            elif dnd_dict.character_dict['player_class']['wizard']['subclass'] == 'School of Gravity':
                print(f'{x}/2')
                dnd_skills.spell_add(graviturgy_wizard_first,dnd_dict.character_dict['spells']['first'],dnd_dict.character_dict['class_spells']['wizard']['first'])
                x+=1
                continue

            else:
                print(f'{x}/2')
                dnd_skills.spell_add(wizard_first,dnd_dict.character_dict['spells']['first'],dnd_dict.character_dict['class_spells']['wizard']['first'])
                x+=1
                continue

        elif x == 3:
            break


def second_wizard_level_up():
    x = 1
    for x in range (x,3):
        if x < 3:
# Un-comment this and comment out the other if statements if you want all of the spells
#            dnd_skills.second_level(all_wizard_first,all_wizard_second,dnd_dict.character_dict['class_spells']['wizard']['first'],dnd_dict.character_dict['class_spells']['wizard']['second'])
#                x+=1
#                continue

            if dnd_dict.character_dict['player_class']['wizard']['subclass'] == 'School of Chronurgy':
                print(f'{x}/2')
                dnd_skills.second_level(chronurgy_wizard_first,chronurgy_wizard_second,dnd_dict.character_dict['class_spells']['wizard']['first'],dnd_dict.character_dict['class_spells']['wizard']['second'])
                x+=1
                continue

            elif dnd_dict.character_dict['player_class']['wizard']['subclass'] == 'School of Gravity':
                print(f'{x}/2')
                dnd_skills.second_level(graviturgy_wizard_first,graviturgy_wizard_second,dnd_dict.character_dict['class_spells']['wizard']['first'],dnd_dict.character_dict['class_spells']['wizard']['second'])
                x+=1
                continue

            else:
                print(f'{x}/2')
                dnd_skills.second_level(wizard_first,wizard_second,dnd_dict.character_dict['class_spells']['wizard']['first'],dnd_dict.character_dict['class_spells']['wizard']['second'])
                x+=1
                continue

        elif x == 3:
            break

def third_wizard_level_up():
    x = 1
    for x in range (x,3):
        if x < 3:
# Un-comment this and comment out the other if statements if you want all of the spells
#            dnd_skills.third_level(all_wizard_first,all_wizard_second,all_wizard_third,dnd_dict.character_dict['class_spells']['wizard']['first'],dnd_dict.character_dict['class_spells']['wizard']['second'],dnd_dict.character_dict['class_spells']['wizard']['third'])
#                x+=1
#                continue

            if dnd_dict.character_dict['player_class']['wizard']['subclass'] == 'School of Chronurgy':
                print(f'{x}/2')
                dnd_skills.third_level(chronurgy_wizard_first,chronurgy_wizard_second,chronurgy_wizard_third,dnd_dict.character_dict['class_spells']['wizard']['first'],dnd_dict.character_dict['class_spells']['wizard']['second'],dnd_dict.character_dict['class_spells']['wizard']['third'])
                x+=1
                continue

            elif dnd_dict.character_dict['player_class']['wizard']['subclass'] == 'School of Gravity':
                print(f'{x}/2')
                dnd_skills.third_level(graviturgy_wizard_first,graviturgy_wizard_second,graviturgy_wizard_third,dnd_dict.character_dict['class_spells']['wizard']['first'],dnd_dict.character_dict['class_spells']['wizard']['second'],dnd_dict.character_dict['class_spells']['wizard']['third'])
                x+=1
                continue

            else:
                print(f'{x}/2')
                dnd_skills.third_level(wizard_first,wizard_second,wizard_third,dnd_dict.character_dict['class_spells']['wizard']['first'],dnd_dict.character_dict['class_spells']['wizard']['second'],dnd_dict.character_dict['class_spells']['wizard']['third'])
                x+=1
                continue

        elif x == 3:
            break



def fourth_wizard_level_up():
    x = 1
    for x in range (x,3):
        if x < 3:
# Un-comment this and comment out the other if statements if you want all of the spells
#            dnd_skills.fourth_level(all_wizard_first,all_wizard_second,all_wizard_third,all_wizard_fourth,dnd_dict.character_dict['class_spells']['wizard']['first'],dnd_dict.character_dict['class_spells']['wizard']['second'],dnd_dict.character_dict['class_spells']['wizard']['third'],dnd_dict.character_dict['class_spells']['wizard']['fourth'])
#                x+=1
#                continue

            if dnd_dict.character_dict['player_class']['wizard']['subclass'] == 'School of Chronurgy':
                print(f'{x}/2')
                dnd_skills.fourth_level(chronurgy_wizard_first,chronurgy_wizard_second,chronurgy_wizard_third,chronurgy_wizard_fourth,dnd_dict.character_dict['class_spells']['wizard']['first'],dnd_dict.character_dict['class_spells']['wizard']['second'],dnd_dict.character_dict['class_spells']['wizard']['third'],dnd_dict.character_dict['class_spells']['wizard']['fourth'])
                x+=1
                continue

            elif dnd_dict.character_dict['player_class']['wizard']['subclass'] == 'School of Gravity':
                print(f'{x}/2')
                dnd_skills.fourth_level(graviturgy_wizard_first,graviturgy_wizard_second,graviturgy_wizard_third,graviturgy_wizard_fourth,dnd_dict.character_dict['class_spells']['wizard']['first'],dnd_dict.character_dict['class_spells']['wizard']['second'],dnd_dict.character_dict['class_spells']['wizard']['third'],dnd_dict.character_dict['class_spells']['wizard']['fourth'])
                x+=1
                continue

            else:
                print(f'{x}/2')
                dnd_skills.fourth_level(wizard_first,wizard_second,wizard_third,wizard_fourth,dnd_dict.character_dict['class_spells']['wizard']['first'],dnd_dict.character_dict['class_spells']['wizard']['second'],dnd_dict.character_dict['class_spells']['wizard']['third'],dnd_dict.character_dict['class_spells']['wizard']['fourth'])
                x+=1
                continue

        elif x == 3:
            break


def fifth_wizard_level_up():
    x = 1
    for x in range (x,3):
        if x < 3:
# Un-comment this and comment out the other if statements if you want all of the spells
#            dnd_skills.fifth_level(all_wizard_first,all_wizard_second,all_wizard_third,all_wizard_fourth,all_wizard_fifth,dnd_dict.character_dict['class_spells']['wizard']['first'],dnd_dict.character_dict['class_spells']['wizard']['second'],dnd_dict.character_dict['class_spells']['wizard']['third'],dnd_dict.character_dict['class_spells']['wizard']['fourth'],dnd_dict.character_dict['class_spells']['wizard']['fifth'])
#                x+=1
#                continue

            if dnd_dict.character_dict['player_class']['wizard']['subclass'] == 'School of Chronurgy':
                print(f'{x}/2')
                dnd_skills.fifth_level(chronurgy_wizard_first,chronurgy_wizard_second,chronurgy_wizard_third,chronurgy_wizard_fourth,chronurgy_wizard_fifth,dnd_dict.character_dict['class_spells']['wizard']['first'],dnd_dict.character_dict['class_spells']['wizard']['second'],dnd_dict.character_dict['class_spells']['wizard']['third'],dnd_dict.character_dict['class_spells']['wizard']['fourth'],dnd_dict.character_dict['class_spells']['wizard']['fifth'])
                x+=1
                continue

            elif dnd_dict.character_dict['player_class']['wizard']['subclass'] == 'School of Gravity':
                print(f'{x}/2')
                dnd_skills.fifth_level(graviturgy_wizard_first,graviturgy_wizard_second,graviturgy_wizard_third,graviturgy_wizard_fourth,graviturgy_wizard_fifth,dnd_dict.character_dict['class_spells']['wizard']['first'],dnd_dict.character_dict['class_spells']['wizard']['second'],dnd_dict.character_dict['class_spells']['wizard']['third'],dnd_dict.character_dict['class_spells']['wizard']['fourth'],dnd_dict.character_dict['class_spells']['wizard']['fifth'])
                x+=1
                continue

            else:
                print(f'{x}/2')
                dnd_skills.fifth_level(wizard_first,wizard_second,wizard_third,wizard_fourth,wizard_fifth,dnd_dict.character_dict['class_spells']['wizard']['first'],dnd_dict.character_dict['class_spells']['wizard']['second'],dnd_dict.character_dict['class_spells']['wizard']['third'],dnd_dict.character_dict['class_spells']['wizard']['fourth'],dnd_dict.character_dict['class_spells']['wizard']['fifth'])
                x+=1
                continue

        elif x == 3:
            break




def sixth_wizard_level_up():
    x = 1
    for x in range (x,3):
        if x < 3:
# Un-comment this and comment out the other if statements if you want all of the spells
#            dnd_skills.sixth_level(all_wizard_first,all_wizard_second,all_wizard_third,all_wizard_fourth,all_wizard_fifth,all_wizard_sixth,dnd_dict.character_dict['class_spells']['wizard']['first'],dnd_dict.character_dict['class_spells']['wizard']['second'],dnd_dict.character_dict['class_spells']['wizard']['third'],dnd_dict.character_dict['class_spells']['wizard']['fourth'],dnd_dict.character_dict['class_spells']['wizard']['fifth'],dnd_dict.character_dict['class_spells']['wizard']['sixth'])
#                x+=1
#                continue

            if dnd_dict.character_dict['player_class']['wizard']['subclass'] == 'School of Chronurgy':
                print(f'{x}/2')
                dnd_skills.sixth_level(chronurgy_wizard_first,chronurgy_wizard_second,chronurgy_wizard_third,chronurgy_wizard_fourth,chronurgy_wizard_fifth,chronurgy_wizard_sixth,dnd_dict.character_dict['class_spells']['wizard']['first'],dnd_dict.character_dict['class_spells']['wizard']['second'],dnd_dict.character_dict['class_spells']['wizard']['third'],dnd_dict.character_dict['class_spells']['wizard']['fourth'],dnd_dict.character_dict['class_spells']['wizard']['fifth'],dnd_dict.character_dict['class_spells']['wizard']['sixth'])
                x+=1
                continue

            elif dnd_dict.character_dict['player_class']['wizard']['subclass'] == 'School of Gravity':
                print(f'{x}/2')
                dnd_skills.sixth_level(graviturgy_wizard_first,graviturgy_wizard_second,graviturgy_wizard_third,graviturgy_wizard_fourth,graviturgy_wizard_fifth,graviturgy_wizard_sixth,dnd_dict.character_dict['class_spells']['wizard']['first'],dnd_dict.character_dict['class_spells']['wizard']['second'],dnd_dict.character_dict['class_spells']['wizard']['third'],dnd_dict.character_dict['class_spells']['wizard']['fourth'],dnd_dict.character_dict['class_spells']['wizard']['fifth'],dnd_dict.character_dict['class_spells']['wizard']['sixth'])
                x+=1
                continue

            else:
                print(f'{x}/2')
                dnd_skills.sixth_level(wizard_first,wizard_second,wizard_third,wizard_fourth,wizard_fifth,wizard_sixth,dnd_dict.character_dict['class_spells']['wizard']['first'],dnd_dict.character_dict['class_spells']['wizard']['second'],dnd_dict.character_dict['class_spells']['wizard']['third'],dnd_dict.character_dict['class_spells']['wizard']['fourth'],dnd_dict.character_dict['class_spells']['wizard']['fifth'],dnd_dict.character_dict['class_spells']['wizard']['sixth'])
                x+=1
                continue

        elif x == 3:
            break




def seventh_wizard_level_up():
    x = 1
    for x in range (x,3):
        if x < 3:
# Un-comment this and comment out the other if statements if you want all of the spells
#            dnd_skills.seventh_level(all_wizard_first,all_wizard_second,all_wizard_third,all_wizard_fourth,all_wizard_fifth,all_wizard_sixth,all_wizard_seventh,dnd_dict.character_dict['class_spells']['wizard']['first'],dnd_dict.character_dict['class_spells']['wizard']['second'],dnd_dict.character_dict['class_spells']['wizard']['third'],dnd_dict.character_dict['class_spells']['wizard']['fourth'],dnd_dict.character_dict['class_spells']['wizard']['fifth'],dnd_dict.character_dict['class_spells']['wizard']['sixth'],dnd_dict.character_dict['class_spells']['wizard']['seventh'])
#                x+=1
#                continue

            if dnd_dict.character_dict['player_class']['wizard']['subclass'] == 'School of Chronurgy':
                print(f'{x}/2')
                dnd_skills.seventh_level(chronurgy_wizard_first,chronurgy_wizard_second,chronurgy_wizard_third,chronurgy_wizard_fourth,chronurgy_wizard_fifth,chronurgy_wizard_sixth,chronurgy_wizard_seventh,dnd_dict.character_dict['class_spells']['wizard']['first'],dnd_dict.character_dict['class_spells']['wizard']['second'],dnd_dict.character_dict['class_spells']['wizard']['third'],dnd_dict.character_dict['class_spells']['wizard']['fourth'],dnd_dict.character_dict['class_spells']['wizard']['fifth'],dnd_dict.character_dict['class_spells']['wizard']['sixth'],dnd_dict.character_dict['class_spells']['wizard']['seventh'])
                x+=1
                continue

            elif dnd_dict.character_dict['player_class']['wizard']['subclass'] == 'School of Gravity':
                print(f'{x}/2')
                dnd_skills.seventh_level(graviturgy_wizard_first,graviturgy_wizard_second,graviturgy_wizard_third,graviturgy_wizard_fourth,graviturgy_wizard_fifth,graviturgy_wizard_sixth,graviturgy_wizard_seventh,dnd_dict.character_dict['class_spells']['wizard']['first'],dnd_dict.character_dict['class_spells']['wizard']['second'],dnd_dict.character_dict['class_spells']['wizard']['third'],dnd_dict.character_dict['class_spells']['wizard']['fourth'],dnd_dict.character_dict['class_spells']['wizard']['fifth'],dnd_dict.character_dict['class_spells']['wizard']['sixth'],dnd_dict.character_dict['class_spells']['wizard']['seventh'])
                x+=1
                continue

            else:
                print(f'{x}/2')
                dnd_skills.seventh_level(wizard_first,wizard_second,wizard_third,wizard_fourth,wizard_fifth,wizard_sixth,wizard_seventh,dnd_dict.character_dict['class_spells']['wizard']['first'],dnd_dict.character_dict['class_spells']['wizard']['second'],dnd_dict.character_dict['class_spells']['wizard']['third'],dnd_dict.character_dict['class_spells']['wizard']['fourth'],dnd_dict.character_dict['class_spells']['wizard']['fifth'],dnd_dict.character_dict['class_spells']['wizard']['sixth'],dnd_dict.character_dict['class_spells']['wizard']['seventh'])
                x+=1
                continue

        elif x == 3:
            break




def eighth_wizard_level_up():
    x = 1
    for x in range (x,3):
        if x < 3:
# Un-comment this and comment out the other if statements if you want all of the spells
#            dnd_skills.eighth_level(all_wizard_first,all_wizard_second,all_wizard_third,all_wizard_fourth,all_wizard_fifth,all_wizard_sixth,all_wizard_seventh,all_wizard_eighth,dnd_dict.character_dict['class_spells']['wizard']['first'],dnd_dict.character_dict['class_spells']['wizard']['second'],dnd_dict.character_dict['class_spells']['wizard']['third'],dnd_dict.character_dict['class_spells']['wizard']['fourth'],dnd_dict.character_dict['class_spells']['wizard']['fifth'],dnd_dict.character_dict['class_spells']['wizard']['sixth'],dnd_dict.character_dict['class_spells']['wizard']['seventh'],dnd_dict.character_dict['class_spells']['wizard']['eighth'])
#                x+=1
#                continue

            if dnd_dict.character_dict['player_class']['wizard']['subclass'] == 'School of Chronurgy':
                print(f'{x}/2')
                dnd_skills.eighth_level(chronurgy_wizard_first,chronurgy_wizard_second,chronurgy_wizard_third,chronurgy_wizard_fourth,chronurgy_wizard_fifth,chronurgy_wizard_sixth,chronurgy_wizard_seventh,chronurgy_wizard_eighth,dnd_dict.character_dict['class_spells']['wizard']['first'],dnd_dict.character_dict['class_spells']['wizard']['second'],dnd_dict.character_dict['class_spells']['wizard']['third'],dnd_dict.character_dict['class_spells']['wizard']['fourth'],dnd_dict.character_dict['class_spells']['wizard']['fifth'],dnd_dict.character_dict['class_spells']['wizard']['sixth'],dnd_dict.character_dict['class_spells']['wizard']['seventh'],dnd_dict.character_dict['class_spells']['wizard']['eighth'])
                x+=1
                continue

            elif dnd_dict.character_dict['player_class']['wizard']['subclass'] == 'School of Gravity':
                print(f'{x}/2')
                dnd_skills.eighth_level(graviturgy_wizard_first,graviturgy_wizard_second,graviturgy_wizard_third,graviturgy_wizard_fourth,graviturgy_wizard_fifth,graviturgy_wizard_sixth,graviturgy_wizard_seventh,graviturgy_wizard_eighth,dnd_dict.character_dict['class_spells']['wizard']['first'],dnd_dict.character_dict['class_spells']['wizard']['second'],dnd_dict.character_dict['class_spells']['wizard']['third'],dnd_dict.character_dict['class_spells']['wizard']['fourth'],dnd_dict.character_dict['class_spells']['wizard']['fifth'],dnd_dict.character_dict['class_spells']['wizard']['sixth'],dnd_dict.character_dict['class_spells']['wizard']['seventh'],dnd_dict.character_dict['class_spells']['wizard']['eighth'])
                x+=1
                continue

            else:
                print(f'{x}/2')
                dnd_skills.eighth_level(wizard_first,wizard_second,wizard_third,wizard_fourth,wizard_fifth,wizard_sixth,wizard_seventh,wizard_eighth,dnd_dict.character_dict['class_spells']['wizard']['first'],dnd_dict.character_dict['class_spells']['wizard']['second'],dnd_dict.character_dict['class_spells']['wizard']['third'],dnd_dict.character_dict['class_spells']['wizard']['fourth'],dnd_dict.character_dict['class_spells']['wizard']['fifth'],dnd_dict.character_dict['class_spells']['wizard']['sixth'],dnd_dict.character_dict['class_spells']['wizard']['seventh'],dnd_dict.character_dict['class_spells']['wizard']['eighth'])
                x+=1
                continue

        elif x == 3:
            break





def ninth_wizard_level_up():
    x = 1
    for x in range (x,3):
        if x < 3:
# Un-comment this and comment out the other if statements if you want all of the spells
#            dnd_skills.ninth_level(all_wizard_first,all_wizard_second,all_wizard_third,all_wizard_fourth,all_wizard_fifth,all_wizard_sixth,all_wizard_seventh,all_wizard_eighth,all_wizard_ninth,dnd_dict.character_dict['class_spells']['wizard']['first'],dnd_dict.character_dict['class_spells']['wizard']['second'],dnd_dict.character_dict['class_spells']['wizard']['third'],dnd_dict.character_dict['class_spells']['wizard']['fourth'],dnd_dict.character_dict['class_spells']['wizard']['fifth'],dnd_dict.character_dict['class_spells']['wizard']['sixth'],dnd_dict.character_dict['class_spells']['wizard']['seventh'],dnd_dict.character_dict['class_spells']['wizard']['eighth'],dnd_dict.character_dict['class_spells']['wizard']['ninth'])
#                x+=1
#                continue

            if dnd_dict.character_dict['player_class']['wizard']['subclass'] == 'School of Chronurgy':
                print(f'{x}/2')
                dnd_skills.ninth_level(chronurgy_wizard_first,chronurgy_wizard_second,chronurgy_wizard_third,chronurgy_wizard_fourth,chronurgy_wizard_fifth,chronurgy_wizard_sixth,chronurgy_wizard_seventh,chronurgy_wizard_eighth,chronurgy_wizard_ninth,dnd_dict.character_dict['class_spells']['wizard']['first'],dnd_dict.character_dict['class_spells']['wizard']['second'],dnd_dict.character_dict['class_spells']['wizard']['third'],dnd_dict.character_dict['class_spells']['wizard']['fourth'],dnd_dict.character_dict['class_spells']['wizard']['fifth'],dnd_dict.character_dict['class_spells']['wizard']['sixth'],dnd_dict.character_dict['class_spells']['wizard']['seventh'],dnd_dict.character_dict['class_spells']['wizard']['eighth'],dnd_dict.character_dict['class_spells']['wizard']['ninth'])
                x+=1
                continue

            elif dnd_dict.character_dict['player_class']['wizard']['subclass'] == 'School of Gravity':
                print(f'{x}/2')
                dnd_skills.ninth_level(graviturgy_wizard_first,graviturgy_wizard_second,graviturgy_wizard_third,graviturgy_wizard_fourth,graviturgy_wizard_fifth,graviturgy_wizard_sixth,graviturgy_wizard_seventh,graviturgy_wizard_eighth,graviturgy_wizard_ninth,dnd_dict.character_dict['class_spells']['wizard']['first'],dnd_dict.character_dict['class_spells']['wizard']['second'],dnd_dict.character_dict['class_spells']['wizard']['third'],dnd_dict.character_dict['class_spells']['wizard']['fourth'],dnd_dict.character_dict['class_spells']['wizard']['fifth'],dnd_dict.character_dict['class_spells']['wizard']['sixth'],dnd_dict.character_dict['class_spells']['wizard']['seventh'],dnd_dict.character_dict['class_spells']['wizard']['eighth'],dnd_dict.character_dict['class_spells']['wizard']['ninth'])
                x+=1
                continue

            else:
                print(f'{x}/2')
                dnd_skills.ninth_level(wizard_first,wizard_second,wizard_third,wizard_fourth,wizard_fifth,wizard_sixth,wizard_seventh,wizard_eighth,wizard_ninth,dnd_dict.character_dict['class_spells']['wizard']['first'],dnd_dict.character_dict['class_spells']['wizard']['second'],dnd_dict.character_dict['class_spells']['wizard']['third'],dnd_dict.character_dict['class_spells']['wizard']['fourth'],dnd_dict.character_dict['class_spells']['wizard']['fifth'],dnd_dict.character_dict['class_spells']['wizard']['sixth'],dnd_dict.character_dict['class_spells']['wizard']['seventh'],dnd_dict.character_dict['class_spells']['wizard']['eighth'],dnd_dict.character_dict['class_spells']['wizard']['ninth'])
                x+=1
                continue

        elif x == 3:
            break






def wizard_level_up_all(all_spells):
    x = 1
    for x in range (x,3):
        if x < 3:
            print(f'{x}/2')
            dnd_skills.spell_add(all_spells,dnd_dict.character_dict['spells'],dnd_dict.character_dict['class_spells']['wizard'])
            x+=1
            continue

        elif x == 3:
            break







def wizard_cantrips():
    if dnd_dict.character_dict['player_class']['wizard']['subclass'] == 'School of Chronurgy':
        dnd_skills.spell_add(chronurgy_wizard_cantrip,dnd_dict.character_dict['spells']['cantrips'],dnd_dict.character_dict['class_spells']['wizard_cantrips'])

    elif dnd_dict.character_dict['player_class']['wizard']['subclass'] == 'School of Gravity':
        dnd_skills.spell_add(graviturgy_wizard_cantrips,dnd_dict.character_dict['spells']['cantrips'],dnd_dict.character_dict['class_spells']['wizard_cantrips'])

    else:
        dnd_skills.spell_add(wizard_cantrip,dnd_dict.character_dict['spells']['cantrips'],dnd_dict.character_dict['class_spells']['wizard_cantrips'])







