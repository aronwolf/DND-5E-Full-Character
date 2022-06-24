import dnd_dict, dnd_class, dnd_skills, dnd_magic, dnd_invocations,dnd_infusions, dnd_features

# If the player has the Spellcasting or Pact Magic features, return True
def spellcasting_check():
    if dnd_dict.character_dict['spell_slots']['first'] > 0 or dnd_dict.character_dict['player_class']['warlock']['class_level'] > 0:
        return True

# Used to check if the player is proficient with any martial weapons for Fighting Initiate
def martial_check():
    weapon_prof = dnd_dict.character_dict['Weapon_Prof']
    if 'martial_weapons' in weapon_prof or 'battleaxes' in weapon_prof or 'flails' in weapon_prof or 'glaives' in weapon_prof or 'greataxes' in weapon_prof or 'greatswords' in weapon_prof or 'halberds' in weapon_prof or 'lances' in weapon_prof or 'longswords' in weapon_prof or 'mauls' in weapon_prof or 'morningstars' in weapon_prof or 'pikes' in weapon_prof or 'rapiers' in weapon_prof or 'shortswords' in weapon_prof or 'scimitars' in weapon_prof or 'tridents' in weapon_prof or 'war_picks' in weapon_prof or 'warhammers' in weapon_prof or 'whips' in weapon_prof or 'blowguns' in weapon_prof or 'hand_crossbows' in weapon_prof or 'heavy_crossbows' in weapon_prof or 'longbows' in weapon_prof or 'nets' in weapon_prof:
        return True

# Used to check if the character has a certain armor proficiency
def armor_check(armor):
    if armor in dnd_dict.character_dict['Armor_Prof'].values():
        return True

# Used to determine if you meet the prerequisites for Strixhaven Mascot
def strixhaven_check():
    if dnd_dict.character_dict['total_level'] >= 4 and 'strixhaven_initiate' in dnd_dict.character_dict['feats']:
        return True


# Used for Feats
def choose_feat():
    race = dnd_dict.character_dict['race']
    level = dnd_dict.character_dict['total_level']
    armor_prof = dnd_dict.character_dict['Armor_Prof']
    strength_score = dnd_dict.character_dict['Stats']['strength']['base']
    dexterity_score = dnd_dict.character_dict['Stats']['dexterity']['base']
    constitution_score = dnd_dict.character_dict['Stats']['constitution']['base']
    intelligence_score = dnd_dict.character_dict['Stats']['intelligence']['base']
    wisdom_score = dnd_dict.character_dict['Stats']['wisdom']['base']
    charisma_score = dnd_dict.character_dict['Stats']['charisma']['base']
    feats = dnd_dict.character_dict['feats']
    while True:
        choice = input("""Select your feat:
1) Abberant Dragonmark (prerequisite: No other dragonmark)
2) Actor
3) Alert
4) Artificer Initiate
5) Athlete
6) Bountiful Luck (prerequisite: Halfling)
7) Charger
8) Chef
9) Crossbow Expert
10) Crusher
11) Defensive Duelist(prerequisite: Dexterity 13+)
12) Dragon Fear (prerequisite: Dragonborn)
13) Dragon Hide (prerequisite: Dragonborn)
14) Drow Hide Magic (prerequisite: Drow)
15) Dual Wielder
16) Dungeon Delver
17) Durable
18) Dwarven Fortitude (prerequisite: Dwarf)
19) Eldritch Adept (prerequisite: Spellcasting)
20) Elemental Adept (prerequisite: Spellcasting)
21) Elven Accuracy (prerequisite: Elf/Half-Elf)
22) Fade Away (prerequisite: Gnome)
23) Fey Teleportation (prerequisite: High Elf)
24) Fey Touched
25) Fighting Initiate (prerequisite: Proficiency with a martial weapon)
26) Flames of Phlegethos (prerequisite: Tiefling)
27) Gift of the Chromatic Dragon
28) Gift of the Gem Dragon
29) Gift of the Metallic Dragon
30) Grappler (prerequisite: Strength 13+)
31) Great Weapon Master
32) Gunner
33) Healer
34) Heavily Armored (prerequisite: Proficiency with medium armor)
35) Heavy Armor Master (prerequisite: Proficiency with heavy armor)
36) Infernal Constitution (prerequisite: Tiefling)
37) Inspiring Leader (prerequisite: Charisma 13+)
38) Keen Mind
39) Lightly Armored
40) Linguist
41) Lucky
42) Mage Slayer
43) Magic Initiate
44) Martial Adept
45) Medium Armor Master (prerequisite: Proficiency with medium armor)
46) Metamagic Adept (prerequisite: Spellcasting)
47) Mobile
48) Moderately Armored (prerequisite: Proficiency with light armor)
49) Mounted Combatant
50) Observant
51) Orcish Fury (prerequisite: Half-Orc)
52) Piercer
53) Poisoner
54) Polearm Master
55) Prodigy (prerequisite: Half-Elf/Half-Orc/Human)
56) Resilient
57) Revenant Blade (prerequisite: Elf)
58) Ritual Caster (prerequisite: Intelligence or Wisdom 13 or higher)
59) Savage Attacker
60) Second Chance (prerequisite: Halfling)
61) Sentinel
62) Shadow Touched
63) Sharpshooter
64) Shield Master
65) Skill Expert
66) Skilled
67) Skulker (prerequisite: Dexterity 13+)
68) Slasher
69) Spell Sniper (prerequisite: Spellcasting)
70) Squat Nimbleness (prerequisite: Dwarf or Small Race)
71) Strixhaven Initiate
72) Strixhaven Mascot (prerequisite: At least Level 4, have Strixhaven Initiate feat)
73) Svirfneblin Magic (prerequisite: Deep Gnome)
74) Tavern Brawler
75) Telekinetic
76) Telepathic
77) Tough
78) War Caster (prerequisite: Spellcasting)
79) Weapon Master
80) Wood Elf Magic (prerequisite: Wood Elf)
Enter your selection: """)
        if choice == '1':
            if dnd_dict.character_dict['dragonmark']:
                print("Error: You already have a dragonmark")
                continue
            elif 'abberant_dragonmark' in feats:
                print("Error: Feat Already Known")
                continue
            else:
                dnd_features.abberant_dragonmark()
                break

        elif choice == '2':
            if 'actor' in feats:
                print("Error: Feat Already Known")
                continue
            else:
                dnd_features.actor()
                break

        elif choice == '3':
            if 'alert' in feats:
                print("Error: Feat Already Known")
                continue
            else:
                dnd_features.alert()
                break

        elif choice == '4':
            if 'artificer_initiate' in feats:
                print("Error: Feat Already Known")
                continue
            else:
                dnd_features.artificer_initiate()
                break

        elif choice == '5':
            if 'athlete' in feats:
                print("Error: Feat Already Known")
                continue
            else:
                dnd_features.athlete()
                break

        elif choice == '6':
            if 'bountiful_luck' in feats:
                print("Error: Feat Already Known")
                continue
            elif 'Halfling' not in dnd_dict.character_dict['race']:
                print("Error: You Must Be a Halfling")
                continue
            else:
                dnd_features.bountiful_luck()
                break

        elif choice == '7':
            if 'charger' in feats:
                print("Error: Feat Already Known")
                continue
            else:
                dnd_features.charger()
                break

        elif choice == '8':
            if 'chef' in feats:
                print("Error: Feat Already Known")
                continue
            else:
                dnd_features.chef()
                break

        elif choice == '9':
            if 'crossbow_expert' in feats:
                print("Error: Feat Already Known")
                continue
            else:
                dnd_features.crossbow_expert()
                break

        elif choice == '10':
            if 'crusher' in feats:
                print("Error: Feat Already Known")
                continue
            else:
                dnd_features.crusher()
                break

        elif choice == '11':
            if 'defensive_duelist' in feats:
                print("Error: Feat Already Known")
                continue
            elif dexterity_score < 13:
                print("Error: Your Dexterity Score Must Be At Least 13")
                continue
            else:
                dnd_features.defensive_duelist()
                break

        elif choice == '12':
            if 'dragon_fear' in feats:
                print("Error: Feat Already Known")
                continue
            elif 'Dragonborn' not in dnd_dict.character_dict['race']:
                print("Error: You Must Be A Dragonborn")
                continue
            else:
                dnd_features.dragon_fear()
                break

        elif choice == '13':
            if 'dragon_hide' in feats:
                print("Error: Feat Already Known")
                continue
            elif 'Dragonborn' not in dnd_dict.character_dict['race']:
                print("Error: You Must Be A Dragonborn")
                continue
            else:
                dnd_features.dragon_hide()
                break

        elif choice == '14':
            if 'drow_high_magic' in feats:
                print("Error: Feat Already Known")
                continue
            elif 'Drow' not in dnd_dict.character_dict['race']:
                print("Error: You Must Be A Drow")
                continue
            else:
                dnd_features.drow_high_magic()
                break

        elif choice == '15':
            if 'dual_wielder' in feats:
                print("Error: Feat Already Known")
                continue
            else:
                dnd_features.dual_wielder()
                break

        elif choice == '16':
            if 'dungeon_delver' in feats:
                print("Error: Feat Already Known")
                continue
            else:
                dnd_features.dungeon_delver()
                break

        elif choice == '17':
            if 'durable' in feats:
                print("Error: Feat Already Known")
                continue
            else:
                dnd_features.durable()
                break

        elif choice == '18':
            if 'dwarven_fortitude' in feats:
                print("Error: Feat Already Known")
                continue
            elif 'Dwarf' not in dnd_dict.character_dict['race']:
                print("Error: You Must Be A Dwarf")
                continue
            else:
                dnd_features.dwarven_fortitude()
                break

        elif choice == '19':
            if 'eldritch_adept' in feats:
                print("Error: Feat Already Known")
                continue
            elif not spellcasting_check():
                print("Error: You Must Have Spellcasting")
                continue
            else:
                dnd_features.eldritch_adept()
                break

        elif choice == '20':
            if 'elemental_adept' in feats:
                print("Error: Feat Already Known")
                continue
            elif not spellcasting_check():
                print("Error: You Must Have Spellcasting")
                continue
            else:
                dnd_features.elemental_adept()
                break

        elif choice == '21':
            if 'elven_accuracy' in feats:
                print("Error: Feat Already Known")
                continue
            elif 'Elf' not in dnd_dict.character_dict['race'] and 'Drow' not in dnd_dict.character_dict['race'] and 'Eladrin' not in dnd_dict.character_dict['race'] and 'Kaladesh' not in dnd_dict.character_dict['race'] and 'Half-Elf' not in  dnd_dict.character_dict['race']:
                print("Error: You Must Be An Elf")
                continue
            else:
                dnd_features.elven_accuracy()
                break

        elif choice == '22':
            if 'fade_away' in feats:
                print("Error: Feat Already Known")
                continue
            elif 'Gnome' not in dnd_dict.character_dict['race']:
                print("Error: You Must Be A Gnome")
                continue
            else:
                dnd_features.fade_away()
                break

        elif choice == '23':
            if 'fey_teleportation' in feats:
                print("Error: Feat Already Known")
                continue
            elif 'High Elf' not in dnd_dict.character_dict['race']:
                print("Error: You Must Be A High Elf")
                continue
            else:
                dnd_features.fey_teleportation()
                break

        elif choice == '24':
            if 'fey_touched' in feats:
                print("Error: Feat Already Known")
                continue
            else:
                dnd_features.fey_touched()
                break

        elif choice == '25':
            if 'fighting_initiate' in feats:
                print("Error: Feat Already Known")
                continue
            elif not martial_check():
                print("Error: You Must Have Proficiency With A Martial Weapon")
                continue
            else:
                dnd_features.fighting_initiate()
                break

        elif choice == '26':
            if 'flames_of_phlegethos' in feats:
                print("Error: Feat Already Known")
                continue
            elif 'Tiefling' not in dnd_dict.character_dict['race']:
                print("Error: You Must Be A Tiefling")
                continue
            else:
                dnd_features.flames_of_phlegethos()
                break

        elif choice == '27':
            if 'gift_of_the_chromatic_dragon' in feats:
                print("Error: Feat Already Known")
                continue
            else:
                dnd_features.gift_of_the_chromatic_dragon()
                break

        elif choice == '28':
            if 'gift_of_the_gem_dragon' in feats:
                print("Error: Feat Already Known")
                continue
            else:
                dnd_features.gift_of_the_gem_dragon()
                break

        elif choice == '29':
            if 'gift_of_the_metallic_dragon' in feats:
                print("Error: Feat Already Known")
                continue
            else:
                dnd_features.gift_of_the_metallic_dragon()
                break

        elif choice == '30':
            if 'grappler' in feats:
                print("Error: Feat Already Known")
                continue
            elif strength_score < 13:
                print("Error: Your Strength Score Must Be At Least 13")
                continue
            else:
                dnd_features.grappler()
                break

        elif choice == '31':
            if 'great_weapon_master' in feats:
                print("Error: Feat Already Known")
                continue
            else:
                dnd_features.great_weapon_master()
                break

        elif choice == '32':
            if 'gunner' in feats:
                print("Error: Feat Already Known")
                continue
            else:
                dnd_features.gunner()
                break

        elif choice == '33':
            if 'healer' in feats:
                print("Error: Feat Already Known")
                continue
            else:
                dnd_features.healer()
                break

        elif choice == '34':
            if 'heavily_armored' in feats:
                print("Error: Feat Already Known")
                continue
            elif not armor_check('Medium Armor'):
                print("Error: You Must Have Proficiency with Medium Armor")
                continue
            else:
                dnd_features.heavily_armored()
                break

        elif choice == '35':
            if 'heavy_armor_master' in feats:
                print("Error: Feat Already Known")
                continue
            elif not armor_check('Heavy Armor'):
                print("Error: You Must Have Proficiency with Heavy Armor")
                continue
            else:
                dnd_features.heavy_armor_master()
                break

        elif choice == '36':
            if 'infernal_constitution' in feats:
                print("Error: Feat Already Known")
                continue
            elif 'Tiefling' not in dnd_dict.character_dict['race']:
                print("Error: You Must Be A Tiefling")
                continue
            else:
                dnd_features.infernal_constitution()
                break

        elif choice == '37':
            if 'inspiring_leader' in feats:
                print("Error: Feat Already Known")
                continue
            elif charisma_score < 13:
                print("Error: Your Charisma Score Must Be At Least 13")
                continue
            else:
                dnd_features.inspiring_leader()
                break

        elif choice == '38':
            if 'keen_mind' in feats:
                print("Error: Feat Already Known")
                continue
            else:
                dnd_features.keen_mind()
                break

        elif choice == '39':
            if 'lightly_armored' in feats:
                print("Error: Feat Already Known")
                continue
            else:
                dnd_features.lightly_armored()
                break

        elif choice == '40':
            if 'linguist' in feats:
                print("Error: Feat Already Known")
                continue
            else:
                dnd_features.linguist()
                break

        elif choice == '41':
            if 'lucky' in feats:
                print("Error: Feat Already Known")
                continue
            else:
                dnd_features.lucky()
                break

        elif choice == '42':
            if 'mage_slayer' in feats:
                print("Error: Feat Already Known")
                continue
            else:
                dnd_features.mage_slayer()
                break

        elif choice == '43':
            if 'magic_initiate' in feats:
                print("Error: Feat Already Known")
                continue
            else:
                dnd_features.magic_initiate()
                break

        elif choice == '44':
            if 'martial_adept' in feats:
                print("Error: Feat Already Known")
                continue
            else:
                dnd_features.martial_adept()
                break

        elif choice == '45':
            if 'medium_armor_master' in feats:
                print("Error: Feat Already Known")
                continue
            elif not armor_check('Medium Armor'):
                print("Error: You Must Have Proficiency with Medium Armor")
                continue
            else:
                dnd_features.medium_armor_master()
                break

        elif choice == '46':
            if 'metamagic_adept' in feats:
                print("Error: Feat Already Known")
                continue
            elif not spellcasting_check():
                print("Error: You Must Have Spellcasting")
                continue
            else:
                dnd_features.metamagic_adept()
                break

        elif choice == '47':
            if 'mobile' in feats:
                print("Error: Feat Already Known")
                continue
            else:
                dnd_features.mobile()
                break

        elif choice == '48':
            if 'moderately_armored' in feats:
                print("Error: Feat Already Known")
                continue
            elif not armor_check('Light Armor'):
                print("Error: You Must Have Proficiency with Light Armor")
                continue
            else:
                dnd_features.moderately_armored()
                break

        elif choice == '49':
            if 'mounted_combatant' in feats:
                print("Error: Feat Already Known")
                continue
            else:
                dnd_features.mounted_combatant()
                break

        elif choice == '50':
            if 'observant' in feats:
                print("Error: Feat Already Known")
                continue
            else:
                dnd_features.observant()
                break

        elif choice == '51':
            if 'orcish_fury' in feats:
                print("Error: Feat Already Known")
                continue
            elif 'Half-Orc' not in dnd_dict.character_dict['race']:
                print("Error: You Must Be A Half-Orc")
                continue
            else:
                dnd_features.orcish_fury()
                break

        elif choice == '52':
            if 'piercer' in feats:
                print("Error: Feat Already Known")
                continue
            else:
                dnd_features.piercer()
                break

        elif choice == '53':
            if 'poisoner' in feats:
                print("Error: Feat Already Known")
                continue
            else:
                dnd_features.poisoner()
                break

        elif choice == '54':
            if 'polearm_master' in feats:
                print("Error: Feat Already Known")
                continue
            else:
                dnd_features.polearm_master()
                break

        elif choice == '55':
            if 'prodigy' in feats:
                print("Error: Feat Already Known")
                continue
            elif 'Half-Orc' not in dnd_dict.character_dict['race'] and 'Human' not in dnd_dict.character_dict['race'] and 'Half-Elf' not in dnd_dict.character_dict['race']:
                print("Error: You Must Be A Half-Orc, Half-Elf, or Human")
                continue
            else:
                dnd_features.prodigy()
                break

        elif choice == '56':
            if 'resilient' in feats:
                print("Error: Feat Already Known")
                continue
            else:
                dnd_features.resilient()
                break

        elif choice == '57':
            if 'revenant_blade' in feats:
                print("Error: Feat Already Known")
                continue
            elif 'Elf' not in dnd_dict.character_dict['race'] and 'Drow' not in dnd_dict.character_dict['race'] and 'Eladrin' not in dnd_dict.character_dict['race'] and 'Kaladesh' not in dnd_dict.character_dict['race'] and 'Half-Elf' in dnd_dict.character_dict['race']:
                print("Error: You Must Be An Elf")
                continue
            else:
                dnd_features.revenant_blade()
                break

        elif choice == '58':
            if 'ritual_caster' in feats:
                print("Error: Feat Already Known")
                continue
            elif intelligence_score < 13 and wisdom_score < 13:
                print("Error: Your Intelligence or Wisdom Score Must Be At Least 13")
                continue
            else:
                dnd_features.ritual_caster()
                break

        elif choice == '59':
            if 'savage_attacker' in feats:
                print("Error: Feat Already Known")
                continue
            else:
                dnd_features.savage_attacker()
                break

        elif choice == '60':
            if 'second_chance' in feats:
                print("Error: Feat Already Known")
                continue
            elif 'Halfling' not in dnd_dict.character_dict['race']:
                print("Error: You Must Be A Halfling")
                continue
            else:
                dnd_features.second_chance()
                break

        elif choice == '61':
            if 'sentinel' in feats:
                print("Error: Feat Already Known")
                continue
            else:
                dnd_features.sentinel()
                break

        elif choice == '62':
            if 'shadow_touched' in feats:
                print("Error: Feat Already Known")
                continue
            else:
                dnd_features.shadow_touched()
                break

        elif choice == '63':
            if 'sharpshooter' in feats:
                print("Error: Feat Already Known")
                continue
            else:
                dnd_features.sharpshooter()
                break

        elif choice == '64':
            if 'shield_master' in feats:
                print("Error: Feat Already Known")
                continue
            else:
                dnd_features.shield_master()
                break

        elif choice == '65':
            if 'skill_expert' in feats:
                print("Error: Feat Already Known")
                continue
            else:
                dnd_features.skill_expert()
                break

        elif choice == '66':
            if 'skilled' in feats:
                print("Error: Feat Already Known")
                continue
            else:
                dnd_features.skilled()
                break

        elif choice == '67':
            if 'skulker' in feats:
                print("Error: Feat Already Known")
                continue
            elif dexterity_score < 13:
                print("Error: Your Dexterity Score Must Be At Least 13")
                continue
            else:
                dnd_features.skulker()
                break

        elif choice == '68':
            if 'slasher' in feats:
                print("Error: Feat Already Known")
                continue
            else:
                dnd_features.slasher()
                break

        elif choice == '69':
            if 'spell_sniper' in feats:
                print("Error: Feat Already Known")
                continue
            elif not dnd_dict.character_dict['spells']:
                print("Error: You Must Be Able To Cast At Least One Spell")
                continue
            else:
                dnd_features.spell_sniper()
                break

        elif choice == '70':
            if 'squat_nimbleness' in feats:
                print("Error: Feat Already Known")
                continue
            elif 'Dwarf' not in dnd_dict.character_dict['race'] and dnd_dict.character_dict['size'] != 'Small':
                print("Error: You Must Be A Dwarf or Small Race")
                continue
            else:
                dnd_features.squat_nimbleness()
                break

        elif choice == '71':
            if 'strixhaven_initiate' in feats:
                print("Error: Feat Already Known")
                continue
            else:
                dnd_features.strixhaven_initiate()
                break

        elif choice == '72':
            if 'strixhaven_mascot' in feats:
                print("Error: Feat Already Known")
                continue
            elif not strixhaven_check():
                print("Error: You Must Be At Least Level 4 And Have The Strixhaven Initiate Feat")
                continue
            else:
                dnd_features.strixhaven_mascot()
                break

        elif choice == '73':
            if 'svirfneblin_magic' in feats:
                print("Error: Feat Already Known")
                continue
            elif dnd_dict.character_dict['race'] != 'Deep Gnome':
                print("Error: You Must Be A Deep Gnome")
                continue
            else:
                dnd_features.svirfneblin_magic()
                break

        elif choice == '74':
            if 'tavern_brawler' in feats:
                print("Error: Feat Already Known")
                continue
            else:
                dnd_features.tavern_brawler()
                break

        elif choice == '75':
            if 'telekinetic' in feats:
                print("Error: Feat Already Known")
                continue
            else:
                dnd_features.telekinetic()
                break

        elif choice == '76':
            if 'telepathic' in feats:
                print("Error: Feat Already Known")
                continue
            else:
                dnd_features.telepathic()
                break

        elif choice == '77':
            if 'tough' in feats:
                print("Error: Feat Already Known")
                continue
            else:
                dnd_features.tough()
                break

        elif choice == '78':
            if 'war_caster' in feats:
                print("Error: Feat Already Known")
                continue
            elif not dnd_dict.character_dict['spells']:
                print("Error: You Must Be Able To Cast At Least One Spell")
                continue
            else:
                dnd_features.war_caster()
                break

        elif choice == '79':
            if 'weapon_master' in feats:
                print("Error: Feat Already Known")
                continue
            else:
                dnd_features.weapon_master()
                break

        elif choice == '80':
            if 'wood_elf_magic' in feats:
                print("Error: Feat Already Known")
                continue
            elif dnd_dict.character_dict['race'] != 'Wood Elf':
                print("Error: You Must Be A Wood Elf")
                continue
            else:
                dnd_features.wood_elf_magic()
                break

        else:
            print("Error: Invalid Input")
            continue







#        elif choice == '':
#            if '' in feats:
#                print("Error: Feat Already Known")
#                continue
#            else:
#                dnd_features.()
#                break
#
#
#        elif choice == '':
#            if '' in feats:
#                print("Error: Feat Already Known")
#                continue
#            elif '' not in dnd_dict.character_dict['race']:
#                print("Error: You Must Be A ")
#                continue
#            else:
#                dnd_features.()
#                break
#
#        elif choice == '':
#            if '' in feats:
#                print("Error: Feat Already Known")
#                continue
#            elif not spellcasting_check():
#                print("Error: You Must Have Spellcasting")
#                continue
#            else:
#                dnd_features.()
#                break
#
#        elif choice == '':
#            if '' in feats:
#                print("Error: Feat Already Known")
#                continue
#            elif _score < 13:
#                print("Error: Your  Score Must Be At Least 13")
#                continue
#            else:
#                dnd_features.()
#                break
#
#        elif choice == '':
#            if '' in feats:
#                print("Error: Feat Already Known")
#                continue
#            elif not armor_check(' Armor'):
#                print("Error: You Must Have Proficiency with  Armor")
#                continue
#            else:
#                dnd_features.()
#                break







































