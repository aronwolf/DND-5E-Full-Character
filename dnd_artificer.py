import dnd_dict, dnd_features, dnd_magic, dnd_skills, dnd_infusions, dnd_level_up,math

level = dnd_dict.character_dict['player_class']['artificer']['class_level']
subclass = dnd_dict.character_dict['player_class']['artificer']['subclass']


def artificer():
    if dnd_dict.character_dict['player_class']['artificer']['class_level']== 1:
        armor_prof = {'light_armor':'Light Armor','medium_armor':'Medium Armor','shields':'Shields'}
        dnd_dict.character_dict['Armor_Prof'].update(armor_prof)
        dnd_dict.character_dict["Kits"]['thieves_tools'] = 'Thieve\'s Tools'
        dnd_dict.character_dict["Tools"]['tinker_tools'] = 'Tinker\'s Tools'


        dnd_dict.character_dict["d8"] += 1
        if dnd_dict.character_dict['spell_slots']['first'] == 0:
            dnd_dict.character_dict['half_caster_level'] +=2
        else:
            dnd_dict.character_dict['half_caster_level'] +=1

        dnd_skills.spell_slot_selection()
        dnd_features.artificer_features()
        dnd_magic.artificer_magic()
        spell_attack = ((dnd_dict.character_dict["Stats"]["intelligence"]['mod']) + dnd_dict.character_dict['prof_bonus'])
        dnd_dict.character_dict["spell_modifier"]['intelligence']['attack'] = spell_attack
        spell_save = ((dnd_dict.character_dict["Stats"]["intelligence"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
        dnd_dict.character_dict["spell_modifier"]['intelligence']['save'] = spell_save
        dnd_dict.character_dict['d8']+=1
        dnd_level_up.level_up(8)

# Level 2
    if dnd_dict.character_dict['player_class']['artificer']['class_level']  == 2:
        dnd_features.infuse_item()
        dnd_infusions.art_infusions2()
        dnd_dict.character_dict['half_caster_level'] +=1
        dnd_dict.character_dict['d8']+=1
        dnd_skills.spell_slot_selection()
        dnd_level_up.level_up(8)

# Level 3
    if dnd_dict.character_dict['player_class']['artificer']['class_level']  == 3:
        dnd_infusions.art_swap(dnd_infusions.artificer_2)
        while True:
            choice = input("""Select the subclass you want to have:
1) Alchemist
2) Armorer
3) Artillerist
4) Battle Smith
Enter your selection: """)
            if choice == '1':
                dnd_dict.character_dict['player_class']['artificer']['subclass']  = 'Alchemist'
                dnd_features.alchemist3()
                new_spells = {'healing_word':'Healing Word','ray_of_sickness':'Ray of Sickness'}
                dnd_dict.character_dict['spells']['first'].update(new_spells)
                dnd_dict.character_dict['class_spells']['artificer']['first'].update(new_spells)
                dnd_dict.character_dict['special_spells']['first'].update(new_spells)
                break

            elif choice == '2':
                dnd_dict.character_dict['player_class']['artificer']['subclass']  = 'Armorer'
                dnd_features.armorer3()
                new_spells = {'magic_missile':'Magic Missile','thunderwave':'Thunderwave'}
                dnd_dict.character_dict['spells']['first'].update(new_spells)
                dnd_dict.character_dict['class_spells']['artificer']['first'].update(new_spells)
                dnd_dict.character_dict['special_spells']['first'].update(new_spells)
                break
                
            elif choice == '3':
                dnd_dict.character_dict['player_class']['artificer']['subclass']  = 'Artillerist'
                dnd_features.artillerist3()
                new_spells = {'shield':'Shield','thunderwave':'Thunderwave'}
                dnd_dict.character_dict['spells']['first'].update(new_spells)
                dnd_dict.character_dict['class_spells']['artificer']['first'].update(new_spells)
                dnd_dict.character_dict['special_spells']['first'].update(new_spells)
                break
                
            elif choice == '4':
                dnd_dict.character_dict['player_class']['artificer']['subclass']  = 'Battle Smith'
                dnd_features.battle_smith3()
                new_spells = {'heroism':'Heroism','shield':'Shield'}
                dnd_dict.character_dict['spells']['first'].update(new_spells)
                dnd_dict.character_dict['class_spells']['artificer']['first'].update(new_spells)
                dnd_dict.character_dict['special_spells']['first'].update(new_spells)
                break
                
            else:
                print("Error: Invalid Input")
                continue

        dnd_dict.character_dict['half_caster_level'] +=1
        dnd_skills.spell_slot_selection()
        dnd_dict.character_dict['d8']+=1
        dnd_level_up.level_up(8)

# Level 4
    if dnd_dict.character_dict['player_class']['artificer']['class_level']  == 4:
        dnd_infusions.art_swap(dnd_infusions.artificer_2)
        dnd_level_up.asi_or_feat()
        dnd_dict.character_dict['half_caster_level'] +=1
        dnd_skills.spell_slot_selection()
        dnd_dict.character_dict['d8']+=1
        dnd_level_up.level_up(8)

# Level 5
    if dnd_dict.character_dict['player_class']['artificer']['class_level']  == 5:
        dnd_infusions.art_swap(dnd_infusions.artificer_2)
        if dnd_dict.character_dict['player_class']['artificer']['subclass']  == 'Alchemist':
            new_spells = {'flaming_sphere':'Flaming Sphere','melf\'s_acid_arrow':'Melf\'s Acid Arrow'}
            dnd_dict.character_dict['spells']['second'].update(new_spells)
            dnd_dict.character_dict['class_spells']['artificer']['second'].update(new_spells)
            dnd_dict.character_dict['special_spells']['second'].update(new_spells)
            dnd_features.alchemist5()

        if dnd_dict.character_dict['player_class']['artificer']['subclass']  == 'Armorer':
            new_spells = {'mirror_image':'Mirror Image','shatter':'Shatter'}
            dnd_dict.character_dict['spells']['second'].update(new_spells)
            dnd_dict.character_dict['class_spells']['artificer']['second'].update(new_spells)
            dnd_dict.character_dict['special_spells']['second'].update(new_spells)
            dnd_features.extra_attack()

        if dnd_dict.character_dict['player_class']['artificer']['subclass']  == 'Artillerist':
            new_spells = {'scorching_ray':'Scorching Ray','shatter':'Shatter'}
            dnd_dict.character_dict['spells']['second'].update(new_spells)
            dnd_dict.character_dict['class_spells']['artificer']['second'].update(new_spells)
            dnd_dict.character_dict['special_spells']['second'].update(new_spells)
            dnd_features.extra_attack()

        if dnd_dict.character_dict['player_class']['artificer']['subclass']  == 'Battle Smith':
            new_spells = {'branding_smite':'Branding Smite','warding_bond':'Warding Bond'}
            dnd_dict.character_dict['spells']['second'].update(new_spells)
            dnd_dict.character_dict['class_spells']['artificer']['second'].update(new_spells)
            dnd_dict.character_dict['special_spells']['second'].update(new_spells)
            dnd_features.extra_attack()


        dnd_magic.artificer_second()
        dnd_dict.character_dict['half_caster_level'] +=1
        dnd_skills.spell_slot_selection()
        dnd_dict.character_dict['d8']+=1
        dnd_level_up.level_up(8)

# Level 6
    if dnd_dict.character_dict['player_class']['artificer']['class_level']  == 6:
        dnd_infusions.art_swap(dnd_infusions.artificer_2)
# Select two more cantrips
        x = 1
        for x in range (x,3):
            if x < 3:
                print(f'{x}/2')
                dnd_skills.spell_add(dnd_magic.artificer_cantrip,dnd_dict.character_dict['spells'],dnd_dict.character_dict['class_spells']['artificer'])
                x+=1
                continue
            elif x == 3:
                break

        dnd_infusions.art_infusions6()
        dnd_features.tool_expertise()
        dnd_dict.character_dict['half_caster_level'] +=1
        dnd_skills.spell_slot_selection()
        dnd_dict.character_dict['d8']+=1
        dnd_level_up.level_up(8)

# Level 7
    if dnd_dict.character_dict['player_class']['artificer']['class_level']  == 7:




        dnd_infusions.art_swap(dnd_infusions.artificer_6)
        dnd_features.flash_of_genius()
        dnd_dict.character_dict['half_caster_level'] +=1
        dnd_skills.spell_slot_selection()
        dnd_dict.character_dict['d8']+=1
        dnd_level_up.level_up(8)

# Level 8
    if dnd_dict.character_dict['player_class']['artificer']['class_level']  == 8:





        dnd_infusions.art_swap(dnd_infusions.artificer_6)
        dnd_level_up.asi_or_feat()
        dnd_dict.character_dict['half_caster_level'] +=1
        dnd_skills.spell_slot_selection()
        dnd_dict.character_dict['d8']+=1
        dnd_level_up.level_up(8)

# Level 9
    if dnd_dict.character_dict['player_class']['artificer']['class_level']  == 9:
        dnd_infusions.art_swap(dnd_infusions.artificer_6)

        if dnd_dict.character_dict['player_class']['artificer']['subclass']  == 'Alchemist':
            new_spells = {'gaseous_form':'Gaseous Form','mass_healing_word':'Mass Healing Word'}
            dnd_dict.character_dict['spells']['third'].update(new_spells)
            dnd_dict.character_dict['class_spells']['artificer']['third'].update(new_spells)
            dnd_dict.character_dict['special_spells']['third'].update(new_spells)
            dnd_features.alchemist9()

        if dnd_dict.character_dict['player_class']['artificer']['subclass']  == 'Armorer':
            new_spells = {'hypnotic_pattern':'Hypnotic Patter','lightning_bolt':'Lightning Bolt'}
            dnd_dict.character_dict['spells']['third'].update(new_spells)
            dnd_dict.character_dict['class_spells']['artificer']['third'].update(new_spells)
            dnd_dict.character_dict['special_spells']['third'].update(new_spells)
            dnd_features.armorer9()

        if dnd_dict.character_dict['player_class']['artificer']['subclass']  == 'Artillerist':
            new_spells = {'fireball':'Fireball','wind_wall':'Wind Wall'}
            dnd_dict.character_dict['spells']['third'].update(new_spells)
            dnd_dict.character_dict['class_spells']['artificer']['third'].update(new_spells)
            dnd_dict.character_dict['special_spells']['third'].update(new_spells)
            dnd_features.artillerist9()

        if dnd_dict.character_dict['player_class']['artificer']['subclass']  == 'Battle Smith':
            new_spells = {'aura_of_vitality':'Aura of Vitality','conjure_barrage':'Conjure Barrage'}
            dnd_dict.character_dict['spells']['third'].update(new_spells)
            dnd_dict.character_dict['class_spells']['artificer']['third'].update(new_spells)
            dnd_dict.character_dict['special_spells']['third'].update(new_spells)
            dnd_features.battle_smith9()





        dnd_magic.artificer_third()
        dnd_dict.character_dict['half_caster_level'] +=1
        dnd_skills.spell_slot_selection()
        dnd_dict.character_dict['d8']+=1
        dnd_level_up.level_up(8)

# Level 10
    if dnd_dict.character_dict['player_class']['artificer']['class_level']  == 10:

        dnd_infusions.art_swap(dnd_infusions.artificer_6)

# Select two more cantrips
        x = 1
        for x in range (x,3):
            if x < 3:
                print(f'{x}/2')
                dnd_skills.spell_add(dnd_magic.artificer_cantrip,dnd_dict.character_dict['spells'],dnd_dict.character_dict['class_spells']['artificer'])
                x+=1
                continue
            elif x == 3:
                break

        dnd_infusions.art_infusions10()
        dnd_features.magic_item_adept()
        dnd_dict.character_dict['half_caster_level'] +=1
        dnd_skills.spell_slot_selection()
        dnd_dict.character_dict['d8']+=1
        dnd_level_up.level_up(8)

# Level 11
    if dnd_dict.character_dict['player_class']['artificer']['class_level']  == 11:
        dnd_infusions.art_swap(dnd_infusions.artificer_10)
        dnd_features.spell_storing_item()
        dnd_dict.character_dict['half_caster_level'] +=1
        dnd_skills.spell_slot_selection()
        dnd_dict.character_dict['d8']+=1
        dnd_level_up.level_up(8)

# Level 12
    if dnd_dict.character_dict['player_class']['artificer']['class_level']  == 12:
        dnd_infusions.art_swap(dnd_infusions.artificer_10)






        dnd_level_up.asi_or_feat()
        dnd_dict.character_dict['half_caster_level'] +=1
        dnd_skills.spell_slot_selection()
        dnd_dict.character_dict['d8']+=1
        dnd_level_up.level_up(8)

# Level 13
    if dnd_dict.character_dict['player_class']['artificer']['class_level']  == 13:
        dnd_infusions.art_swap(dnd_infusions.artificer_10)

        if dnd_dict.character_dict['player_class']['artificer']['subclass']  == 'Alchemist':
            new_spells = {'blight':'Blight','death_ward':'Death Ward'}
            dnd_dict.character_dict['spells']['fourth'].update(new_spells)
            dnd_dict.character_dict['class_spells']['artificer']['fourth'].update(new_spells)
            dnd_dict.character_dict['special_spells']['fourth'].update(new_spells)

        if dnd_dict.character_dict['player_class']['artificer']['subclass']  == 'Armorer':
            new_spells = {'fire_shield':'Fire Shield','greater_invisibility':'Greater Invisibility'}
            dnd_dict.character_dict['spells']['fourth'].update(new_spells)
            dnd_dict.character_dict['class_spells']['artificer']['fourth'].update(new_spells)
            dnd_dict.character_dict['special_spells']['fourth'].update(new_spells)

        if dnd_dict.character_dict['player_class']['artificer']['subclass']  == 'Artillerist':
            new_spells = {'ice_storm':'Ice Storm','wall_of_fire':'Wall of Fire'}
            dnd_dict.character_dict['spells']['fourth'].update(new_spells)
            dnd_dict.character_dict['class_spells']['artificer']['fourth'].update(new_spells)
            dnd_dict.character_dict['special_spells']['fourth'].update(new_spells)

        if dnd_dict.character_dict['player_class']['artificer']['subclass']  == 'Battle Smith':
            new_spells = {'aura_of_purity':'Aura of Purity','fire_shield':'Fire Shield'}
            dnd_dict.character_dict['spells']['fourth'].update(new_spells)
            dnd_dict.character_dict['class_spells']['artificer']['fourth'].update(new_spells)
            dnd_dict.character_dict['special_spells']['fourth'].update(new_spells)





        dnd_magic.artificer_fourth()
        dnd_dict.character_dict['half_caster_level'] +=1
        dnd_skills.spell_slot_selection()
        dnd_dict.character_dict['d8']+=1
        dnd_level_up.level_up(8)

# Level 14
    if dnd_dict.character_dict['player_class']['artificer']['class_level']  == 14:
        dnd_infusions.art_swap(dnd_infusions.artificer_10)
        dnd_infusions.art_infusions14()
        dnd_features.magic_item_savant()
        dnd_dict.character_dict['half_caster_level'] +=1
        dnd_skills.spell_slot_selection()
        dnd_dict.character_dict['d8']+=1
        dnd_level_up.level_up(8)

# Level 15
    if dnd_dict.character_dict['player_class']['artificer']['class_level']  == 15:
        dnd_infusions.art_swap(dnd_infusions.artificer_14)
        if dnd_dict.character_dict['player_class']['artificer']['subclass']  == 'Alchemist':
            dnd_features.alchemist15()

        if dnd_dict.character_dict['player_class']['artificer']['subclass']  == 'Armorer':
            dnd_features.armorer15()

        if dnd_dict.character_dict['player_class']['artificer']['subclass']  == 'Artillerist':
            dnd_features.artillerist15()

        if dnd_dict.character_dict['player_class']['artificer']['subclass']  == 'Battle Smith':
            dnd_features.battle_smith15()


        dnd_dict.character_dict['half_caster_level'] +=1
        dnd_skills.spell_slot_selection()
        dnd_dict.character_dict['d8']+=1
        dnd_level_up.level_up(8)

# Level 16
    if dnd_dict.character_dict['player_class']['artificer']['class_level']  == 16:
        dnd_infusions.art_swap(dnd_infusions.artificer_14)






        dnd_level_up.asi_or_feat()
        dnd_dict.character_dict['half_caster_level'] +=1
        dnd_skills.spell_slot_selection()
        dnd_dict.character_dict['d8']+=1
        dnd_level_up.level_up(8)

# Level 17
    if dnd_dict.character_dict['player_class']['artificer']['class_level']  == 17:
        dnd_infusions.art_swap(dnd_infusions.artificer_14)

        if dnd_dict.character_dict['player_class']['artificer']['subclass']  == 'Alchemist':
            new_spells = {'cloudkill':'Cloudkill','raise_dead':'Raise Dead'}
            dnd_dict.character_dict['spells']['fifth'].update(new_spells)
            dnd_dict.character_dict['class_spells']['artificer']['fifth'].update(new_spells)
            dnd_dict.character_dict['special_spells']['fifth'].update(new_spells)

        if dnd_dict.character_dict['player_class']['artificer']['subclass']  == 'Armorer':
            new_spells = {'passwall':'Passwall','wall_of_force':'Wall of Force'}
            dnd_dict.character_dict['spells']['fifth'].update(new_spells)
            dnd_dict.character_dict['class_spells']['artificer']['fifth'].update(new_spells)
            dnd_dict.character_dict['special_spells']['fifth'].update(new_spells)

        if dnd_dict.character_dict['player_class']['artificer']['subclass']  == 'Artillerist':
            new_spells = {'cone_of_cold':'Cone of Cold','wall_of_force':'Wall of Force'}
            dnd_dict.character_dict['spells']['fifth'].update(new_spells)
            dnd_dict.character_dict['class_spells']['artificer']['fifth'].update(new_spells)
            dnd_dict.character_dict['special_spells']['fifth'].update(new_spells)

        if dnd_dict.character_dict['player_class']['artificer']['subclass']  == 'Battle Smith':
            new_spells = {'banishing_smite':'Banishing Smite','mass_cure_wounds':'Mass Cure Wounds'}
            dnd_dict.character_dict['spells']['fifth'].update(new_spells)
            dnd_dict.character_dict['class_spells']['artificer']['fifth'].update(new_spells)
            dnd_dict.character_dict['special_spells']['fifth'].update(new_spells)


        dnd_magic.artificer_fifth()
        dnd_dict.character_dict['half_caster_level'] +=1
        dnd_skills.spell_slot_selection()
        dnd_dict.character_dict['d8']+=1
        dnd_level_up.level_up(8)

# Level 18
    if dnd_dict.character_dict['player_class']['artificer']['class_level']  == 18:
        dnd_infusions.art_swap(dnd_infusions.artificer_14)

# Select two more cantrips
        x = 1
        for x in range (x,3):
            if x < 3:
                print(f'{x}/2')
                dnd_skills.spell_add(dnd_magic.artificer_cantrip,dnd_dict.character_dict['spells'],dnd_dict.character_dict['class_spells']['artificer'])
                x+=1
                continue
            elif x == 3:
                break


        dnd_features.magic_item_master()
        dnd_dict.character_dict['half_caster_level'] +=1
        dnd_skills.spell_slot_selection()
        dnd_dict.character_dict['d8']+=1
        dnd_level_up.level_up(8)

# Level 19
    if dnd_dict.character_dict['player_class']['artificer']['class_level']  == 19:
        dnd_infusions.art_swap(dnd_infusions.artificer_14)


        dnd_level_up.asi_or_feat()
        dnd_dict.character_dict['half_caster_level'] +=1
        dnd_skills.spell_slot_selection()
        dnd_dict.character_dict['d8']+=1
        dnd_level_up.level_up(8)

# Level 20
    if dnd_dict.character_dict['player_class']['artificer']['class_level']  == 20:
        dnd_infusions.art_swap(dnd_infusions.artificer_14)

        dnd_features.soul_of_artifice()
        dnd_dict.character_dict['half_caster_level'] +=1
        dnd_skills.spell_slot_selection()
        dnd_dict.character_dict['d8']+=1
        dnd_level_up.level_up(8)















