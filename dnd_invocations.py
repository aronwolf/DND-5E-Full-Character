import dnd_dict, dnd_features,dnd_skills

dict = dnd_dict.character_dict["invocations"]
pact = dnd_dict.character_dict["player_class"]["warlock"].values()
spell = dnd_dict.character_dict["spells"].values()
#cantrip = dnd_dict.character_dict['spells']
needed_cantrip = dnd_dict.character_dict['spells']

# Used if Eldritch Blast is needed as a cantrip
def eldritch_req():
    if 'eldritch_blast' in dnd_dict.character_dict['spells']['cantrips']:
        return True

# Used if a level requirement is needed
def level_req(level):
    if dnd_dict.character_dict["total_level"] >= level:
        return True

# Used if you need a pact
def pact_req(pact_needed):
    if dnd_dict.character_dict['player_class']['warlock']['pact'] == pact_needed:
        return True

# Used if a level requirement and pact feature are  needed
def level_pact(level,pact_req):
    if dnd_dict.character_dict["total_level"] >= level and dnd_dict.character_dict['player_class']['warlock']['pact'] == pact_req:
        return True

# Used if a level requirement is needed and Hex in spells
def spell_req(level):
    if dnd_dict.character_dict["total_level"] >= level and 'Hex' in dnd_dict.character_dict['spells']['first'].values():
        return True

# Check to see if the player has at least one level in the warlock class
def warlock_class():
    if dnd_dict.character_dict['player_class']['warlock']['class_level'] == 0:
        return True

def invocations():
    while True:
        choice = input("""Select the invocation you want:
1) Agonizing Blast (need Eldritch Blast cantrip)
2) Armor of Shadows
3) Ascendant Step (need to be at least level 9)
4) Aspect of the Moon (need Pact of the Tome)
5) Beast Speech
6) Beguiling Influence
7) Bewitching Whispers (need to be at least level 7)
8) Bond of the Talisman (need Pact of the Talisman and at least level 12)
9) Book of Ancient Secrets (need Pact of the Tome)
10) Chains of Carceri (need Pact of the Chain and at least level 15)
11) Cloak of Flies (need to be at least level 5)
12) Devil's Sight
13) Dreadful Word (need to be at least level 7)
14) Eldritch Mind
15) Eldritch Sight
16) Eldritch Smite (need Pact of the Blade and at least level 5)
17) Eldritch Spear (need Eldritch Blast)
18) Eyes of the Rune Keeper
19) Far Scribe (need Pact of the Tome and at least level 5)
20) Fiendish Vigor
21) Gaze of Two Minds
22) Ghostly Gaze (need to be at least level 7)
23) Gift of the Depths (need to be at least level 5)
24) Gift of the Ever-Living Ones (need Pact of the Chain)
25) Gift of the Protectors (need Pact of the Tome and to be at least level 9)
26) Grasp of Hadar (need Eldritch Blast)
27) Improved Pact Weapon (need Pact of the Blade)
28) Investment of the Chain Master (need Pact of the Chain)
29) Lance of Lethargy (need Eldritch Blast)
30) Lifedrinker (need Pact of the Blade and to be at least level 12)
31) Maddening Hex (need to be at least level 5 and have the Hex spell or a warlock feature that curses)
32) Mask of Many Faces
33) Master of Myriad Forms (need to be at least level 15)
34) Minions of Chaos (need to be at least level 9)
35) Mire the Mind (need to be at least level 5)
36) Misty Visions
37) One with Shadows (need to be at least level 5)
38) Otherworldly Leap (need to be at least level 9)
39) Protection of the Talisman (need to have Pact of the Talisman and to be at least level 7)
40) Rebuke of the Talisman (need Pact of the Talisman)
41) Relentless Hex (need to be at least level 7 and have Hex or a warlock feature that curses)
42) Repelling Blast (need Eldritch Blast)
43) Sculptor of Flesh (need to be at least level 7)
44) Shroud of Shadow (need to be at least level 15)
45) Sign of Ill Omen (need to be at least level 5)
46) Thief of Five Fates
47) Thirsting Blade (need Pact of the Blade and to be at least level 5)
48) Tomb of Levistus (need to be at least level 5)
49) Trickster's Escape (need to be at least level 7)
50) Undying Servitude (need to be at least 5th-level warlock)
51) Visions of Distant Realms (need to be at least level 15)
52) Voice of the Chain Master (need Pact of the Chain)
53) Whispers of the Grave (need to be at least level 9)
54) Witch Sight (need to be at least level 15)
Enter your selection: """)


        if choice == '1':
            if "agonizing_blast" in dict:
                print("Invocation already known")
                continue
            elif eldritch_req():
                dnd_features.agonizing_blast()
                break
            else:
                print("Error: You Must Know Eldritch Blast")
                continue

        elif choice == '2':
            if 'armor_of_shadows' in dict:
                print("Invocation already known")
                continue
            else:
                dnd_features.armor_of_shadows()
                break
    
        elif choice == '3':
            if 'ascendant_step' in dict:
                print("Invocation already known")
                continue
            elif level_req(9):
                dnd_features.ascendant_step()
                break
            else:
                print("Error: You Must Be At Least Level 9")
                continue
    
        elif choice == '4':
            if 'aspect_of_the_moon' in dict:
                print("Invocation already known")
                continue
            elif pact_req("Tome"):
                dnd_features.aspect_of_the_moon()
                break
            else:
                print("Error: You Must Have the Pact of the Tome")
                continue
    
        elif choice == '5':
            if 'beast_speech' in dict:
                print("Invocation already known")
                continue
            else:
                dnd_features.beast_speech()
                break
    
        elif choice == '6':
            if 'beguiling_influence' in dict:
                print("Invocation already known")
                continue
            elif 'deception' in dnd_dict.character_dict['skill_prof'] and 'persuasion' in dnd_dict.character_dict['skill_prof']:
                print("You are already proficient with Deception and Persuasion")
                continue
            else:
                dnd_features.beguiling_influence()
                break
    
        elif choice == '7':
            if 'bewitching_whispers' in dict:
                print("Invocation already known")
                continue
            elif level_req(7):
                dnd_features.bewitching_whispers()
                break
            else:
                print("Error: You Must Be At Least Level 7")
                continue
    
    
        elif choice == '8':
            if 'bond_of_the_talisman' in dict:
                print("Invocation already known")
                continue
            elif level_pact(12,'Talisman'):
                dnd_features.bond_of_the_talisman()
                break
            elif dnd_dict.character_dict['total_level'] < 12 and 'Talisman' not in pact:
                print("Error: You Must Be At Least Level 12 and Have Pact of the Talisman")
                continue
            elif dnd_dict.character_dict['total_level'] < 12:
                print("Error: You Must Be At Least Level 12")
                continue
            elif 'Talisman' not in pact:
                print("Error: You Must Have the Pact of the Talisman")
                continue
    
    
        elif choice == '9':
            if 'book_of_ancient_secrets' in dict:
                print("Invocation already known")
                continue
            elif pact_req("Tome"):
                dnd_features.book_of_ancient_secrets()
                break
            else:
                print("Error: You Must Have the Pact of the Tome")
                continue
    
    
        elif choice == '10':
            if 'chains_of_carceri' in dict:
                print("Invocation already known")
                continue
            elif level_pact(15,'Chain'):
                dnd_features.chains_of_carceri()
                break
            elif dnd_dict.character_dict['total_level'] < 15 and 'Chain' not in pact:
                print("Error: You Must Be At Least Level 15 and Have Pact of the Chain")
                continue
            elif dnd_dict.character_dict['total_level'] < 15:
                print("Error: You Must Be At Least Level 15")
                continue
            elif 'Chain' not in pact:
                print("Error: You Must Have the Pact of the Chain")
                continue
    
        elif choice == '11':
            if 'cloak_of_flies' in dict:
                print("Invocation already known")
                continue
            elif level_req(5):
                dnd_features.cloak_of_flies()
                break
            else:
                print("Error: You Must Be At Least Level 5")
                continue
    
        elif choice == '12':
            if 'devils_sight' in dict:
                print("Invocation already known")
                continue
            else:
                dnd_features.devils_sight()
                break
    
        elif choice == '13':
            if 'dreadful_word' in dict:
                print("Invocation already known")
                continue
            elif level_req(7):
                dnd_features.dreadful_word()
                break
            else:
                print("Error: You Must Be At Least Level 7")
                continue
    
        elif choice == '14':
            if 'eldritch_mind' in dict:
                print("Invocation already known")
                continue
            else:
                dnd_features.eldritch_mind()
                break
    
        elif choice == '14':
            if 'eldritch_mind' in dict:
                print("Invocation already known")
                continue
            else:
                dnd_features.eldritch_mind()
                break
    
        elif choice == '15':
            if 'eldritch_sight' in dict:
                print("Invocation already known")
                continue
            else:
                dnd_features.eldritch_sight()
                break
    
        elif choice == '16':
            if 'eldritch_smite' in dict:
                print("Invocation already known")
                continue
            elif level_pact(5,'Blade'):
                dnd_features.eldritch_smite()
                break
            elif dnd_dict.character_dict['total_level'] < 5 and 'Blade' not in pact:
                print("Error: You Must Be At Least Level 5 and Have Pact of the Blade")
                continue
            elif dnd_dict.character_dict['total_level'] < 5:
                print("Error: You Must Be At Least Level 5")
                continue
            elif 'Blade' not in pact:
                print("Error: You Must Have the Pact of the Blade")
                continue
    
        elif choice == '17':
            if "eldritch_spear" in dict:
                print("Invocation already known")
                continue
            elif eldritch_req():
                dnd_features.eldritch_spear()
                break
            else:
                print("Error: You Must Know Eldritch Blast")
                continue
    
        elif choice == '18':
            if 'eyes_of_the_rune_keeper' in dict:
                print("Invocation already known")
                continue
            else:
                dnd_features.eyes_of_the_rune_keeper()
                break
    
        elif choice == '19':
            if 'far_scribe' in dict:
                print("Invocation already known")
                continue
            elif level_pact(5,'Tome'):
                dnd_features.far_scribe()
                break
            elif dnd_dict.character_dict['total_level'] < 5 and 'Tome' not in pact:
                print("Error: You Must Be At Least Level 5 and Have Pact of the Tome")
                continue
            elif dnd_dict.character_dict['total_level'] < 5:
                print("Error: You Must Be At Least Level 5")
                continue
            elif 'Tome' not in pact:
                print("Error: You Must Have the Pact of the Tome")
                continue
    
        elif choice == '20':
            if 'fiendish_vigor' in dict:
                print("Invocation already known")
                continue
            else:
                dnd_features.fiendish_vigor()
                break
    
        elif choice == '21':
            if 'gaze_of_two_minds' in dict:
                print("Invocation already known")
                continue
            else:
                dnd_features.gaze_of_two_minds()
                break
    
        elif choice == '22':
            if 'ghostly_gaze' in dict:
                print("Invocation already known")
                continue
            elif level_req(7):
                dnd_features.ghostly_gaze()
                break
            else:
                print("Error: You Must Be At Least Level 7")
                continue
    
        elif choice == '23':
            if 'gift_of_the_depths' in dict:
                print("Invocation already known")
                continue
            elif level_req(5):
                dnd_features.gift_of_the_depths()
                break
            else:
                print("Error: You Must Be At Least Level 5")
                continue
    
    
        elif choice == '24':
            if 'gift_of_the_ever-living_ones' in dict:
                print("Invocation already known")
                continue
            elif pact_req("Chain"):
                dnd_features.gift_of_the_ever_living_ones()
                break
            else:
                print("Error: You Must Have Pact of the Chain")
                continue
    
        elif choice == '25':
            if 'gift_of_the_protectors' in dict:
                print("Invocation already known")
                continue
            elif level_pact(9,'Tome'):
                dnd_features.gift_of_the_protectors()
                break
            elif dnd_dict.character_dict['total_level'] < 9 and 'Tome' not in pact:
                print("Error: You Must Be At Least Level 9 and Have Pact of the Tome")
                continue
            elif dnd_dict.character_dict['total_level'] < 9:
                print("Error: You Must Be At Least Level 9")
                continue
            elif 'Tome' not in pact:
                print("Error: You Must Have the Pact of the Tome")
                continue
    
        elif choice == '26':
            if "grasp_of_hadar" in dict:
                print("Invocation already known")
                continue
            elif eldritch_req():
                dnd_features.grasp_of_hadar()
                break
            else:
                print("Error: You Must Know Eldritch Blast")
                continue
    
        elif choice == '27':
            if 'improved_pact_weapon' in dict:
                print("Invocation already known")
                continue
            elif pact_req("Blade"):
                dnd_features.improved_pact_weapon()
                break
            else:
                print("Error: You Must Have the Pact of the Blade")
                continue
    
        elif choice == '28':
            if 'investment_of_the_chain_master' in dict:
                print("Invocation already known")
                continue
            elif pact_req("Chain"):
                dnd_features.investment_of_the_chain_master()
                break
            else:
                print("Error: You Must Have the Pact of the Chain")
                continue
    
        elif choice == '29':
            if "lance_of_lethargy" in dict:
                print("Invocation already known")
                continue
            elif eldritch_req():
                dnd_features.lance_of_lethargy()
                break
            else:
                print("Error: You Must Know Eldritch Blast")
                continue
    
        elif choice == '30':
            if 'lifedrinker' in dict:
                print("Invocation already known")
                continue
            elif level_pact(12,'Blade'):
                dnd_features.lifedrinker()
                break
            elif dnd_dict.character_dict['total_level'] < 12 and 'Blade' not in pact:
                print("Error: You Must Be At Least Level 12 and Have Pact of the Blade")
                continue
            elif dnd_dict.character_dict['total_level'] < 12:
                print("Error: You Must Be At Least Level 12")
                continue
            elif 'Blade' not in pact:
                print("Error: You Must Have the Pact of the Blade")
                continue
    
        elif choice == '31':
            if 'maddening_hex' in dict:
                print("Invocation already known")
                continue
            elif spell_req(5):
                dnd_features.maddening_hex()
                break
            elif dnd_dict.character_dict['total_level'] < 5 and 'Hex' not in dnd_dict.character_dict['spells'].values():
                print("Error: You Must Be At Least Level 5 and Know Hex")
                continue
            elif dnd_dict.character_dict['total_level'] < 5:
                print("Error: You Must Be At Least Level 5")
                continue
            elif "Hex" not in dnd_dict.character_dict['spells'].values():
                print("Error: You Must Know Hex")
                continue
    
        elif choice == '32':
            if 'mask_of_many_faces' in dict:
                print("Invocation already known")
                continue
            else:
                dnd_features.mask_of_many_faces()
                break
    
        elif choice == '33':
            if 'master_of_myriad_forms' in dict:
                print("Invocation already known")
                continue
            elif level_req(15):
                dnd_features.master_of_myriad_forms()
                break
            else:
                print("Error: You Must Be At Least Level 15")
                continue
    
        elif choice == '34':
            if 'minions_of_chaos' in dict:
                print("Invocation already known")
                continue
            elif level_req(9):
                dnd_features.minions_of_chaos()
                break
            else:
                print("Error: You Must Be At Least Level 9")
                continue
    
        elif choice == '35':
            if 'mire_the_mind' in dict:
                print("Invocation already known")
                continue
            elif level_req(5):
                dnd_features.mire_the_mind()
                break
            else:
                print("Error: You Must Be At Least Level 5")
                continue
    
        elif choice == '36':
            if 'misty_visions' in dict:
                print("Invocation already known")
                continue
            else:
                dnd_features.misty_visions()
                break
    
        elif choice == '37':
            if 'one_with_shadows' in dict:
                print("Invocation already known")
                continue
            elif level_req(5):
                dnd_features.one_with_shadows()
                break
            else:
                print("Error: You Must Be At Least Level 5")
                continue
    
        elif choice == '38':
            if 'otherworldly_leap' in dict:
                print("Invocation already known")
                continue
            elif level_req(9):
                dnd_features.otherworldly_leap()
                break
            else:
                print("Error: You Must Be At Least Level 9")
                continue
    
        elif choice == '39':
            if 'protection_of_the_talisman' in dict:
                print("Invocation already known")
                continue
            elif level_pact(7,'Talisman'):
                dnd_features.protection_of_the_talisman()
                break
            elif dnd_dict.character_dict['total_level'] < 9 and 'Talisman' not in pact:
                print("Error: You Must Be At Least Level 9 and Have Pact of the Talisman")
                continue
            elif dnd_dict.character_dict['total_level'] < 9:
                print("Error: You Must Be At Least Level 9")
                continue
            elif 'Talisman' not in pact:
                print("Error: You Must Have the Pact of the Talisman")
                continue
    
        elif choice == '40':
            if 'rebuke_of_the_talisman' in dict:
                print("Invocation already known")
                continue
            elif pact_req("Talisman"):
                dnd_features.rebuke_of_the_talisman()
                break
            else:
                print("Error: You Must Have the Pact of the Talisman")
                continue
    
        elif choice == '41':
            if 'relentless_hex' in dict:
                print("Invocation already known")
                continue
            elif spell_req(7):
                dnd_features.relentless_hex()
                break
            elif dnd_dict.character_dict['total_level'] < 7 and 'Hex' not in dnd_dict.character_dict['spells'].values():
                print("Error: You Must Be At Least Level 7 and Know Hex")
                continue
            elif dnd_dict.character_dict['total_level'] < 7:
                print("Error: You Must Be At Least Level 7")
                continue
            elif "Hex" not in dnd_dict.character_dict['spells'].values():
                print("Error: You Must Know Hex")
                continue
    
        elif choice == '42':
            if "repelling_blast" in dict:
                print("Invocation already known")
                continue
            elif eldritch_req():
                dnd_features.repelling_blast()
                break
            else:
                print("Error: You Must Know Eldritch Blast")
                continue
    
        elif choice == '43':
            if 'sculptor_of_flesh' in dict:
                print("Invocation already known")
                continue
            elif level_req(7):
                dnd_features.sculptor_of_flesh()
                break
            else:
                print("Error: You Must Be At Least Level 7")
                continue
    
        elif choice == '44':
            if 'shroud_of_shadow' in dict:
                print("Invocation already known")
                continue
            elif level_req(15):
                dnd_features.shroud_of_shadow()
                break
            else:
                print("Error: You Must Be At Least Level 15")
                continue
    
        elif choice == '45':
            if 'sign_of_ill_omen' in dict:
                print("Invocation already known")
                continue
            elif level_req(5):
                dnd_features.sign_of_ill_omen()
                break
            else:
                print("Error: You Must Be At Least Level 5")
                continue
    
        elif choice == '46':
            if 'thief_of_five_fates' in dict:
                print("Invocation already known")
                continue
            else:
                dnd_features.thief_of_five_fates()
                break
    
        elif choice == '47':
            if 'thirsting_blade' in dict:
                print("Invocation already known")
                continue
            elif level_pact(5,'Blade'):
                dnd_features.thirsting_blade()
                break
            elif dnd_dict.character_dict['total_level'] < 5 and 'Blade' not in pact:
                print("Error: You Must Be At Least Level 5 and Have Pact of the Blade")
                continue
            elif dnd_dict.character_dict['total_level'] < 5:
                print("Error: You Must Be At Least Level 5")
                continue
            elif 'Blade' not in pact:
                print("Error: You Must Have the Pact of the Blade")
                continue
    
        elif choice == '48':
            if 'tomb_of_levistus' in dict:
                print("Invocation already known")
                continue
            elif level_req(5):
                dnd_features.tomb_of_levistus()
                break
            else:
                print("Error: You Must Be At Least Level 5")
                continue
    
        elif choice == '49':
            if 'tricksters_escape' in dict:
                print("Invocation already known")
                continue
            elif level_req(7):
                dnd_features.tricksters_escape()
                break
            else:
                print("Error: You Must Be At Least Level 7")
                continue
    
        elif choice == '50':
            if 'undying_sevitude' in dict:
                print("Invocation already known")
                continue
            elif dnd_dict.character_dict['player_class']['warlock']['class_level'] >=5:
                dnd_features.undying_servitude()
                break
            else:
                print("Error: You Must Have At Least 5 Levels in the Warlock Class")
                continue
    
        elif choice == '51':
            if 'visions_of_distant_realms' in dict:
                print("Invocation already known")
                continue
            elif level_req(15):
                dnd_features.visions_of_distant_realms()
                break
            else:
                print("Error: You Must Be At Least Level 15")
                continue
    
        elif choice == '52':
            if 'voice_of_the_chain_master' in dict:
                print("Invocation already known")
                continue
            elif pact_req("Chain"):
                dnd_features.voice_of_the_chain_master()
                break
            else:
                print("Error: You Must Have the Pact of the Chain")
                continue
    
        elif choice == '53':
            if 'whispers_of_the_grave' in dict:
                print("Invocation already known")
                continue
            elif level_req(9):
                dnd_features.whispers_of_the_grave()
                break
            else:
                print("Error: You Must Be At Least Level 9")
                continue
    
        elif choice == '54':
            if 'witch_sight' in dict:
                print("Invocation already known")
                continue
            elif level_req(15):
                dnd_features.witch_sight()
                break
            else:
                print("Error: You Must Be At Least Level 15")
                continue
    
        else:
            print("Error: Invalid Input")
            continue



def eldritch_adept_invocations():
    while True:
        choice = input("""Select the invocation you want:
1) Agonizing Blast (need Eldritch Blast cantrip)
2) Armor of Shadows
3) Ascendant Step (need to be at least level 9)
4) Aspect of the Moon (need Pact of the Tome)
5) Beast Speech
6) Beguiling Influence
7) Bewitching Whispers (need to be at least level 7)
8) Bond of the Talisman (need Pact of the Talisman and at least level 12)
9) Book of Ancient Secrets (need Pact of the Tome)
10) Chains of Carceri (need Pact of the Chain and at least level 15)
11) Cloak of Flies (need to be at least level 5)
12) Devil's Sight
13) Dreadful Word (need to be at least level 7)
14) Eldritch Mind
15) Eldritch Sight
16) Eldritch Smite (need Pact of the Blade and at least level 5)
17) Eldritch Spear (need Eldritch Blast)
18) Eyes of the Rune Keeper
19) Far Scribe (need Pact of the Tome and at least level 5)
20) Fiendish Vigor
21) Gaze of Two Minds
22) Ghostly Gaze (need to be at least level 7)
23) Gift of the Depths (need to be at least level 5)
24) Gift of the Ever-Living Ones (need Pact of the Chain)
25) Gift of the Protectors (need Pact of the Tome and to be at least level 9)
26) Grasp of Hadar (need Eldritch Blast)
27) Improved Pact Weapon (need Pact of the Blade)
28) Investment of the Chain Master (need Pact of the Chain)
29) Lance of Lethargy (need Eldritch Blast)
30) Lifedrinker (need Pact of the Blade and to be at least level 12)
31) Maddening Hex (need to be at least level 5 and have the Hex spell or a warlock feature that curses)
32) Mask of Many Faces
33) Master of Myriad Forms (need to be at least level 15)
34) Minions of Chaos (need to be at least level 9)
35) Mire the Mind (need to be at least level 5)
36) Misty Visions
37) One with Shadows (need to be at least level 5)
38) Otherworldly Leap (need to be at least level 9)
39) Protection of the Talisman (need to have Pact of the Talisman and to be at least level 7)
40) Rebuke of the Talisman (need Pact of the Talisman)
41) Relentless Hex (need to be at least level 7 and have Hex or a warlock feature that curses)
42) Repelling Blast (need Eldritch Blast)
43) Sculptor of Flesh (need to be at least level 7)
44) Shroud of Shadow (need to be at least level 15)
45) Sign of Ill Omen (need to be at least level 5)
46) Thief of Five Fates
47) Thirsting Blade (need Pact of the Blade and to be at least level 5)
48) Tomb of Levistus (need to be at least level 5)
49) Trickster's Escape (need to be at least level 7)
50) Undying Servitude (need to be at least 5th-level warlock)
51) Visions of Distant Realms (need to be at least level 15)
52) Voice of the Chain Master (need Pact of the Chain)
53) Whispers of the Grave (need to be at least level 9)
54) Witch Sight (need to be at least level 15)
Enter your selection: """)


        if choice == '1':
            if "agonizing_blast" in dict:
                print("Invocation already known")
                continue
            elif warlock_class():
                print("Error: You must have at least 1 level in Warlock to select this invocation")
                continue
            elif eldritch_req():
                dnd_features.agonizing_blast()
                break
            else:
                print("Error: You Must Know Eldritch Blast")
                continue

        elif choice == '2':
            if 'armor_of_shadows' in dict:
                print("Invocation already known")
                continue
            else:
                dnd_features.armor_of_shadows()
                break
    
        elif choice == '3':
            if 'ascendant_step' in dict:
                print("Invocation already known")
                continue
            elif level_req(9):
                dnd_features.ascendant_step()
                break
            elif warlock_class():
                print("Error: You must have at least 1 level in Warlock to select this invocation")
                continue
            else:
                print("Error: You Must Be At Least Level 9")
                continue
    
        elif choice == '4':
            if 'aspect_of_the_moon' in dict:
                print("Invocation already known")
                continue
            elif warlock_class():
                print("Error: You must have at least 1 level in Warlock to select this invocation")
                continue
            elif pact_req("Tome"):
                dnd_features.aspect_of_the_moon()
                break
            else:
                print("Error: You Must Have the Pact of the Tome")
                continue
    
        elif choice == '5':
            if 'beast_speech' in dict:
                print("Invocation already known")
                continue
            else:
                dnd_features.beast_speech()
                break
    
        elif choice == '6':
            if 'beguiling_influence' in dict:
                print("Invocation already known")
                continue
            elif 'deception' in dnd_dict.character_dict['skill_prof'] and 'persuasion' in dnd_dict.character_dict['skill_prof']:
                print("You are already proficient with Deception and Persuasion")
                continue
            else:
                dnd_features.beguiling_influence()
                break
    
        elif choice == '7':
            if 'bewitching_whispers' in dict:
                print("Invocation already known")
                continue
            elif warlock_class():
                print("Error: You must have at least 1 level in Warlock to select this invocation")
                continue
            elif level_req(7):
                dnd_features.bewitching_whispers()
                break
            else:
                print("Error: You Must Be At Least Level 7")
                continue
    
    
        elif choice == '8':
            if 'bond_of_the_talisman' in dict:
                print("Invocation already known")
                continue
            elif warlock_class():
                print("Error: You must have at least 1 level in Warlock to select this invocation")
                continue
            elif level_pact(12,'Talisman'):
                dnd_features.bond_of_the_talisman()
                break
            elif dnd_dict.character_dict['total_level'] < 12 and 'Talisman' not in pact:
                print("Error: You Must Be At Least Level 12 and Have Pact of the Talisman")
                continue
            elif dnd_dict.character_dict['total_level'] < 12:
                print("Error: You Must Be At Least Level 12")
                continue
            elif 'Talisman' not in pact:
                print("Error: You Must Have the Pact of the Talisman")
                continue
    
    
        elif choice == '9':
            if 'book_of_ancient_secrets' in dict:
                print("Invocation already known")
                continue
            elif warlock_class():
                print("Error: You must have at least 1 level in Warlock to select this invocation")
                continue
            elif pact_req("Tome"):
                dnd_features.book_of_ancient_secrets()
                break
            else:
                print("Error: You Must Have the Pact of the Tome")
                continue
    
    
        elif choice == '10':
            if 'chains_of_carceri' in dict:
                print("Invocation already known")
                continue
            elif warlock_class():
                print("Error: You must have at least 1 level in Warlock to select this invocation")
                continue
            elif level_pact(15,'Chain'):
                dnd_features.chains_of_carceri()
                break
            elif dnd_dict.character_dict['total_level'] < 15 and 'Chain' not in pact:
                print("Error: You Must Be At Least Level 15 and Have Pact of the Chain")
                continue
            elif dnd_dict.character_dict['total_level'] < 15:
                print("Error: You Must Be At Least Level 15")
                continue
            elif 'Chain' not in pact:
                print("Error: You Must Have the Pact of the Chain")
                continue
    
        elif choice == '11':
            if 'cloak_of_flies' in dict:
                print("Invocation already known")
                continue
            elif warlock_class():
                print("Error: You must have at least 1 level in Warlock to select this invocation")
                continue
            elif level_req(5):
                dnd_features.cloak_of_flies()
                break
            else:
                print("Error: You Must Be At Least Level 5")
                continue
    
        elif choice == '12':
            if 'devils_sight' in dict:
                print("Invocation already known")
                continue
            else:
                dnd_features.devils_sight()
                break
    
        elif choice == '13':
            if 'dreadful_word' in dict:
                print("Invocation already known")
                continue
            elif warlock_class():
                print("Error: You must have at least 1 level in Warlock to select this invocation")
                continue
            elif level_req(7):
                dnd_features.dreadful_word()
                break
            else:
                print("Error: You Must Be At Least Level 7")
                continue
    
        elif choice == '14':
            if 'eldritch_mind' in dict:
                print("Invocation already known")
                continue
            else:
                dnd_features.eldritch_mind()
                break
    
        elif choice == '14':
            if 'eldritch_mind' in dict:
                print("Invocation already known")
                continue
            else:
                dnd_features.eldritch_mind()
                break
    
        elif choice == '15':
            if 'eldritch_sight' in dict:
                print("Invocation already known")
                continue
            else:
                dnd_features.eldritch_sight()
                break
    
        elif choice == '16':
            if 'eldritch_smite' in dict:
                print("Invocation already known")
                continue
            elif warlock_class():
                print("Error: You must have at least 1 level in Warlock to select this invocation")
                continue
            elif level_pact(5,'Blade'):
                dnd_features.eldritch_smite()
                break
            elif dnd_dict.character_dict['total_level'] < 5 and 'Blade' not in pact:
                print("Error: You Must Be At Least Level 5 and Have Pact of the Blade")
                continue
            elif dnd_dict.character_dict['total_level'] < 5:
                print("Error: You Must Be At Least Level 5")
                continue
            elif 'Blade' not in pact:
                print("Error: You Must Have the Pact of the Blade")
                continue
    
        elif choice == '17':
            if "eldritch_spear" in dict:
                print("Invocation already known")
                continue
            elif warlock_class():
                print("Error: You must have at least 1 level in Warlock to select this invocation")
                continue
            elif eldritch_req():
                dnd_features.eldritch_spear()
                break
            else:
                print("Error: You Must Know Eldritch Blast")
                continue
    
        elif choice == '18':
            if 'eyes_of_the_rune_keeper' in dict:
                print("Invocation already known")
                continue
            else:
                dnd_features.eyes_of_the_rune_keeper()
                break
    
        elif choice == '19':
            if 'far_scribe' in dict:
                print("Invocation already known")
                continue
            elif warlock_class():
                print("Error: You must have at least 1 level in Warlock to select this invocation")
                continue
            elif level_pact(5,'Tome'):
                dnd_features.far_scribe()
                break
            elif dnd_dict.character_dict['total_level'] < 5 and 'Tome' not in pact:
                print("Error: You Must Be At Least Level 5 and Have Pact of the Tome")
                continue
            elif dnd_dict.character_dict['total_level'] < 5:
                print("Error: You Must Be At Least Level 5")
                continue
            elif 'Tome' not in pact:
                print("Error: You Must Have the Pact of the Tome")
                continue
    
        elif choice == '20':
            if 'fiendish_vigor' in dict:
                print("Invocation already known")
                continue
            else:
                dnd_features.fiendish_vigor()
                break
    
        elif choice == '21':
            if 'gaze_of_two_minds' in dict:
                print("Invocation already known")
                continue
            else:
                dnd_features.gaze_of_two_minds()
                break
    
        elif choice == '22':
            if 'ghostly_gaze' in dict:
                print("Invocation already known")
                continue
            elif warlock_class():
                print("Error: You must have at least 1 level in Warlock to select this invocation")
                continue
            elif level_req(7):
                dnd_features.ghostly_gaze()
                break
            else:
                print("Error: You Must Be At Least Level 7")
                continue
    
        elif choice == '23':
            if 'gift_of_the_depths' in dict:
                print("Invocation already known")
                continue
            elif warlock_class():
                print("Error: You must have at least 1 level in Warlock to select this invocation")
                continue
            elif level_req(5):
                dnd_features.gift_of_the_depths()
                break
            else:
                print("Error: You Must Be At Least Level 5")
                continue
    
    
        elif choice == '24':
            if 'gift_of_the_ever-living_ones' in dict:
                print("Invocation already known")
                continue
            elif warlock_class():
                print("Error: You must have at least 1 level in Warlock to select this invocation")
                continue
            elif pact_req("Chain"):
                dnd_features.gift_of_the_ever_living_ones()
                break
            else:
                print("Error: You Must Have Pact of the Chain")
                continue
    
        elif choice == '25':
            if 'gift_of_the_protectors' in dict:
                print("Invocation already known")
                continue
            elif warlock_class():
                print("Error: You must have at least 1 level in Warlock to select this invocation")
                continue
            elif level_pact(9,'Tome'):
                dnd_features.gift_of_the_protectors()
                break
            elif dnd_dict.character_dict['total_level'] < 9 and 'Tome' not in pact:
                print("Error: You Must Be At Least Level 9 and Have Pact of the Tome")
                continue
            elif dnd_dict.character_dict['total_level'] < 9:
                print("Error: You Must Be At Least Level 9")
                continue
            elif 'Tome' not in pact:
                print("Error: You Must Have the Pact of the Tome")
                continue
    
        elif choice == '26':
            if "grasp_of_hadar" in dict:
                print("Invocation already known")
                continue
            elif warlock_class():
                print("Error: You must have at least 1 level in Warlock to select this invocation")
                continue
            elif eldritch_req():
                dnd_features.grasp_of_hadar()
                break
            else:
                print("Error: You Must Know Eldritch Blast")
                continue
    
        elif choice == '27':
            if 'improved_pact_weapon' in dict:
                print("Invocation already known")
                continue
            elif warlock_class():
                print("Error: You must have at least 1 level in Warlock to select this invocation")
                continue
            elif pact_req("Blade"):
                dnd_features.improved_pact_weapon()
                break
            else:
                print("Error: You Must Have the Pact of the Blade")
                continue
    
        elif choice == '28':
            if 'investment_of_the_chain_master' in dict:
                print("Invocation already known")
                continue
            elif warlock_class():
                print("Error: You must have at least 1 level in Warlock to select this invocation")
                continue
            elif pact_req("Chain"):
                dnd_features.investment_of_the_chain_master()
                break
            else:
                print("Error: You Must Have the Pact of the Chain")
                continue
    
        elif choice == '29':
            if "lance_of_lethargy" in dict:
                print("Invocation already known")
                continue
            elif warlock_class():
                print("Error: You must have at least 1 level in Warlock to select this invocation")
                continue
            elif eldritch_req():
                dnd_features.lance_of_lethargy()
                break
            else:
                print("Error: You Must Know Eldritch Blast")
                continue
    
        elif choice == '30':
            if 'lifedrinker' in dict:
                print("Invocation already known")
                continue
            elif warlock_class():
                print("Error: You must have at least 1 level in Warlock to select this invocation")
                continue
            elif level_pact(12,'Blade'):
                dnd_features.lifedrinker()
                break
            elif dnd_dict.character_dict['total_level'] < 12 and 'Blade' not in pact:
                print("Error: You Must Be At Least Level 12 and Have Pact of the Blade")
                continue
            elif dnd_dict.character_dict['total_level'] < 12:
                print("Error: You Must Be At Least Level 12")
                continue
            elif 'Blade' not in pact:
                print("Error: You Must Have the Pact of the Blade")
                continue
    
        elif choice == '31':
            if 'maddening_hex' in dict:
                print("Invocation already known")
                continue
            elif warlock_class():
                print("Error: You must have at least 1 level in Warlock to select this invocation")
                continue
            elif spell_req(5):
                dnd_features.maddening_hex()
                break
            elif dnd_dict.character_dict['total_level'] < 5 and 'Hex' not in dnd_dict.character_dict['spells'].values():
                print("Error: You Must Be At Least Level 5 and Know Hex")
                continue
            elif dnd_dict.character_dict['total_level'] < 5:
                print("Error: You Must Be At Least Level 5")
                continue
            elif "Hex" not in dnd_dict.character_dict['spells'].values():
                print("Error: You Must Know Hex")
                continue
    
        elif choice == '32':
            if 'mask_of_many_faces' in dict:
                print("Invocation already known")
                continue
            else:
                dnd_features.mask_of_many_faces()
                break
    
        elif choice == '33':
            if 'master_of_myriad_forms' in dict:
                print("Invocation already known")
                continue
            elif warlock_class():
                print("Error: You must have at least 1 level in Warlock to select this invocation")
                continue
            elif level_req(15):
                dnd_features.master_of_myriad_forms()
                break
            else:
                print("Error: You Must Be At Least Level 15")
                continue
    
        elif choice == '34':
            if 'minions_of_chaos' in dict:
                print("Invocation already known")
                continue
            elif warlock_class():
                print("Error: You must have at least 1 level in Warlock to select this invocation")
                continue
            elif level_req(9):
                dnd_features.minions_of_chaos()
                break
            else:
                print("Error: You Must Be At Least Level 9")
                continue
    
        elif choice == '35':
            if 'mire_the_mind' in dict:
                print("Invocation already known")
                continue
            elif warlock_class():
                print("Error: You must have at least 1 level in Warlock to select this invocation")
                continue
            elif level_req(5):
                dnd_features.mire_the_mind()
                break
            else:
                print("Error: You Must Be At Least Level 5")
                continue
    
        elif choice == '36':
            if 'misty_visions' in dict:
                print("Invocation already known")
                continue
            else:
                dnd_features.misty_visions()
                break
    
        elif choice == '37':
            if 'one_with_shadows' in dict:
                print("Invocation already known")
                continue
            elif warlock_class():
                print("Error: You must have at least 1 level in Warlock to select this invocation")
                continue
            elif level_req(5):
                dnd_features.one_with_shadows()
                break
            else:
                print("Error: You Must Be At Least Level 5")
                continue
    
        elif choice == '38':
            if 'otherworldly_leap' in dict:
                print("Invocation already known")
                continue
            elif warlock_class():
                print("Error: You must have at least 1 level in Warlock to select this invocation")
                continue
            elif level_req(9):
                dnd_features.otherworldly_leap()
                break
            else:
                print("Error: You Must Be At Least Level 9")
                continue
    
        elif choice == '39':
            if 'protection_of_the_talisman' in dict:
                print("Invocation already known")
                continue
            elif warlock_class():
                print("Error: You must have at least 1 level in Warlock to select this invocation")
                continue
            elif level_pact(7,'Talisman'):
                dnd_features.protection_of_the_talisman()
                break
            elif dnd_dict.character_dict['total_level'] < 9 and 'Talisman' not in pact:
                print("Error: You Must Be At Least Level 9 and Have Pact of the Talisman")
                continue
            elif dnd_dict.character_dict['total_level'] < 9:
                print("Error: You Must Be At Least Level 9")
                continue
            elif 'Talisman' not in pact:
                print("Error: You Must Have the Pact of the Talisman")
                continue
    
        elif choice == '40':
            if 'rebuke_of_the_talisman' in dict:
                print("Invocation already known")
                continue
            elif warlock_class():
                print("Error: You must have at least 1 level in Warlock to select this invocation")
                continue
            elif pact_req("Talisman"):
                dnd_features.rebuke_of_the_talisman()
                break
            else:
                print("Error: You Must Have the Pact of the Talisman")
                continue
    
        elif choice == '41':
            if 'relentless_hex' in dict:
                print("Invocation already known")
                continue
            elif warlock_class():
                print("Error: You must have at least 1 level in Warlock to select this invocation")
                continue
            elif spell_req(7):
                dnd_features.relentless_hex()
                break
            elif warlock_class():
                print("Error: You must have at least 1 level in Warlock to select this invocation")
                continue
            elif dnd_dict.character_dict['total_level'] < 7 and 'Hex' not in dnd_dict.character_dict['spells'].values():
                print("Error: You Must Be At Least Level 7 and Know Hex")
                continue
            elif dnd_dict.character_dict['total_level'] < 7:
                print("Error: You Must Be At Least Level 7")
                continue
            elif "Hex" not in dnd_dict.character_dict['spells'].values():
                print("Error: You Must Know Hex")
                continue
    
        elif choice == '42':
            if "repelling_blast" in dict:
                print("Invocation already known")
                continue
            elif warlock_class():
                print("Error: You must have at least 1 level in Warlock to select this invocation")
                continue
            elif eldritch_req():
                dnd_features.repelling_blast()
                break
            else:
                print("Error: You Must Know Eldritch Blast")
                continue
    
        elif choice == '43':
            if 'sculptor_of_flesh' in dict:
                print("Invocation already known")
                continue
            elif warlock_class():
                print("Error: You must have at least 1 level in Warlock to select this invocation")
                continue
            elif level_req(7):
                dnd_features.sculptor_of_flesh()
                break
            else:
                print("Error: You Must Be At Least Level 7")
                continue
    
        elif choice == '44':
            if 'shroud_of_shadow' in dict:
                print("Invocation already known")
                continue
            elif warlock_class():
                print("Error: You must have at least 1 level in Warlock to select this invocation")
                continue
            elif level_req(15):
                dnd_features.shroud_of_shadow()
                break
            else:
                print("Error: You Must Be At Least Level 15")
                continue
    
        elif choice == '45':
            if 'sign_of_ill_omen' in dict:
                print("Invocation already known")
                continue
            elif warlock_class():
                print("Error: You must have at least 1 level in Warlock to select this invocation")
                continue
            elif level_req(5):
                dnd_features.sign_of_ill_omen()
                break
            else:
                print("Error: You Must Be At Least Level 5")
                continue
    
        elif choice == '46':
            if 'thief_of_five_fates' in dict:
                print("Invocation already known")
                continue
            else:
                dnd_features.thief_of_five_fates()
                break
    
        elif choice == '47':
            if 'thirsting_blade' in dict:
                print("Invocation already known")
                continue
            elif warlock_class():
                print("Error: You must have at least 1 level in Warlock to select this invocation")
                continue
            elif level_pact(5,'Blade'):
                dnd_features.thirsting_blade()
                break
            elif dnd_dict.character_dict['total_level'] < 5 and 'Blade' not in pact:
                print("Error: You Must Be At Least Level 5 and Have Pact of the Blade")
                continue
            elif dnd_dict.character_dict['total_level'] < 5:
                print("Error: You Must Be At Least Level 5")
                continue
            elif 'Blade' not in pact:
                print("Error: You Must Have the Pact of the Blade")
                continue
    
        elif choice == '48':
            if 'tomb_of_levistus' in dict:
                print("Invocation already known")
                continue
            elif warlock_class():
                print("Error: You must have at least 1 level in Warlock to select this invocation")
                continue
            elif level_req(5):
                dnd_features.tomb_of_levistus()
                break
            else:
                print("Error: You Must Be At Least Level 5")
                continue
    
        elif choice == '49':
            if 'tricksters_escape' in dict:
                print("Invocation already known")
                continue
            elif warlock_class():
                print("Error: You must have at least 1 level in Warlock to select this invocation")
                continue
            elif level_req(7):
                dnd_features.tricksters_escape()
                break
            else:
                print("Error: You Must Be At Least Level 7")
                continue
    
        elif choice == '50':
            if 'undying_sevitude' in dict:
                print("Invocation already known")
                continue
            elif dnd_dict.character_dict['player_class']['warlock']['class_level'] >=5:
                dnd_features.undying_servitude()
                break
            else:
                print("Error: You Must Have At Least 5 Levels in the Warlock Class")
                continue
    
        elif choice == '51':
            if 'visions_of_distant_realms' in dict:
                print("Invocation already known")
                continue
            elif warlock_class():
                print("Error: You must have at least 1 level in Warlock to select this invocation")
                continue
            elif level_req(15):
                dnd_features.visions_of_distant_realms()
                break
            else:
                print("Error: You Must Be At Least Level 15")
                continue
    
        elif choice == '52':
            if 'voice_of_the_chain_master' in dict:
                print("Invocation already known")
                continue
            elif warlock_class():
                print("Error: You must have at least 1 level in Warlock to select this invocation")
                continue
            elif pact_req("Chain"):
                dnd_features.voice_of_the_chain_master()
                break
            else:
                print("Error: You Must Have the Pact of the Chain")
                continue
    
        elif choice == '53':
            if 'whispers_of_the_grave' in dict:
                print("Invocation already known")
                continue
            elif warlock_class():
                print("Error: You must have at least 1 level in Warlock to select this invocation")
                continue
            elif level_req(9):
                dnd_features.whispers_of_the_grave()
                break
            else:
                print("Error: You Must Be At Least Level 9")
                continue
    
        elif choice == '54':
            if 'witch_sight' in dict:
                print("Invocation already known")
                continue
            elif warlock_class():
                print("Error: You must have at least 1 level in Warlock to select this invocation")
                continue
            elif level_req(15):
                dnd_features.witch_sight()
                break
            else:
                print("Error: You Must Be At Least Level 15")
                continue
    
        else:
            print("Error: Invalid Input")
            continue







def first_invocations():
    x = 1
    for x in range (x,3):
        if x < 3:
            print(f'{x}/2')
            invocations()
            x+=1
            continue

        elif x == 3:
            break

# Delete the skill from the skill list.
def invocation_swap():
    while True:
        choice = input("""Do you want to swap out an invocation?
1) Yes
2) No
Enter your choice: """)
        if choice == '1':
            dnd_skills.invocation_change(dnd_dict.character_dict['invocations'],dnd_dict.character_dict['pact_invocations'],dnd_dict.character_dict['features'])
            invocations()
            break
        elif choice == '2':
            break
        else:
            print("Error: Invalid Input")
            continue

def eldritch_adept_swap():
    if 'eldritch_adept' in dnd_dict.character_dict['feats']:
        while True:
            choice = input("""Do you want to swap out an invocation?
1) Yes
2) No
Enter your choice: """)
            if choice == '1':
                dnd_skills.invocation_change(dnd_dict.character_dict['invocations'],dnd_dict.character_dict['pact_invocations'],dnd_dict.character_dict['features'])
                eldritch_adept_invocations()
                break
            elif choice == '2':
                break
            else:
                print("Error: Invalid Input")
                continue
