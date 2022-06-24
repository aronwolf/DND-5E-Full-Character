import dnd_dict,dnd_class,dnd_skills

def simple_weapon():
    while True:
        choice = input("""Choose your simple weapon:
1) Club
2) Dagger
3) Great-Club
4) Handaxe
5) Javelin
6) Light Hammer
7) Mace
8) Quarterstaff
9) Sickle
10) Spear
11) Light Crossbow
12) Dart
13) Shortbow
14) Sling
Enter your Selection: """)
        if choice=='1':
            dnd_skills.equip_mod('club1','Club')
            dnd_dict.character_dict['weapons']['club'] = 'Club'
            break
 
        elif choice=='2':
            dnd_skills.equip_mod('dagger1','Dagger')
            dnd_dict.character_dict['weapons']['dagger'] = 'Dagger'
            break

        elif choice=='3':
            dnd_skills.equip_mod('great_club1','Great Club')
            dnd_dict.character_dict['weapons']['great_club'] = 'Great Club'
            break

        elif choice=='4':
            dnd_skills.equip_mod('handaxe1','Handaxe')
            dnd_dict.character_dict['weapons']['handaxe'] = 'Handaxe'
            break

        elif choice=='5':
            dnd_skills.equip_mod('javelin1','Javelin')
            dnd_dict.character_dict['weapons']['javelin'] = 'Javelin'
            break

        elif choice=='6':
            dnd_skills.equip_mod('light_hammer1','Light Hammer')
            dnd_dict.character_dict['weapons']['light_hammer'] = 'Light Hammer'
            break

        elif choice=='7':
            dnd_skills.equip_mod('mace1','Mace')
            dnd_dict.character_dict['weapons']['mace'] = 'Mace'
            break

        elif choice=='8':
            dnd_skills.equip_mod('quarterstaff1','Quarterstaff')
            dnd_dict.character_dict['weapons']['quarterstaff'] = 'Quarterstaff'
            break

        elif choice=='9':
            dnd_skills.equip_mod('sickle1','Sickle')
            dnd_dict.character_dict['weapons']['sickle'] = 'Sickle'
            break

        elif choice=='10':
            dnd_skills.equip_mod('spear1','Spear')
            dnd_dict.character_dict['weapons']['spear'] = 'Spear'
            break

        elif choice=='11':
            dnd_skills.equip_mod('light_crossbow1','Light Crossbow')
            dnd_dict.character_dict['weapons']['light_crossbow'] = 'Light Crossbow'
            break

        elif choice=='12':
            dnd_skills.equip_mod('dart1','Dart')
            dnd_dict.character_dict['weapons']['dart'] = 'Dart'
            break

        elif choice=='13':
            dnd_skills.equip_mod('shortbow1','Shortbow')
            dnd_dict.character_dict['weapons']['shortbow'] = 'Shortbow'
            break

        elif choice=='14':
            dnd_skills.equip_mod('sling1','Sling')
            dnd_dict.character_dict['weapons']['sling'] = 'Sling'
            break

        else:
            print("Invalid Selection")
            continue


def simple_melee():
    while True:
        choice = input("""Choose your simple melee weapon:
1) Club
2) Dagger
3) Great-Club
4) Hand-Axe
5) Javelin
6) Light Hammer
7) Mace
8) Quarterstaff
9) Sickle
10) Spear
Enter your Selection: """)
        if choice=='1':
            dnd_skills.equip_mod('club1','Club')
            dnd_dict.character_dict['weapons']['club'] = 'Club'
            break
 
        elif choice=='2':
            dnd_skills.equip_mod('dagger1','Dagger')
            dnd_dict.character_dict['weapons']['dagger'] = 'Dagger'
            break

        elif choice=='3':
            dnd_skills.equip_mod('great_club1','Great Club')
            dnd_dict.character_dict['weapons']['great_club'] = 'Great Club'
            break

        elif choice=='4':
            dnd_skills.equip_mod('handaxe1','Handaxe')
            dnd_dict.character_dict['weapons']['handaxe'] = 'Handaxe'
            break

        elif choice=='5':
            dnd_skills.equip_mod('javelin1','Javelin')
            dnd_dict.character_dict['weapons']['javelin'] = 'Javelin'
            break

        elif choice=='6':
            dnd_skills.equip_mod('light_hammer1','Light Hammer')
            dnd_dict.character_dict['weapons']['light_hammer'] = 'Light Hammer'
            break

        elif choice=='7':
            dnd_skills.equip_mod('mace1','Mace')
            dnd_dict.character_dict['weapons']['mace'] = 'Mace'
            break

        elif choice=='8':
            dnd_skills.equip_mod('quarterstaff1','Quarterstaff')
            dnd_dict.character_dict['weapons']['quarterstaff'] = 'Quarterstaff'
            break

        elif choice=='9':
            dnd_skills.equip_mod('sickle1','Sickle')
            dnd_dict.character_dict['weapons']['sickle'] = 'Sickle'
            break

        elif choice=='10':
            dnd_skills.equip_mod('spear1','Spear')
            dnd_dict.character_dict['weapons']['spear'] = 'Spear'
            break

        else:
            print("Invalid Selection")
            continue


def double_simple():
    x = 1
    while x < 3:
        if x < 3:
            print(f'{x}/2')
            simple_weapon()
            x+=1
        elif x == 3:
            break

def double_simple_melee():
    x = 1
    while x < 3:
        if x < 3:
            print(f'{x}/2')
            simple_melee()
            x+=1
        elif x == 3:
            break

def martial_weapon():
    while True:
        choice = input("""Enter your martial weapon:
1) Battleaxe
2) Flail
3) Glaive
4) Greataxe
5) Greatsword
6) Halberd
7) Lance
8) Longsword
9) Maul
10) Morningstar
11) Pike
12) Rapier
13) Scimitar
14) Shortsword
15) Trident
16) War Pick
17) Warhammer
18) Whip
19) Blowgun
20) Hand Crossbow
21) Heavy Crossbow
22) Longbow
23) Net
Enter your selection: """)
    
        if choice=='1':
            dnd_skills.equip_mod('battleaxe1','Battleaxe')
            dnd_dict.character_dict['weapons']['battleaxe'] = 'Battleaxe'
            break

        elif choice=='2':
            dnd_skills.equip_mod('flail1','Flail')
            dnd_dict.character_dict['weapons']['flail'] = 'Flail'
            break

        elif choice=='3':
            dnd_skills.equip_mod('glaive1','Glaive')
            dnd_dict.character_dict['weapons']['glaive'] = 'Glaive'
            break

        elif choice=='4':
            dnd_skills.equip_mod('greataxe1','Greataxe')
            dnd_dict.character_dict['weapons']['greataxe'] = 'Greataxe'
            break

        elif choice=='5':
            dnd_skills.equip_mod('greatsword1','Greatsword')
            dnd_dict.character_dict['weapons']['greatsword'] = 'Greatsword'
            break

        elif choice=='6':
            dnd_skills.equip_mod('halberd1','Halberd')
            dnd_dict.character_dict['weapons']['halberd'] = 'Halberd'
            break

        elif choice=='7':
            dnd_skills.equip_mod('lance1','Lance')
            dnd_dict.character_dict['weapons']['lance'] = 'Lance'
            break

        elif choice=='8':
            dnd_skills.equip_mod('longsword1','Longsword')
            dnd_dict.character_dict['weapons']['longsword'] = 'Longsword'
            break

        elif choice=='9':
            dnd_skills.equip_mod('maul1','Maul')
            dnd_dict.character_dict['weapons']['maul'] = 'Maul'
            break

        elif choice=='10':
            dnd_skills.equip_mod('morningstar1','Morningstar')
            dnd_dict.character_dict['weapons']['morningstar'] = 'Morningstar'
            break
    
        elif choice=='11':
            dnd_skills.equip_mod('pike1','Pike')
            dnd_dict.character_dict['weapons']['pike'] = 'Pike'
            break

        elif choice=='12':
            dnd_skills.equip_mod('rapier1','Rapier')
            dnd_dict.character_dict['weapons']['rapier'] = 'Rapier'
            break

        elif choice=='13':
            dnd_skills.equip_mod('scimitar1','Scimitar')
            dnd_dict.character_dict['weapons']['scimitar'] = 'Scimitar'
            break

        elif choice=='14':
            dnd_skills.equip_mod('shortsword1','Shortsword')
            dnd_dict.character_dict['weapons']['shortsword'] = 'Shortsword'
            break

        elif choice=='15':
            dnd_skills.equip_mod('trident1','Trident')
            dnd_dict.character_dict['weapons']['trident'] = 'Trident'
            break

        elif choice=='16':
            dnd_skills.equip_mod('war_pick1','War Pick')
            dnd_dict.character_dict['weapons']['warpick'] = 'Warpick'
            break

        elif choice=='17':
            dnd_skills.equip_mod('warhammer1','Warhammer')
            dnd_dict.character_dict['weapons']['warhammer'] = 'Warhammer'
            break

        elif choice=='18':
            dnd_skills.equip_mod('whip1','Whip')
            dnd_dict.character_dict['weapons']['whip'] = 'Whip'
            break

        elif choice=='19':
            dnd_skills.equip_mod('blowgun1','Blowgun')
            dnd_dict.character_dict['weapons']['blowgun'] = 'Blowgun'
            break

        elif choice=='20':
            dnd_skills.equip_mod('hand_crossbow1','Hand Crossbow')
            dnd_dict.character_dict['weapons']['hand_crossbow'] = 'Hand Crossbow'
            break

        elif choice=='21':
            dnd_skills.equip_mod('heavy_crossbow1','Heavy Crossbow')
            dnd_dict.character_dict['weapons']['heavy_crossbow'] = 'Heavy Crossbow'
            break

        elif choice=='22':
            dnd_skills.equip_mod('longbow1','Longbow')
            dnd_dict.character_dict['weapons']['longbow'] = 'Longbow'
            break

        elif choice=='23':
            dnd_skills.equip_mod('net1','Net')
            dnd_dict.character_dict['weapons']['net'] = 'Net'
            break

        else:
            print("Invalid Selection")
            continue

def double_martial():
    x = 1
    while x < 3:
        if x < 3:
            print(f'{x}/2')
            martial_weapon()
            x+=1
        elif x == 3:
            break

def martial_melee():
    while True:
        choice = input("""Enter your martial weapon:
1) Battleaxe
2) Flail
3) Glaive
4) Greataxe
5) Greatsword
6) Halberd
7) Lance
8) Longsword
9) Maul
10) Morningstar
11) Pike
12) Rapier
13) Scimitar
14) Shortsword
15) Trident
16) War Pick
17) Warhammer
18) Whip
Enter your selection: """)

        if choice=='1':
            dnd_skills.equip_mod('battleaxe1','Battleaxe')
            dnd_dict.character_dict['weapons']['battleaxe'] = 'Battleaxe'
            break

        elif choice=='2':
            dnd_skills.equip_mod('flail1','Flail')
            dnd_dict.character_dict['weapons']['flail'] = 'Flail'
            break

        elif choice=='3':
            dnd_skills.equip_mod('glaive1','Glaive')
            dnd_dict.character_dict['weapons']['glaive'] = 'Glaive'
            break

        elif choice=='4':
            dnd_skills.equip_mod('greataxe1','Greataxe')
            dnd_dict.character_dict['weapons']['greataxe'] = 'Greataxe'
            break

        elif choice=='5':
            dnd_skills.equip_mod('greatsword1','Greatsword')
            dnd_dict.character_dict['weapons']['greatsword'] = 'Greatsword'
            break

        elif choice=='6':
            dnd_skills.equip_mod('halberd1','Halberd')
            dnd_dict.character_dict['weapons']['halberd'] = 'Halberd'
            break

        elif choice=='7':
            dnd_skills.equip_mod('lance1','Lance')
            dnd_dict.character_dict['weapons']['lance'] = 'Lance'
            break

        elif choice=='8':
            dnd_skills.equip_mod('longsword1','Longsword')
            dnd_dict.character_dict['weapons']['longsword'] = 'Longsword'
            break

        elif choice=='9':
            dnd_skills.equip_mod('maul1','Maul')
            dnd_dict.character_dict['weapons']['maul'] = 'Maul'
            break

        elif choice=='10':
            dnd_skills.equip_mod('morningstar1','Morningstar')
            dnd_dict.character_dict['weapons']['morningstar'] = 'Morningstar'
            break
    
        elif choice=='11':
            dnd_skills.equip_mod('pike1','Pike')
            dnd_dict.character_dict['weapons']['pike'] = 'Pike'
            break

        elif choice=='12':
            dnd_skills.equip_mod('rapier1','Rapier')
            dnd_dict.character_dict['weapons']['rapier'] = 'Rapier'
            break

        elif choice=='13':
            dnd_skills.equip_mod('scimitar1','Scimitar')
            dnd_dict.character_dict['weapons']['scimitar'] = 'Scimitar'
            break

        elif choice=='14':
            dnd_skills.equip_mod('shortsword1','Shortsword')
            dnd_dict.character_dict['weapons']['shortsword'] = 'Shortsword'
            break

        elif choice=='15':
            dnd_skills.equip_mod('trident1','Trident')
            dnd_dict.character_dict['weapons']['trident'] = 'Trident'
            break

        elif choice=='16':
            dnd_skills.equip_mod('war_pick1','War Pick')
            dnd_dict.character_dict['weapons']['warpick'] = 'Warpick'
            break

        elif choice=='17':
            dnd_skills.equip_mod('warhammer1','Warhammer')
            dnd_dict.character_dict['weapons']['warhammer'] = 'Warhammer'
            break

        elif choice=='18':
            dnd_skills.equip_mod('whip1','Whip')
            dnd_dict.character_dict['weapons']['whip'] = 'Whip'
            break
        else:
            print("Invalid Selection")
            continue

#Leather Armor
def light_armor(base):
    dnd_dict.character_dict['armor_class'] = ((dnd_dict.character_dict["Stats"]["dexterity"]["mod"]) + base)


