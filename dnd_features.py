import dnd_dict, dnd_skills, dnd_language, dnd_magic,dnd_class,dnd_infusions,dnd_invocations,dnd_tools,dnd_maneuvers,dnd_fighting_styles,dnd_four_elements, dnd_metamagic
# These are all of the features and flavor text for the races, backgrounds,
# and classes that would be too lengthy to put in the main program
# Put the racial bonuses in a different dictionary in case the player changes races throughout the campaign

def dragonborn_features():
    feature = """Draconic Ancestry. You are distantly related to a particular kind of dragon. Choose a type of dragon from the below list; this determines the damage and area of your breath weapon, and the type of resistance you gain.
Dragon Color 	Damage Type 	Breath Weapon
Black 	Acid 	5' by 30' line (DEX save)
Blue 	Lightning 	5' by 30' line (DEX save)
Brass 	Fire 	5' by 30' line (DEX save)
Bronze 	Lightning 	5' by 30' line (DEX save)
Copper 	Acid 	5' by 30' line (DEX save)
Gold 	Fire 	15' cone (DEX save)
Green 	Poison 	15' cone (CON save)
Red 	Fire 	15' cone (DEX save)
Silver 	Cold 	15' cone (CON save)
White 	Cold 	15' cone (CON save)

• Breath Weapon. You can use your action to exhale destructive energy. It deals damage in an area according to your ancestry. When you use your breath weapon, all creatures in the area must make a saving throw, the type of which is determined by your ancestry. The DC of this saving throw is 8 + your Constitution modifier + your proficiency bonus. A creature takes 2d6 damage on a failed save, and half as much damage on a successful one. The damage increase to 3d6 at 6th level, 4d6 at 11th, and 5d6 at 16th level. After using your breath weapon, you cannot use it again until you complete a short or long rest. HBInstead, you may use your breath weapon a number of times equal to your Constitution modifier. You regain expended uses on a short or long rest."""
    dnd_dict.character_dict["racial_features"]['draconic_ancestry'] = feature

def dwarf_hill_features():

    darkvision = "Darkvision. Accustomed to life underground, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray."

    resilience = "Dwarven Resilience. You have advantage on saving throws against poison, and you have resistance against poison damage."

    stonecutting = "Stonecunning. Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check, instead of your normal proficiency bonus."
    toughness = "Dwarven Toughness. Your hit point maximum increases by 1, and it increases by 1 every time you gain a level."
    dwarven_combat_training = "Dwarven Combat Training. You have proficiency with the battleaxe, handaxe, light hammer, and warhammer."

    dnd_dict.character_dict["racial_features"]['darkvision'] = darkvision
    dnd_dict.character_dict["racial_features"]['dwarven_resilience'] = resilience
    dnd_dict.character_dict["racial_features"]['stonecutting'] = stonecutting
    dnd_dict.character_dict["racial_features"]['dwarven_toughness'] = toughness
    dnd_dict.character_dict["racial_features"]['dwarven_combat_training'] = dwarven_combat_training

def dwarf_mountain_features():

    darkvision = "Darkvision. Accustomed to life underground, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray."

    resilience = "Dwarven Resilience. You have advantage on saving throws against poison, and you have resistance against poison damage."

    stonecutting = "Stonecunning. Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check, instead of your normal proficiency bonus."
    dwarven_combat_training = "Dwarven Combat Training. You have proficiency with the battleaxe, handaxe, light hammer, and warhammer."

    dnd_dict.character_dict["racial_features"]['darkvision'] = darkvision
    dnd_dict.character_dict["racial_features"]['dwarven_resilience'] = resilience
    dnd_dict.character_dict["racial_features"]['stonecutting'] = stonecutting
    dnd_dict.character_dict["racial_features"]['dwarven_combat_training'] = dwarven_combat_training

def elf_features():


    darkvision = "Darkvision. Accustomed to life underground, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray."
    fey_ancestry = "Fey Ancestry. You have advantage on saving throws against being charmed, and magic can't put you to sleep."
    trance = 'Trance. Elves do not sleep. Instead they meditate deeply, remaining semi-conscious, for 4 hours a day. The Common word for this meditation is "trance". While meditating, you dream after a fashion; such dreams are actually mental exercises that have become reflexive after years of practice. After resting in this way, you gain the same benefit a human would from 8 hours of sleep.'
    elf_weapon_training = "Elf Weapon Training. You have proficiency with the longsword, shortsword, shortbow, and longbow."
    keen_senses = "Keen Senses. You have proficiency in the Perception skill."

    dnd_dict.character_dict["racial_features"]['darkvision'] = darkvision
    dnd_dict.character_dict["racial_features"]['fey_ancestry'] = fey_ancestry
    dnd_dict.character_dict["racial_features"]['trance'] = trance
    dnd_dict.character_dict["racial_features"]['elf_weapon_training'] = elf_weapon_training
    dnd_dict.character_dict["racial_features"]['keen_senses'] = keen_senses


def gnome_forest_features():

    darkvision = """Darkvision. Accustomed to life underground, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray."""

    gnome_cunning = "Gnome Cunning. You have advantage on all Intelligence, Wisdom, and Charisma saves against magic."

    natural_illusionist = "Natural Illusionist. You know the Minor Illusion cantrip. Intelligence is your spellcasting modifier for it."

    speak_with_small_beasts = "Speak with Small Beasts. Through sound and gestures, you may communicate simple ideas with Small or smaller beasts."

    dnd_dict.character_dict["racial_features"]['darkvision'] = darkvision
    dnd_dict.character_dict["racial_features"]['gnome_cunning'] = gnome_cunning
    dnd_dict.character_dict["racial_features"]['natural_illusionist'] = natural_illusionist
    dnd_dict.character_dict["racial_features"]['speak_with_small_beasts'] = speak_with_small_beasts
    dnd_dict.character_dict['special_spells']['racial_spells']['minor_illusion'] = 'Minor Illusion'
    dnd_dict.character_dict['spells']['cantrips']['minor_illusion'] = 'Minor Illusion'

def gnome_rock_features():

    darkvision = """Darkvision. Accustomed to life underground, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray."""

    gnome_cunning = "Gnome Cunning. You have advantage on all Intelligence, Wisdom, and Charisma saves against magic."

    artificer_lore = "Artificer's Lore. Whenever you make an Intelligence (History) check related to magical, alchemical, or technological items, you can add twice your proficiency bonus instead of any other proficiency bonus that may apply."

    tinker = """Tinker. You have proficiency with artisan tools (tinker's tools). Using those tools, you can spend 1 hour and 10 gp worth of materials to construct a Tiny clockwork device (AC 5, 1 hp). The device ceases to function after 24 hours (unless you spend 1 hour repairing it to keep the device functioning), or when you use your action to dismantle it; at that time, you can reclaim the materials used to create it. You can have up to three such devices active at a time. When you create a device, choose one of the following options:

Clockwork Toy. This toy is a clockwork animal, monster, or person, such as a frog, mouse, bird, dragon, or soldier. When placed on the ground, the toy moves 5 feet across the ground on each of your turns in a random direction. It makes noises as appropriate to the creature it represents.

Fire Starter. The device produces a miniature flame, which you can use to light a candle, torch, or campfire. Using the device requires your action.

Music Box. When opened, this music box plays a single song at a moderate volume. The box stops playing when it reaches the song's end or when it is closed.

At your DM's discretion, you may make other objects with effects similar in power to these. The Prestidigitation cantrip is a good baseline for such effects."""

    dnd_dict.character_dict["racial_features"]['darkvision'] = darkvision
    dnd_dict.character_dict["racial_features"]['gnome_cunning'] = gnome_cunning
    dnd_dict.character_dict["racial_features"]['artificer_lore'] = artificer_lore
    dnd_dict.character_dict["racial_features"]['tinker'] = tinker



def half_elf_features():

    darkvision = """Darkvision. Accustomed to life underground, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray."""
    fey_ancestry = "Fey Ancestry. You have advantage on saving throws against being charmed, and magic can't put you to sleep."

    dnd_dict.character_dict["racial_features"]['darkvision'] = darkvision
    dnd_dict.character_dict["racial_features"]['fey_ancestry'] = fey_ancestry

def halfling_lightfoot_features():

    lucky = "Lucky. When you roll a 1 on an attack roll, ability check, or saving throw, you can reroll the die. You must use the new result, even if it is a 1."

    brave = "Brave. You have advantage on saving throws against being frightened."

    nimble = "Nimble. You can move through the space of any creature that is of a size larger than yours."

    naturally_stealthy = "Naturally Stealthy. You can attempt to hide even when you are only obscured by a creature that is at least one size larger than you."

    dnd_dict.character_dict["racial_features"]['lucky'] = lucky
    dnd_dict.character_dict["racial_features"]['brave'] = brave
    dnd_dict.character_dict["racial_features"]['nimble'] = nimble
    dnd_dict.character_dict["racial_features"]['naturally_stealthy'] = naturally_stealthy


def halfling_stout_features():

    lucky = "Lucky. When you roll a 1 on an attack roll, ability check, or saving throw, you can reroll the die. You must use the new result, even if it is a 1."

    brave = "Brave. You have advantage on saving throws against being frightened."

    nimble = "Nimble. You can move through the space of any creature that is of a size larger than yours."

    stout_resilience = "Stout Resilience. You have advantage on saving throws against poison, and you have resistance to poison damage."

    dnd_dict.character_dict["racial_features"]['lucky'] = lucky
    dnd_dict.character_dict["racial_features"]['brave'] = brave
    dnd_dict.character_dict["racial_features"]['nimble'] = nimble
    dnd_dict.character_dict["racial_features"]['stout_resilience'] = stout_resilience


def half_orc_features():

    darkvision = """Darkvision. Accustomed to life underground, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray."""

    menacing = "Menacing. You gain proficiency in the Intimidation skill."

    relentless_endurance = "Relentless Endurance. When you are reduced to 0 hit points but not killed outright, you can drop to 1 hit point instead. You can't use this feature again until you finish a long rest."

    savage_attacks = "Savage Attacks. When you score a critical hit with a melee weapon attack, you can roll one of the weapon's damage dice one additional time and add it to the extra damage of the critical hit."

    dnd_dict.character_dict["racial_features"]['darkvision'] = darkvision
    dnd_dict.character_dict["racial_features"]['menacing'] = menacing
    dnd_dict.character_dict["racial_features"]['relentless_endurance'] = relentless_endurance
    dnd_dict.character_dict["racial_features"]['savage_attacks'] = savage_attacks


def tiefling_features():


    darkvision = "Darkvision. Accustomed to life underground, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray."

    hellish_resistance = "Hellish Resistance. You have resistance to fire damage."

    infernal_legacy = "Infernal Legacy. You know the Thaumaturgy cantrip. Once you reach 3rd level, you can cast the Hellish Rebuke spell once as a 2nd-level spell. Once you reach 5th level, you can also cast the Darkness spell once. You must finish a long rest to cast these spells again with this trait. Charisma is your spellcasting ability for these spells."

    dnd_dict.character_dict["racial_features"]['darkvision'] = darkvision
    dnd_dict.character_dict["racial_features"]['hellish_resistence'] = hellish_resistance
    dnd_dict.character_dict["racial_features"]['infernal_legacy'] = infernal_legacy
    dnd_dict.character_dict['spells']['cantrips']['thaumaturgy'] = 'Thaumaturgy'
    dnd_dict.character_dict['special_spells']['racial_spells']['thaumaturgy'] = 'Thaumaturgy'


def acolyte_features():
    feature = """Feature: Shelter of the Faithful

As an acolyte, you command the respect of those who share your faith, and you can perform the religious ceremonies of your deity. You and your adventuring companions can expect to receive free healing and care at a temple, shrine, or other established presence of your faith, though you must provide any material components needed for spells. Those who share your religion will support you (but only you) at a modest lifestyle.

You might also have ties to a specific temple dedicated to your chosen deity or pantheon, and you have a residence there. This could be the temple where you used to serve, if you remain on good terms with it, or a temple where you have found a new home. While near your temple, you can call upon the priests for assistance, provided the assistance you ask for is not hazardous and you remain in good standing with your temple."""

    dnd_dict.character_dict["features"]['shelter_of_the_faithful'] = feature

def anthropologist_features():
    feature = """Feature: Cultural Chameleon

Before becoming an adventurer, you spent much of your adult life away from your homeland, living among people different from your kin. You came to understand these foreign cultures and the ways of their people, who eventually treated you as one of their own. One culture had more of an influence on you than any other, shaping your beliefs and customs. Choose a race whose culture you've adopted."""
    feature2 = """Feature: Adept Linguist

You can communicate with humanoids who don't speak any language you know. You must observe the humanoids interacting with one another for at least 1 day, after which you learn a handful of important words, expressions, and gestures – enough to communicate on a rudimentary level."""

    dnd_dict.character_dict["features"]['cultural_chameleon'] = feature
    dnd_dict.character_dict["features"]['adept_linguist'] = feature2

def archeologist_features():

    feature = """Feature: Dust Digger

Prior to becoming an adventurer, you spent most of your young life crawling around in the dust, pilfering relics of questionable value from crypts and ruins. Though you managed to sell a few of your discoveries and earn enough coin to buy proper adventuring gear, you have held onto an item that has great emotional value to you. Roll on the Signature Item table to see what you have, or choose an item from the table.
d8 	Signature Item
1 	10-foot pole
2 	Medallion
3 	Crowbar
4 	Shovel
5 	Hat
6 	Sledgehammer
7 	Hooded lantern
8 	Whip"""
    feature2 = """Feature: Historical Knowledge

When you enter a ruin or dungeon, you can correctly ascertain its original purpose and determine its builders, whether those were dwarves, elves, humans, yuan-ti, or some other known race. In addition, you can determine the monetary value of art objects more than a century old."""

    dnd_dict.character_dict["features"]['dust_digger'] = feature
    dnd_dict.character_dict["features"]['historical_knowledge'] = feature2

def charlatan_features():
    feature = """Feature: Favorite Schemes

Every charlatan has an angle they use in preference to other schemes. Choose a favorite scam or roll on the table below.
d6 	Scam
1 	I cheat at games of chance.
2 	I shave coins or forge documents.
3 	I insinuate myself into people's lives to prey on their weakness and secure their fortunes.
4 	I put on new identities like clothes.
5 	I run sleight-of-hand cons on street corners.
6 	I convince people that worthless junk is worth their hard-earned money."""
    feature2 = """Feature: False Identity

You have created a second identity that includes documentation, established acquaintances, and disguises that allow you to assume that persona. Additionally, you can forge documents including official papers and personal letters, as long as you have seen an example of the kind of document or the handwriting you are trying to copy."""

    dnd_dict.character_dict["features"]['favorite_schemes'] = feature
    dnd_dict.character_dict["features"]['false_identity'] = feature2

def city_watch_features():
    feature = """Feature: Watcher's Eye

Your experience in enforcing the law, and dealing with lawbreakers, gives you a feel for local laws and criminals. You can easily find the local outpost of the watch or a similar organization, and just as easily pick out the dens of criminal activity in a community, although you're more likely to be welcome in the former locations rather than the latter."""

    dnd_dict.character_dict["features"]['watchers_eye'] = feature

def cloistered_scholar_features():
    feature = """Feature: Library Access

Though others must often endure extensive interviews and significant fees to gain access to even the most common archives in your library, you have free and easy access to the majority of the library, though it might also have repositories of lore that are too valuable, magical, or secret to permit anyone immediate access.

You have a working knowledge of your cloister's personnel and bureaucracy, and you know how to navigate those connections with some ease.

Additionally, you are likely to gain preferential treatment at other libraries across the Realms, as professional courtesy shown to a fellow scholar."""

    dnd_dict.character_dict["features"]['library_access'] = feature

def criminal_features():
    feature = """Feature: Criminal Specialty

There are many kinds of criminals, and within a thieves' guild or similar criminal organization, individual members have particular specialties. Even criminals who operate outside of such organizations have strong preferences for certain kinds of crimes over others. Choose the role you played in your criminal life, or roll on the table below.
d8 	Specialty
1 	Blackmailer
2 	Burglar
3 	Enforcer
4 	Fence
5 	Highway robber
6 	Hired killer
7 	Pickpocket
8 	Smuggler"""
    feature2 = """Feature: Criminal Contact

You have a reliable and trustworthy contact who acts as your liaison to a network of other criminals. You know how to get messages to and from your contact, even over great distances; specifically, you know the local messengers, corrupt caravan masters, and seedy sailors who can deliver messages for you."""

    dnd_dict.character_dict["features"]['criminal_specialty'] = feature
    dnd_dict.character_dict["features"]['criminal_contact'] = feature2

def entertainer_features():

    feature = """Feature: Entertainer Routines

A good entertainer is versatile, spicing up every performance with a variety of different routines. Choose one to three routines or roll on the table below to define your expertise as an entertainer.
d10 	Entertainer Routine
1 	Actor
2 	Dancer
3 	Fire-eater
4 	Jester
5 	Juggler
6 	Instrumentalist
7 	Poet
8 	Singer
9 	Storyteller
10 	Tumbler"""
    feature2 = """Feature: By Popular Demand

You can always find a place to perform, usually in an inn or tavern but possibly with a circus, at a theater, or even in a noble's court. At such a place, you receive free lodging and food of a modest or comfortable standard (depending on the quality of the establishment), as long as you perform each night. In addition, your performance makes you something of a local figure. When strangers recognize you in a town where you have performed, they typically take a liking to you."""

    dnd_dict.character_dict["features"]['entertainer_routines'] = feature
    dnd_dict.character_dict["features"]['by_popular_demand'] = feature2

def far_traveler_features():
    feature = """Feature: Why Are You Here?

A far traveler might have set out on a journey for one of a number of reasons, and the departure from his or her homeland could have been voluntary or involuntary. To determine why you are so far from home, roll on the table below or choose from the options provided. The following section, discussing possible homelands, includes some suggested reasons that are appropriate for each location.
d6 	Reason
1 	Emissary
2 	Exile
3 	Fugitive
4 	Pilgrim
5 	Sightseer
6 	Wanderer"""
    feature2 = """Feature: Where Are You From?

NOTE: You do not have to use this if you are making your own world. If you are,
feel free to create your own setting.

The most important decision in creating a far traveler background is determining your homeland. The places discussed here are all sufficiently distant from the North and the Sword Coast to justify the use of this background.

Evermeet. The fabled elven islands far to the west are home to elves who have never been to Faerun. They often find it a harsher place than they expected when they do make the trip. If you are an elf, Evermeet is a logical (though not mandatory) choice for your homeland.

Most of those who emigrate from Evermeet are either exiles, forced out for committing some infraction of elven law, or emissaries who come to Faerun for a purpose that benefits elven culture or society.

Halruaa. Located on the southern edges of the Shining South, and hemmed in by mountains all around, the magocracy of Halruaa is a bizarre land to most in Faerun who know about it. Many folk have heard of the strange skyships the Halruaans sail, and a few know of the tales that even the least of their people can work magic.

Halruaans usually make their journeys into Faerun for personal reasons, since their government has a strict stance against unauthorized involvement with other nations and organizations. You might have been exiled for breaking one of Halruaa's many byzantine laws, or you could be a pilgrim who seeks the shrines of the gods of magic.

Kara-Tur. The continent of Kara-Tur, far to the east of Faerûn, is home to people whose customs are unfamiliar to the folk of the Sword Coast. If you come from Kara-Tur, the people of Faerûn likely refer to you as Shou, even if that isn't your true ethnicity, because that's the blanket term they use for everyone who shares your origin.

The folk of Kara-Tur occasionally travel to Faerûn as diplomats or to forge trade relations with prosperous merchant cartels. You might have come here as part of some such delegation, then decided to stay when the mission was over.

Mulhorand. From the terrain to the architecture to the god-kings who rule over these lands, nearly everything about Mulhorand is a lien to someone from the Sword Coast. You likely experienced the same sort of culture shock when you left your desert home and traveled to the unfamiliar climes of northern Faerûn. Recent events in your homeland have led to the abolition of slavery, and a corresponding increase in the traffic between Mulhorand and the distant parts of Faerûn.

Those who leave behind Mulhorand's sweltering deserts and ancient pyramids for a glimpse at a different life do so for many reasons. You might be in the North simply to see the strangeness this wet land has to offer, or because you have made too many enemies among the desert communities of your home.

Sossal. Few have heard of your homeland, but many have questions about it upon seeing you. Humans from Sossal seem crafted from snow, with alabaster skin and white hair, and typically dressed in white.

Sossal exists far to the northeast, hard up against the endless ice to the north and bounded on its other sides by hundreds of miles of the Great Glacier and the Great Ice Sea. No one from your nation makes the effort to cross such colossal barriers without a convincing reason. You must fear something truly terrible or seek something incredibly important.

Zakhara. As the saying goes among those in Faerûn who know of the place, "To get to Zakhara, go south. Then go south some more." Of course, you followed an equally long route when you came north from your place of birth. Though it isn't unusual for Zakharans to visit the southern extremes of Faerûn for trading purposes, few of them stray as far from home as you have.

You might be traveling to discover what wonders are to be found outside the deserts and sword-like mountains of your homeland, or perhaps you are on a pilgrimage to understand the gods that others worship, so that you might better appreciate your own deities.

The Underdark. Though your home is physically closer to the Sword Coast than the other locations discussed here, it is far more unnatural. You hail from one of the settlements in the Underdark, each of which has its own strange customs and laws. If you are a native of one of the great subterranean cities or settlements, you are probably a member of the race that occupies the place but you might also have grown up there after being captured and brought below when you were a child.

If you are a true Underdark native, you might have come to the surface as an emissary of your people, or perhaps to escape accusations of criminal behavior (whether warranted or not). If you aren't a native, your reason for leaving "home" probably has something to do with getting away from a bad situation.
Feature: All Eyes on You

Your accent, mannerisms, figures of speech, and perhaps even your appearance all mark you as foreign. Curious glances are directed your way wherever you go, which can be a nuisance, but you also gain the friendly interest of scholars and others intrigued by far-off lands, to say nothing of everyday folk who are eager to hear stories of your homeland.

You can parley this attention into access to people and places you might not otherwise have, for you and your traveling companions. Noble lords, scholars, and merchant princes, to name a few, might be interested in hearing about your distant homeland and people."""

    dnd_dict.character_dict["features"]['why_are_you_here'] = feature
    dnd_dict.character_dict["features"]['where_are_you_from'] = feature2

def folk_hero_features():
    feature = """Feature: Defining Event

You previously pursued a simple profession among the peasantry, perhaps as a farmer, miner, servant, shepherd, woodcutter, or gravedigger. But something happened that set you on a different path and marked you for greater things. Choose or randomly determine a defining event that marked you as a hero of the people.
d10 	Defining Event
1 	I stood up to a tyrant's agents.
2 	I saved people during a natural disaster.
3 	I stood alone against a terrible monster.
4 	I stole from a corrupt merchant to help the poor.
5 	I led a militia to fight off an invading army.
6 	I broke into a tyrant's castle and stole weapons to arm the people.
7 	I trained the peasantry to use farm implements as weapons against a tyrant's soldiers.
8 	A lord rescinded an unpopular decree after I led a symbolic act of protect against it.
9 	A celestial, fey, or similar creature gave me a blessing or revealed my secret origin.
10 	Recruited into a lord's army, I rose to leadership and was commended for my heroism."""
    feature2 = """Feature: Rustic Hospitality

Since you come from the ranks of the common folk, you fit in among them with ease. You can find a place to hide, rest, or recuperate among other commoners, unless you have shown yourself to be a danger to them. They will shield you from the law or anyone else searching for you, though they will not risk their lives for you. """

    dnd_dict.character_dict["features"]['defining_event'] = feature
    dnd_dict.character_dict["features"]['rustic_hospitality'] = feature2

def gladiator_features():
    feature = """Feature: Entertainer Routines

A good entertainer is versatile, spicing up every performance with a variety of different routines. Choose one to three routines or roll on the table below to define your expertise as an entertainer.
d10 	Entertainer Routine
1 	Actor
2 	Dancer
3 	Fire-eater
4 	Jester
5 	Juggler
6 	Instrumentalist
7 	Poet
8 	Singer
9 	Storyteller
10 	Tumbler"""
    feature2 = """Feature: By Popular Demand

You can always find a place to perform, usually in an inn or tavern but possibly with a circus, at a theater, or even in a noble's court. At such a place, you receive free lodging and food of a modest or comfortable standard (depending on the quality of the establishment), as long as you perform each night. In addition, your performance makes you something of a local figure. When strangers recognize you in a town where you have performed, they typically take a liking to you.
A gladiator is as much an entertainer as any minstrel or circus performer trained to make the arts of combat into a spectacle the crowd can enjoy. This kind of flashy combat is your entertainer routine, though you might also have some skills as a tumbler or actor. Using your By Popular Demand feature, you can find a place to perform in any place that features combat for entertainment-perhaps a gladiatorial arena or secret pit fighting club. You can replace the musical instrument in your equipment package with an inexpensive but unusual weapon, such as a trident or net."""

    dnd_dict.character_dict["features"]['entertainer_routines'] = feature
    dnd_dict.character_dict["features"]['by_popular_demand'] = feature2

def guild_artisan_features():
    feature = """Feature: Guild Business

Guilds are generally found in cities large enough to support several artisans practicing the same trade. However, your guild might instead be a loose network of artisans who each work in a different village within a larger realm. Work with your DM to determine the nature of your guild. You can select your guild business from the Guild Business table or roll randomly.
d8 	Guild Business
1 	Alchemists and apothecaries
2 	Armorers, locksmiths, and finesmiths
3 	Brewers, distillers, and vintners
4 	Calligraphers, scribes, and scriveners
5 	Carpenters, roofers, and plasterers
6 	Cartographers, surveyors, and chart-makers
7 	Cobblers and shoemakers
8 	Cooks and bakers
9 	Glassblowers and glaziers
10 	Jewelers and gemcutters
11 	Leatherworkers, skinners, and tanners
12 	Masons and stonecutters
13 	Painters, limners, and sign-makers
14 	Potters and tile-makers
15 	Shipwrights and sailmakers
16 	Smiths and metal-forgers
17 	Tinkers, pewterers, and casters
18 	Wagon-makers and wheelwrights
19 	Weavers and dyers
20 	Woodcarvers, coopers, and bowyers

As a member of your guild, you know the skills needed to create finished items from raw materials (reflected in your proficiency with a certain kind of artisan's tools), as well as the principles of trade and good business practices. The question now is whether you abandon your trade for adventure, or take on the extra effort to weave adventuring and trade together."""
    feature2 = """Feature: Guild Membership

As an established and respected member of a guild, you can rely on certain benefits that membership provides. Your fellow guild members will provide you with lodging and food if necessary, and pay for your funeral if needed. In some cities and towns, a guildhall offers a central place to meet other members of your profession, which can be a good place to meet potential patrons, allies, or hirelings.

Guilds often wield tremendous political power. If you are accused of a crime, your guild will support you if a good case can be made for your innocence or the crime is justifiable. You can also gain access to powerful political figures through the guild, if you are a member in good standing. Such connections might require the donation of money or magic items to the guild's coffers.

You must pay dues of 5 gp per month to the guild. If you miss payments, you must make up back dues to remain in the guild's good graces."""

    dnd_dict.character_dict["features"]['guild_business'] = feature
    dnd_dict.character_dict["features"]['guild_membership'] = feature2


def haunted_one_features():
    feature = """Feature: Harrowing Event

Prior to becoming an adventurer, your path in life was defined by one dark moment, one fateful decision, or one tragedy. Now you feel a darkness threatening to consume you, and you fear there may be no hope of escape. Choose a harrowing event that haunts you, or roll one on the Harrowing Events table.
d10 	Harrowing Event
1 	A monster that slaughtered dozens of innocent people spared your life, and you don’t know why.
2 	You were born under a dark star. You can feel it watching you, coldly and distantly. Sometimes it beckons you in the dead of night.
3 	An apparition that has haunted your family for generations now haunts you. You don’t know what it wants, and it won’t leave you alone.
4 	Your family has a history of practicing the dark arts. You dabbled once and felt something horrible clutch at your soul, whereupon you fled in terror.
5 	An oni took your sibling one cold, dark night, and you were unable to stop it.
6 	You were cursed with lycanthropy and later cured. You are now haunted by the innocents you slaughtered.
7 	A hag kidnapped and raised you. You escaped, but the hag still has a magical hold over you and fills your mind with evil thoughts.
8 	You opened an eldritch tome and saw things unfit for a sane mind. You burned the book, but its words and images are burned into your psyche.
9 	A fiend possessed you as a child. You were locked away but escaped. The fiend is still inside you, but now you try to keep it locked away.
10 	You did terrible things to avenge the murder of someone you loved. You became a monster, and it haunts your waking dreams."""
    feature2 = """Feature: Heart of Darkness

Those who look into your eyes can see that you have faced unimaginable horror and that you are no stranger to darkness. Though they might fear you, commoners will extend you every courtesy and do their utmost to help you. Unless you have shown yourself to be a danger to them, they will even take up arms to fight alongside you, should you find yourself facing an enemy alone."""

    dnd_dict.character_dict["features"]['harrowing_event'] = feature
    dnd_dict.character_dict["features"]['heart_of_darkness'] = feature2

def hermit_features():
    feature = """Feature: Life of Seclusion

What was the reason for your isolation, and what changed to allow you to end your solitude? You can work with your DM to determine the exact nature of your seclusion, or you can choose to roll on the table below to determine the reason behind your seclusion.
d8 	Life of Seclusion
1 	I was searching for spiritual enlightenment.
2 	I was partaking of communal living in accordance with the dictates of a religious order.
3 	I was exiled for a crime I didn't commit.
4 	I retreated from society after a life-altering event.
5 	I needed a quiet place to work on my art, literature, music, or manifesto.
6 	I needed to commune with nature, far from civilization.
7 	I was the caretaker of an ancient ruin or relic.
8 	I was a pilgrim in search of a person, place, or relic of spiritual significance."""
    feature2 = """Feature: Discovery

The quiet seclusion of your extended hermitage gave you access to a unique and powerful discovery. The exact nature of this revelation depends on the nature of your seclusion. It might be a great truth about the cosmos, the deities, the powerful beings of the outer planes, or the forces of nature. It could be a site that no one else has ever seen. You might have uncovered a fact that has long been forgotten, or unearthed some relic of the past that could rewrite history. It might be information that would be damaging to the people who or consigned you to exile, and hence the reason for your return to society.

Work with your DM to determine the details of your discovery and its impact on the campaign."""

    dnd_dict.character_dict["features"]['life_of_seclusion'] = feature
    dnd_dict.character_dict["features"]['discovery'] = feature2

def inquisitor_features():
    feature = """Feature: Legal Authority

As an inquisitor of the church, you have the authority to arrest criminals. In the absence of other authorities, you are authorized to pass judgment and even carry out sentencing. If you abuse this power, however, your superiors in the church might strip it from you."""

    dnd_dict.character_dict["features"]['legal_authority'] = feature

def investigator_features():
    feature = """Feature: Watcher's Eye

Your experience in enforcing the law, and dealing with lawbreakers, gives you a feel for local laws and criminals. You can easily find the local outpost of the watch or a similar organization, and just as easily pick out the dens of criminal activity in a community, although you're more likely to be welcome in the former locations rather than the latter."""


    dnd_dict.character_dict["features"]['watchers_eye'] = feature

def knight_features():
    feature = """Feature: Position of Privilege

Thanks to your noble birth, people are inclined to think the best of you. You are welcome in high society, and people assume you have the right to be wherever you are. The common folk make every effort to accommodate you and avoid your displeasure, and other people of high birth treat you as a member of the same social sphere. You can secure an audience with a local noble if you need to."""
    feature2 = """Variant Feature: Retainers

If your character has a noble background, you may select this background feature instead of Position of Privilege.

You have the service of three retainers loyal to your family. These retainers can be attendants or messengers, and one might be a majordomo. Your retainers are commoners who can perform mundane tasks for you, but they do not fight for you, will not follow you into obviously dangerous areas (such as dungeons), and will leave if they are frequently endangered or abused."""


    dnd_dict.character_dict["features"]['position_of_privilege'] = feature
    dnd_dict.character_dict["features"]['retainers'] = feature2

def marine_features():
    feature = """Feature: Hardship Endured

Hardship in your past has forged you into an unstoppable living weapon. This hardship is essential to you and is at the heart of a personal philosophy or ethos that often guides your actions. You can roll on the following table to determine this hardship or choose one that best fits your character.
d6 	Hardship
1 	You hid underwater to avoid detection by enemies and held your breath for an extremely long time. Just before you would have died, you had a revelation about your existence.
2 	You spent months enduring thirst, starvation, and torture at the hands of your enemy, but you never broke.
3 	You enabled the escape of your fellow soldiers, but at great cost to yourself. Some of your past comrades may think you're dead.
4 	No reasonable explanation can explain how you survived a particular battle. Every arrow and bolt missed you. You slew scores of enemies single-handedly and led your comrades to victory.
5 	For days, you hid in the bilge of an enemy ship, surviving on brackish water and foolhardy rats. At the right moment, you crept up to the deck and took over the ship on your own.
6 	You carried an injured marine for miles to avoid capture and death."""
    feature2 = """Feature: Steady

You can move twice the normal amount of time (up to 16 hours) each day before being subject to the effect of a forced march (see "Travel Pace" in chapter 8 of the Player's Handbook). Additionally, you can automatically find a safe route to land a boat on shore, provided such a route exists."""

    dnd_dict.character_dict["features"]['hardship_endured'] = feature
    dnd_dict.character_dict["features"]['steady'] = feature2

def mercenary_features():
    feature = """NOTE: if you are making your own setting, you do not have to use these location names.
Feature: Mercenaries of the North

Countless mercenary companies operate up and down the Sword Coast and throughout the North. Most are small-scale operations that employ a dozen to a hundred folk who offer security services, hunt monsters and brigands, or go to war in exchange for gold. Some organizations, such as the Zhentarim, Flaming Fist, and the nation of Mintarn have hundreds or thousands of members and can provide private armies to those with enough funds. A few organizations operating in the North are described below.

The Chill. The cold and mysterious Lurkwood serves as the home of numerous groups of goblinoids that have banded together into one tribe called the Chill. Unlike most of their kind, the Chill refrain s from raiding the people of the North and maintains relatively good relations so that they can hire them selves out as warriors. Few city-states in the North are willing to field an army alongside the Chill, but several are happy to quietly pay the Chill to battle the Uthgardt, ores, trolls of the Evermoors, and other threats to civilization.

Silent Rain. Consisting solely of elves, Silent Rain is a legendary mercenary company operating out of Evereska. Caring little for gold or fame, Silent Rain agrees only to jobs that either promote elven causes or involve destroying ores, gnolls, and the like. Prospective employers must leave written word (in Elvish) near Evereska, and the Silent Rain sends a representative if interested.

The Bloodaxes. Founded in Sundabar nearly two centuries ago, the Bloodaxes were originally a group of dwarves outcast from their clans for crimes against the teachings of Moradin Soulforger. They began hiring out as mercenaries to whoever in the North would pay them. Since then the mercenary company has broadened its membership to other races , but every member is an exile, criminal, or misfit of some sort looking for a fresh start and a new family among the bold Bloodaxes."""
    feature2 = """Feature: Mercenary Life

You know the mercenary life as only someone who has experienced it can. You are able to identify mercenary companies by their emblems, and you know a little about any such company, including the names and reputations of its commanders and leaders, and who has hired them recently. You can find the taverns and festhalls where mercenaries abide in any area, as long as you speak the language. You can find mercenary work between adventures sufficient to maintain a comfortable lifestyle."""

    dnd_dict.character_dict["features"]['mercenaries_of_the_north'] = feature
    dnd_dict.character_dict["features"]['mercenary_life'] = feature2

def noble_features():
    feature = """Feature: Position of Privilege

Thanks to your noble birth, people are inclined to think the best of you. You are welcome in high society, and people assume you have the right to be wherever you are. The common folk make every effort to accommodate you and avoid your displeasure, and other people of high birth treat you as a member of the same social sphere. You can secure an audience with a local noble if you need to."""
    feature2 = """Variant Feature: Retainers

If your character has a noble background, you may select this background feature instead of Position of Privilege.

You have the service of three retainers loyal to your family. These retainers can be attendants or messengers, and one might be a majordomo. Your retainers are commoners who can perform mundane tasks for you, but they do not fight for you, will not follow you into obviously dangerous areas (such as dungeons), and will leave if they are frequently endangered or abused."""

    dnd_dict.character_dict["features"]['position_of_privilege'] = feature
    dnd_dict.character_dict["features"]['retainers'] = feature2

def outlander_features():
    feature = """Feature: Origin

You've been to strange places and seen things that others cannot begin to fathom. Consider some of the distant lands you have visited, and how they impacted you. You can roll on the following table to determine your occupation during your time in the wild, or choose one that best fits your character.
d10 	Origin
1 	Forester
2 	Trapper
3 	Homesteader
4 	Guide
5 	Exile or outcast
6 	Bounty hunter
7 	Pilgrim
8 	Tribal nomad
9 	Hunter-gatherer
10 	Tribal marauder"""
    feature2 = """Feature: Wanderer

You have an excellent memory for maps and geography, and you can always recall the general layout of terrain, settlements, and other features around you. In addition, you can find food and fresh water for yourself and up to five other people each day, provided that the land offers berries, small game, water, and so forth."""

    dnd_dict.character_dict["features"]['origin'] = feature
    dnd_dict.character_dict["features"]['wanderer'] = feature2

def pirate_features():
    feature = """Feature: Ship's Passage

When you need to, you can secure free passage on a sailing ship for yourself and your adventuring companions. You might sail on the ship you served on, or another ship you have good relations with (perhaps one captained by a former crewmate). Because you're calling in a favor, you can't be certain of a schedule or route that will meet your every need. Your DM will determine how long it takes to get where you need to go. In return for your free passage, you and your companions are expected to assist the crew during the voyage.
Variant Sailor: Pirate

You spent your youth under the sway of a dread pirate, a ruthless cutthroat who taught you how to survive in a world of sharks and savages. You've indulged in larceny on the high seas and sent more than one deserving soul to a briny grave. Fear and bloodshed are no strangers to you, and you've garnered a somewhat unsavory reputation in many a port town.

If you decide that your sailing career involved piracy, you can choose the Bad Reputation feature below instead of the Ship's Passage feature."""
    feature2 = """Variant Feature: Bad Reputation

If your character has a sailor background, you may select this background feature instead of Ship's Passage.

No matter where you go, people are afraid of you due to your reputation. When you are in a civilized settlement, you can get away with minor criminal offenses, such as refusing to pay for food at a tavern or breaking down doors at a local shop, since most people will not report your activity to the authorities."""

    dnd_dict.character_dict["features"]['ships_passage'] = feature
    dnd_dict.character_dict["features"]['bad_reputation'] = feature2

def sage_features():
    feature = """Feature: Specialty

To determine the nature of your scholarly training, roll a d8 or choose from the options in the table below.
d8 	Specialty
1 	Alchemist
2 	Astronomer
3 	Discredited academic
4 	Librarian
5 	Professor
6 	Researcher
7 	Wizard's apprentice
8 	Scribe"""
    feature2 = """Feature: Researcher

When you attempt to learn or recall a piece of lore, if you do not know that information, you often know where and from whom you can obtain it. Usually, this information comes from a library, scriptorium, university, or a sage or other learned person or creature. Your DM might rule that the knowledge you seek is secreted away in an almost inaccessible place, or that it simply cannot be found. Unearthing the deepest secrets of the multiverse can require an adventure or even a whole campaign."""

    dnd_dict.character_dict["features"]['sage_specialty'] = feature
    dnd_dict.character_dict["features"]['researcher'] = feature2

def sailor_features():
    feature = """Feature: Ship's Passage

When you need to, you can secure free passage on a sailing ship for yourself and your adventuring companions. You might sail on the ship you served on, or another ship you have good relations with (perhaps one captained by a former crewmate). Because you're calling in a favor, you can't be certain of a schedule or route that will meet your every need. Your DM will determine how long it takes to get where you need to go. In return for your free passage, you and your companions are expected to assist the crew during the voyage."""

    dnd_dict.character_dict["features"]['ships_passage'] = feature

def soldier_features():
    feature = """Feature: Specialty

During your time as a soldier, you had a specific role to play in your unit or army. Roll a d8 or choose from the options in the table below to determine your role:
d8 	Specialty
1 	Officer
2 	Scout
3 	Infantry
4 	Cavalry
5 	Healer
6 	Quartermaster
7 	Standard bearer
8 	Support staff (cook, blacksmith, or the like)"""
    feature2 = """Feature: Military Rank

You have a military rank from your career as a soldier. Soldiers loyal to your former military organization still recognize your authority and influence, and they defer to you if they are of a lower rank. You can invoke your rank to exert influence over other soldiers and requisition simple equipment or horses for temporary use. You can also usually gain access to friendly military encampments and fortresses where your rank is recognized."""

    dnd_dict.character_dict["features"]['soldier_specialty'] = feature
    dnd_dict.character_dict["features"]['military_rank'] = feature2

def spy_features():
    feature = """Feature: Criminal Specialty

There are many kinds of criminals, and within a thieves' guild or similar criminal organization, individual members have particular specialties. Even criminals who operate outside of such organizations have strong preferences for certain kinds of crimes over others. Choose the role you played in your criminal life, or roll on the table below.
d8 	Specialty
1 	Blackmailer
2 	Burglar
3 	Enforcer
4 	Fence
5 	Highway robber
6 	Hired killer
7 	Pickpocket
8 	Smuggler"""
    feature2 = """Feature: Criminal Contact

You have a reliable and trustworthy contact who acts as your liaison to a network of other criminals. You know how to get messages to and from your contact, even over great distances; specifically, you know the local messengers, corrupt caravan masters, and seedy sailors who can deliver messages for you."""
    feature3 = """Variant Criminal: Spy

Although your capabilities are not much different from those of a burglar or smuggler, you learned and practiced them in a very different context: as an espionage agent. You might have been an officially sanctioned agent of the crown, or perhaps you sold the secrets you uncovered to the highest bidder."""

    dnd_dict.character_dict["features"]['criminal_specialty'] = feature
    dnd_dict.character_dict["features"]['criminal_contact'] = feature2
    dnd_dict.character_dict["features"]['spy'] = feature3


def urban_bounty_hunter_features():
    feature = """Feature: Ear to the Ground

You are in frequent contact with people in the segment of society that your chosen quarries move through. These people might be associated with the criminal underworld, the rough-and-tumble folk of the streets, or members of high society. This connection comes in the form of a contact in any city you visit, a person who provides information about the people and places of the local area."""

    dnd_dict.character_dict["features"]['ear_to_the_ground'] = feature

def urchin_features():

    feature = """Feature: City Secrets

You know the secret patterns and flow to cities and can find passages through the urban sprawl that others would miss. When you are not in combat, you (and companions you lead) can travel between any two locations in the city twice as fast as your speed would normally allow."""

    dnd_dict.character_dict["features"]['city_secrets'] = feature


#Player classes
def artificer_features():
    feature = """
Optional Rule: Firearm Proficiency

If your Dungeon Master uses the rules on firearms in chapter 9 of the Dungeon Master's Guide and your artificer has been exposed to the operations of such weapons, your artificer is proficient with them."""
    feature2 = """
Magical Tinkering

At 1st level, you learn how to invest a spark of magic in objects that would otherwise be mundane. To use this ability, you must tinker’s tools, or other artisan’s tools in hand. You then touch a Tiny nonmagical object as an action and give it one of the following magical properties of your choice:

    The object sheds bright light in a 5-foot radius and dim light for an additional 5 feet.
    Whenever tapped by a creature, the object emits a recorded message that can be heard up to 10 feet away. You utter the message when you bestow this property on the object, and the recording can be no more than 6 seconds long.
    The object continuously emits your choice of an odor or a nonverbal sound (wind, waves, chirping, or the like). The chosen phenomenon is perceivable up to 10 feet away.
    A static visual effect appears on one of the object’s surfaces. This effect can be a picture, up to 25 words of text, lines and shapes, or a mixture of these elements, as you like.

The chosen property lasts indefinitely. As an action, you can touch the object and end the property early.

You can give the magic of this feature to multiple objects, touching one object each time you use the feature, and a single object can bear only one of the properties at a time. The maximum number of objects you can affect with the feature at one time is equal to your Intelligence modifier (minimum of one object). If you try to exceed your maximum, the oldest property immediately ends, and then the new property applies.
"""

    dnd_dict.character_dict["features"]['firearm_proficiency'] = feature
    dnd_dict.character_dict["features"]['magical_tinkering'] = feature2


def barbarian_features():
    feature = """
Rage

In battle, you fight with primal ferocity. On your turn, you can enter a rage as a bonus action.

While raging, you gain the following benefits if you aren't wearing heavy armor:

    You have advantage on Strength checks and Strength saving throws.
    When you make a melee weapon attack using Strength, you gain a bonus to the damage roll that increases as you gain levels as a barbarian, as shown in the Rage Damage column of the Barbarian table.
    You have resistance to bludgeoning, piercing, and slashing damage.

If you are able to cast spells, you can't cast them or concentrate on them while raging.

Your rage lasts for 1 minute. It ends early if you are knocked unconscious or if your turn ends and you haven't attacked a hostile creature since your last turn or taken damage since then. You can also end your rage on your turn as a bonus action.

Once you have raged the number of times shown for your barbarian level in the Rages column of the Barbarian table, you must finish a long rest before you can rage again."""

    feature2 = """Unarmored Defense

While you are not wearing any armor, your armor class equals 10 + your Dexterity modifier + your Constitution modifier. You can use a shield and still gain this benefit."""

    dnd_dict.character_dict["features"]['rage'] = feature
    dnd_dict.character_dict["features"]['unarmored_defense_barbarian'] = feature2


def druid_features():
    feature = """Druidic

You know Druidic, the secret language of druids. You can speak the language and use it to leave hidden messages. You and others who know this language automatically spot such a message. Others spot the message's presence with a successful DC 15 Wisdom (Perception) check but can't decipher it without magic."""

    dnd_dict.character_dict["features"]['druidic'] = feature



def monk_features():
    feature = """
Unarmored Defense

Beginning at 1st level, while you are wearing no armor and not wielding a shield, your AC equals 10 + your Dexterity modifier + your Wisdom modifier."""
    feature2 = """Martial Arts

At 1st level, your practice of martial arts gives you mastery of combat styles that use unarmed strikes and monk weapons, which are shortswords and any simple melee weapons that don't have the two-handed or heavy property.

You gain the following benefits while you are unarmed or wielding only monk weapons and you aren't wearing armor or wielding a shield:

    You can use Dexterity instead of Strength for the attack and damage rolls of your unarmed strikes and monk weapons.

    You can roll a d4 in place of the normal damage of your unarmed strike or monk weapon. This die changes as you gain monk levels, as shown in the Martial Arts column of the Monk table.

    When you use the Attack action with an unarmed strike or a monk weapon on your turn, you can make one unarmed strike as a bonus action. For example, if you take the Attack action and attack with a quarterstaff, you can also make an unarmed strike as a bonus action, assuming you haven't already taken a bonus action this turn.

Certain monasteries use specialized forms of the monk weapons. For example, you might use a club that is two lengths of wood connected by a short chain (called a nunchaku) or a sickle with a shorter, straighter blade (called a kama). Whatever name you use for a monk weapon, you can use the game statistics provided for the weapon on the Weapons page.
"""
    dnd_dict.character_dict["features"]['unarmored_defense_monk'] = feature
    dnd_dict.character_dict["features"]['martial_arts'] = feature2
    dnd_dict.character_dict['martial_arts'] = '1d4'

def paladin_features():
    feature = """Divine Sense

The presence of strong evil registers on your senses like a noxious odor, and powerful good rings like heavenly music in your ears. As an action, you can open your awareness to detect such forces. Until the end of your next turn, you know the location of any celestial, fiend, or undead within 60 feet of you that is not behind total cover. You know the type (celestial, fiend, or undead) of any being whose presence you sense, but not its identity (the vampire Count Strahd von Zarovich, for instance). Within the same radius, you also detect the presence of any place or object that has been consecrated or desecrated, as with the Hallow spell.

You can use this feature a number of times equal to 1 + your Charisma modifier. When you finish a long rest, you regain all expended uses."""
    feature2 = """Lay on Hands

Your blessed touch can heal wounds. You have a pool of healing power that replenishes when you take a long rest. With that pool, you can restore a total number of hit points equal to your paladin level x 5.

As an action, you can touch a creature and draw power from the pool to restore a number of hit points to that creature. up to the maximum amount remaining in your pool.

Alternatively, you can expend 5 hit points from your pool of healing to cure the target of one disease or neutralize one poison affecting it. You can cure multiple diseases and neutralize multiple poisons with a single use of Lay on Hands, expending hit points separately for each one.

This feature has no effect on undead and constructs.
"""

    dnd_dict.character_dict["features"]['divine_sense'] = feature
    dnd_dict.character_dict["features"]['lay_on_hands'] = feature2

# Enter more entries if you want
def favored_enemy_humanoid():
    while True:
        choice = input("""Select the humanoids you want to be your favored enemies:
1) Dragonborn
2) Dwarves
3) Elves
4) Gnolls
5) Gnomes
6) Goblins
7) Halflings
8) Humans
9) Hobgoblins
10) Orcs
11) Tiefling
Enter your selection: """)
        if choice == '1':
            if 'dragonborn' in dnd_dict.character_dict['favored_enemies']:
                print("Error: Already a Favored Enemy")
                continue
            else:
                dnd_dict.character_dict['favored_enemies']['dragonborn'] = 'Dragonborn'
                dnd_dict.character_dict['Languages']['draconic'] = 'Draconic'
                break

        elif choice == '2':
            if 'dwarves' in dnd_dict.character_dict['favored_enemies']:
                print("Error: Already a Favored Enemy")
                continue
            else:
                dnd_dict.character_dict['favored_enemies']['dwarves'] = 'Dwarves'
                dnd_dict.character_dict['Languages']['dwarven'] = 'Dwarven'
                break

        elif choice == '3':
            if 'elves' in dnd_dict.character_dict['favored_enemies']:
                print("Error: Already a Favored Enemy")
                continue
            else:
                dnd_dict.character_dict['favored_enemies']['elves'] = 'Elves'
                dnd_dict.character_dict['Languages']['elven'] = 'Elven'
                break

        elif choice == '4':
            if 'gnolls' in dnd_dict.character_dict['favored_enemies']:
                print("Error: Already a Favored Enemy")
                continue
            else:
                dnd_dict.character_dict['favored_enemies']['gnolls'] = 'Gnolls'
                break

        elif choice == '5':
            if 'gnomes' in dnd_dict.character_dict['favored_enemies']:
                print("Error: Already a Favored Enemy")
                continue
            else:
                dnd_dict.character_dict['favored_enemies']['gnomes'] = 'Gnomes'
                dnd_dict.character_dict['Languages']['gnomish'] = 'Gnomish'
                break

        elif choice == '6':
            if 'goblins' in dnd_dict.character_dict['favored_enemies']:
                print("Error: Already a Favored Enemy")
                continue
            else:
                dnd_dict.character_dict['favored_enemies']['goblins'] = 'Goblins'
                dnd_dict.character_dict['Languages']['goblin'] = 'Goblin'
                break

        elif choice == '7':
            if 'halflings' in dnd_dict.character_dict['favored_enemies']:
                print("Error: Already a Favored Enemy")
                continue
            else:
                dnd_dict.character_dict['favored_enemies']['halflings'] = 'Halflings'
                dnd_dict.character_dict['Languages']['halfling'] = 'Halfling'
                break

        elif choice == '8':
            if 'humans' in dnd_dict.character_dict['favored_enemies']:
                print("Error: Already a Favored Enemy")
                continue
            else:
                dnd_dict.character_dict['favored_enemies']['humans'] = 'Humans'
                break

        elif choice == '9':
            if 'hobgoblins' in dnd_dict.character_dict['favored_enemies']:
                print("Error: Already a Favored Enemy")
                continue
            else:
                dnd_dict.character_dict['favored_enemies']['hobgoblins'] = 'Hobgoblins'
                dnd_dict.character_dict['Languages']['goblin'] = 'Goblin'
                break

        elif choice == '10':
            if 'orcs' in dnd_dict.character_dict['favored_enemies']:
                print("Error: Already a Favored Enemy")
                continue
            else:
                dnd_dict.character_dict['favored_enemies']['orcs'] = 'Orcs'
                dnd_dict.character_dict['Languages']['orcish'] = 'Orcish'
                break

        elif choice == '11':
            if 'tieflings' in dnd_dict.character_dict['favored_enemies']:
                print("Error: Already a Favored Enemy")
                continue
            else:
                dnd_dict.character_dict['favored_enemies']['tieflings'] = 'Tieflings'
                dnd_dict.character_dict['Languages']['infernal'] = 'Infernal'
                break

        else:
            print("Error: Invalid Input")
            continue

def favored_enemy_creature():
    while True:
        choice2 = input("""Select the type of creature you want to be your favored foe:
1) Abberations
2) Beasts
3) Celestials
4) Constructs
5) Dragons
6) Elementals
7) Fey
8) Fiends
9) Giants
10) Monstrosities
11) Oozes
12) Plants
13) Undead
Enter your selection: """)
        if choice2 == '1':
            if 'abberations' in dnd_dict.character_dict['favored_enemies']:
                print("Error: Already a Favored Enemy")
                continue
            else:
                dnd_dict.character_dict['favored_enemies']['abberations'] = 'Abberations'
                dnd_dict.character_dict['Languages']['deep_speech'] = 'Deep Speech'
                break

        elif choice2 == '2':
            if 'beasts' in dnd_dict.character_dict['favored_enemies']:
                print("Error: Already a Favored Enemy")
                continue
            else:
                dnd_dict.character_dict['favored_enemies']['beasts'] = 'Beasts'
                break

        elif choice2 == '3':
            if 'celestials' in dnd_dict.character_dict['favored_enemies']:
                print("Error: Already a Favored Enemy")
                continue
            else:
                dnd_dict.character_dict['favored_enemies']['celestials'] = 'Celestials'
                dnd_dict.character_dict['Languages']['celestial'] = 'Celestial'
                break

        elif choice2 == '4':
            if 'constructs' in dnd_dict.character_dict['favored_enemies']:
                print("Error: Already a Favored Enemy")
                continue
            else:
                dnd_dict.character_dict['favored_enemies']['constructs'] = 'Constructs'
                break

        elif choice2 == '5':
            if 'dragons' in dnd_dict.character_dict['favored_enemies']:
                print("Error: Already a Favored Enemy")
                continue
            else:
                dnd_dict.character_dict['favored_enemies']['dragons'] = 'Dragons'
                dnd_dict.character_dict['Languages']['draconic'] = 'Draconic'
                break

        elif choice2 == '6':
            if 'elementals' in dnd_dict.character_dict['favored_enemies']:
                print("Error: Already a Favored Enemy")
                continue
            else:
                dnd_dict.character_dict['favored_enemies']['elementals'] = 'Elementals'
                dnd_dict.character_dict['Languages']['primordial'] = 'Primordial'
                break

        elif choice2 == '7':
            if 'fey' in dnd_dict.character_dict['favored_enemies']:
                print("Error: Already a Favored Enemy")
                continue
            else:
                dnd_dict.character_dict['favored_enemies']['fey'] = 'Fey'
                dnd_dict.character_dict['Languages']['sylvan'] = 'Sylvan'
                break

        elif choice2 == '8':
            if 'fiends' in dnd_dict.character_dict['favored_enemies']:
                print("Error: Already a Favored Enemy")
                continue
            else:
                dnd_dict.character_dict['favored_enemies']['fiends'] = 'Fiends'
                dnd_dict.character_dict['Languages']['infernal'] = 'Infernal'
                break

        elif choice2 == '9':
            if 'giants' in dnd_dict.character_dict['favored_enemies']:
                print("Error: Already a Favored Enemy")
                continue
            else:
                dnd_dict.character_dict['favored_enemies']['giants'] = 'Giants'
                dnd_dict.character_dict['Languages']['giant'] = 'Giant'
                break

        elif choice2 == '10':
            if 'monstrosities' in dnd_dict.character_dict['favored_enemies']:
                print("Error: Already a Favored Enemy")
                continue
            else:
                dnd_dict.character_dict['favored_enemies']['monstrosities'] = 'Monstrosities'
                break

        elif choice2 == '11':
            if 'oozes' in dnd_dict.character_dict['favored_enemies']:
                print("Error: Already a Favored Enemy")
                continue
            else:
                dnd_dict.character_dict['favored_enemies']['oozes'] = 'Oozes'
                break

        elif choice2 == '12':
            if 'plants' in dnd_dict.character_dict['favored_enemies']:
                print("Error: Already a Favored Enemy")
                continue
            else:
                dnd_dict.character_dict['favored_enemies']['plants'] = 'Plants'
                break

        elif choice2 == '13':
            if 'undead' in dnd_dict.character_dict['favored_enemies']:
                print("Error: Already a Favored Enemy")
                continue
            else:
                dnd_dict.character_dict['favored_enemies']['undead'] = 'Undead'
                break

        else:
            print("Error: Invalid Input")
            continue

# Used for the initial Favored Enemy Feature
def favored_enemy_first():
    while True:
        choice1 = input("""Do you want your favored foe to be a non-humanoid or two types of humanoids?
1) Non-Humanoid
2) Two Types of Humanoid
Enter your selection: """)
        if choice1 == '1':
            favored_enemy_creature()
            break

        elif choice1 == '2':
            i = 1
            for i in range(i,3):
                if i < 3:
                    print(f'{i}/2')
                    favored_enemy_humanoid()
                    i+=1
                    continue
                if i == 3:
                    break
            break
        else:
            print("Error: Invalid Input")
            continue

# Used for the next Favored Enemy Features
def favored_enemy_after():
    while True:
        choice1 = input("""Do you want your favored foe to be a non-humanoid or two types of humanoids?
1) Non-Humanoid
2) Two Types of Humanoid
Enter your selection: """)
        if choice1 == '1':
            favored_enemy_creature()
            break

        elif choice1 == '2':
            favored_enemy_humanoid()
            break

        else:
            print("Error: Invalid Input")
            continue

def canny():
    dnd_dict.character_dict['features']['canny'] = 'Canny'
    dnd_skills.expertise()
    dnd_language.language()
    dnd_language.language()

def roving():

    dnd_dict.character_dict['features']['roving'] = 'Roving'
    dnd_dict.character_dict['speed'] += 5
    dnd_dict.character_dict['climb_speed'] == dnd_dict.character_dict['speed']
    dnd_dict.character_dict['swim_speed'] == dnd_dict.character_dict['speed']
    if dnd_dict.character_dict['unarmored_movement_barbarian'] > 0:
        dnd_dict.character_dict['unarmored_movement_barbarian'] +=5
    if dnd_dict.character_dict['unarmored_movement_monk'] > 0:
        dnd_dict.character_dict['unarmored_movement_monk'] +=5

def tireless():
    dnd_dict.character_dict['features']['tireless'] = 'Tireless'

def natural_explorer():
    favored_terrain = ['Arctic','Coast','Desert','Forest','Grassland','Mountain','Swamp','Underdark']
    print("Select the Favored Terrain you want to add")
    dnd_skills.skill_addition(favored_terrain,dnd_dict.character_dict['favored_terrain'])

def ranger_features():
    feature = """
Favored Enemy

Beginning at 1st level, you have significant experience studying, tracking, hunting, and even talking to a certain type of enemy commonly encountered in the wilds.

Choose a type of favored enemy: beasts, fey, humanoids, monstrosities, or undead. You gain a +2 bonus to damage rolls with weapon attacks against creatures of the chosen type. Additionally, you have advantage on Wisdom (Survival) checks to track your favored enemies, as well as on Intelligence checks to recall information about them.

When you gain this feature, you also learn one language of your choice, typically one spoken by your favored enemy or creatures associated with it. However, you are free to pick any language you wish to learn."""
    feature2 = """Natural Explorer

You are a master of navigating the natural world, and you react with swift and decisive action when attacked. This grants you the following benefits:

• You ignore difficult terrain.

• You have advantage on initiative rolls.

• On your first turn during combat, you have advantage on attack rolls against creatures that have not yet acted.

In addition, you are skilled at navigating the wilderness. You gain the following benefits when traveling for an hour or more:

• Difficult terrain doesn’t slow your group’s travel.

• Your group can’t become lost except by magical means.

• Even when you are engaged in another activity while traveling (such as foraging, navigating, or tracking), you remain alert to danger.

• If you are traveling alone, you can move stealthily at a normal pace.

• When you forage, you find twice as much food as you normally would.

• While tracking other creatures, you also learn their exact number, their sizes, and how long ago they passed through the area.
"""
    feature3 = """Favored Foe (Optional)

This 1st-level feature replaces the Favored Enemy feature and works with the Foe Slayer feature. You gain no benefit from the replaced feature and don't qualify for anything in the game that requires it.

When you hit a creature with an attack roll, you can call on your mystical bond with nature to mark the target as your favored enemy for 1 minute or until you lose your concentration (as if you were concentrating on a spell).

The first time on each of your turns that you hit the favored enemy and deal damage to it, including when you mark it, you increase that damage by 1d4.

You can use this feature to mark a favored enemy a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.

This feature's extra damage increases when you reach certain levels in this class: to 1d6 at 6th level and to 1d8 at 14th level."""

    feature4 = """Deft Explorer (Optional)

This 1st-level feature replaces the Natural Explorer feature. You gain no benefit from the replaced feature and don't qualify for anything in the game that requires it.

You are an unsurpassed explorer and survivor, both in the wilderness and in dealing with others on your travels. You gain the Canny benefit below, and you gain an additional benefit when you reach 6th level and 10th level in this class.

Canny (1st Level)

Choose one of your skill proficiencies. Your proficiency bonus is doubled for any ability check you make using the chosen skill.

You can also speak, read, and write 2 additional languages of your choice.

Roving (6th Level)

Your walking speed increases by 5, and you gain a climbing speed and a swimming speed equal to your walking speed.
Tireless (10th Level)

As an action, you can give yourself a number of temporary hit points equal to 1d8 + your Wisdom modifier (minimum of 1 temporary hit point). You can use this action a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.

In addition, whenever you finish a short rest, your exhaustion level, if any, is decreased by 1."""



    while True:
        choice = input("""Do you want the Favored Enemy or Favored Foe Feature?
1) Favored Enemy
2) Favored Foe
 Enter your selection: """)
        if choice == '1':
            print(feature)
            dnd_dict.character_dict["features"]['favored_enemy'] = feature
            favored_enemy_first()
            break

        elif choice == '2':
            print(feature3)
            dnd_dict.character_dict["features"]['favored_foe'] = feature3
            break

        else:
            print("Error: Invalid Input")
            continue

    while True:
        choice2 = input("""Do you want the Natural Explorer or Deft Explorer Feature?
1) Natural Explorer
2) Deft Explorer
 Enter your selection: """)
        if choice2 == '1':
            print(feature2)
            natural_explorer()
            dnd_dict.character_dict["features"]['natural_explorer'] = feature2
            break

        elif choice2 == '2':
            print(feature4)
            dnd_dict.character_dict["features"]['deft_explorer'] = feature4
            canny()
            break

        else:
            print("Error: Invalid Input")
            continue


def rogue_features():
    feature = """
Sneak Attack

Beginning at 1st level, you know how to strike subtly and exploit a foe's distraction. Once per turn, you can deal an extra 1d6 damage to one creature you hit with an attack if you have advantage on the attack roll. The attack must use a finesse or a ranged weapon.

You don't need advantage on the attack roll if another enemy of the target is within 5 feet of it, that enemy isn't incapacitated, and you don't have disadvantage on the attack roll.

The amount of the extra damage increases as you gain levels in this class, as shown in the Sneak Attack column of the Rogue table."""
    feature2 = """Thieves' Cant

During your rogue training you learned thieves' cant, a secret mix of dialect, jargon, and code that allows you to hide messages in seemingly normal conversation. Only another creature that knows thieves' cant understands such messages. It takes four times longer to convey such a message than it does to speak the same idea plainly.

In addition, you understand a set of secret signs and symbols used to convey short, simple messages, such as whether an area is dangerous or the territory of a thieves' guild, whether loot is nearby, or whether the people in an area are easy marks or will provide a safe house for thieves on the run.
"""

    feature3 = """Expertise

At 1st level, choose two of your skill proficiencies, or one of your skill proficiencies and your proficiency with thieves' tools. Your proficiency bonus is doubled for any ability check you make that uses either of the chosen proficiencies.

At 6th level, you can choose two more of your proficiencies (in skills or with thieves' tools) to gain this benefit."""

    print(feature)
    print(feature2)
    print(feature3)
    dnd_dict.character_dict["features"]['sneak_attack'] = feature
    dnd_dict.character_dict["features"]['thieves_cant'] = feature2
    dnd_dict.character_dict["features"]['expertise_rogue'] = feature3
    dnd_dict.character_dict['Languages']['thieves_cant'] = 'Thieves\' Cant'
    dnd_skills.expertise_choice()
    dnd_dict.character_dict['sneak_attack'] += 1

def agonizing_blast():
    feature = """Agonizing Blast

Prerequisite: Eldritch Blast cantrip
When you cast Eldritch Blast, add your Charisma modifier to the damage it deals on a hit."""
    dnd_dict.character_dict['invocations']['agonizing_blast'] = 'Agonizing Blast'
    dnd_dict.character_dict['features']['agonizing_blast'] = feature

def armor_of_shadows():
    feature = """Armor of Shadows

You can cast Mage Armor on yourself at will, without expending a spell slot or material components."""
    dnd_dict.character_dict['invocations']['armor_of_shadows'] = 'Armor of Shadows'
    dnd_dict.character_dict['features']['armor_of_shadows'] = feature

def ascendant_step():
    feature = """Ascendant Step

Prerequisite: 9th level
You can cast Levitate on yourself at will, without expending a spell slot or material components."""
    dnd_dict.character_dict['invocations']['ascendant_step'] = 'Ascendant Step'
    dnd_dict.character_dict['features']['ascendant_step'] = feature

def aspect_of_the_moon():
    feature = """Aspect of the Moon

Prerequisite: Pact of the Tome feature
You no longer need to sleep and can’t be forced to sleep by any means. To gain the benefits of a long rest, you can spend all 8 hours doing light activity, such as reading your Book of Shadows and keeping watch."""
    dnd_dict.character_dict['invocations']['aspect_of_the_moon'] = 'Aspect of the Moon'
    dnd_dict.character_dict['pact_invocations']['aspect_of_the_moon'] = 'Aspect of the Moon'
    dnd_dict.character_dict['features']['aspect_of_the_moon'] = feature

def beast_speech():
    feature = """Beast Speech

You can cast Speak with Animals at will, without expending a spell slot."""
    dnd_dict.character_dict['invocations']['beast_speech'] = 'Beast Speech'
    dnd_dict.character_dict['features']['beast_speech'] = feature

def beguiling_influence():
    feature = """Beguiling Influence

You gain proficiency in the Deception and Persuasion skills."""
    dnd_dict.character_dict['invocations']['beguiling_influence'] = 'Beguiling Influence'
    dnd_dict.character_dict['features']['beguiling_influence'] = feature

# If deception or persuasion are not in the proficiency dict, add them there and also to a separate dict. If the invocation is removed, remove them from both dicts.
    if 'deception' not in dnd_dict.character_dict['skill_prof'] or dnd_dict.character_dict['expertise']:
        dnd_dict.character_dict['influence']['deception'] = 'Deception'
        dnd_dict.character_dict['skill_prof']['deception'] = 'Deception'

    if 'persuasion' not in dnd_dict.character_dict['skill_prof'] or dnd_dict.character_dict['expertise']:
        dnd_dict.character_dict['influence']['persuasion'] = 'Persuasion'
        dnd_dict.character_dict['skill_prof']['persuasion'] = 'Persuasion'

def bewitching_whispers():
    feature = """Bewitching Whispers

Prerequisite: 7th level
You can cast Compulsion once using a warlock spell slot. You can't do so again until you finish a long rest."""
    dnd_dict.character_dict['invocations']['bewitching_whispers'] = 'Bewitching Whispers'
    dnd_dict.character_dict['features']['bewitching_whispers'] = feature

def bond_of_the_talisman():
    feature = """Bond of the Talisman

Prerequisite: 12th level, Pact of the Talisman feature
While someone else is wearing your talisman, you can use your action to teleport to the unoccupied space closest to them, provided the two of you are on the same plane of existence. The wearer of your talisman can do the same thing, using their action to teleport to you. The teleportation can be used a number of times equal to your proficiency bonus, and all expended uses are restored when you finish a long rest."""

    dnd_dict.character_dict['invocations']['bond_of_the_talisman'] = 'Bond of the Talisman'
    dnd_dict.character_dict['pact_invocations']['bond_of_the_talisman'] = 'Bond of the Talisman'
    dnd_dict.character_dict['features']['bond_of_the_talisman'] = feature

def book_of_ancient_secrets():
    feature = """Book of Ancient Secrets

Prerequisite: Pact of the Tome feature
You can now inscribe magical rituals in your Book of Shadows. Choose two 1st-level spells that have the ritual tag from any class's spell list; these rituals needn’t be from the same spell list. The spells appear in the book and don't count against the number of spells you know. With your Book of Shadows in hand, you can cast the chosen spells as rituals. You can't cast the spells except as rituals, unless you've learned them by some other means. You can also cast a warlock spell you know as a ritual if it has the ritual tag.

On your adventures, you can add other ritual spells to your Book of Shadows. When you find such a spell, you can add it to the book if the spell's level is equal to or less than half your warlock level (rounded up) and if you can spare the time to transcribe the spell. For each level of the spell, the transcription process takes 2 hours and costs 50 gp for the rare inks needed to inscribe it."""

    dnd_dict.character_dict['invocations']['book_of_ancient_secrets'] = 'Book of Ancient Secrets'
    dnd_dict.character_dict['pact_invocations']['book_of_ancient_secrets'] = 'Book of Ancient Secrets'
    dnd_dict.character_dict['features']['book_of_ancient_secrets'] = feature
    x = 1
    for x in range (x,3):
        if x < 3:
            dnd_skills.book_spell_add(dnd_magic.warlock_ritual_first,dnd_dict.character_dict['spells']['first'],dnd_dict.character_dict['special_spells']['tome_ritual'])
            x+=1
            continue
        else:
            break


def chains_of_carceri():
    feature = """Chains of Carceri

Prerequisite: 15th level, Pact of the Chain feature
You can cast Hold Monster at will – targeting a celestial, fiend, or elemental – without expending a spell slot or material components. You must finish a long rest before you can use this invocation on the same creature again."""

    dnd_dict.character_dict['invocations']['chains_of_carceri'] = 'Chains of Carceri'
    dnd_dict.character_dict['pact_invocations']['chains_of_carceri'] = 'Chains of Carceri'
    dnd_dict.character_dict['features']['chains_of_carceri'] = feature

def cloak_of_flies():
    feature = """Cloak of Flies

Prerequisite: 5th level
As a bonus action, you can surround yourself with a magical aura that looks like buzzing flies. The aura extends 5 feet from you in every direction, but not through total cover. It lasts until you're incapacitated or you dismiss it as a bonus action.

The aura grants you advantage on Charisma (Intimidation) checks but disadvantage on all other Charisma checks. Any other creature that starts its turn in the aura takes poison damage equal to your Charisma modifier (minimum of 0 damage).

Once you use this invocation, you can’t use it again until you finish a short or long rest."""

    dnd_dict.character_dict['invocations']['cloak_of_flies'] = 'Cloak of Flies'
    dnd_dict.character_dict['features']['cloak_of_flies'] = feature

def devils_sight():
    feature = """Devil's Sight

You can see normally in darkness, both magical and nonmagical, to a distance of 120 feet."""
    dnd_dict.character_dict['invocations']['devils_sight'] = 'Devil\'s Sight'
    dnd_dict.character_dict['features']['devils_sight'] = feature

def dreadful_word():
    feature = """Dreadful Word

Prerequisite: 7th level
You can cast Confusion once using a warlock spell slot. You can't do so again until you finish a long rest."""
    dnd_dict.character_dict['invocations']['dreadful_word'] = 'Dreadful Word'
    dnd_dict.character_dict['features']['dreadful_word'] = feature

def eldritch_mind():
    feature = """Eldritch Mind

You have advantage on Constitution saving throws that you make to maintain your concentration on a spell."""
    dnd_dict.character_dict['invocations']['eldritch_mind'] = 'Eldritch Mind'
    dnd_dict.character_dict['features']['eldritch_mind'] = feature

def eldritch_sight():
    feature = """Eldritch Sight

You can cast Detect Magic at will, without expending a spell slot or material components."""
    dnd_dict.character_dict['invocations']['eldritch_sight'] = 'Eldritch Sight'
    dnd_dict.character_dict['features']['eldritch_sight'] = feature

def eldritch_smite():
    feature = """Eldritch Smite

Prerequisite: 5th level, Pact of the Blade feature
Once per turn when you hit a creature with your pact weapon, you can expend a warlock spell slot to deal an extra 1d8 force damage to the target, plus another 1d8 per level of the spell slot, and you can knock the target prone if it is Huge or smaller."""
    dnd_dict.character_dict['invocations']['eldritch_smite'] = 'Eldritch Smite'
    dnd_dict.character_dict['pact_invocations']['eldritch_smite'] = 'Eldritch Smite'
    dnd_dict.character_dict['features']['eldritch_smite'] = feature

def eldritch_spear():
    feature = """Eldritch Spear

Prerequisite: Eldritch Blast cantrip
When you cast Eldritch Blast, its range is 300 feet."""
    dnd_dict.character_dict['invocations']['eldritch_spear'] = 'Eldritch Spear'
    dnd_dict.character_dict['features']['eldritch_spear'] = feature


def eyes_of_the_rune_keeper():
    feature = """Eyes of the Rune Keeper

You can read all writing."""
    dnd_dict.character_dict['invocations']['eyes_of_the_rune_keeper'] = 'Eyes of the Rune Keeper'
    dnd_dict.character_dict['features']['eyes_of_the_rune_keeper'] = feature

def far_scribe():
    feature = """Far Scribe

Prerequisite: 5th level, Pact of the Tome feature
A new page appears in your Book of Shadows. With your permission, a creature can use its action to write its name on that page, which can contain a number of names equal to your proficiency bonus.

You can cast the Sending spell, targeting a creature whose name is on the page, without using a spell slot and without using material components. To do so, you must write the message on the page. The target hears the message in their mind, and if the target replies, their message appears on the page, rather than in your mind. The writing disappears after 1 minute.

As an action, you can magically erase a name on the page by touching it."""
    dnd_dict.character_dict['invocations']['far_scribe'] = 'Far Scribe'
    dnd_dict.character_dict['pact_invocations']['far_scribe'] = 'Far Scribe'
    dnd_dict.character_dict['features']['far_scribe'] = feature

def fiendish_vigor():
    feature = """Fiendish Vigor

You can cast False Life on yourself at will as a 1st-level spell, without expending a spell slot or material components."""
    dnd_dict.character_dict['invocations']['fiendish_vigor'] = 'Fiendish Vigor'
    dnd_dict.character_dict['features']['fiendish_vigor'] = feature

def gaze_of_two_minds():
    feature = """Gaze of Two Minds

You can use your action to touch a willing humanoid and perceive through its senses until the end of your next turn. As long as the creature is on the same plane of existence as you, you can use your action on subsequent turns to maintain this connection, extending the duration until the end of your next turn. While perceiving through the other creature's senses, you benefit from any special senses possessed by that creature, and you are blinded and deafened to your own surroundings."""
    dnd_dict.character_dict['invocations']['gaze_of_two_minds'] = 'Gaze of Two Minds'
    dnd_dict.character_dict['features']['gaze_of_two_minds'] = feature

def ghostly_gaze():
    feature = """Ghostly Gaze

Prerequisite: 7th level
As an action, you gain the ability to see through solid objects to a range of 30 feet. Within that range, you have darkvision if you don’t already have it. This special sight lasts for 1 minute or until your concentration ends (as if you were concentrating on a spell). During that time, you perceive objects as ghostly, transparent images.

Once you use this invocation, you can’t use it again until you finish a short or long rest."""
    dnd_dict.character_dict['invocations']['ghostly_gaze'] = 'Ghostly Gaze'
    dnd_dict.character_dict['features']['ghostly_gaze'] = feature

def gift_of_the_ever_living_ones():
    feature = """Gift of the Ever-Living Ones

Prerequisite: Pact of the Chain feature
Whenever you regain hit points while your familiar is within 100 feet of you, treat any dice rolled to determine the hit points you regain as having rolled their maximum value for you."""
    dnd_dict.character_dict['invocations']['gift_of_the_ever-living_ones'] = 'Gift of the Ever-Living Ones'
    dnd_dict.character_dict['pact_invocations']['gift_of_the_ever-living_ones'] = 'Gift of the Ever-Living Ones'
    dnd_dict.character_dict['features']['gift_of_the_ever-living_ones'] = feature

def gift_of_the_protectors():
    feature = """Gift of the Protectors

Prerequisite: 9th level, Pact of the Tome feature
A new page appears in your Book of Shadows. With your permission, a creature can use its action to write its name on that page, which can contain a number of names equal to your proficiency bonus.

When any creature whose name is on the page is reduced to 0 hit points but not killed outright, the creature magically drops to 1 hit point instead. Once this magic is triggered, no creature can benefit from it until you finish a long rest.

As an action, you can magically erase a name on the page by touching it."""
    dnd_dict.character_dict['invocations']['gift_of_the_protectors'] = 'Gift of the Protectors'
    dnd_dict.character_dict['pact_invocations']['gift_of_the_protectors'] = 'Gift of the Protectors'
    dnd_dict.character_dict['features']['gift_of_the_protectors'] = feature

def grasp_of_hadar():
    feature = """Grasp of Hadar

Prerequisite: Eldritch Blast cantrip
Once on each of your turns when you hit a creature with your Eldritch Blast, you can move that creature in a straight line 10 feet closer to yourself."""
    dnd_dict.character_dict['invocations']['grasp_of_hadar'] = 'Grasp of Hadar'
    dnd_dict.character_dict['features']['grasp_of_hadar'] = feature

def improved_pact_weapon():
    feature = """Improved Pact Weapon

Prerequisite: Pact of the Blade feature
You can use any weapon you summon with your Pact of the Blade feature as a spellcasting focus for your warlock spells.

In addition, the weapon gains a +1 bonus to its attack and damage rolls, unless it is a magic weapon that already has a bonus to those rolls.

Finally, the weapon you conjure can be a shortbow, longbow, light crossbow, or heavy crossbow."""
    dnd_dict.character_dict['invocations']['improved_pact_weapon'] = 'Improved Pact Weapon'
    dnd_dict.character_dict['pact_invocations']['improved_pact_weapon'] = 'Improved Pact Weapon'
    dnd_dict.character_dict['features']['improved_pact_weapon'] = feature

def investment_of_the_chain_master():
    feature = """Investment of the Chain Master

Prerequisite: Pact of the Chain feature
When you cast Find Familiar, you infuse the summoned familiar with a measure of your eldritch power, granting the creature the following benefits:

    The familiar gains either a flying speed or a swimming speed (your choice) of 40 feet.

    As a bonus action, you can command the familiar to take the Attack action.

    The familiar’s weapon attacks are considered magical for the purpose of overcoming immunity and resistance to nonmagical attacks.

    If the familiar forces a creature to make a saving throw, it uses your spell save DC.

    When the familiar takes damage, you can use your reaction to grant it resistance against that damage.
"""
    dnd_dict.character_dict['invocations']['investment_of_the_chain_master'] = 'Investment of the Chain Master'
    dnd_dict.character_dict['pact_invocations']['investment_of_the_chain_master'] = 'Investment of the Chain Master'
    dnd_dict.character_dict['features']['investment_of_the_chain_master'] = feature

def lance_of_lethargy():
    feature = """Lance of Lethargy

Prerequisite: Eldritch Blast cantrip
Once on each of your turns when you hit a creature with your Eldritch Blast, you can reduce that creature’s speed by 10 feet until the end of your next turn."""
    dnd_dict.character_dict['invocations']['lance_of_lethargy'] = 'Lance of Lethargy'
    dnd_dict.character_dict['features']['lance_of_lethargy'] = feature

def lifedrinker():
    feature = """Lifedrinker

Prerequisite: 12th level, Pact of the Blade feature
When you hit a creature with your pact weapon, the creature takes extra necrotic damage equal to your Charisma modifier (minimum 1)."""
    dnd_dict.character_dict['invocations']['lifedrinker'] = 'Lifedrinker'
    dnd_dict.character_dict['pact_invocations']['lifedrinker'] = 'Lifedrinker'
    dnd_dict.character_dict['features']['lifedrinker'] = feature

def maddening_hex():
    feature = """Maddening Hex

Prerequisite: 5th level, Hex spell or a warlock feature that curses
As a bonus action, you cause a psychic disturbance around the target cursed by your Hex spell or by a warlock feature of yours, such as Hexblade’s Curse and Sign of Ill Omen. When you do so, you deal psychic damage to the cursed target and each creature of your choice within 5 feet of it. The psychic damage equals your Charisma modifier (minimum of 1 damage). To use this invocation, you must be able to see the cursed target, and it must be within 30 feet of you."""
    dnd_dict.character_dict['invocations']['maddening_hex'] = 'Maddening Hex'
    dnd_dict.character_dict['features']['maddening_hex'] = feature

def mask_of_many_faces():
    feature = """Mask of Many Faces

You can cast Disguise Self at will, without expending a spell slot."""
    dnd_dict.character_dict['invocations']['mask_of_many_faces'] = 'Mask of Many Faces'
    dnd_dict.character_dict['features']['mask_of_many_faces'] = feature

def master_of_myriad_forms():
    feature = """Master of Myriad Forms

Prerequisite: 15th level
You can cast Alter Self at will, without expending a spell slot."""
    dnd_dict.character_dict['invocations']['master_of_myriad_forms'] = 'Master of Myriad Forms'
    dnd_dict.character_dict['features']['master_of_myriad_forms'] = feature

def minions_of_chaos():
    feature = """Minions of Chaos

Prerequisite: 9th level
You can cast Conjure Elemental once using a warlock spell slot. You can't do so again until you finish a long rest."""
    dnd_dict.character_dict['invocations']['minions_of_chaos'] = 'Minions of Chaos'
    dnd_dict.character_dict['features']['minions_of_chaos'] = feature

def mire_the_mind():
    feature = """Mire the Mind

Prerequisite: 5th level
You can cast Slow once using a warlock spell slot. You can't do so again until you finish a long rest."""
    dnd_dict.character_dict['invocations']['mire_the_mind'] = 'Mire the Mind'
    dnd_dict.character_dict['features']['mire_the_mind'] = feature

def misty_visions():
    feature = """Misty Visions

You can cast Silent Image at will, without expending a spell slot or material components."""
    dnd_dict.character_dict['invocations']['misty_visions'] = 'Misty Visions'
    dnd_dict.character_dict['features']['misty_visions'] = feature

def one_with_shadows():
    feature = """One with Shadows

Prerequisite: 5th level
When you are in an area of dim light or darkness, you can use your action to become invisible until you move or take an action or a reaction."""
    dnd_dict.character_dict['invocations']['one_with_shadows'] = 'One with Shadows'
    dnd_dict.character_dict['features']['one_with_shadows'] = feature

def otherworldly_leap():
    feature = """Otherworldly Leap

Prerequisite: 9th level
You can cast Jump at will, without expending a spell slot."""
    dnd_dict.character_dict['invocations']['otherworldly_lead'] = 'Otherworldly Leap'
    dnd_dict.character_dict['features']['otherworldly_lead'] = feature

def protection_of_the_talisman():
    feature = """Protection of the Talisman

Prerequisite: 7th level, Pact of the Talisman feature
When the wearer of your talisman fails a saving throw, they can add a d4 to the roll, potentially turning the save into a success. This benefit can be used a number of times equal to your proficiency bonus, and all expended uses are restored when you finish a long rest."""
    dnd_dict.character_dict['invocations']['protection_of_the_talisman'] = 'Protection of the Talisman'
    dnd_dict.character_dict['pact_invocations']['protection_of_the_talisman'] = 'Protection of the Talisman'
    dnd_dict.character_dict['features']['protection_of_the_talisman'] = feature

def rebuke_of_the_talisman():
    feature = """Rebuke of the Talisman

Prerequisite: Pact of the Talisman feature
When the wearer of your talisman is hit by an attacker you can see within 30 feet of you, you can use your reaction to deal psychic damage to the attacker equal to your proficiency bonus and push it up to 10 feet away from the talisman's wearer."""
    dnd_dict.character_dict['invocations']['rebuke_of_the_talisman'] = 'Rebuke of the Talisman'
    dnd_dict.character_dict['pact_invocations']['rebuke_of_the_talisman'] = 'Rebuke of the Talisman'
    dnd_dict.character_dict['features']['rebuke_of_the_talisman'] = feature

def relentless_hex():
    feature = """Relentless Hex

Prerequisite: 7th level, Hex spell or a warlock feature that curses
Your curse creates a temporary bond between you and your target. As a bonus action, you can magically teleport up to 30 feet to an unoccupied space you can see within 5 feet of the target cursed by your Hex spell or by a warlock feature of yours, such as Hexblade’s Curse and Sign of Ill Omen. To teleport in this way, you must be able to see the cursed target."""
    dnd_dict.character_dict['invocations']['relentless_hex'] = 'Relentless Hex'
    dnd_dict.character_dict['features']['relentless_hex'] = feature

def repelling_blast():
    feature = """Repelling Blast

Prerequisite: Eldritch Blast cantrip
When you hit a creature with Eldritch Blast, you can push the creature up to 10 feet away from you in a straight line."""
    dnd_dict.character_dict['invocations']['repelling_blast'] = 'Repelling Blast'
    dnd_dict.character_dict['features']['repelling_blast'] = feature

def sculptor_of_flesh():
    feature = """Sculptor of Flesh

Prerequisite: 7th level
You can cast Polymorph once using a warlock spell slot. You can't do so again until you finish a long rest."""
    dnd_dict.character_dict['invocations']['sculptor_of_flesh'] = 'Sculptor of Flesh'
    dnd_dict.character_dict['features']['sculptor_of_flesh'] = feature

def shroud_of_shadow():
    feature = """Shroud of Shadow

Prerequisite: 15th level
You can cast Invisibility at will, without expending a spell slot."""
    dnd_dict.character_dict['invocations']['shroud_of_shadow'] = 'Shroud of Shadow'
    dnd_dict.character_dict['features']['shroud_of_shadow'] = feature

def sign_of_ill_omen():
    feature = """Sign of Ill Omen

Prerequisite: 5th level
You can cast Bestow Curse once using a warlock spell slot. You can't do so again until you finish a long rest."""
    dnd_dict.character_dict['invocations']['sign_of_ill_omen'] = 'Sign of Ill Omen'
    dnd_dict.character_dict['features']['sign_of_ill_omen'] = feature

def thief_of_five_fates():
    feature = """Thief of Five Fates

You can cast Bane once using a warlock spell slot. You can't do so again until you finish a long rest."""
    dnd_dict.character_dict['invocations']['thief_of_five_fates'] = 'Thief of Five Fates'
    dnd_dict.character_dict['features']['thief_of_five_fates'] = feature

def thirsting_blade():
    feature = """Thirsting Blade

Prerequisite: 5th level, Pact of the Blade feature
You can attack with your pact weapon twice, instead of once, whenever you take the Attack action on your turn."""
    dnd_dict.character_dict['invocations']['thirsting_blade'] = 'Thirsting Blade'
    dnd_dict.character_dict['pact_invocations']['thirsting_blade'] = 'Thirsting Blade'
    dnd_dict.character_dict['features']['thirsting_blade'] = feature

def tomb_of_levistus():
    feature = """Tomb of Levistus

Prerequisite: 5th level
As a reaction when you take damage, you can entomb yourself in ice, which melts away at the end of your next turn. You gain 10 temporary hit points per warlock level, which take as much of the triggering damage as possible. Immediately after you take the damage, you gain vulnerability to fire damage, your speed is reduced to 0, and you are incapacitated. These effects, including any remaining temporary hit points, all end when the ice melts.

Once you use this invocation, you can’t use it again until you finish a short or long rest."""
    dnd_dict.character_dict['invocations']['tomb_of_levistus'] = 'Tomb of Levistus'
    dnd_dict.character_dict['features']['tomb_of_levistus'] = feature

def tricksters_escape():
    feature = """Trickster's Escape

Prerequisite: 7th level
You can cast Freedom of Movement once on yourself without expending a spell slot. You regain the ability to do so when you finish a long rest."""
    dnd_dict.character_dict['invocations']['tricksters_escape'] = 'Trickster\'s Escape'
    dnd_dict.character_dict['features']['tricksters_escape'] = feature

def undying_servitude():
    feature = """Undying Servitude

Prerequisite: 5th-level warlock
You can cast Animate Dead without using a spell slot. Once you do so, you can't cast it in this way again until you finish a long rest."""
    dnd_dict.character_dict['invocations']['undying_servitude'] = 'Undying Servitude'
    dnd_dict.character_dict['features']['undying_servitude'] = feature

def visions_of_distant_realms():
    feature = """Visions of Distant Realms

Prerequisite: 15th level
You can cast Arcane Eye at will, without expending a spell slot."""
    dnd_dict.character_dict['invocations']['visions_of_distant_realms'] = 'Visions of Distant Realms'
    dnd_dict.character_dict['features']['visions_of_distant_realms'] = feature

def voice_of_the_chain_master():
    feature = """Voice of the Chain Master

Prerequisite: Pact of the Chain feature
You can communicate telepathically with your familiar and perceive through your familiar's senses as long as you are on the same plane of existence. Additionally, while perceiving through your familiar's senses, you can also speak through your familiar in your own voice, even if your familiar is normally incapable of speech."""
    dnd_dict.character_dict['invocations']['voice_of_the_chain_master'] = 'Voice of the Chain Master'
    dnd_dict.character_dict['pact_invocations']['voice_of_the_chain_master'] = 'Voice of the Chain Master'
    dnd_dict.character_dict['features']['voice_of_the_chain_master'] = feature

def whispers_of_the_grave():
    feature = """Whispers of the Grave

Prerequisite: 9th level
You can cast Speak with Dead at will, without expending a spell slot."""
    dnd_dict.character_dict['invocations']['whispers_of_the_grave'] = 'Whispers of the Grave'
    dnd_dict.character_dict['features']['whispers_of_the_grave'] = feature

def witch_sight():
    feature = """Witch Sight

Prerequisite: 15th level
You can see the true form of any shapechanger or creature concealed by illusion or transmutation magic while the creature is within 30 feet of you and within line of sight."""
    dnd_dict.character_dict['invocations']['witch_sight'] = 'Witch Sight'
    dnd_dict.character_dict['features']['witch_sight'] = feature

def ambush():
    feature = """Ambush

When you make a Dexterity (Stealth) check or an initiative roll, you can expend one superiority die and add the die to the roll, provided you aren't incapacitated."""
    dnd_dict.character_dict['features']['ambush'] = feature
    dnd_dict.character_dict['maneuvers']['types']['ambush'] = 'Ambush'

def bait_and_switch():
    feature = """Bait and Switch

When you're within 5 feet of a creature on your turn, you can expend one superiority die and switch places with that creature, provided you spend at least 5 feet of movement and the creature is willing and isn't incapacitated. This movement doesn't provoke opportunity attacks.

Roll the superiority die. Until the start of your next turn, you or the other creature (your choice) gains a bonus to AC equal to the number rolled."""
    dnd_dict.character_dict['features']['bait_and_switch'] = feature
    dnd_dict.character_dict['maneuvers']['types']['bait_and_switch'] = 'Bait and Switch'

def brace():
    feature = """Brace

When a creature you can see moves into the reach you have with the melee weapon you're wielding, you can use your reaction to expend one superiority die and make one attack against the creature, using that weapon. If the attack hits, add the superiority die to the weapon's damage roll."""
    dnd_dict.character_dict['features']['brace'] = feature
    dnd_dict.character_dict['maneuvers']['types']['brace'] = 'Brace'

def commanders_strike():
    feature = """Commander's Strike

When you take the Attack action on your turn, you can forgo one of your attacks and use a bonus action to direct one of your companions to strike. When you do so, choose a friendly creature who can see or hear you and expend one superiority die. That creature can immediately use its reaction to make one weapon attack, adding the superiority die to the attack's damage roll."""
    dnd_dict.character_dict['features']['commanders_strike'] = feature
    dnd_dict.character_dict['maneuvers']['types']['commanders_strike'] = 'Commander\'s Strike'

def commanding_presence():
    feature = """Commanding Presence

When you make a Charisma (Intimidation), a Charisma (Performance), or a Charisma (Persuasion) check, you can expend one superiority die and add the superiority die to the ability check."""
    dnd_dict.character_dict['features']['commanding_presence'] = feature
    dnd_dict.character_dict['maneuvers']['types']['commanding_presence'] = 'Commanding Presence'

def disarming_attack():
    feature = """Disarming Attack

When you hit a creature with a weapon attack, you can expend one superiority die to attempt to disarm the target, forcing it to drop one item of your choice that it's holding. You add the superiority die to the attack's damage roll, and the target must make a Strength saving throw. On a failed save, it drops the object you choose. The object lands at its feet."""
    dnd_dict.character_dict['features']['disarming_attack'] = feature
    dnd_dict.character_dict['maneuvers']['types']['disarming_attack'] = 'Disarming Attack'

def distracting_strike():
    feature = """Distracting Strike

When you hit a creature with a weapon attack, you can expend one superiority die to distract the creature, giving your allies an opening. You add the superiority die to the attack's damage roll. The next attack roll against the target by an attacker other than you has advantage if the attack is made before the start of your next turn."""
    dnd_dict.character_dict['features']['distracting_strike'] = feature
    dnd_dict.character_dict['maneuvers']['types']['distracting_strike'] = 'Distracting Strike'

def evasive_footwork():
    feature = """Evasive Footwork

When you move, you can expend one superiority die, rolling the die and adding the number rolled to your AC until you stop moving."""
    dnd_dict.character_dict['features']['evasive_footwork'] = feature
    dnd_dict.character_dict['maneuvers']['types']['evasive_footwork'] = 'Evasive Footwork'

def feinting_attack():
    feature = """Feinting Attack

You can expend one superiority die and use a bonus action on your turn to feint, choosing one creature within 5 feet of you as your target. You have advantage on your next attack roll against that creature before the end of your turn. If that attack hits, add the superiority die to the attack's damage roll."""
    dnd_dict.character_dict['features']['feinting_attack'] = feature
    dnd_dict.character_dict['maneuvers']['types']['feinting_attack'] = 'Feinting Attack'

def goading_attack():
    feature = """Goading Attack

When you hit a creature with a weapon attack, you can expend one superiority die to attempt to goad the target into attacking you. You add the superiority die to the attack's damage roll, and the target must make a Wisdom saving throw. On a failed save, the target has disadvantage on all attack rolls against targets other than you until the end of your next turn."""
    dnd_dict.character_dict['features']['goading_attack'] = feature
    dnd_dict.character_dict['maneuvers']['types']['goading_attack'] = 'Goading Attack'

def grappling_strike():
    feature = """Grappling Strike

Immediately after you hit a creature with a melee attack on your turn, you can expend one superiority die and then try to grapple the target as a bonus action (see the Player's Handbook for rules on grappling). Add the superiority die to your Strength (Athletics) check."""
    dnd_dict.character_dict['features']['grappling_strike'] = feature
    dnd_dict.character_dict['maneuvers']['types']['grappling_strike'] = 'Grappling Strike'

def lunging_attack():
    feature = """Lunging Attack

When you make a melee weapon attack on your turn, you can expend one superiority die to increase your reach for that attack by 5 feet. If you hit, you add the superiority die to the attack's damage roll."""
    dnd_dict.character_dict['features']['lunging_attack'] = feature
    dnd_dict.character_dict['maneuvers']['types']['lunging_attack'] = 'Lunging Attack'

def maneuvering_attack():
    feature = """Maneuvering Attack

When you hit a creature with a weapon attack, you can expend one superiority die to maneuver one of your comrades into a more advantageous position. You add the superiority die to the attack's damage roll, and you choose a friendly creature who can see or hear you. That creature can use its reaction to move up to half its speed without provoking opportunity attacks from the target of your attack."""
    dnd_dict.character_dict['features']['maneuvering_attack'] = feature
    dnd_dict.character_dict['maneuvers']['types']['maneuvering_attack'] = 'Manuevering Attack'

def menacing_attack():
    feature = """Menacing Attack

When you hit a creature with a weapon attack, you can expend one superiority die to attempt to frighten the target. You add the superiority die to the attack's damage roll, and the target must make a Wisdom saving throw. On a failed save, it is frightened of you until the end of your next turn."""
    dnd_dict.character_dict['features']['menacing_attack'] = feature
    dnd_dict.character_dict['maneuvers']['types']['menacing_attack'] = 'Menacing Attack'

def parry():
    feature = """Parry

When another creature damages you with a melee attack, you can use your reaction and expend one superiority die to reduce the damage by the number you roll on your superiority die + your Dexterity modifier."""
    dnd_dict.character_dict['features']['parry'] = feature
    dnd_dict.character_dict['maneuvers']['types']['parry'] = 'Parry'

def precision_attack():
    feature = """Precision Attack

When you make a weapon attack roll against a creature, you can expend one superiority die to add it to the roll. You can use this maneuver before or after making the attack roll, but before any effects of the attack are applied."""
    dnd_dict.character_dict['features']['precision_attack'] = feature
    dnd_dict.character_dict['maneuvers']['types']['precision_attack'] = 'Precision Attack'

def pushing_attack():
    feature = """Pushing Attack

When you hit a creature with a weapon attack, you can expend one superiority die to attempt to drive the target back. You add the superiority die to the attack's damage roll, and if the target is Large or smaller, it must make a Strength saving throw. On a failed save, you push the target up to 15 feet away from you."""
    dnd_dict.character_dict['features']['pushing_attack'] = feature
    dnd_dict.character_dict['maneuvers']['types']['pushing_attack'] = 'Pushing Attack'

def quick_toss():
    feature = """Quick Toss

As a bonus action, you can expend one superiority die and make a ranged attack with a weapon that has the thrown property. You can draw the weapon as part of making this attack. If you hit, add the superiority die to the weapon's damage roll."""
    dnd_dict.character_dict['features']['quick_toss'] = feature
    dnd_dict.character_dict['maneuvers']['types']['quick_toss'] = 'Quick Toss'

def rally():
    feature = """Rally

On your turn, you can use a bonus action and expend one superiority die to bolster the resolve of one of your companions. When you do so, choose a friendly creature who can see or hear you. That creature gains temporary hit points equal to the superiority die roll + your Charisma modifier."""
    dnd_dict.character_dict['features']['rally'] = feature
    dnd_dict.character_dict['maneuvers']['types']['rally'] = 'Rally'

def riposte():
    feature = """Riposte

When a creature misses you with a melee attack, you can use your reaction and expend one superiority die to make a melee weapon attack against the creature. If you hit, you add the superiority die to the attack's damage roll."""
    dnd_dict.character_dict['features']['riposte'] = feature
    dnd_dict.character_dict['maneuvers']['types']['riposte'] = 'Riposte'

def sweeping_attack():
    feature = """Sweeping Attack

When you hit a creature with a melee weapon attack, you can expend one superiority die to attempt to damage another creature with the same attack. Choose another creature within 5 feet of the original target and within your reach. If the original attack roll would hit the second creature, it takes damage equal to the number you roll on your superiority die. The damage is of the same type dealt by the original attack."""
    dnd_dict.character_dict['features']['sweeping_attack'] = feature
    dnd_dict.character_dict['maneuvers']['types']['sweeping_attack'] = 'Sweeping Attack'

def tactical_assessment():
    feature = """Tactical Assessment

When you make an Intelligence (Investigation), an Intelligence (History), or a Wisdom (Insight) check, you can expend one superiority die and add the superiority die to the ability check."""
    dnd_dict.character_dict['features']['tactical_assessment'] = feature
    dnd_dict.character_dict['maneuvers']['types']['tactical_assessment'] = 'Tactical Assessment'

def trip_attack():
    feature = """Trip Attack

When you hit a creature with a weapon attack, you can expend one superiority die to attempt to knock the target down. You add the superiority die to the attack's damage roll, and if the target is Large or smaller, it must make a Strength saving throw. On a failed save, you knock the target prone."""
    dnd_dict.character_dict['features']['trip_attack'] = feature
    dnd_dict.character_dict['maneuvers']['types']['trip_attack'] = 'Trip Attack'


def firearm_proficiency():
    feature = """Optional Rule: Firearm Proficiency

The secrets of gunpowder weapons have been discovered in various corners of the D&D multiverse. If your Dungeon Master uses the rules on firearms in the Dungeon Master's Guide and your artificer has been exposed to the operation of such weapons, your artificer is proficient with them."""
    print(feature)
    dnd_dict.character_dict['features']['firearm_proficiency'] = feature

def infuse_item():
    feature = """Infuse Item

At 2nd level, you've gained the ability to imbue mundane items with certain magical infusions, turning those objects into magic items.
Infusions Known

When you gain this feature, pick four artificer infusions to learn. You learn additional infusions of your choice when you reach certain levels in this class, as shown in the Infusions Known column of the Artificer table.

Whenever you gain a level in this class, you can replace one of the artificer infusions you learned with a new one.
Infusing an Item

Whenever you finish a long rest, you can touch a nonmagical object and imbue it with one of your artificer infusions, turning it into a magic item. An infusion works on only certain kinds of objects, as specified in the infusion's description. If the item requires attunement, you can attune yourself to it the instant you infuse the item. If you decide to attune to the item later, you must do so using the normal process for attunement (see the attunement rules in the Dungeon Master's Guide).

Your infusion remains in an item indefinitely, but when you die, the infusion vanishes after a number of days equal to your Intelligence modifier (minimum of 1 day). The infusion also vanishes if you replace your knowledge of the infusion.

You can infuse more than one nonmagical object at the end of a long rest; the maximum number of objects appears in the Infused Items column of the Artificer table. You must touch each of the objects, and each of your infusions can be in only one object at a time. Moreover, no object can bear more than one of your infusions at a time. If you try to exceed your maximum number of infusions, the oldest infusion ends, and then the new infusion applies.

If an infusion ends on an item that contains other things, like a bag of holding, its contents harmlessly appear in and around its space."""

    print(feature)
    dnd_dict.character_dict['features']['infuse_item'] = feature




def right_tool():
    feature = """The Right Tool for the Job

At 3rd level, you've learned how to produce exactly the tool you need: with thieves' tools or artisan's tools in hand, you can magically create one set of artisan's tools in an unoccupied space within 5 feet of you. This creation requires 1 hour of uninterrupted work, which can coincide with a short or long rest. Though the product of magic, the tools are nonmagical, and they vanish when you use this feature again."""

    print(feature)
    dnd_dict.character_dict['features']['right_tool'] = feature

def tool_expertise():
    feature = """Tool Expertise

At 6th level, your proficiency bonus is now doubled for any ability check you make that uses your proficiency with a tool."""

    print(feature)
    dnd_dict.character_dict['features']['tool_expertise'] = feature

def flash_of_genius():
    feature = """Flash of Genius

At 7th level, you've gained the ability to come up with solutions under pressure. When you or another creature you can see within 30 feet of you makes an ability check or a saving throw, you can use your reaction to add your Intelligence modifier to the roll.

You can use this feature a number of times equal to your Intelligence modifier (minimum of once). You regain all expended uses when you finish a long rest."""
    print(feature)
    dnd_dict.character_dict['features']['flash_of_genius'] = feature


def magic_item_adept():
    feature = """Magic Item Adept

When you reach 10th level, you achieve a profound understanding of how to use and make magic items:

    You can attune to up to four magic items at once.

    If you craft a magic item with a rarity of common or uncommon, it takes you a quarter of the normal time, and it costs you half as much of the usual gold."""
    print(feature)
    dnd_dict.character_dict['features']['magic_item_adept'] = feature


def spell_storing_item():
    feature = """Spell-Storing Item

At 11th level, you can now store a spell in an object. Whenever you finish a long rest, you can touch one simple or martial weapon or one item that you can use as a spellcasting focus, and you store a spell in it, choosing a lst- or 2nd-level spell from the artificer spell list that requires 1 action to cast (you needn't have it prepared).

While holding the object, a creature can take an action to produce the spell's effect from it, using your spellcasting ability modifier. If the spell requires concentration, the creature must concentrate. The spell stays in the object until it's been used a number of times equal to twice your Intelligence modifier (minimum of twice) or until you use this feature again to store a spell in an object."""
    print(feature)
    dnd_dict.character_dict['features']['spell-storing_item'] = feature

def magic_item_savant():
    feature = """Magic Item Savant

At 14th level, your skill with magic items deepens more:

    You can attune to up to five magic items at once.

    You ignore all class, race, spell and level requirements on attuning to or using a magic item."""
    print(feature)
    dnd_dict.character_dict['features']['magic_item_savant'] = feature


def magic_item_master():
    feature = """Magic Item Master

Starting at 18th level, you can attune up to six magic items at once."""
    print(feature)
    dnd_dict.character_dict['features']['magic_item_master'] = feature

def soul_of_artifice():
    feature = """Soul of Artifice

At 20th level, you develop a mystical connection to your magic items, which you can draw on for protection:

    You gain a +1 bonus to all saving throws per magic item you are currently attuned to.

    If you're reduced to 0 hit points but not killed out-right, you can use your reaction to end one of your artificer infusions, causing you to drop to 1 hit point instead of 0."""
    print(feature)
    dnd_dict.character_dict['features']['soul_of_artifice'] = feature



def alchemist3():
    feature = """Experimental Elixir

Beginning at 3rd level, whenever you finish a long rest, you can magically produce an experimental elixir in an empty flask you touch. Roll on the Experimental Elixir table for the elixir's effect, which is triggered when someone drinks the elixir. As an action, a creature can drink the elixir or administer it to an incapacitated creature.

You can create additional experimental elixirs by expending a spell slot of 1st level or higher for each one. When you do so, you use your action to create the elixir in an empty flask you touch, and you choose the elixir's effect from the Experimental Elixir table.

Creating an experimental elixir requires you to have alchemist supplies on your person, and any elixir you create with this feature lasts until it is drunk or until the end of your next long rest.

When you reach certain levels in this class, you can make more elixirs at the end of a long rest: two at 6th level and three at 15th level. Roll for each elixir's effect separately. Each elixir requires its own flask.
Experimental Elixir
d6 	Effect
1 	Healing. The drinker regains a number of hit points equal to 2d4 + your Intelligence Modifier
2 	Swiftness. The drinker's walking speed increases by 10 feet for 1 hour.
3 	Resilience. The drinker gains a +1 bonus to AC for 10 minutes.
4 	Boldness. The drinker can roll a d4 and add the number rolled to every attack roll and saving throw they make for the next minute.
5 	Flight. The drinker gains a flying speed of 10 feet for 10 minutes.
6 	Transformation. The drinker's body is transformed as if by the Alter Self spell. The drinker determines the transformation caused by the spell, the effects of which last for 10 minutes."""

    feature2 = """Alchemist Spells

Starting at 3rd level, you always have certain spells prepared after you reach particular levels in this class, as shown in the Alchemist Spells table. These spells count as artificer spells for you, but they don’t count against the number of artificer spells you prepare.
Alchemist Spells
Artificer Level 	Alchemist Spells
3rd 	Healing Word, Ray of Sickness
5th 	Flaming Sphere, Melf's Acid Arrow
9th 	Gaseous Form, Mass Healing Word
13th 	Blight, Death Ward
17th 	Cloudkill, Raise Dead"""


    print(feature)
    print(feature2)
    dnd_dict.character_dict['features']['experimental_elixer'] = feature
    dnd_dict.character_dict['features']['alchemist_spells'] = feature2

    feature2 = """Tool Proficiency

When you adopt this specialization at 3rd level, you gain proficiency with alchemist's supplies. If you already have this proficiency, you gain proficiency with one other type of artisan's tools of your choice."""
    print(feature2)
    dnd_dict.character_dict['features']['alchemist_tool_prof'] = feature2

    if "Alchemist\'s Supplies" in dnd_dict.character_dict['Tools'].values():
        dnd_tools.artisan_tools()
    else:
        dnd_dict.character_dict['Tools']['alchemist\'s_supplies'] = 'Alchemist\'s Supplies'





def alchemist5():
    feature = """Alchemical Savant

At 5th level, you've developed masterful command of magical chemicals, enhancing the healing and damage you create through them. Whenever you cast a spell using your alchemist's supplies as the spellcasting focus, you gain a bonus to one roll of the spell. That roll must restore hit points or be a damage roll that deals acid, fire, necrotic, or poison damage, and the bonus equals your Intelligence modifier (minimum of +1)."""
    print(feature)
    dnd_dict.character_dict['features']['alchemical_savant'] = feature

def alchemist9():
    feature = """Restorative Reagents

Starting at 9th level, you can incorporate restorative reagents into some of your works:

    Whenever a creature drinks an experimental elixir you created, the creature gains temporary hit points equal to 2d6 + your Intelligence modifier (minimum of 1 temporary hit point).

    You can cast Lesser Restoration without expending a spell slot and without preparing the spell, provided you use alchemist's supplies as the spellcasting focus. You can do so a number of times equal to your Intelligence modifier (minimum of once), and you regain all expended uses when you finish a long rest."""
    print(feature)
    dnd_dict.character_dict['features']['restorative_reagents'] = feature


def alchemist15():
    feature = """Chemical Mastery

By 15th level, you have been exposed to so many chemicals that they pose little risk to you, and you can use them to quickly end certain ailments:

    You gain resistance to acid damage and poison damage, and you are now immune to the poisoned condition.

    You can cast Greater Restoration and Heal without expending a spell slot, without preparing the spell, and without providing the material component, provided you use alchemist’s supplies as the spellcasting focus. Once you cast either spell with this feature, you can't cast that spell with it again until you finish a long rest."""
    print(feature)
    dnd_dict.character_dict['features']['chemical_mastery'] = feature




def armorer3():
    feature = """Arcane Armor

Beginning at 3rd level, your metallurgical pursuits have led to you making armor a conduit for your magic. As an action, you can turn a suit of armor you are wearing into Arcane Armor, provided you have smith's tools in hand.

You gain the following benefits while wearing this armor:

    If the armor normally has a Strength requirement, the arcane armor lacks this requirement for you.

    You can use the arcane armor as a spellcasting focus for your artificer spells.

    The armor attaches to you and can’t be removed against your will. It also expands to cover your entire body, although you can retract or deploy the helmet as a bonus action. The armor replaces any missing limbs, functioning identically to a body part it is replacing.

    You can doff or don the armor as an action.

The armor continues to be Arcane Armor until you don another suit of armor or you die."""

    feature2 = """Armor Model

Beginning at 3rd level, you can customize your Arcane Armor. When you do so, choose one of the following armor models: Guardian or Infiltrator. The model you choose gives you special benefits while you wear it.

Each model includes a special weapon. When you attack with that weapon, you can add your Intelligence modifier, instead of Strength or Dexterity, to the attack and damage rolls.

You can change the armor's model whenever you finish a short or long rest, provided you have smith's tools in hand.

Guardian. You design your armor to be in the front line of conflict. It has the following features:

    Thunder Gauntlets. Each of the armor's gauntlets counts as a simple melee weapon while you aren't holding anything in it, and it deals 1d8 thunder damage on a hit. A creature hit by the gauntlet has disadvantage on attack rolls against targets other than you until the start of your next turn, as the armor magically emits a distracting pulse when the creature attacks someone else.

    Defensive Field. As a bonus action, you can gain temporary hit points equal to your level in this class, replacing any temporary hit points you already have. You lose these temporary hit points if you doff the armor. You can use this bonus action a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.

Infiltrator. You customize your armor for subtle undertakings. It has the following features:

    Lightning Launcher. A gemlike node appears on one of your armored fists or on the chest (your choice). It counts as a simple ranged weapon, with a normal range of 90 feet and a long range of 300 feet, and it deals 1d6 lightning damage on a hit. Once on each of your turns when you hit a creature with it, you can deal an extra 1d6 lightning damage to that target.

    Powered Steps. Your walking speed increases by 5 feet.

    Dampening Field. You have advantage on Dexterity (Stealth) checks. If the armor normally imposes disadvantage on such checks, the advantage and disadvantage cancel each other, as normal.
"""
    feature3 = """Tools of the Trade

When you adopt this specialization at 3rd level, you gain proficiency with heavy armor. You also gain proficiency with smith's tools. If you already have this tool proficiency, you gain proficiency with one other type of artisan's tools of your choice."""

    feature4 = """Armorer Spells

Starting at 3rd level, you always have certain spells prepared after you reach particular levels in this class, as shown in the Armorer Spells table. These spells count as artificer spells for you, but they don't count against the number of artificer spells you prepare.
Armorer Spells
Artificer Level 	Armorer Spells
3rd 	Magic Missile, Thunderwave
5th 	Mirror Image, Shatter
9th 	Hypnotic Pattern, Lightning Bolt
13th 	Fire Shield, Greater Invisibility
17th 	Passwall, Wall of Force"""


    print(feature)
    dnd_dict.character_dict['features']['arcane_armor'] = feature
    print(feature2)
    dnd_dict.character_dict['features']['armor_model'] = feature2
    print(feature3)
    dnd_dict.character_dict['features']['tools_of_the_trade_armorer'] = feature3
    print(feature4)
    dnd_dict.character_dict['features']['armorer_spells'] = feature4
    dnd_dict.character_dict['Armor_Prof']['heavy_armor'] = 'Heavy Armor'
    if "Smith\'s Supplies" in dnd_dict.character_dict['Tools'].values():
        dnd_tools.artisan_tools()
    else:
        dnd_dict.character_dict['Tools']['smith\'s_supplies'] = 'Smith\'s Supplies'




def extra_attack():
    feature = """Extra Attack

Starting at 5th level, you can attack twice, rather than once, whenever you take the Attack action on your turn."""
# If the player already has the Fighter's version of extra attack, then ignore this feature.
    if dnd_dict.character_dict['player_class']['fighter']['class_level'] < 5:
        print(feature)
        dnd_dict.character_dict['features']['extra_attack'] = feature

def armorer9():
    feature = """Armor Modifications

At 9th level, you learn how to use your artificer infusions to specially modify your Arcane Armor. That armor now counts as separate items for the purposes of your Infuse Items feature: armor (the chest piece), boots, helmet, and the armor's special weapon. Each of those items can bear one of your infusions, and the infusions transfer over if you change your armor's model with the Armor Model feature. In addition, the maximum number of items you can infuse at once increases by 2, but those extra items must be part of your Arcane Armor."""
    print(feature)
    dnd_dict.character_dict['features']['armor_modifications'] = feature


def armorer15():
    feature = """Perfected Armor

At 15th level, your Arcane Armor gains additional benefits based on its model, as shown below.

Guardian. When a Huge or smaller creature you can see ends its turn within 30 feet of you, you can use your reaction to magically force the creature to make a Strength saving throw against your spell save DC, pulling the creature up to 30 feet toward you to an unoccupied space. If you pull the target to a space within 5 feet of you, you can make a melee weapon attack against it as part of this reaction.

You can use this reaction a number of times equal to your proficiency bonus, and you regain all expended uses of it when you finish a long rest.

Infiltrator. Any creature that takes lightning damage from your Lightning Launcher glimmers with magical light until the start of your next turn. The glimmering creature sheds dim light in a 5-foot radius, and it has disadvantage on attack rolls against you, as the light jolts it if it attacks you. In addition, the next attack roll against it has advantage, and if that attack hits, the target takes an extra 1d6 lightning damage."""
    print(feature)
    dnd_dict.character_dict['features']['perfected_armor'] = feature

def artillerist3():
    feature = """Tool Proficiency

When you adopt this specialization at 3rd level, you gain proficiency with woodcarver's tools. If you already have this proficiency, you gain proficiency with one other type of artisan's tools of your choice."""
    feature2 = """Artillerist Spells

Starting at 3rd level, you always have certain spells prepared after you reach particular levels in this class, as shown in the Artillerist Spells table. These spells count as artificer spells for you, but they don’t count against the number of artificer spells you prepare.
Artillerist Spells
Artificer Level 	Artillerist Spells
3rd 	Shield, Thunderwave
5th 	Scorching Ray, Shatter
9th 	Fireball, Wind Wall
13th 	Ice Storm, Wall of Fire
17th 	Cone of Cold, Wall of Force"""


    print(feature)
    dnd_dict.character_dict['features']['artillerist_tool_proficiency'] = feature
    print(feature2)
    dnd_dict.character_dict['features']['artillerist_spells'] = feature2

    if "Woodcarver\'s Supplies" in dnd_dict.character_dict['Tools'].values():
        dnd_tools.artisan_tools()
    else:
        dnd_dict.character_dict['Tools']['woodcarver\'s_supplies'] = 'Woodcarver\'s Supplies'

    feature2 = """Eldritch Cannon

Also at 3rd level, you've learned how to create a magical cannon. Using woodcarver's tools or smith's tools, you can take an action to magically create a Small or Tiny eldritch cannon in an unoccupied space on a horizontal surface within 5 feet of you. A Small eldritch cannon occupies its space, and a Tiny one can be held in one hand. Once you create a cannon, you can't do so again until you finish a long rest or until you expend a spell slot to create one. You can have only one cannon at a time and can't create one while your cannon is present.

The cannon is a magical object. Regardless of size, the cannon has an AC of 18 and a number of hit points equal to five times your artificer level. It is immune to poison damage and psychic damage. If it is forced to make an ability check or a saving throw, treat all its ability scores as 10 (+0). If the mending spell is cast on it, it regains 2d6 hit points. It disappears if it is reduced to 0 hit points or after 1 hour. You can dismiss it early as an action.

When you create the cannon, you determine its appearance and whether it has legs. You also decide which type it is, choosing from the options on the Eldritch Cannons table. On each of your turns, you can take a bonus action to cause the cannon to activate if you are within 60 feet of it. As part of the same bonus action, you can direct the cannon to walk or climb up to 15 feet to an unoccupied space, provided it has legs.
Eldritch Cannon
Cannon 	Activation
Flamethrower 	The cannon exhales fire in an adjacent 15-foot cone that you designate. Each creature in that area must make a Dexterity saving throw against your spell save DC, taking 2d8 fire damage on a failed save or half as much damage on a successful one. The fire ignites any flammable objects in the area that aren't being worn or carried.
Force Ballista 	Make a ranged spell attack, originating from the cannon, at one creature or object within 120 feet of it. On a hit, the target takes 2d8 force damage, and if the target is a creature, it is pushed up to 5 feet away from the cannon.
Protector 	The cannon emits a burst of positive energy that grants itself and each creature of your choice within 10 feet of it a number of temporary hit points equal to 1d8 + your Intelligence modifier (minimum of +1)."""
    print(feature2)
    dnd_dict.character_dict['features']['eldritch_cannon'] = feature2

def artillerist_5():
    feature = """Arcane Firearm

At 5th level, You know how to turn a wand, staff, or rod into an arcane firearm, a conduit for your destructive spells. When you finish a long rest, you can use woodcarver's tools to carve special sigils into a wand, staff, or rod and thereby turn it into your arcane firearm. The sigils disappear from the object if you later carve them on a different item. The sigils otherwise last indefinitely.

You can use your arcane firearm as a spellcasting focus for your artificer spells. When you cast an artificer spell through the firearm, roll a d8, and you gain a bonus to one of the spell's damage rolls equal to the number rolled."""
    print(feature)
    dnd_dict.character_dict['features']['arcane_firearm'] = feature

def artillerist9():
    feature = """Explosive Cannon

Starting at 9th level, every eldritch cannon you create is more destructive:

    The cannon's damage rolls all increase by 1d8.

    As an action, you can command the cannon to detonate if you are within 60 feet of it. Doing so destroys the cannon and forces each creature within 20 feet of it to make a Dexterity saving throw against your spell save DC, taking 3d8 force damage on a failed save or half as much damage on a successful one."""
    print(feature)
    dnd_dict.character_dict['features']['explosive_cannon'] = feature

def artillerist15():
    feature = """Fortified Position

By 15th level, you’re a master at forming well-defended emplacements using Eldritch Cannon:

    You and your allies have half cover while within 10 feet of a cannon you create with Eldritch Cannon, as a result of a shimmering field of magical protection that the cannon emits.

    You can now have two cannons at the same time. You can create two with the same action (but not the same spell slot), and you can activate both of them with the same bonus action. You determine whether the cannons are identical to each other or different. You can't create a third cannon while you have two."""
    print(feature)
    dnd_dict.character_dict['features']['fortified_position'] = feature


def battle_smith3():
    feature = """Tool Proficiency

When you adopt this specialization at 3rd level, you gain proficiency with smith's tools. If you already have this proficiency, you gain proficiency with one other type of artisan's tools of your choice."""

    feature2 = """Battle Ready

When you reach 3rd level, your combat training and your experiments with magic have paid off in two ways:

    You gain proficiency with martial weapons.

    When you attack with a magic weapon, you can use your Intelligence modifier, instead of Strength or Dexterity modifier, for the attack and damage rolls."""

    feature3 = """Steel Defender

By 3rd level, your tinkering has borne you a faithful companion, a steel defender. It's friendly to you and your companions, and it obeys your commands. See its game statistics in the Steel Defender stat block, which uses your proficiency bonus (PB) in several places. You determine the creature's appearance and whether it has two legs or four; your choice has no effect on its game statistics.

In combat, the defender shares your initiative count, but it takes its turn immediately after yours. It can move and use its reaction on its own, but the only action it takes on its turn is the Dodge action, unless you take a bonus action on your turn to command it to take another action. That action can be one in its stat block or some other action. If you are incapacitated, the defender can take any action of its choice, not just Dodge.

If the Mending spell is cast on it, it regains 2d6 hit points. If it has died within the last hour, you can use your smith's tools as an action to revive it, provided you are within 5 feet of it and you expend a spell slot of 1st level or higher. The steel defender returns to life after 1 minute with all its hit points restored.

At the end of a long rest, you can create a new steel defender if you have smith's tools with you. If you already have a defender from this feature, the first one immediately perishes. The defender also perishes if you die.
Steel Defender
Medium construct
Armor Class: 15 (natural armor)
Hit Points: 2 + your Intelligence modifier + 5 times your artificer level (the defender has a number of Hit Dice [d8s] equal to your artificer level)
Speed: 40 ft.
STR 	DEX 	CON 	INT 	WIS 	CHA
14 (+2) 	12 (+1) 	14 (+2) 	4 (−3) 	10 (+0) 	6 (−2)
Saving Throws: Dex +1 plus PB, Con +2 plus PB
Skills: Athletics +2 plus PB, Perception +0 plus PB x 2
Damage Immunities: poison
Condition Immunities: charmed, exhaustion, poisoned
Senses: darkvision 60 ft., passive Perception 10 + (PB x 2)
Languages: understands the languages you speak
Challenge: —
Proficiency Bonus (PB): equals your bonus
Vigilant. The defender can't be surprised.
Actions
Force-Empowered Rend. Melee Weapon Attack: your spell attack modifier to hit, reach 5 ft., one target you can see. Hit: 1d8 + PB force damage.
Repair (3/Day). The magical mechanisms inside the defender restore 2d8 + PB hit points to itself or to one construct or object within 5 feet of it.
Reactions
Deflect Attack. The defender imposes disadvantage on the attack roll of one creature it can see that is within 5 feet of it, provided the attack roll is against a creature other than the defender."""

    feature4 = """Battle Smith Spells

Starting at 3rd level, you always have certain spells prepared after you reach particular levels in this class, as shown in the Battle Smith Spells table. These spells count as artificer spells for you, but they don’t count against the number of artificer spells you prepare.
Battle Smith Spells
Artificer Level 	Battle Smith Spells
3rd 	Heroism, Shield
5th 	Branding Smite, Warding Bond
9th 	Aura of Vitality, Conjure Barrage
13th 	Aura of Purity, Fire Shield
17th 	Banishing Smite, Mass Cure Wounds"""

    dnd_dict.character_dict['Weapon_Prof']['martial_weapons'] = 'Martial Weapons'
    if "Smith\'s Supplies" in dnd_dict.character_dict['Tools'].values():
        dnd_tools.artisan_tools()
    else:
        dnd_dict.character_dict['Tools']['smith\'s_supplies'] = 'Smith\'s Supplies'

    print(feature)
    dnd_dict.character_dict['features']['tool_proficiency_battle_smith'] = feature
    print(feature2)
    dnd_dict.character_dict['features']['battle_ready'] = feature2
    print(feature3)
    dnd_dict.character_dict['features']['steel_defender'] = feature3
    print(feature4)
    dnd_dict.character_dict['features']['battle_smith_spells'] = feature4

def battle_smith9():
    feature = """Arcane Jolt

At 9th level, you've learn new ways to channel arcane energy to harm or heal. When either you hit a target with a magic weapon attack or your steel defender hits a target, you can channel magical energy through the strike to create one of the following effects:

    The target takes an extra 2d6 force damage.

    Choose one creature or object you can see within 30 feet of the target. Healing energy flows into the chosen recipient, restoring 2d6 hit points to it.

You can use this energy a number of times equal to your Intelligence modifier (minimum of once), but you can do so no more than once on a turn. You regain all expended uses when you finish a long rest."""
    print(feature)
    dnd_dict.character_dict['features']['arcane_jolt'] = feature

def battle_smith15():
    feature = """Improved Defender

At 15th level, your Arcane Jolt and steel defender become more powerful:

    The extra damage and the healing of your Arcane Jolt both increase to 4d6.

    Your steel defender gains a +2 bonus to Armor Class.

    Whenever your steel defender uses its Deflect Attack, the attacker takes force damage equal to 1d4 + your Intelligence modifier."""
    print(feature)
    dnd_dict.character_dict['features']['improved_defender'] = feature




def barbarian2():
    feature = """Danger Sense

At 2nd level, you gain an uncanny sense of when things nearby aren't as they should be, giving you an edge when you dodge away from danger. You have advantage on Dexterity saving throws against effects that you can see, such as traps and spells. To gain this benefit, you can't be blinded, deafened, or incapacitated."""
    feature2 = """Reckless Attack

Starting at 2nd level, you can throw aside all concern for defense to attack with fierce desperation. When you make your first attack on your turn, you can decide to attack recklessly. Doing so gives you advantage on melee weapon attack rolls using Strength during this turn, but attack rolls against you have advantage until your next turn."""
    print(feature)
    dnd_dict.character_dict['features']['danger_sense'] = feature
    print(feature2)
    dnd_dict.character_dict['features']['reckless_attack'] = feature2

def barbarian3():
    feature = """Primal Knowledge (Optional)

When you reach 3rd level and again at 10th level, you gain proficiency in one skill of your choice from the list of skills available to barbarians at 1st level."""
    skill_list = ['Animal Handling','Athletics','Intimidation','Nature','Perception','Survival']
    if 'Animal Handling' not in dnd_dict.character_dict['skill_prof'].values() or 'Athletics' not in dnd_dict.character_dict['skill_prof'].values() or 'Intimidation' not in dnd_dict.character_dict['skill_prof'].values() or 'Nature' not in dnd_dict.character_dict['skill_prof'].values() or 'Perception' not in dnd_dict.character_dict['skill_prof'].values() or 'Survival' not in dnd_dict.character_dict['skill_prof'].values():
        dnd_skills.skill_addition(skill_list,dnd_dict.character_dict['skill_prof'])

def barbarian5():
    extra_attack()
    feature = """Fast Movement

Starting at 5th level, your speed increases by 10 feet while you aren't wearing heavy armor."""
    print(feature)
    dnd_dict.character_dict['features']['fast_movement'] = feature
    new_speed = dnd_dict.character_dict['speed'] + 10
    dnd_dict.character_dict['unarmored_movement_barbarian'] = new_speed
    if dnd_dict.character_dict['unarmored_movement_monk'] > 0:
        dnd_dict.character_dict['unarmored_movement_monk'] +=10


def barbarian7():
    feature = """Feral Instinct

By 7th level, your instincts are so honed that you have advantage on initiative rolls.

Additionally, if you are surprised at the beginning of combat and aren't incapacitated, you can act normally on your first turn, but only if you enter your rage before doing anything else on that turn."""

    feature2 = """Instinctive Pounce (Optional)

At 7th level, as part of the bonus action you take to enter your rage, you can move up to half your speed."""

    print(feature)
    dnd_dict.character_dict['features']['feral_instinct'] = feature
    print(feature2)
    dnd_dict.character_dict['features']['instinctive_pounce'] = feature2


def barbarian9():
    feature = """Brutal Critical

Beginning at 9th level, you can roll one additional weapon damage die when determining the extra damage for a critical hit with a melee attack.

This increases to two additional dice at 13th level and three additional dice at 17th level."""
    print(feature)
    dnd_dict.character_dict['features']['brutal_critical'] = feature

def barbarian11():
    feature = """Relentless Rage

Starting at 11th level, your rage can keep you fighting despite grievous wounds. If you drop to 0 hit points while you're raging and don't die outright, you can make a DC 10 Constitution saving throw. If you succeed, you drop to 1 hit point instead.

Each time you use this feature after the first, the DC increases by 5. When you finish a short or long rest, the DC resets to 10."""
    print(feature)
    dnd_dict.character_dict['features']['relentless_rage'] = feature

def barbarian15():
    feature = """Persistent Rage

Beginning at 15th level, your rage is so fierce that it ends early only if you fall unconscious or if you choose to end it.
"""
    print(feature)
    dnd_dict.character_dict['features']['persistent_rage'] = feature

def barbarian18():
    feature = """Indomitable Might

Beginning at 18th level, if your total for a Strength check is less than your Strength score, you can use that score in place of the total."""
    print(feature)
    dnd_dict.character_dict['features']['indomitable_might'] = feature

def barbarian20():
    feature = """Primal Champion

At 20th level, you embody the power of the wilds. Your Strength and Constitution scores increase by 4. Your maximum for those scores is now 24."""
    print(feature)
    dnd_dict.character_dict['features']['primal_champion'] = feature

    dnd_dict.character_dict['Stats']['strength']['base'] +=4
    dnd_dict.character_dict['Stats']['strength']['mod'] = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['strength']['base'])
    dnd_dict.character_dict['Stats']['constitution']['base'] +=4
    dnd_dict.character_dict['Stats']['constitution']['mod'] = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['constitution']['base'])
# HP increases by 40 because the Con modifier goes up twice
    dnd_dict.character_dict['hp'] += 40


def berserker3():
    feature = """Frenzy

Starting when you choose this path at 3rd level, you can go into a frenzy when you rage. If you do so, for the duration of your rage you can make a single melee weapon attack as a bonus action on each of your turns after this one. When your rage ends, you suffer one level of exhaustion."""
    print(feature)
    dnd_dict.character_dict['features']['frenzy'] = feature

def berserker6():
    feature = """Mindless Rage

Beginning at 6th level, you can't be charmed or frightened while raging. If you are charmed or frightened when you enter your rage, the effect is suspended for the duration of the rage."""
    print(feature)
    dnd_dict.character_dict['features']['mindless_rage'] = feature

def berserker10():
    feature = """Intimidating Presence

Beginning at 10th level, you can use your action to frighten someone with your menacing presence. When you do so, choose one creature that you can see within 30 feet of you. If the creature can see or hear you, it must succeed on a Wisdom saving throw (DC equal to 8 + your proficiency bonus + your Charisma modifier) or be frightened of you until the end of your next turn. On subsequent turns, you can use your action to extend the duration of this effect on the frightened creature until the end of your next turn. This effect ends if the creature ends its turn out of line of sight or more than 60 feet away from you.

If the creature succeeds on its saving throw, you can't use this feature on that creature again for 24 hours."""
    print(feature)
    dnd_dict.character_dict['features']['intimidating_presence'] = feature

def berserker14():
    feature = """Retaliation

Starting at 14th level, when you take damage from a creature that is within 5 feet of you, you can use your reaction to make a melee weapon attack against that creature."""
    print(feature)
    dnd_dict.character_dict['features']['retaliation'] = feature

def totem_warrior3():
    feature = """Spirit Seeker

Yours is a path that seeks attunement with the natural world, giving you a kinship with beasts. At 3rd level when you adopt this path, you gain the ability to cast the Beast Sense and Speak with Animals spells, but only as rituals."""
    print(feature)
    dnd_dict.character_dict['features']['spirit_seeker'] = feature
# Don't put in the other totems in the Features dict
    feature2 = """Totem Spirit

At 3rd level, when you adopt this path, you choose a totem spirit and gain its feature. You must make or acquire a physical totem object – an amulet or similar adornment – that incorporates fur or feathers, claws, teeth, or bones of the totem animal. At your option, you also gain minor physical attributes that are reminiscent of your totem spirit. For example, if you have a bear totem spirit, you might be unusually hairy and thick-skinned, or if your totem is the eagle, your eyes turn bright yellow.

Your totem animal might be an animal related to those listed here but more appropriate to your homeland. For example, you could choose a hawk or vulture in place of an eagle.Bear. While raging, you have resistance to all damage except psychic damage. The spirit of the bear makes you tough enough to stand up to any punishment."""

    feature4 = """Totem Spirit

At 3rd level, when you adopt this path, you choose a totem spirit and gain its feature. You must make or acquire a physical totem object – an amulet or similar adornment – that incorporates fur or feathers, claws, teeth, or bones of the totem animal. At your option, you also gain minor physical attributes that are reminiscent of your totem spirit. For example, if you have a bear totem spirit, you might be unusually hairy and thick-skinned, or if your totem is the eagle, your eyes turn bright yellow.

Your totem animal might be an animal related to those listed here but more appropriate to your homeland. For example, you could choose a hawk or vulture in place of an eagle.Bear. While raging, you have resistance to all damage except psychic damage. The spirit of the bear makes you tough enough to stand up to any punishment.

Bear. While raging, you have resistance to all damage except psychic damage. The spirit of the bear makes you tough enough to stand up to any punishment.

Eagle. While you're raging and aren't wearing heavy armor, other creatures have disadvantage on opportunity attack rolls against you, and you can use the Dash action as a bonus action on your turn. The spirit of the eagle makes you into a predator who can weave through the fray with ease.

Elk. While you're raging and aren't wearing heavy armor, your walking speed increases by 15 feet. The spirit of the elk makes you extraordinarily swift.

Tiger. While raging, you can add 10 feet to your long jump distance and 3 feet to your high jump distance. The spirit of the tiger empowers your leaps.

Wolf. While you're raging, your friends have advantage on melee attack rolls against any creature within 5 feet of you that is hostile to you. The spirit of the wolf makes you a leader of hunters."""
    print(feature4)
    dnd_dict.character_dict['features']['totem_spirit'] = feature4
    while True:
        choice = input("""Select the totem you wish to use:
1) Bear
2) Eagle
3) Elk
4) Tiger
5) Wolf
Enter your Selection: """)
        if choice == '1':
            feature3 = """Totem Spirit: Bear. While raging, you have resistance to all damage except psychic damage. The spirit of the bear makes you tough enough to stand up to any punishment."""
            print(feature3)
            dnd_dict.character_dict['features']['bear_totem3'] = feature3
            break

        elif choice == '2':
            feature3 = """Totem Spirit: Eagle. While you're raging and aren't wearing heavy armor, other creatures have disadvantage on opportunity attack rolls against you, and you can use the Dash action as a bonus action on your turn. The spirit of the eagle makes you into a predator who can weave through the fray with ease."""
            print(feature3)
            dnd_dict.character_dict['features']['eagle_totem3'] = feature3
            break

        elif choice == '3':
            feature3 = """Totem Spirit: Elk. While you're raging and aren't wearing heavy armor, your walking speed increases by 15 feet. The spirit of the elk makes you extraordinarily swift."""
            print(feature3)
            dnd_dict.character_dict['features']['elk_totem3'] = feature3
            break

        elif choice == '4':
            feature3 = """Totem Spirit: Tiger. While raging, you can add 10 feet to your long jump distance and 3 feet to your high jump distance. The spirit of the tiger empowers your leaps."""
            print(feature3)
            dnd_dict.character_dict['features']['tiger_totem3'] = feature3
            break

        elif choice == '5':
            feature3 = """Totem Spirit: Wolf. While you're raging, your friends have advantage on melee attack rolls against any creature within 5 feet of you that is hostile to you. The spirit of the wolf makes you a leader of hunters."""
            print(feature3)
            dnd_dict.character_dict['features']['wolf_totem3'] = feature3
            break

        else:
            print("Error: Invalid Input")
            continue

def totem_warrior6():

    feature2 = """Aspect of the Beast

At 6th level, you gain a magical benefit based on the totem animal of your choice. You can choose the same animal you selected at 3rd level or a different one.

Bear. You gain the might of a bear. Your carrying capacity (including maximum load and maximum lift) is doubled, and you have advantage on Strength checks made to push, pull, lift, or break objects.

Eagle. You gain the eyesight of an eagle. You can see up to 1 mile away with no difficulty, able to discern even fine details as though looking at something no more than 100 feet away from you. Additionally, dim light doesn't impose disadvantage on your Wisdom (Perception) checks.

Elk. Whether mounted or on foot, your travel pace is doubled, as is the travel pace of up to ten companions while they're within 60 feet of you and you're not incapacitated. The elk spirit helps you roam far and fast.

Tiger. You gain proficiency in two skills from the following list: Athletics, Acrobatics, Stealth, and Survival. The cat spirit hones your survival instincts.

Wolf. You gain the hunting sensibilities of a wolf. You can track other creatures while traveling at a fast pace, and you can move stealthily while traveling at a normal pace."""
    print(feature2)
    while True:
        choice = input("""Select the totem you wish to use:
1) Bear
2) Eagle
3) Elk
4) Tiger
5) Wolf
Enter your Selection: """)
        if choice == '1':
            feature3 = """Aspect of the Beast: Bear. You gain the might of a bear. Your carrying capacity (including maximum load and maximum lift) is doubled, and you have advantage on Strength checks made to push, pull, lift, or break objects."""
            print(feature3)
            dnd_dict.character_dict['features']['bear_totem6'] = feature3
            break

        elif choice == '2':
            feature3 = """Aspect of the Beast: Eagle. You gain the eyesight of an eagle. You can see up to 1 mile away with no difficulty, able to discern even fine details as though looking at something no more than 100 feet away from you. Additionally, dim light doesn't impose disadvantage on your Wisdom (Perception) checks."""
            print(feature3)
            dnd_dict.character_dict['features']['eagle_totem6'] = feature3
            break

        elif choice == '3':
            feature3 = """Aspect of the Beast: Elk. Whether mounted or on foot, your travel pace is doubled, as is the travel pace of up to ten companions while they're within 60 feet of you and you're not incapacitated. The elk spirit helps you roam far and fast."""
            print(feature3)
            dnd_dict.character_dict['features']['elk_totem6'] = feature3
            break

        elif choice == '4':
            skill_list = ['Athletics','Acrobatics','Stealth','Survival']
            i = 1
            while i < 3:
                check_prof = dnd_dict.character_dict['skill_prof']
                if 'athletics' in check_prof and 'acrobatics' in check_prof and 'stealth' in check_prof and 'survival' in check_prof:
                    i+=2
                    break
                else:
                    print(f'{i}/2')
                    dnd_skills.skill_addition(skill_list,check_prof)
                    i+=1

            feature3 = """Aspect of the Beast: Tiger. You gain proficiency in two skills from the following list: Athletics, Acrobatics, Stealth, and Survival. The cat spirit hones your survival instincts."""
            print(feature3)
            dnd_dict.character_dict['features']['tiger_totem6'] = feature3
            break

        elif choice == '5':
            feature3 = """Aspect of the Beast: Wolf. You gain the hunting sensibilities of a wolf. You can track other creatures while traveling at a fast pace, and you can move stealthily while traveling at a normal pace."""
            print(feature3)
            dnd_dict.character_dict['features']['wolf_totem6'] = feature3
            break

        else:
            print("Error: Invalid Input")
            continue


def totem_warrior10():
    feature = """Spirit Walker

At 10th level, you can cast the Commune with Nature spell, but only as a ritual. When you do so, a spiritual version of one of the animals you chose for Totem Spirit or Aspect of the Beast appears to you to convey the information you seek."""
    print(feature)
    dnd_dict.character_dict['features']['spirit_walker'] = feature


def totem_warrior14():
    feature2 = """Totemic Attunement

At 14th level, you gain a magical benefit based on a totem animal of your choice. You can choose the same animal you selected previously or a different one.

Bear. While you're raging, any creature within 5 feet of you that's hostile to you has disadvantage on attack rolls against targets other than you or another character with this feature. An enemy is immune to this effect if it can't see or hear you or if it can't be frightened.

Eagle. While raging, you have a flying speed equal to your current walking speed. This benefit works only in short bursts; you fall if you end your turn in the air and nothing else is holding you aloft.

Elk. While raging, you can use a bonus action during your move to pass through the space of a Large or smaller creature. That creature must succeed on a Strength saving throw (DC 8 + your Strength bonus + your proficiency bonus) or be knocked prone and take bludgeoning damage equal to 1d12 + your Strength modifier.

Tiger. While you're raging, if you move at least 20 feet in a straight line toward a Large or smaller target right before making a melee weapon attack against it, you can use a bonus action to make an additional melee weapon attack against it.

Wolf. While you're raging, you can use a bonus action on your turn to knock a Large or smaller creature prone when you hit it with melee weapon attack."""


    print(feature2)
    while True:
        choice = input("""Select the totem you wish to use:
1) Bear
2) Eagle
3) Elk
4) Tiger
5) Wolf
Enter your Selection: """)
        if choice == '1':
            feature3 = """Totemic Attunement: Bear. While you're raging, any creature within 5 feet of you that's hostile to you has disadvantage on attack rolls against targets other than you or another character with this feature. An enemy is immune to this effect if it can't see or hear you or if it can't be frightened."""
            print(feature3)
            dnd_dict.character_dict['features']['bear_totem14'] = feature3
            break

        elif choice == '2':
            feature3 = """Totemic Attunement: Eagle. While raging, you have a flying speed equal to your current walking speed. This benefit works only in short bursts; you fall if you end your turn in the air and nothing else is holding you aloft."""
            print(feature3)
            dnd_dict.character_dict['features']['eagle_totem14'] = feature3
            break

        elif choice == '3':
            feature3 = """Totemic Attunement: Elk. While raging, you can use a bonus action during your move to pass through the space of a Large or smaller creature. That creature must succeed on a Strength saving throw (DC 8 + your Strength bonus + your proficiency bonus) or be knocked prone and take bludgeoning damage equal to 1d12 + your Strength modifier."""
            print(feature3)
            dnd_dict.character_dict['features']['elk_totem14'] = feature3
            break

        elif choice == '4':
            feature3 = """Totemic Attunement: Tiger. While you're raging, if you move at least 20 feet in a straight line toward a Large or smaller target right before making a melee weapon attack against it, you can use a bonus action to make an additional melee weapon attack against it."""
            print(feature3)
            dnd_dict.character_dict['features']['tiger_totem14'] = feature3
            break

        elif choice == '5':
            feature3 = """Totemic Attunement: Wolf. While you're raging, you can use a bonus action on your turn to knock a Large or smaller creature prone when you hit it with melee weapon attack."""
            print(feature3)
            dnd_dict.character_dict['features']['wolf_totem14'] = feature3
            break

        else:
            print("Error: Invalid Input")
            continue


def bard1():
    feature = """Spellcasting

You have learned to untangle and reshape the fabric of reality in harmony with your wishes and music. Your spells are part of your vast repertoire, magic that you can tune to different situations.
Cantrips

You know two cantrips of your choice from the bard spell list. You learn additional bard cantrips of your choice at higher levels, as shown in the Cantrips Known column of the Bard table.
Spell Slots

The Bard table shows how many spell slots you have to cast your bard spells of 1st level and higher. To cast one of these spells, you must expend a slot of the spell's level or higher. You regain all expended spell slots when you finish a long rest. For example, if you know the 1st-level spell Cure Wounds and have a 1st-level and a 2nd-level spell slot available, you can cast Cure Wounds using either slot.
Spells Known of 1st Level and Higher

You know four 1st-level spells of your choice from the bard spell list.

The Spells Known column of the Bard table shows when you learn more bard spells of your choice. Each of these spells must be of a level for which you have spell slots, as shown on the table. For instance, when you reach 3rd level in this class, you can learn one new spell of 1st or 2nd level.

Additionally, when you gain a level in this class, you can choose one of the bard spells you know and replace it with another spell from the bard spell list, which also must be of a level for which you have spell slots.
Spellcasting Ability

Charisma is your spellcasting ability for your bard spells. Your magic comes from the heart and soul you pour into the performance of your music or oration. You use your Charisma whenever a spell refers to your spellcasting ability. In addition, you use your Charisma modifier when setting the saving throw DC for a bard spell you cast and when making an attack roll with one.

Spell save DC = 8 + your proficiency bonus + your Charisma modifier

Spell attack modifier = your proficiency bonus + your Charisma modifier"""

    print(feature)
    dnd_dict.character_dict['features']['bard_spellcasting'] = feature

    feature2 = """Ritual Casting

You can cast any bard spell you know as a ritual if that spell has the ritual tag."""

    print(feature2)
    dnd_dict.character_dict['features']['ritual_casting'] = feature2

    feature3 = """Bardic Inspiration

You can inspire others through stirring words or music. To do so, you use a bonus action on your turn to choose one creature other than yourself within 60 feet of you who can hear you. That creature gains one Bardic Inspiration die, a d6.

Once within the next 10 minutes, the creature can roll the die and add the number rolled to one ability check, attack roll, or saving throw it makes. The creature can wait until after it rolls the d20 before deciding to use the Bardic Inspiration die, but must decide before the DM says whether the roll succeeds or fails. Once the Bardic Inspiration die is rolled, it is lost. A creature can have only one Bardic Inspiration die at a time.

You can use this feature a number of times equal to your Charisma modifier (a minimum of once). You regain any expended uses when you finish a long rest.

Your Bardic Inspiration die changes when you reach certain levels in this class. The die becomes a d8 at 5th level, a d10 at 10th level, and a d12 at 15th level."""

    print(feature3)
    dnd_dict.character_dict['features']['bardic_inspiration'] = feature3
    dnd_dict.character_dict['inspiration_die'] = 'd6'


def bard2():
    feature = """Jack of All Trades

Starting at 2nd level, you can add half your proficiency bonus, rounded down, to any ability check you make that doesn't already include your proficiency bonus."""

    print(feature)
    dnd_dict.character_dict['features']['jack_of_all_trades'] = feature

    feature2 = """Song of Rest

Beginning at 2nd level, you can use soothing music or oration to help revitalize your wounded allies during a short rest. If you or any friendly creatures who can hear your performance regain hit points at the end of the short rest by spending one or more Hit Dice, each of those creatures regains an extra 1d6 hit points.

The extra Hit Points increase when you reach certain levels in this class: to 1d8 at 9th level, to 1d10 at 13th level, and to 1d12 at 17th level."""

    print(feature2)
    dnd_dict.character_dict['features']['song_of_rest'] = feature

    feature3 = """Magical Inspiration (Optional)

At 2nd level, if a creature has a Bardic Inspiration die from you and casts a spell that restores hit points or deals damage, the creature can roll that die and choose a target affected by the spell. Add the number rolled as a bonus to the hit points regained or the damage dealt. The Bardic Inspiration die is then lost."""

    print(feature3)
    dnd_dict.character_dict['features']['magical_inspiration'] = feature3


def bard3():
    dnd_skills.expertise_choice()

def bardic_versatility():
    while True:
        choice = input("""Select one option:
1) Replace one Expertise feature
2) Replace one cantrip
0) Neither
Enter your selection: """)
        if choice == '1':
            dnd_skills.skill_swap(dnd_dict.character_dict['expertise'])
            dnd_skills.expertise()
            break

        elif choice == '2':
            dnd_skills.cantrip_swap(dnd_magic.bard_cantrip,dnd_dict.character_dict['class_spells']['bard_cantrips'])
            break

        elif choice == '0':
            break

        else:
            print("Error: Invalid Input")
            continue

def bard5():
    feature = """Font of Inspiration

Beginning when you reach 5th level, you regain all of your expended uses of Bardic Inspiration when you finish a short or long rest."""
    print(feature)
    dnd_dict.character_dict['features']['font_of_inspiration'] = feature

def bard6():
    feature = """Countercharm

At 6th level, you gain the ability to use musical notes or words of power to disrupt mind-influencing effects. As an action, you can start a performance that lasts until the end of your next turn. During that time, you and any friendly creatures within 30 feet of you have advantage on saving throws against being frightened or charmed. A creature must be able to hear you to gain this benefit. The performance ends early if you are incapacitated or silenced or if you voluntarily end it (no action required)."""
    print(feature)
    dnd_dict.character_dict['features']['countercharm'] = feature

def bard10():
    feature = """Magical Secrets

By 10th level, you have plundered magical knowledge from a wide spectrum of disciplines. Choose two spells from any classes, including this one. A spell you choose must be of a level you can cast, as shown on the Bard table, or a cantrip.

The chosen spells count as bard spells for you and are included in the number in the Spells Known column of the Bard table.

You learn two additional spells from any classes at 14th level and again at 18th level."""
    print(feature)
    dnd_dict.character_dict['features']['magical_secrets'] = feature
    dnd_magic.magical_secrets10()




def bard14():
    dnd_magic.magical_secrets14()




def bard18():
    dnd_magic.magical_secrets18()



def bard20():
    feature = """Superior Inspiration

At 20th level, when you roll initiative and have no uses of Bardic Inspiration left, you regain one use."""

    print(feature)
    dnd_dict.character_dict['features']['superior_inspiration'] = feature


def lore_bard3():
    y = 1
    for x in range(y,4):
        if y < 4:
            print(f'{y}/3')
            dnd_skills.skill_choice()
            y+=1
            continue
        elif y == 4:
            break


    feature = """Cutting Words

Also at 3rd level, you learn how to use your wit to distract, confuse, and otherwise sap the confidence and competence of others. When a creature that you can see within 60 feet of you makes an attack roll, an ability check, or a damage roll, you can use your reaction to expend one of your uses of Bardic Inspiration, rolling a Bardic Inspiration die and subtracting the number rolled from the creature's roll. You can choose to use this feature after the creature makes its roll, but before the DM determines whether the attack roll or ability check succeeds or fails, or before the creature deals its damage. The creature is immune if it can't hear you or if it's immune to being charmed."""

    print(feature)
    dnd_dict.character_dict['features']['cutting_words'] = feature

def lore_bard6():
    feature = """Additional Magical Secrets

At 6th level, you learn two spells of your choice from any class. A spell you choose must be of a level you can cast, as shown on the Bard table, or a cantrip. The chosen spells count as bard spells for you but don't count against the number of bard spells you know."""
    print(feature)
    dnd_dict.character_dict['features']['additional_magical_secrets'] = feature
    dnd_magic.magical_secrets6()


def lore_bard14():
    feature = """Peerless Skill

Starting at 14th level, when you make an ability check, you can expend one use of Bardic Inspiration. Roll a Bardic Inspiration die and add the number rolled to your ability check. You can choose to do so after you roll the die for the ability check, but before the DM tells you whether you succeed or fail."""

    print(feature)
    dnd_dict.character_dict['features']['peerless_skill'] = feature


def valor_bard3():
    feature1 = """Bonus Proficiencies

When you join the College of Valor at 3rd level, you gain proficiency with medium armor, shields, and martial weapons."""
    print(feature1)

    armor_prof = {'medium_armor':'Medium Armor','shields':'Shields'}
    dnd_dict.character_dict['Armor_Prof'].update(armor_prof)
    dnd_dict.character_dict['Weapon_Prof']['martial_weapons'] = 'Martial Weapons'

    feature2 = """Combat Inspiration

Also at 3rd level, you learn to inspire others in battle. A creature that has a Bardic Inspiration die from you can roll that die and add the number rolled to a weapon damage roll it just made. Alternatively, when an attack roll is made against the creature, it can use its reaction to roll the Bardic Inspiration die and add the number rolled to its AC against that attack, after seeing the roll but before knowing whether it hits or misses."""

    print(feature2)
    dnd_dict.character_dict['features']['combat_inspiration'] = feature2

def valor_bard6():
    extra_attack()

def valor_bard14():
    feature = """Battle Magic

At 14th level, you have mastered the art of weaving spellcasting and weapon use into a single harmonious act. When you use your action to cast a bard spell, you can make one weapon attack as a bonus action."""
    print(feature)
    dnd_dict.character_dict['features']['battle_magic'] = feature




def cleric2():
    feature = """Channel Divinity

At 2nd level, you gain the ability to channel divine energy directly from your deity, using that energy to fuel magical effects. You start with two such effects: Turn Undead and an effect determined by your domain. Some domains grant you additional effects as you advance in levels, as noted in the domain description.

When you use your Channel Divinity, you choose which effect to create. You must then finish a short or long rest to use your Channel Divinity again.

Some Channel Divinity effects require saving throws. When you use such an effect from this class, the DC equals your cleric spell save DC.

Beginning at 6th level, you can use your Channel Divinity twice between rests, and beginning at 18th level, you can use it three times between rests. When you finish a short or long rest, you regain your expended uses."""

    feature2 = """Channel Divinity: Turn Undead

As an action, you present your holy symbol and speak a prayer censuring the undead. Each undead that can see or hear you within 30 feet of you must make a Wisdom saving throw. If the creature fails its saving throw, it is turned for 1 minute or until it takes any damage.

A turned creature must spend its turns trying to move as far away from you as it can, and it can't willingly move to a space within 30 feet of you. It also can't take reactions. For its action, it can use only the Dash action or try to escape from an effect that prevents it from moving. If there's nowhere to move, the creature can use the Dodge action."""

    feature3 = """Harness Divine Power (Optional)

At 2nd level, you can expend a use of your Channel Divinity to fuel your spells. As a bonus action, you touch your holy symbol, utter a prayer, and regain one expended spell slot, the level of which can be no higher than half your proficiency bonus (rounded up). The number of times you can use this feature is based on the level you've reached in this class: 2nd level, once; 6th level, twice; and 18th level, thrice. You regain all expended uses when you finish a long rest."""

    print(feature)
    dnd_dict.character_dict['features']['channel_divinity_cleric'] = feature

    print(feature2)
    dnd_dict.character_dict['features']['turn_undead'] = feature2

    print(feature3)
    dnd_dict.character_dict['features']['harness_divine_power'] = feature3


def cantrip_versatility(spell_list,full_dict,class_dict):
    while True:
        choice = input("""Do you want to replace one Cleric cantrip?
1) Yes
2) No
Enter your selection: """)
        if choice == '1':
#            dnd_skills.spell_swap(class_dict,full_dict,class_dict)
            dnd_skills.maneuver_swap(class_dict,full_dict)
            dnd_skills.spell_add(spell_list,full_dict,class_dict)
            break

        elif choice == '2':
            break

        else:
            print("Error: Invalid Selection")
            continue



def cleric5():
    feature = """Destroy Undead

Starting at 5th level, when an undead fails its saving throw against your Turn Undead feature, the creature is instantly destroyed if its challenge rating is at or below a certain threshold, as shown in the Cleric table above."""

    print(feature)
    dnd_dict.character_dict['features']['destroy_undead'] = feature

def cleric10():
    feature = """Divine Intervention

Beginning at 10th level, you can call on your deity to intervene on your behalf when your need is great.

Imploring your deity's aid requires you to use your action. Describe the assistance you seek, and roll percentile dice. If you roll a number equal to or lower than your cleric level, your deity intervenes. The DM chooses the nature of the intervention; the effect of any cleric spell or cleric domain spell would be appropriate. If your deity intervenes, you can't use this feature again for 7 days. Otherwise, you can use it again after you finish a long rest.

At 20th level, your call for intervention succeeds automatically, no roll required."""

    print(feature)
    dnd_dict.character_dict['features']['divine_intervention'] = feature







def knowledge_cleric1():
    feature = """Blessings of Knowledge

At 1st level, you learn two languages of your choice. You also become proficient in your choice of two of the following skills: Arcana, History, Nature, or Religion.

Your proficiency bonus is doubled for any ability check you make that uses either of those skills."""

    feature2 = """Knowledge Domain Spells
Cleric Level 	Spells
1st 	Command, Identify
3rd 	Augury, Suggestion
5th 	Nondetection, Speak with Dead
7th 	Arcane Eye, Confusion
9th 	Legend Lore, Scrying"""

    dnd_dict.character_dict["player_class"]["cleric"]["subclass"] = "Knowledge Domain"
    dnd_dict.character_dict["features"]['blessings_of_knowledge'] = feature
    dnd_dict.character_dict["features"]['knowledge_domain_spells'] = feature2
    print(feature)
    print(feature2)
    dnd_language.double_language()
    added_spells = {'command':'Command','identify':'Identify'}
    dnd_dict.character_dict['spells']['first'].update(added_spells)
    dnd_dict.character_dict['class_spells']['cleric']['first'].update(added_spells)
    dnd_dict.character_dict['special_spells']['first'].update(added_spells)
# Used to double the proficiency of the ability check
    i = 1
    for i in range(i,3):
# If the player is proficient in all of these skills, pass.
        check_prof = dnd_dict.character_dict['expertise']
        if i < 3:
            if 'arcana' in check_prof and 'history' in check_prof and 'nature' in check_prof and 'religion' in check_prof: 
                break
            else:
                skill_list = ['Arcana','History','Nature','Religion']
                print(f'{i}/2')
                dnd_skills.skill_addition(skill_list,check_prof)
                i+=1
                continue
        if i == 3:
                break




def knowledge_cleric2():
    feature = """Channel Divinity: Knowledge of the Ages

Starting at 2nd level, you can use your Channel Divinity to tap into a divine well of knowledge. As an action, you choose one skill or tool. For 10 minutes, you have proficiency with the chosen skill or tool."""
    print(feature)
    dnd_dict.character_dict["features"]['knowledge_of_the_ages'] = feature

def knowledge_cleric3():
    added_spells = {'augury':'Augury','suggestion':'Suggestion'}
    dnd_dict.character_dict['spells']['second'].update(added_spells)
    dnd_dict.character_dict['class_spells']['cleric']['second'].update(added_spells)
    dnd_dict.character_dict['special_spells']['second'].update(added_spells)

def knowledge_cleric5():
    added_spells = {'nondetection':'Nondetection','speak_with_dead':'Speak with Dead'}
    dnd_dict.character_dict['spells']['third'].update(added_spells)
    dnd_dict.character_dict['class_spells']['cleric']['third'].update(added_spells)
    dnd_dict.character_dict['special_spells']['third'].update(added_spells)

def knowledge_cleric6():
    feature = """Channel Divinity: Read Thoughts

At 6th level, you can use your Channel Divinity to read a creature's thoughts. You can then use your access to the creature's mind to command it.

As an action, choose one creature that you can see within 60 feet of you. That creature must make a Wisdom saving throw. If the creature succeeds on the saving throw, you can't use this feature on it again until you finish a long rest.

If the creature fails its save, you can read its surface thoughts (those foremost in its mind, reflecting its current emotions and what it is actively thinking about) when it is within 60 feet of you. This effect lasts for 1 minute.

During that time, you can use your action to end this effect and cast the Suggestion spell on the creature without expending a spell slot. The target automatically fails its saving throw against the spell."""

    print(feature)
    dnd_dict.character_dict["features"]['channel_divinity_read_thoughts'] = feature

def knowledge_cleric8():
    while True:
        choice = input("""Do you want the Potent Spellcasting feature or Blessed Strikes feature?
1) Potent Spellcasting
2) Blessed Strikes
Enter your selection: """)
        if choice == '1':
            feature = """Potent Spellcasting

Starting at 8th level, you add your Wisdom modifier to the damage you deal with any cleric cantrip."""
            dnd_dict.character_dict["features"]['potent_spellcasting'] = feature
            break

        elif choice == '2':
            feature = """Blessed Strikes (Optional)

Replaces the Divine Strike or Potent Spellcasting feature

When you reach 8th level, you are blessed with divine might in battle. When a creature takes damage from one of your cantrips or weapon attacks, you can also deal 1d8 radiant damage to that creature. Once you deal this damage, you can't use this feature again until the start of your next turn."""
            dnd_dict.character_dict["features"]['blessed_strikes'] = feature
            break
        
        else:
            print("Error: Invalid Input")
            continue

def knowledge_cleric17():
    feature = """Visions of the Past

Starting at 17th level, you can call up visions of the past that relate to an object you hold or your immediate surroundings. You spend at least 1 minute in meditation and prayer, then receive dreamlike, shadowy glimpses of recent events. You can meditate in this way for a number of minutes equal to your Wisdom score and must maintain concentration during that time, as if you were casting a spell.

Once you use this feature, you can't use it again until you finish a short or long rest.

Object Reading. Holding an object as you meditate, you can see visions of the object's previous owner. After meditating for 1 minute, you learn how the owner acquired and lost the object, as well as the most recent significant event involving the object and that owner. If the object was owned by another creature in the recent past (within a number of days equal to your Wisdom score), you can spend 1 additional minute for each owner to learn the same information about that creature.

Area Reading. As you meditate, you see visions of recent events in your immediate vicinity (a room, street, tunnel, clearing, or the like, up to a 50-foot cube), going back a number of days equal to your Wisdom score. For each minute you meditate, you learn about one significant event, beginning with the most recent. Significant events typically involve powerful emotions, such as battles and betrayals, marriages and murders, births and funerals. However, they might also include more mundane events that are nevertheless important in your current situation."""

    print(feature)
    dnd_dict.character_dict["features"]['visions_of_the_past'] = feature


def knowledge_cleric7():
    added_spells = {'arcane_eye':'Arcane Eye','confusion':'Confusion'}
    dnd_dict.character_dict['spells']['fourth'].update(added_spells)
    dnd_dict.character_dict['class_spells']['cleric']['fourth'].update(added_spells)
    dnd_dict.character_dict['special_spells']['fourth'].update(added_spells)


def knowledge_cleric9():
    added_spells = {'legend_lore':'Legend Lore','scrying':'Scrying'}
    dnd_dict.character_dict['spells']['fifth'].update(added_spells)
    dnd_dict.character_dict['class_spells']['cleric']['fifth'].update(added_spells)
    dnd_dict.character_dict['special_spells']['fifth'].update(added_spells)







def life_cleric1():
    feature = """Bonus Proficiency

When you choose this domain at 1st level, you gain proficiency with heavy armor.
Disciple of Life

Also starting at 1st level, your healing spells are more effective. Whenever you use a spell of 1st level or higher to restore hit points to a creature, the creature regains additional hit points equal to 2 + the spell's level."""
    feature2 = """Life Domain Spells
Cleric Level 	Spells
1st 	Bless, Cure Wounds
3rd 	Lesser Restoration, Spiritual Weapon
5th 	Beacon of Hope, Revivify
7th 	Death Ward, Guardian of Faith
9th 	Mass Cure Wounds, Raise Dead"""

    added_spells = {'bless':'Bless','cure_wounds':'Cure Wounds'}
    dnd_dict.character_dict['spells']['first'].update(added_spells)
    dnd_dict.character_dict['class_spells']['cleric']['first'].update(added_spells)
    dnd_dict.character_dict['special_spells']['first'].update(added_spells)
    dnd_dict.character_dict["player_class"]["cleric"]["subclass"] = "Life Domain"
    print(feature)
    dnd_dict.character_dict["features"]['disciple_of_life'] = feature
    dnd_dict.character_dict["Armor_Prof"]['heavy_armor'] = 'Heavy Armor'
    print(feature2)
    dnd_dict.character_dict["features"]['life_cleric_spells'] = feature2


def life_cleric2():
    feature = """Channel Divinity: Preserve Life

Starting at 2nd level, you can use your Channel Divinity to heal the badly injured.

As an action, you present your holy symbol and evoke healing energy that can restore a number of hit points equal to five times your cleric level. Choose any creatures within 30 feet of you, and divide those hit points among them. This feature can restore a creature to no more than half of its hit point maximum. You can't use this feature on an undead or a construct."""

    print(feature)
    dnd_dict.character_dict["features"]['preserve_life'] = feature

def life_cleric3():
    added_spells = {'lesser_restoration':'Lesser Restoration','spiritual_weapon':'Spiritual Weapon'}
    dnd_dict.character_dict['spells']['second'].update(added_spells)
    dnd_dict.character_dict['class_spells']['cleric']['second'].update(added_spells)
    dnd_dict.character_dict['special_spells']['second'].update(added_spells)

def life_cleric5():
    added_spells = {'beacon_of_hope':'Beacon of Hope','revivify':'Revivify'}
    dnd_dict.character_dict['spells']['third'].update(added_spells)
    dnd_dict.character_dict['class_spells']['cleric']['third'].update(added_spells)
    dnd_dict.character_dict['special_spells']['third'].update(added_spells)


def life_cleric6():
    feature = """Blessed Healer

Beginning at 6th level, the healing spells you cast on others heal you as well. When you cast a spell of 1st level or higher that restores hit points to a creature other than you, you regain hit points equal to 2 + the spell's level."""
    print(feature)
    dnd_dict.character_dict["features"]['blessed_healer'] = feature


def life_cleric7():
    added_spells = {'death_ward':'Death Ward','guardian_of_faith':'Guardian of Faith'}
    dnd_dict.character_dict['spells']['fourth'].update(added_spells)
    dnd_dict.character_dict['class_spells']['cleric']['fourth'].update(added_spells)
    dnd_dict.character_dict['special_spells']['fourth'].update(added_spells)


def life_cleric8():
    while True:
        choice = input("""Do you want the Divine Strike feature or Blessed Strikes feature?
1) Divine Strike
2) Blessed Strikes
Enter your selection: """)
        if choice == '1':
            feature = """Divine Strike

At 8th level, you gain the ability to infuse your weapon strikes with divine energy. Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra 1d8 radiant damage to the target. When you reach 14th level, the extra damage increases to 2d8."""
            dnd_dict.character_dict["features"]['divine_strike'] = feature
            break

        elif choice == '2':
            feature = """Blessed Strikes (Optional)

Replaces the Divine Strike or Potent Spellcasting feature

When you reach 8th level, you are blessed with divine might in battle. When a creature takes damage from one of your cantrips or weapon attacks, you can also deal 1d8 radiant damage to that creature. Once you deal this damage, you can't use this feature again until the start of your next turn."""
            dnd_dict.character_dict["features"]['blessed_strikes'] = feature
            break
        
        else:
            print("Error: Invalid Input")
            continue


def life_cleric9():
    added_spells = {'mass_cure_wounds':'Mass Cure Wounds','raise_dead':'Raise Dead'}
    dnd_dict.character_dict['spells']['fifth'].update(added_spells)
    dnd_dict.character_dict['class_spells']['cleric']['fifth'].update(added_spells)
    dnd_dict.character_dict['special_spells']['fifth'].update(added_spells)


def life_cleric17():
    feature = """Supreme Healing

Starting at 17th level, when you would normally roll one or more dice to restore hit points with a spell, you instead use the highest number possible for each die. For example, instead of restoring 2d6 hit points to a creature, you restore 12."""
    print(feature)
    dnd_dict.character_dict["features"]['supreme_healing'] = feature


def light_cleric1():
    feature = """Bonus Cantrip

When you choose this domain at 1st level, you gain the Light cantrip if you don't already know it.
Warding Flare

Also at 1st level, you can interpose divine light between yourself and an attacking enemy. When you are attacked by a creature within 30 feet of you that you can see, you can use your reaction to impose disadvantage on the attack roll, causing light to flare before the attacker before it hits or misses. An attacker that can't be blinded is immune to this feature.

You can use this feature a number of times equal to your Wisdom modifier (a minimum of once). You regain all expended uses when you finish a long rest."""

    feature2 = """Light Domain Spells
Cleric Level 	Spells
1st 	Burning Hands, Faerie Fire
3rd 	Flaming Sphere, Scorching Ray
5th 	Daylight, Fireball
7th 	Guardian of Faith, Wall of Fire
9th 	Flame Strike, Scrying"""

    added_spells = {'burning_hands':'Burning Hands', 'faerie_fire':'Faerie Fire'}
    dnd_dict.character_dict['spells']['first'].update(added_spells)
    dnd_dict.character_dict['class_spells']['cleric']['first'].update(added_spells)
    dnd_dict.character_dict['special_spells']['first'].update(added_spells)
    dnd_dict.character_dict["player_class"]["cleric"]["subclass"] = "Light Domain"
    dnd_dict.character_dict['spells']['light']= 'Light'
    print(feature)
    dnd_dict.character_dict["features"]['warding_flare'] = feature
    print(feature2)
    dnd_dict.character_dict["features"]['light_domain_spells'] = feature2


def light_cleric2():
    feature = """Channel Divinity: Radiance of the Dawn

Starting at 2nd level, you can use your Channel Divinity to harness sunlight, banishing darkness and dealing radiant damage to your foes.

As an action, you present your holy symbol, and any magical darkness within 30 feet of you is dispelled. Additionally, each hostile creature within 30 feet of you must make a Constitution saving throw. A creature takes radiant damage equal to 2d10 + your cleric level on a failed saving throw, and half as much damage on a successful one. A creature that has total cover from you is not affected."""
    print(feature)
    dnd_dict.character_dict["features"]['radiance_of_the_dawn'] = feature

def light_cleric3():
    added_spells = {'flaming_sphere':'Flaming Sphere','scorching_ray':'Scorching Ray'}
    dnd_dict.character_dict['spells']['second'].update(added_spells)
    dnd_dict.character_dict['class_spells']['cleric']['second'].update(added_spells)
    dnd_dict.character_dict['special_spells']['second'].update(added_spells)

def light_cleric5():
    added_spells = {'daylight':'Daylight','fireball':'Fireball'}
    dnd_dict.character_dict['spells']['third'].update(added_spells)
    dnd_dict.character_dict['class_spells']['cleric']['third'].update(added_spells)
    dnd_dict.character_dict['special_spells']['third'].update(added_spells)

def light_cleric6():
    feature = """Improved Flare

Starting at 6th level, you can also use your Warding Flare feature when a creature that you can see within 30 feet of you attacks a creature other than you."""
    print(feature)
    dnd_dict.character_dict["features"]['improved_flare'] = feature

def light_cleric7():
    added_spells = {'guardian_of_faith':'Guardian of Faith','wall_of_fire':'Wall of Fire'}
    dnd_dict.character_dict['spells']['fourth'].update(added_spells)
    dnd_dict.character_dict['class_spells']['cleric']['fourth'].update(added_spells)
    dnd_dict.character_dict['special_spells']['fourth'].update(added_spells)

def light_cleric8():
    while True:
        choice = input("""Do you want the Potent Spellcasting feature or Blessed Strikes feature?
1) Potent Spellcasting
2) Blessed Strikes
Enter your selection: """)
        if choice == '1':
            feature = """Potent Spellcasting

Starting at 8th level, you add your Wisdom modifier to the damage you deal with any cleric cantrip."""
            dnd_dict.character_dict["features"]['potent_spellcasting'] = feature
            break

        elif choice == '2':
            feature = """Blessed Strikes (Optional)

Replaces the Divine Strike or Potent Spellcasting feature

When you reach 8th level, you are blessed with divine might in battle. When a creature takes damage from one of your cantrips or weapon attacks, you can also deal 1d8 radiant damage to that creature. Once you deal this damage, you can't use this feature again until the start of your next turn."""
            dnd_dict.character_dict["features"]['blessed_strikes'] = feature
            break
        
        else:
            print("Error: Invalid Input")
            continue


def light_cleric9():
    added_spells = {'flame_strike':'Flame Strike','scrying':'Scrying'}
    dnd_dict.character_dict['spells']['fifth'].update(added_spells)
    dnd_dict.character_dict['class_spells']['cleric']['fifth'].update(added_spells)
    dnd_dict.character_dict['special_spells']['fifth'].update(added_spells)

def light_cleric17():
    feature = """Corona of Light

Starting at 17th level, you can use your action to activate an aura of sunlight that lasts for 1 minute or until you dismiss it using another action. You emit bright light in a 60-foot radius and dim light 30 feet beyond that. Your enemies in the bright light have disadvantage on saving throws against any spell that deals fire or radiant damage."""
    print(feature)
    dnd_dict.character_dict["features"]['corona_of_light'] = feature


def nature_cleric1():
    feature = """Acolyte of Nature

At 1st level, you learn one cantrip of your choice from the druid spell list. You also gain proficiency in one of the following skills of your choice: Animal Handling, Nature, or Survival.
Bonus Proficiency

Also at 1st level, you gain proficiency with heavy armor."""
    feature2 = """Nature Domain Spells
Cleric Level 	Spells
1st 	Animal Friendship, Speak with Animals
3rd 	Barkskin, Spike Growth
5th 	Plant Growth, Wind Wall
7th 	Dominate Beast, Grasping Vine
9th 	Insect Plague, Tree Stride"""
    added_spells = {'animal_friendship':'Animal Friendship', 'speak_with_animals':'Speak with Animals'}
    dnd_dict.character_dict['spells']['first'].update(added_spells)
    dnd_dict.character_dict['class_spells']['cleric']['first'].update(added_spells)
    dnd_dict.character_dict['special_spells']['first'].update(added_spells)
    dnd_dict.character_dict["player_class"]["cleric"]["subclass"] = "Nature Domain"
    print(feature)
    dnd_dict.character_dict["features"]['acolyte_of_nature'] = feature
    print(feature2)
    dnd_dict.character_dict["features"]['nature_domain_spells'] = feature2
    dnd_dict.character_dict['Armor_Prof']['heavy_armor'] = 'Heavy Armor'

# If the player is proficient in all of these skills, pass.
    check_prof = dnd_dict.character_dict['skill_prof']
    if 'animal_handling' in check_prof and 'nature' in skill_prof and 'survival' in skill_prof:
        pass
    else:
        skill_list = ['Animal Handling','Nature','Survival']
        dnd_skills.skill_addition(skill_list,check_prof)


def nature_cleric2():
    feature = """Channel Divinity: Charm Animals and Plants

Starting at 2nd level, you can use your Channel Divinity to charm animals and plants.

As an action, you present your holy symbol and invoke the name of your deity. Each beast or plant creature that can see you within 30 feet of you must make a Wisdom saving throw. If the creature fails its saving throw, it is charmed by you for 1 minute or until it takes damage. While it is charmed by you, it is friendly to you and other creatures you designate."""
    print(feature)
    dnd_dict.character_dict["features"]['charm_animals_and_plants'] = feature


def nature_cleric3():
    added_spells = {'barkskin':'Barkskin','spike_growth':'Spike Growth'}
    dnd_dict.character_dict['spells']['second'].update(added_spells)
    dnd_dict.character_dict['class_spells']['cleric']['second'].update(added_spells)
    dnd_dict.character_dict['special_spells']['second'].update(added_spells)


def nature_cleric5():
    added_spells = {'plant_growth':'Plant Growth','wind_wall':'Wind Wall'}
    dnd_dict.character_dict['spells']['third'].update(added_spells)
    dnd_dict.character_dict['class_spells']['cleric']['third'].update(added_spells)
    dnd_dict.character_dict['special_spells']['third'].update(added_spells)

def nature_cleric6():
    feature = """Dampen Elements

Starting at 6th level, when you or a creature within 30 feet of you takes acid, cold, fire, lightning, or thunder damage, you can use your reaction to grant resistance to the creature against that instance of the damage."""
    print(feature)
    dnd_dict.character_dict["features"]['dampen_elements'] = feature

def nature_cleric7():
    added_spells = {'dominate_beast':'Dominate Beast','grasping_vine':'Grasping Vine'}
    dnd_dict.character_dict['spells']['fourth'].update(added_spells)
    dnd_dict.character_dict['class_spells']['cleric']['fourth'].update(added_spells)
    dnd_dict.character_dict['special_spells']['fourth'].update(added_spells)

def nature_cleric8():
    while True:
        choice = input("""Do you want the Divine Strike feature or Blessed Strikes feature?
1) Divine Strike
2) Blessed Strikes
Enter your selection: """)
        if choice == '1':
            feature = """Divine Strike

At 8th level, you gain the ability to infuse your weapon strikes with divine energy. Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra 1d8 cold, fire, or lightning damage (your choice) to the target. When you reach 14th level, the extra damage increases to 2d8."""
            dnd_dict.character_dict["features"]['divine_strike'] = feature
            break

        elif choice == '2':
            feature = """Blessed Strikes (Optional)

Replaces the Divine Strike or Potent Spellcasting feature

When you reach 8th level, you are blessed with divine might in battle. When a creature takes damage from one of your cantrips or weapon attacks, you can also deal 1d8 radiant damage to that creature. Once you deal this damage, you can't use this feature again until the start of your next turn."""
            dnd_dict.character_dict["features"]['blessed_strikes'] = feature
            break
        
        else:
            print("Error: Invalid Input")
            continue

def nature_cleric9():
    added_spells = {'insect_plague':'Insect Plague','tree_stride':'Tree Stride'}
    dnd_dict.character_dict['spells']['fifth'].update(added_spells)
    dnd_dict.character_dict['class_spells']['cleric']['fifth'].update(added_spells)
    dnd_dict.character_dict['special_spells']['fifth'].update(added_spells)

def nature_cleric17():
    feature = """Master of Nature

At 17th level, you gain the ability to command animals and plant creatures. While creatures are charmed by your Charm Animals and Plants feature, you can take a bonus action on your turn to verbally command what each of those creatures will do on its next turn."""
    print(feature)
    dnd_dict.character_dict["features"]['master_of_nature'] = feature

def tempest_cleric1():
    feature = """Bonus Proficiencies

At 1st level, you gain proficiency with martial weapons and heavy armor.
Wrath of the Storm

Also at 1st level, you can thunderously rebuke attackers. When a creature within 5 feet of you that you can see hits you with an attack, you can use your reaction to cause the creature to make a Dexterity saving throw. The creature takes 2d8 lightning or thunder damage (your choice) on a failed saving throw, and half as much damage on a successful one.

You can use this feature a number of times equal to your Wisdom modifier (a minimum of once). You regain all expended uses when you finish a long rest."""
    feature2 = """Tempest Domain Spells
Cleric Level 	Spells
1st 	Fog Cloud, Thunderwave
3rd 	Gust of Wind, Shatter
5th 	Call Lightning, Sleet Storm
7th 	Control Water, Ice Storm
9th 	Destructive Wave, Insect Plague"""
    added_spells = {'fog_cloud':'Fog Cloud', 'thunderwave':'Thunderwave'}
    dnd_dict.character_dict['spells']['first'].update(added_spells)
    dnd_dict.character_dict['class_spells']['cleric']['first'].update(added_spells)
    dnd_dict.character_dict['special_spells']['first'].update(added_spells)
    dnd_dict.character_dict["player_class"]["cleric"]["subclass"] = "Tempest Domain"
    dnd_dict.character_dict["Weapon_Prof"]['martial_weapons'] = 'Martial Weapons'
    dnd_dict.character_dict['Armor_Prof']['heavy_armor'] = 'Heavy Armor'
    print(feature)
    dnd_dict.character_dict["features"]['wrath_of_the_storm'] = feature
    print(feature2)
    dnd_dict.character_dict["features"]['tempest_domain_spells'] = feature2

def tempest_cleric2():
    feature = """Channel Divinity: Destructive Wrath

Starting at 2nd level, you can use your Channel Divinity to wield the power of the storm with unchecked ferocity.

When you roll lightning or thunder damage, you can use your Channel Divinity to deal maximum damage, instead of rolling."""
    print(feature)
    dnd_dict.character_dict["features"]['destructive_wrath'] = feature

def tempest_cleric3():
    added_spells = {'gust_of_wind':'Gust of Wind','shatter':'Shatter'}
    dnd_dict.character_dict['spells']['second'].update(added_spells)
    dnd_dict.character_dict['class_spells']['cleric']['second'].update(added_spells)
    dnd_dict.character_dict['special_spells']['second'].update(added_spells)


def tempest_cleric5():
    added_spells = {'call_lightning':'Call Lightning','sleet_storm':'Sleet Storm'}
    dnd_dict.character_dict['spells']['third'].update(added_spells)
    dnd_dict.character_dict['class_spells']['cleric']['third'].update(added_spells)
    dnd_dict.character_dict['special_spells']['third'].update(added_spells)

def tempest_cleric6():
    feature = """Thunderous Strike

At 6th level, when you deal lightning damage to a Large or smaller creature, you can also push it up to 10 feet away from you."""
    print(feature)
    dnd_dict.character_dict["features"]['thunderous_strike'] = feature

def tempest_cleric7():
    added_spells = {'control_water':'Control Water','ice_storm':'Ice Storm'}
    dnd_dict.character_dict['spells']['fourth'].update(added_spells)
    dnd_dict.character_dict['class_spells']['cleric']['fourth'].update(added_spells)
    dnd_dict.character_dict['special_spells']['fourth'].update(added_spells)

def tempest_cleric8():
    while True:
        choice = input("""Do you want the Divine Strike feature or Blessed Strikes feature?
1) Divine Strike
2) Blessed Strikes
Enter your selection: """)
        if choice == '1':
            feature = """Divine Strike

At 8th level, you gain the ability to infuse your weapon strikes with divine energy. Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra 1d8 thunder damage to the target. When you reach 14th level, the extra damage increases to 2d8."""
            dnd_dict.character_dict["features"]['divine_strike'] = feature
            break

        elif choice == '2':
            feature = """Blessed Strikes (Optional)

Replaces the Divine Strike or Potent Spellcasting feature

When you reach 8th level, you are blessed with divine might in battle. When a creature takes damage from one of your cantrips or weapon attacks, you can also deal 1d8 radiant damage to that creature. Once you deal this damage, you can't use this feature again until the start of your next turn."""
            dnd_dict.character_dict["features"]['blessed_strikes'] = feature
            break
        
        else:
            print("Error: Invalid Input")
            continue


def tempest_cleric9():
    added_spells = {'destructive_wave':'Destructive Wave','insect_plague':'Insect Plague'}
    dnd_dict.character_dict['spells']['fifth'].update(added_spells)
    dnd_dict.character_dict['class_spells']['cleric']['fifth'].update(added_spells)
    dnd_dict.character_dict['special_spells']['fifth'].update(added_spells)

def tempest_cleric17():
    feature = """Stormborn

At 17th level, you have a flying speed equal to your current walking speed whenever you are not underground or indoors."""
    print(feature)
    dnd_dict.character_dict["features"]['stormborn'] = feature

def trickery_cleric1():
    feature = """Blessing of the Trickster

Starting when you choose this domain at 1st level, you can use your action to touch a willing creature other than yourself to give it advantage on Dexterity (Stealth) checks. This blessing lasts for 1 hour or until you use this feature again."""
    feature2 = """Trickery Domain Spells
Cleric Level 	Spells
1st 	Charm Person, Disguise Self
3rd 	Mirror Image, Pass without Trace
5th 	Blink, Dispel Magic
7th 	Dimension Door, Polymorph
9th 	Dominate Person, Modify Memory"""
    added_spells = {'charm_person':'Charm Person', 'diguise_self':'Disguise Self'}
    dnd_dict.character_dict['spells']['first'].update(added_spells)
    dnd_dict.character_dict['class_spells']['cleric']['first'].update(added_spells)
    dnd_dict.character_dict['special_spells']['first'].update(added_spells)
    dnd_dict.character_dict["player_class"]["cleric"]["subclass"] = "Trickery Domain"
    print(feature)
    dnd_dict.character_dict["features"]['blessing_of_the_trickster'] = feature
    print(feature2)
    dnd_dict.character_dict["features"]['trickery_domain_spells'] = feature

def trickery_cleric2():
    feature = """Channel Divinity: Invoke Duplicity

Starting at 2nd level, you can use your Channel Divinity to create an illusory duplicate of yourself.

As an action, you create a perfect illusion of yourself that lasts for 1 minute, or until you lose your concentration (as if you were concentrating on a spell). The illusion appears in an unoccupied space that you can see within 30 feet of you. As a bonus action on your turn, you can move the illusion up to 30 feet to a space you can see, but it must remain within 120 feet of you.

For the duration, you can cast spells as though you were in the illusion's space, but you must use your own senses. Additionally, when both you and your illusion are within 5 feet of a creature that can see the illusion, you have advantage on attack rolls against that creature, given how distracting the illusion is to the target."""
    print(feature)
    dnd_dict.character_dict["features"]['invoke_duplicity'] = feature


def trickery_cleric3():
    added_spells = {'mirror_image':'Mirror Image','pass_without_trace':'Pass without Trace'}
    dnd_dict.character_dict['spells']['second'].update(added_spells)
    dnd_dict.character_dict['class_spells']['cleric']['second'].update(added_spells)
    dnd_dict.character_dict['special_spells']['second'].update(added_spells)


def trickery_cleric5():
    added_spells = {'blink':'Blink','dispel_magic':'Dispel Magic'}
    dnd_dict.character_dict['spells']['third'].update(added_spells)
    dnd_dict.character_dict['class_spells']['cleric']['third'].update(added_spells)
    dnd_dict.character_dict['special_spells']['third'].update(added_spells)

def trickery_cleric6():
    feature = """Channel Divinity: Cloak of Shadows

Starting at 6th level, you can use your Channel Divinity to vanish.

As an action, you become invisible until the end of your next turn. You become visible if you attack or cast a spell."""
    print(feature)
    dnd_dict.character_dict["features"]['cloak_of_shadows'] = feature

def trickery_cleric7():
    added_spells = {'dimension_door':'Dimension Door','polymorph':'Polymorph'}
    dnd_dict.character_dict['spells']['fourth'].update(added_spells)
    dnd_dict.character_dict['class_spells']['cleric']['fourth'].update(added_spells)
    dnd_dict.character_dict['special_spells']['fourth'].update(added_spells)

def trickery_cleric8():
    while True:
        choice = input("""Do you want the Divine Strike feature or Blessed Strikes feature?
1) Divine Strike
2) Blessed Strikes
Enter your selection: """)
        if choice == '1':
            feature = """Divine Strike

At 8th level, you gain the ability to infuse your weapon strikes with divine energy. Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra 1d8 poison damage to the target. When you reach 14th level, the extra damage increases to 2d8."""
            dnd_dict.character_dict["features"]['divine_strike'] = feature
            break

        elif choice == '2':
            feature = """Blessed Strikes (Optional)

Replaces the Divine Strike or Potent Spellcasting feature

When you reach 8th level, you are blessed with divine might in battle. When a creature takes damage from one of your cantrips or weapon attacks, you can also deal 1d8 radiant damage to that creature. Once you deal this damage, you can't use this feature again until the start of your next turn."""
            dnd_dict.character_dict["features"]['blessed_strikes'] = feature
            break
        
        else:
            print("Error: Invalid Input")
            continue

def trickery_cleric9():
    added_spells = {'dominate_person':'Dominate Person','modify_memory':'Modify Memory'}
    dnd_dict.character_dict['spells']['fifth'].update(added_spells)
    dnd_dict.character_dict['class_spells']['cleric']['fifth'].update(added_spells)
    dnd_dict.character_dict['special_spells']['fifth'].update(added_spells)

def trickery_cleric17():
    feature = """Improved Duplicity

At 17th level, you can create up to four duplicates of yourself, instead of one, when you use Invoke Duplicity. As a bonus action on your turn, you can move any number of them up to 30 feet, to a maximum range of 120 feet."""
    print(feature)
    dnd_dict.character_dict["features"]['improved_duplicity'] = feature


def war_cleric1():
    feature = """Bonus Proficiency

At 1st level, you gain proficiency with martial weapons and heavy armor.
War Priest

From 1st level, your god delivers bolts of inspiration to you while you are engaged in battle. When you use the Attack action, you can make one weapon attack as a bonus action.

You can use this feature a number of times equal to your Wisdom modifier (a minimum of once). You regain all expended uses when you finish a long rest."""
    feature2 = """War Domain Spells
Cleric Level 	Spells
1st 	Divine Favor, Shield of Faith
3rd 	Magic Weapon, Spiritual Weapon
5th 	Crusader's Mantle, Spirit Guardians
7th 	Freedom of Movement, Stoneskin
9th 	Flame Strike, Hold Monster"""
    added_spells = {'divine_favor':'Divine Favor', 'shield_of_faith':'Shield of Faith'}
    dnd_dict.character_dict['spells']['first'].update(added_spells)
    dnd_dict.character_dict['class_spells']['cleric']['first'].update(added_spells)
    dnd_dict.character_dict['special_spells']['first'].update(added_spells)
    dnd_dict.character_dict["player_class"]["cleric"]["subclass"] = "War Domain"
    armor_prof = ['Heavy Armor']
    weapon_prof = ['Martial Weapons']
    dnd_dict.character_dict['Weapon_Prof']['martial_weapons'] = 'Martial Weapons'
    dnd_dict.character_dict['Armor_Prof']['heavy_armor'] = 'Heavy Armor'
    print(feature)
    dnd_dict.character_dict["features"]['war_priest'] = feature
    print(feature2)
    dnd_dict.character_dict["features"]['war_domain_spells'] = feature2


def war_cleric2():
    feature = """Channel Divinity: Guided Strike

Starting at 2nd level, you can use your Channel Divinity to strike with supernatural accuracy. When you make an attack roll, you can use your Channel Divinity to gain a +10 bonus to the roll. You make this choice after you see the roll, but before the DM says whether the attack hits or misses."""
    print(feature)
    dnd_dict.character_dict["features"]['guided_strike'] = feature


def war_cleric3():
    added_spells = {'magic_weapon':'Magic Weapon','spiritual_weapon':'Spiritual Weapon'}
    dnd_dict.character_dict['spells']['second'].update(added_spells)
    dnd_dict.character_dict['class_spells']['cleric']['second'].update(added_spells)
    dnd_dict.character_dict['special_spells']['second'].update(added_spells)

def war_cleric5():
    added_spells = {'crusader\'s_mantle':'Crusader\'s Mantle','spirit_guardians':'Spirit Guardians'}
    dnd_dict.character_dict['spells']['third'].update(added_spells)
    dnd_dict.character_dict['class_spells']['cleric']['third'].update(added_spells)
    dnd_dict.character_dict['special_spells']['third'].update(added_spells)

def war_cleric6():
    feature = """Channel Divinity: War God's Blessing

At 6th level, when a creature within 30 feet of you makes an attack roll, you can use your reaction to grant that creature a +10 bonus to the roll, using your Channel Divinity. You make this choice after you see the roll, but before the DM says whether the attack hits or misses."""
    print(feature)
    dnd_dict.character_dict["features"]['war_god\'s_blessing'] = feature

def war_cleric7():
    added_spells = {'freedom_of_movement':'Freedom of Movement','stoneskin':'Stoneskin'}
    dnd_dict.character_dict['spells']['fourth'].update(added_spells)
    dnd_dict.character_dict['class_spells']['cleric']['fourth'].update(added_spells)
    dnd_dict.character_dict['special_spells']['fourth'].update(added_spells)

def war_cleric8():
    while True:
        choice = input("""Do you want the Divine Strike feature or Blessed Strikes feature?
1) Divine Strike
2) Blessed Strikes
Enter your selection: """)
        if choice == '1':
            feature = """Divine Strike

At 8th level, you gain the ability to infuse your weapon strikes with divine energy. Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra 1d8 damage of the same type dealt by the weapon to the target. When you reach 14th level, the extra damage increases to 2d8."""
            dnd_dict.character_dict["features"]['divine_strike'] = feature
            break

        elif choice == '2':
            feature = """Blessed Strikes (Optional)

Replaces the Divine Strike or Potent Spellcasting feature

When you reach 8th level, you are blessed with divine might in battle. When a creature takes damage from one of your cantrips or weapon attacks, you can also deal 1d8 radiant damage to that creature. Once you deal this damage, you can't use this feature again until the start of your next turn."""
            dnd_dict.character_dict["features"]['blessed_strikes'] = feature
            break
        
        else:
            print("Error: Invalid Input")
            continue

def war_cleric9():
    added_spells = {'flame_strike':'Flame Strike','hold_monster':'Hold Monster'}
    dnd_dict.character_dict['spells']['fifth'].update(added_spells)
    dnd_dict.character_dict['class_spells']['cleric']['fifth'].update(added_spells)
    dnd_dict.character_dict['special_spells']['fifth'].update(added_spells)


def war_cleric17():
    feature = """Avatar of Battle

At 17th level, you gain resistance to bludgeoning, piercing, and slashing damage from nonmagical attacks."""
    print(feature)
    dnd_dict.character_dict["features"]['avatar_of_battle'] = feature


def druid2():
    feature = """Wild Shape

Starting at 2nd level, you can use your action to magically assume the shape of a beast that you have seen before. You can use this feature twice. You regain expended uses when you finish a short or long rest.

Your druid level determines the beasts you can transform into, as shown in the Beast Shapes table. At 2nd level, for example, you can transform into any beast that has a challenge rating of 1/4 or lower that doesn't have a flying or swimming speed.
Beast Shapes
Level 	Max. CR 	Limitations 	Example
2nd 	1/4 	No flying or swimming speed 	Wolf
4th 	1/2 	No flying speed 	Crocodile
8th 	1 		Giant eagle

You can stay in a beast shape for a number of hours equal to half your druid level (rounded down). You then revert to your normal form unless you expend another use of this feature. You can revert to your normal form earlier by using a bonus action on your turn. You automatically revert if you fall unconscious, drop to 0 hit points, or die.

While you are transformed, the following rules apply:

    Your game statistics are replaced by the statistics of the beast, but you retain your alignment, personality, and Intelligence, Wisdom, and Charisma scores. You also retain all of your skill and saving throw proficiencies, in addition to gaining those of the creature. If the creature has the same proficiency as you and the bonus in its stat block is higher than yours, use the creature's bonus instead of yours. If the creature has any legendary or lair actions, you can't use them.

    When you transform, you assume the beast's hit points and Hit Dice. When you revert to your normal form, you return to the number of hit points you had before you transformed. However, if you revert as a result of dropping to 0 hit points, any excess damage carries over to your normal form, For example, if you take 10 damage in animal form and have only 1 hit point left, you revert and take 9 damage. As long as the excess damage doesn't reduce your normal form to 0 hit points, you aren't knocked unconscious.

    You can't cast spells, and your ability to speak or take any action that requires hands is limited to the capabilities of your beast form. Transforming doesn't break your concentration on a spell you've already cast, however, or prevent you from taking actions that are part of a spell, such as Call Lightning, that you've already cast.

    You retain the benefit of any features from your class, race, or other source and can use them if the new form is physically capable of doing so. However, you can't use any of your special senses, such as darkvision, unless your new form also has that sense.

    You choose whether your equipment falls to the ground in your space, merges into your new form, or is worn by it. Worn equipment functions as normal, but the DM decides whether it is practical for the new form to wear a piece of equipment, based on the creature's shape and size. Your equipment doesn't change size or shape to match the new form, and any equipment that the new form can't wear must either fall to the ground or merge with it. Equipment that merges with the form has no effect until you leave the form.
"""

    print(feature)
    dnd_dict.character_dict["features"]['wild_shape'] = feature

    feature2 = """Wild Companion (Optional)

At 2nd level, you gain the ability to summon a spirit that assumes an animal form: as an action, you can expend a use of your Wild Shape feature to cast the Find Familiar spell, without material components.

When you cast the spell in this way, the familiar is a fey instead of a beast, and the familiar disappears after a number of hours equal to half your druid level."""
    print(feature2)
    dnd_dict.character_dict["features"]['wild_companion'] = feature2

    dnd_dict.character_dict['spells']['find_familiar']['first'] = 'Find Familiar'
    dnd_dict.character_dict['class_spells']['druid']['first']['find_familiar'] = 'Find Familiar'
    dnd_dict.character_dict['special_spells']['first']['find_familiar'] = 'Find Familiar'


def druid18():
    feature = """Timeless Body

Starting at 18th level, the primal magic that you wield causes you to age more slowly. For every 10 years that pass, your body ages only 1 year."""

    print(feature)
    dnd_dict.character_dict["features"]['timeless_body_druid'] = feature

    feature2 = """Beast Spells

Beginning at 18th level, you can cast many of your druid spells in any shape you assume using Wild Shape. You can perform the somatic and verbal components of a druid spell while in a beast shape, but you aren't able to provide material components."""

    print(feature2)
    dnd_dict.character_dict["features"]['beast_spells'] = feature

def druid20():
    feature = """Archdruid

At 20th level, you can use your Wild Shape an unlimited number of times.

Additionally, you can ignore the verbal and somatic components of your druid spells, as well as any material components that lack a cost and aren't consumed by a spell. You gain this benefit in both your normal shape and your beast shape from Wild Shape."""

    print(feature)
    dnd_dict.character_dict["features"]['archdruid'] = feature


def land_druid2():

    dnd_skills.spell_add(dnd_magic.druid_cantrip,dnd_dict.character_dict['spells']['cantrips'],dnd_dict.character_dict['class_spells']['druid_cantrips'])

    feature = """Natural Recovery

Starting at 2nd level, you can regain some of your magical energy by sitting in meditation and communing with nature. During a short rest, you choose expended spell slots to recover. The spell slots can have a combined level that is equal to or less than half your druid level (rounded up), and none of the slots can be 6th level or higher. You can't use this feature again until you finish a long rest.

For example, when you are a 4th-level druid, you can recover up to two levels worth of spell slots. You can recover either a 2nd-level slot or two 1st-level slots."""

    print(feature)
    dnd_dict.character_dict["features"]['natural_recovery_druid'] = feature
    dnd_dict.character_dict["player_class"]["druid"]["subclass"] = "Circle of the Land"



def land_druid3():
    print("""Circle Spells

Your mystical connection to the land infuses you with the ability to cast certain spells. At 3rd, 5th, 7th, and 9th level you gain access to circle spells connected to the land where you became a druid. Choose that land – arctic, coast, desert, forest, grassland, mountain, swamp, or Underdark – and consult the associated list of spells.

Once you gain access to a circle spell, you always have it prepared, and it doesn't count against the number of spells you can prepare each day. If you gain access to a spell that doesn't appear on the druid spell list, the spell is nonetheless a druid spell for you.""")

    while True:
        choice = input("""Select your connection to the land and spells you will receive:
1) Arctic (Hold Person and Spike Growth)
2) Coast (Mirror Image and Misty Step)
3) Desert (Blur and Silence)
4) Forest (Barkskin and Spider Climb)
5) Grassland (Invisibility and Pass Without Trace)
6) Mountain (Spider Climb and Spike Growth)
7) Swamp (Darkness and Melf's Acid Arrow)
8) Underdark (Spider Climb and Web)
Enter your selection: """)
        if choice == '1':
            added_spells = {'hold_person':'Hold Person','spike_growth':'Spike Growth'}
            dnd_dict.character_dict['spells']['second'].update(added_spells)
            dnd_dict.character_dict['class_spells']['druid']['second'].update(added_spells)
            dnd_dict.character_dict['special_spells']['second'].update(added_spells)
            break

        elif choice == '2':
            added_spells = {'mirror_image':'Mirror Image','misty_step':'Misty Step'}
            dnd_dict.character_dict['spells']['second'].update(added_spells)
            dnd_dict.character_dict['class_spells']['druid']['second'].update(added_spells)
            dnd_dict.character_dict['special_spells']['second'].update(added_spells)
            break

        elif choice == '3':
            added_spells = {'blur':'Blur','silence':'Silence'}
            dnd_dict.character_dict['spells']['second'].update(added_spells)
            dnd_dict.character_dict['class_spells']['druid']['second'].update(added_spells)
            dnd_dict.character_dict['special_spells']['second'].update(added_spells)
            break

        elif choice == '4':
            added_spells = {'barkskin':'Barkskin','spider_climb':'Spider Climb'}
            dnd_dict.character_dict['spells']['second'].update(added_spells)
            dnd_dict.character_dict['class_spells']['druid']['second'].update(added_spells)
            dnd_dict.character_dict['special_spells']['second'].update(added_spells)
            break

        elif choice == '5':
            added_spells = {'invisibility':'Invisibility','pass_without_trace':'Pass Without Trace'}
            dnd_dict.character_dict['spells']['second'].update(added_spells)
            dnd_dict.character_dict['class_spells']['druid']['second'].update(added_spells)
            dnd_dict.character_dict['special_spells']['second'].update(added_spells)
            break

        elif choice == '6':
            added_spells = {'spider_climb':'Spider Climb','spike_growth':'Spike Growth'}
            dnd_dict.character_dict['spells']['second'].update(added_spells)
            dnd_dict.character_dict['class_spells']['druid']['second'].update(added_spells)
            dnd_dict.character_dict['special_spells']['second'].update(added_spells)
            break

        elif choice == '7':
            added_spells = {'darkness':'Darkness','melf\'s_acid_arrow':'Melf\'s Acid Arrow'}
            dnd_dict.character_dict['spells']['second'].update(added_spells)
            dnd_dict.character_dict['class_spells']['druid']['second'].update(added_spells)
            dnd_dict.character_dict['special_spells']['second'].update(added_spells)
            break

        elif choice == '8':
            added_spells = {'spider_climb':'Spider Climb','web':'Web'}
            dnd_dict.character_dict['spells']['second'].update(added_spells)
            dnd_dict.character_dict['class_spells']['druid']['second'].update(added_spells)
            dnd_dict.character_dict['special_spells']['second'].update(added_spells)
            break

        else:
            print("Error: Invalid Input")
            continue

def land_druid5():
    while True:
        choice = input("""Select your connection to the land and spells you will receive:
1) Arctic (Sleet Storm and Slow)
2) Coast (Water Breathing and Water Walk)
3) Desert (Create Food and Water and Protection from Energy)
4) Forest (Call Lightning and Plant Growth)
5) Grassland (Daylight and Haste)
6) Mountain (Lightning Bolt and Meld into Stone)
7) Swamp (Water Walk and Stinking Cloud)
8) Underdark (Gaseous Form and Stinking Cloud)
Enter your selection: """)
        if choice == '1':
            added_spells = {'sleet_storm':'Sleet Storm','slow':'Slow'}
            dnd_dict.character_dict['spells']['third'].update(added_spells)
            dnd_dict.character_dict['class_spells']['druid']['third'].update(added_spells)
            dnd_dict.character_dict['special_spells']['third'].update(added_spells)
            break

        elif choice == '2':
            added_spells = {'water_breathing':'Water Breathing','water_walk':'Water Walk'}
            dnd_dict.character_dict['spells']['third'].update(added_spells)
            dnd_dict.character_dict['class_spells']['druid']['third'].update(added_spells)
            dnd_dict.character_dict['special_spells']['third'].update(added_spells)
            break

        elif choice == '3':
            added_spells = {'create_food_and_water':'Create Food and Water','protection_from_energy':'Protection from Energy'}
            dnd_dict.character_dict['spells']['third'].update(added_spells)
            dnd_dict.character_dict['class_spells']['druid']['third'].update(added_spells)
            dnd_dict.character_dict['special_spells']['third'].update(added_spells)
            break

        elif choice == '4':
            added_spells = {'call_lightning':'Call Lightning','plant_growth':'Plant Growth'}
            dnd_dict.character_dict['spells']['third'].update(added_spells)
            dnd_dict.character_dict['class_spells']['druid']['third'].update(added_spells)
            dnd_dict.character_dict['special_spells']['third'].update(added_spells)
            break

        elif choice == '5':
            added_spells = {'daylight':'Daylight','haste':'Haste'}
            dnd_dict.character_dict['spells']['third'].update(added_spells)
            dnd_dict.character_dict['class_spells']['druid']['third'].update(added_spells)
            dnd_dict.character_dict['special_spells']['third'].update(added_spells)
            break

        elif choice == '6':
            added_spells = {'lightning_bolt':'Lightning Bolt','meld_into_stone':'Meld into Stone'}
            dnd_dict.character_dict['spells']['third'].update(added_spells)
            dnd_dict.character_dict['class_spells']['druid']['third'].update(added_spells)
            dnd_dict.character_dict['special_spells']['third'].update(added_spells)
            break

        elif choice == '7':
            added_spells = {'water_walk':'Water Walk','stinking_cloud':'Stinking Cloud'}
            dnd_dict.character_dict['spells']['third'].update(added_spells)
            dnd_dict.character_dict['class_spells']['druid']['third'].update(added_spells)
            dnd_dict.character_dict['special_spells']['third'].update(added_spells)
            break

        elif choice == '8':
            added_spells = {'gaseous_form':'Gaseous Form','stinking_cloud':'Stinking Cloud'}
            dnd_dict.character_dict['spells']['third'].update(added_spells)
            dnd_dict.character_dict['class_spells']['druid']['third'].update(added_spells)
            dnd_dict.character_dict['special_spells']['third'].update(added_spells)
            break

        else:
            print("Error: Invalid Input")
            continue


def land_druid6():
    feature = """Land's Stride

Starting at 6th level, moving through nonmagical difficult terrain costs you no extra movement. You can also pass through nonmagical plants without being slowed by them and without taking damage from them if they have thorns, spines, or a similar hazard.

In addition, you have advantage on saving throws against plants that are magically created or manipulated to impede movement, such as those created by the Entangle spell."""

    print(feature)
    dnd_dict.character_dict["features"]['land\'s_stride'] = feature



def land_druid7():
    while True:
        choice = input("""Select your connection to the land and spells you will receive:
1) Arctic (Freedom of Movement and Ice Storm)
2) Coast (Control Water and Freedom of Movement)
3) Desert (Blight and Hallucinatory Terrain)
4) Forest (Divination and Freedom of Movement)
5) Grassland (Divination and Freedom of Movement)
6) Mountain (Stone Shape and Stoneskin)
7) Swamp (Freedom of Movement and Locate Creature)
8) Underdark (Greater Invisibility and Stone Shape)
Enter your selection: """)
        if choice == '1':
            added_spells = {'freedom_of_movement':'Freedom of Movement','ice_storm':'Ice Storm'}
            dnd_dict.character_dict['spells']['fourth'].update(added_spells)
            dnd_dict.character_dict['class_spells']['druid']['fourth'].update(added_spells)
            dnd_dict.character_dict['special_spells']['fourth'].update(added_spells)
            break

        elif choice == '2':
            added_spells = {'control_water':'Control Water','freedom_of_movement':'Freedom of Movement'}
            dnd_dict.character_dict['spells']['fourth'].update(added_spells)
            dnd_dict.character_dict['class_spells']['druid']['fourth'].update(added_spells)
            dnd_dict.character_dict['special_spells']['fourth'].update(added_spells)
            break

        elif choice == '3':
            added_spells = {'blight':'Blight','hallucinatory_terrain':'Hallucinatory Terrain'}
            dnd_dict.character_dict['spells']['fourth'].update(added_spells)
            dnd_dict.character_dict['class_spells']['druid']['fourth'].update(added_spells)
            dnd_dict.character_dict['special_spells']['fourth'].update(added_spells)
            break

        elif choice == '4':
            added_spells = {'divination':'Divination','freedom_of_movement':'Freedom of Movement'}
            dnd_dict.character_dict['spells']['fourth'].update(added_spells)
            dnd_dict.character_dict['class_spells']['druid']['fourth'].update(added_spells)
            dnd_dict.character_dict['special_spells']['fourth'].update(added_spells)
            break

        elif choice == '5':
            added_spells = {'divination':'Divination','freedom_of_movement':'Freedom of Movement'}
            dnd_dict.character_dict['spells']['fourth'].update(added_spells)
            dnd_dict.character_dict['class_spells']['druid']['fourth'].update(added_spells)
            dnd_dict.character_dict['special_spells']['fourth'].update(added_spells)
            break

        elif choice == '6':
            added_spells = {'stone_shape':'Stone Shape','stoneskin':'Stoneskin'}
            dnd_dict.character_dict['spells']['fourth'].update(added_spells)
            dnd_dict.character_dict['class_spells']['druid']['fourth'].update(added_spells)
            dnd_dict.character_dict['special_spells']['fourth'].update(added_spells)
            break

        elif choice == '7':
            added_spells = {'freedom_of_movement':'Freedom of Movement','locate_creature':'Locate Creature'}
            dnd_dict.character_dict['spells']['fourth'].update(added_spells)
            dnd_dict.character_dict['class_spells']['druid']['fourth'].update(added_spells)
            dnd_dict.character_dict['special_spells']['fourth'].update(added_spells)
            break

        elif choice == '8':
            added_spells = {'greater_invisibility':'Greater Invisibility','stone_shape':'Stone Shape'}
            dnd_dict.character_dict['spells']['fourth'].update(added_spells)
            dnd_dict.character_dict['class_spells']['druid']['fourth'].update(added_spells)
            dnd_dict.character_dict['special_spells']['fourth'].update(added_spells)
            break

        else:
            print("Error: Invalid Input")
            continue

def land_druid9():
    while True:
        choice = input("""Select your connection to the land and spells you will receive:
1) Arctic (Commune with Nature and Cone of Cold)
2) Coast (Conjure Elemental and Scrying)
3) Desert (Insect Plague and Wall of Stone)
4) Forest (Commune with Nature and Tree Stride)
5) Grassland (Dream and Insect Plague)
6) Mountain (Passwall and Wall of Stone)
7) Swamp (Insect Plague and Scrying)
8) Underdark (Cloudkill and Insect Plague)
Enter your selection: """)
        if choice == '1':
            added_spells = {'commune_with_nature':'Commune with Nature','cone_of_cold':'Cone of Cold'}
            dnd_dict.character_dict['spells']['fifth'].update(added_spells)
            dnd_dict.character_dict['class_spells']['druid']['fifth'].update(added_spells)
            dnd_dict.character_dict['special_spells']['fifth'].update(added_spells)
            break

        elif choice == '2':
            added_spells = {'conjure_elemental':'Conjure Elemental','scrying':'Scrying'}
            dnd_dict.character_dict['spells']['fifth'].update(added_spells)
            dnd_dict.character_dict['class_spells']['druid']['fifth'].update(added_spells)
            dnd_dict.character_dict['special_spells']['fifth'].update(added_spells)
            break

        elif choice == '3':
            added_spells = {'insect_plague':'Insect Plague','wall_of_stone':'Wall of Stone'}
            dnd_dict.character_dict['spells']['fifth'].update(added_spells)
            dnd_dict.character_dict['class_spells']['druid']['fifth'].update(added_spells)
            dnd_dict.character_dict['special_spells']['fifth'].update(added_spells)
            break

        elif choice == '4':
            added_spells = {'commune_with_nature':'Commune with Nature','tree_stride':'Tree Stride'}
            dnd_dict.character_dict['spells']['fifth'].update(added_spells)
            dnd_dict.character_dict['class_spells']['druid']['fifth'].update(added_spells)
            dnd_dict.character_dict['special_spells']['fifth'].update(added_spells)
            break

        elif choice == '5':
            added_spells = {'dream':'Dream','insect_plague':'Insect Plague'}
            dnd_dict.character_dict['spells']['fifth'].update(added_spells)
            dnd_dict.character_dict['class_spells']['druid']['fifth'].update(added_spells)
            dnd_dict.character_dict['special_spells']['fifth'].update(added_spells)
            break

        elif choice == '6':
            added_spells = {'passwall':'Passwall','wall_of_stone':'Wall of Stone'}
            dnd_dict.character_dict['spells']['fifth'].update(added_spells)
            dnd_dict.character_dict['class_spells']['druid']['fifth'].update(added_spells)
            dnd_dict.character_dict['special_spells']['fifth'].update(added_spells)
            break

        elif choice == '7':
            added_spells = {'insect_plague':'Insect Plague','scrying':'Scrying'}
            dnd_dict.character_dict['spells']['fifth'].update(added_spells)
            dnd_dict.character_dict['class_spells']['druid']['fifth'].update(added_spells)
            dnd_dict.character_dict['special_spells']['fifth'].update(added_spells)
            break

        elif choice == '8':
            added_spells = {'cloudkill':'Cloudkill','insect_plague':'Insect Plague'}
            dnd_dict.character_dict['spells']['fifth'].update(added_spells)
            dnd_dict.character_dict['class_spells']['druid']['fifth'].update(added_spells)
            dnd_dict.character_dict['special_spells']['fifth'].update(added_spells)
            break

        else:
            print("Error: Invalid Input")
            continue

def land_druid10():
    feature = """Nature's Ward

When you reach 10th level, you can't be charmed or frightened by elementals or fey, and you are immune to poison and disease."""

    print(feature)
    dnd_dict.character_dict["features"]['nature\'s_ward'] = feature

def land_druid14():
    feature = """Nature's Sanctuary

When you reach 14th level, creatures of the natural world sense your connection to nature and become hesitant to attack you. When a beast or plant creature attacks you, that creature must make a Wisdom saving throw against your druid spell save DC. On a failed save, the creature must choose a different target, or the attack automatically misses. On a successful save, the creature is immune to this effect for 24 hours.

The creature is aware of this effect before it makes its attack against you."""

    print(feature)
    dnd_dict.character_dict["features"]['nature\'s_sanctuary'] = feature

def moon_druid2():
    feature = """Combat Wild Shape

When you choose this circle at 2nd level, you gain the ability to use Wild Shape on your turn as a bonus action, rather than as an action.

Additionally, while you are transformed by Wild Shape, you can use a bonus action to expend one spell slot to regain 1d8 hit points per level of the spell slot expended."""

    print(feature)
    dnd_dict.character_dict["features"]['combat_wild_shape'] = feature
    dnd_dict.character_dict["player_class"]["druid"]["subclass"] = "Circle of the Moon"

    feature2 = """Circle Forms

The rites of your circle grant you the ability to transform into more dangerous animal forms. Starting at 2nd level, you can use your Wild Shape to transform into a beast with a challenge rating as high as 1. You ignore the Max. CR column of the Beast Shapes table, but must abide by the other limitations there.

Starting at 6th level, you can transform into a beast with a challenge rating as high as your druid level divided by 3, rounded down."""

    print(feature2)
    dnd_dict.character_dict["features"]['circle_forms'] = feature2

def moon_druid6():
    feature = """Primal Strike

Starting at 6th level, your attacks in beast form count as magical for the purpose of overcoming resistance and immunity to nonmagical attacks and damage."""

    print(feature)
    dnd_dict.character_dict["features"]['primal_strike'] = feature

def moon_druid10():
    feature = """Elemental Wild Shape

At 10th level, you can expend two uses of Wild Shape at the same time to transform into an air elemental, an earth elemental, a fire elemental, or a water elemental."""

    print(feature)
    dnd_dict.character_dict["features"]['elemental_wild_shape'] = feature

def moon_druid14():
    feature = """Thousand Forms

By 14th level, you have learned to use magic to alter your physical form in more subtle ways. You can cast the Alter Self spell at will."""

    print(feature)
    dnd_dict.character_dict["features"]['thousand_forms'] = feature
    dnd_dict.character_dict['spells']['second']['alter_self'] = 'Alter Self'
    dnd_dict.character_dict['class_spells']['druid']['second']['alter_self'] = 'Alter Self'
    dnd_dict.character_dict['special_spells']['second']['alter_self'] = 'Alter Self'


def archery(full_dict):
    feature = """Archery. You gain a +2 bonus to attack rolls you make with ranged weapons."""
    print(feature)
    dnd_dict.character_dict["features"]['archery_fighting_style'] = feature
    full_dict['archery_fighting_style'] = 'Archery'

def blessed_warrior(full_dict):
    feature = """Blessed Warrior. You learn two cantrips of your choice from the cleric spell list. They count as paladin spells for you, and Charisma is your spellcasting ability for them. Whenever you gain a level in this class, you can replace one of these cantrips with another cantrip from the cleric spell list."""
    print(feature)
    dnd_dict.character_dict["features"]['blessed_warrior_fighting_style'] = feature
    full_dict['blessed_warrior_fighting_style'] = 'Blessed Warrior'
    x = 1
    for x in range(x,3):
        if x < 3:
            print(f'{x}/2')
            dnd_skills.spell_add(dnd_magic.cleric_cantrip,dnd_dict.character_dict['spells']['cantrips'],dnd_dict.character_dict['special_spells']['fighting_cleric'])
            x+=1
            continue
        elif x == 3:
            break

def blind_fighting(full_dict):
    feature = """Blind Fighting. You have blindsight with a range of 10 feet. Within that range, you can effectively see anything that isn't behind total cover, even if you're blinded or in darkness. Moreover, you can see an invisible creature within that range, unless the creature successfully hides from you."""
    print(feature)
    dnd_dict.character_dict["features"]['blind_fighting_fighting_style'] = feature
    full_dict['blind_fighting_fighting_style'] = 'Blind Fighting'

def defense(full_dict):
    feature = "Defense. While you are wearing armor, you gain a +1 bonus to AC."
    print(feature)
    dnd_dict.character_dict["features"]['defense_fighting_style'] = feature
    full_dict['defense_fighting_style'] = 'Defense'

def druidic_warrior(full_dict):
    feature = """Druidic Warrior. You learn two cantrips of your choice from the Druid spell list. They count as ranger spells for you, and Wisdom is your spellcasting ability for them. Whenever you gain a level in this class, you can replace one of these cantrips with another cantrip from the Druid spell list."""
    print(feature)
    dnd_dict.character_dict["features"]['druidic_warrior_fighting_style'] = feature
    full_dict['druidic_warrior_fighting_style'] = 'Druidic Warrior'
    x = 1
    for x in range(x,3):
        if x < 3:
            print(f'{x}/2')
            dnd_skills.spell_add(dnd_magic.druid_cantrip,dnd_dict.character_dict['spells']['cantrips'],dnd_dict.character_dict['special_spells']['fighting_druid'])
            x+=1
            continue
        elif x == 3:
            break

def dueling(full_dict):
    feature = """Dueling. When you are wielding a melee weapon in one hand and no other weapons, you gain a +2 bonus to damage rolls with that weapon."""
    print(feature)
    dnd_dict.character_dict["features"]['dueling_fighting_style'] = feature
    full_dict['dueling_fighting_style'] = 'Dueling'

def great_weapon_fighting(full_dict):
    feature = """Great Weapon Fighting. When you roll a 1 or 2 on a damage die for an attack you make with a melee weapon that you are wielding with two hands, you can reroll the die and must use the new roll, even if the new roll is a 1 or a 2. The weapon must have the two-handed or versatile property for you to gain this benefit."""
    print(feature)
    dnd_dict.character_dict["features"]['great_weapon_fighting_fighting_style'] = feature
    full_dict['great_weapon_fighting_style'] = 'Great Weapon Fighting'

def interception(full_dict):
    feature = """Interception. When a creature you can see hits a target, other than you, within 5 feet of you with an attack, you can use your reaction to reduce the damage the target takes by 1d10 + your proficiency bonus (to a minimum of 0 damage). You must be wielding a shield or a simple or martial weapon to use this reaction."""
    print(feature)
    dnd_dict.character_dict["features"]['interception_fighting_style'] = feature
    full_dict['interception_fighting_style'] = 'Interception'

def protection(full_dict):
    feature = """Protection. When a creature you can see attacks a target other than you that is within 5 feet of you, you can use your reaction to impose disadvantage on the attack roll. You must be wielding a shield."""
    print(feature)
    dnd_dict.character_dict["features"]['protection_fighting_style'] = feature
    full_dict['protection_fighting_style'] = 'Protection'

def superior_technique(full_dict):
    feature = """
    Superior Technique. You learn one maneuver of your choice from among those available to the Battle Master archetype. If a maneuver you use requires your target to make a saving throw to resist the maneuver's effects, the saving throw DC equals 8 + your proficiency bonus + your Strength or Dexterity modifier (your choice.)
        You gain one superiority die, which is a d6 (this die is added to any superiority dice you have from another source). This die is used to fuel your maneuvers. A superiority die is expended when you use it. You regain your expended superiority dice when you finish a short or long rest.
"""
    print(feature)
    dnd_dict.character_dict["features"]['superior_technique_fighting_style'] = feature
    dnd_maneuvers.maneuvers()
    dnd_dict.character_dict['maneuvers']['d6'] += 1
    full_dict['superior_technique_fighting_style'] = 'Superior Technique'

def thrown_weapon_fighting(full_dict):
    feature = """
    Thrown Weapon Fighting. You can draw a weapon that has the thrown property as part of the attack you make with the weapon.
        In addition, when you hit with a ranged attack using a thrown weapon, you gain a +2 bonus to the damage roll.
"""
    print(feature)
    dnd_dict.character_dict["features"]['thrown_weapon_fighting_fighting_style'] = feature
    full_dict['thrown_weapon_fighting_fighting_style'] = 'Thrown Weapon Fighting'

def two_weapon_fighting(full_dict):
    feature = """Two-Weapon Fighting. When you engage in two-weapon fighting, you can add your ability modifier to the damage of the second attack."""
    print(feature)
    dnd_dict.character_dict["features"]['two_weapon_fighting_fighting_style'] = feature
    full_dict['two_weapon_fighting_fighting_style'] = 'Two-Weapon Fighting'

def unarmed_fighting(full_dict):
    feature = """
    Unarmed Fighting. Your unarmed strikes can deal bludgeoning damage equal to 1d6 + your Strength modifier on a hit. If you aren't wielding any weapons or a shield when you make the attack roll, the d6 becomes a d8.
        At the start of each of your turns, you can deal 1d4 bludgeoning damage to one creature grappled by you.
"""
    print(feature)
    dnd_dict.character_dict["features"]['unarmed_fighting_fighting_style'] = feature
    full_dict['unarmed_fighting_fighting_style'] = 'Unarmed Fighting'

def fighter1():
    feature = """Second Wind

You have a limited well of stamina that you can draw on to protect yourself from harm. On your turn, you can use a bonus action to regain hit points equal to 1d10 + your fighter level.

Once you use this feature, you must finish a short or long rest before you can use it again."""
    print(feature)
    dnd_dict.character_dict["features"]['second_wind'] = feature
    dnd_fighting_styles.fighter_fighting_styles()


def fighter2():
    feature = """Action Surge

Starting at 2nd level, you can push yourself beyond your normal limits for a moment. On your turn, you can take one additional action.

Once you use this feature, you must finish a short or long rest before you can use it again. Starting at 17th level, you can use it twice before a rest, but only once on the same turn."""
    print(feature)
    dnd_dict.character_dict["features"]['action_surge'] = feature


def fighter5():
    feature = """Extra Attack

Beginning at 5th level, you can attack twice, instead of once, whenever you take the Attack action on your turn.

The number of attacks increases to three when you reach 11th level in the Fighter class and to four when you reach 20th level in the Fighter class."""
    print(feature)
    dnd_dict.character_dict["features"]['extra_attack'] = feature

def fighter9():
    feature = """Indomitable

Beginning at 9th level, you can reroll a saving throw that you fail. If you do so, you must use the new roll, and you can't use this feature again until you finish a long rest.

You can use this feature twice between long rests starting at 13th level and three times between long rests starting at 17th level."""
    print(feature)
    dnd_dict.character_dict["features"]['indomitable'] = feature

def battle_master3():
    feature = """Combat Superiority

When you choose this archetype at 3rd level, you learn maneuvers that are fueled by special dice called superiority dice.

Maneuvers. You learn three maneuvers of your choice. Many maneuvers enhance an attack in some way. You can use only one maneuver per attack. You learn two additional maneuvers of your choice at 7th, 10th, and 15th level. Each time you learn new maneuvers, you can also replace one maneuver you know with a different one.

Superiority Dice. You have four superiority dice, which are d8s. A superiority die is expended when you use it. You regain all of your expended superiority dice when you finish a short or long rest. You gain another superiority die at 7th level and one more at 15th level.

Saving Throws. Some of your maneuvers require your target to make a saving throw to resist the maneuver's effects. The saving throw DC is calculated as follows:

Maneuver save DC = 8 + your proficiency bonus + your Strength or Dexterity modifier (your choice)"""
    x = 1
    for x in range(x,4):
        if x < 4:
            print(f'{x}/3')
            dnd_maneuvers.maneuvers()
            x+=1
            continue
        elif x == 4:
            break

    print(feature)
    dnd_dict.character_dict["features"]['combat_superiority'] = feature
    dnd_dict.character_dict['maneuvers']['die'] = 'd8'
    dnd_dict.character_dict['maneuvers']['number'] += 4
    
    dnd_tools.artisan_tools()

def battle_master7():
    feature = """Know Your Enemy

Starting at 7th level, if you spend at least 1 minute observing or interacting with another creature outside combat, you can learn certain information about its capabilities compared to your own. The DM tells you if the creature is your equal, superior, or inferior in regard to two of the following characteristics of your choice:

    Strength score

    Dexterity score

    Constitution score

    Armor Class

    Current hit points

    Total class levels, if any

    Fighter class levels, if any
"""
    print(feature)
    dnd_dict.character_dict["features"]['know_your_enemy'] = feature
    dnd_dict.character_dict['maneuvers']['number'] += 1
    dnd_maneuvers.maneuver_choice()
    x = 1
    for x in range(x,3):
        if x < 3:
            print(f'{x}/2')
            dnd_maneuvers.maneuvers()
            x+=1
            continue
        elif x == 3:
            break

def battle_master10():
    feature = """Improved Combat Superiority

At 10th level, your superiority dice turn into d10s. At 18th level, they turn into d12s."""
    print(feature)
    dnd_dict.character_dict["features"]['improved_combat_superiority'] = feature
    dnd_dict.character_dict['maneuvers']['die'] = 'd10'
    dnd_maneuvers.maneuver_choice()
    x = 1
    for x in range(x,3):
        if x < 3:
            print(f'{x}/2')
            dnd_maneuvers.maneuvers()
            x+=1
            continue
        elif x == 3:
            break


def battle_master15():
    feature = """Relentless

Starting at 15th level, when you roll initiative and have no superiority dice remaining, you regain 1 superiority die."""
    print(feature)
    dnd_dict.character_dict["features"]['relentless'] = feature
    dnd_dict.character_dict['maneuvers']['number'] += 1
    dnd_maneuvers.maneuver_choice()
    x = 1
    for x in range(x,3):
        if x < 3:
            print(f'{x}/2')
            dnd_maneuvers.maneuvers()
            x+=1
            continue
        elif x == 3:
            break

def battle_master18():
    dnd_dict.character_dict['maneuvers']['die'] = 'd12'

def champion3():
    feature = """Improved Critical

Beginning when you choose this archetype at 3rd level, your weapon attacks score a critical hit on a roll of 19 or 20."""
    print(feature)
    dnd_dict.character_dict["features"]['improved_critical'] = feature

def champion7():
    feature = """Remarkable Athlete

Starting at 7th level, you can add half your proficiency bonus (rounded up) to any Strength, Dexterity, or Constitution check you make that doesn't already use your proficiency bonus.

In addition, when you make a running long jump, the distance you can cover increases by a number of feet equal to your Strength modifier."""
    print(feature)
    dnd_dict.character_dict["features"]['remarkable_athlete'] = feature

def champion10():
    dnd_fighting_styles.fighter_fighting_styles()

def champion15():
    feature = """Superior Critical

Starting at 15th level, your weapon attacks score a critical hit on a roll of 18-20."""
    print(feature)
    dnd_dict.character_dict["features"]['superior_critical'] = feature


def champion18():
    feature = """Survivor

At 18th level, you attain the pinnacle of resilience in battle. At the start of each of your turns, you regain hit points equal to 5 + your Constitution modifier if you have no more than half of your hit points left. You don't gain this benefit if you have 0 hit points."""
    print(feature)
    dnd_dict.character_dict["features"]['survivor'] = feature






# This function is for when the Fighter gets spells from any class. The Limited variables are used for Evocation and Abjuration schools, while the Full variables are used for any school of magic.

# Used to swap out the second level spells for Evocation and Abjuration, but only second level for all spells.
def fighter_spell_swap_second():
    while True:
        choice = input("""Do you want to replace one Fighter spell?
1) An Evocation or Abjuration Spell
2) Any School of Magic
0) No
Enter your selection: """)
        if choice == '1':
            dnd_skills.second_swap(dnd_magic.eldritch_knight_first,dnd_magic.eldritch_knight_second,dnd_dict.character_dict['class_spells']['fighter']['first'],dnd_dict.character_dict['class_spells']['fighter']['second'])
            break

        elif choice == '2':
            dnd_skills.second_swap(dnd_magic.wizard_first,dnd_magic.wizard_second,dnd_dict.character_dict['class_spells']['fighter_special']['first'],dnd_dict.character_dict['class_spells']['fighter_special']['second'])
            break

        elif choice == '0':
            break

        else:
            print("Error: Invalid Selection")
            continue

# Used to swap out the third level spells for Evocation and Abjuration, but only second level for all spells.
def fighter_spell_swap_third_early():
    while True:
        choice = input("""Do you want to replace one Fighter spell?
1) An Evocation or Abjuration Spell
2) Any School of Magic
0) No
Enter your selection: """)
        if choice == '1':
            dnd_skills.third_swap(dnd_magic.eldritch_knight_first,dnd_magic.eldritch_knight_second,dnd_magic.eldritch_knight_third,dnd_dict.character_dict['class_spells']['fighter']['first'],dnd_dict.character_dict['class_spells']['fighter']['second'],dnd_dict.character_dict['class_spells']['fighter']['third'])
            break

        elif choice == '2':
            dnd_skills.second_swap(dnd_magic.wizard_first,dnd_magic.wizard_second,dnd_dict.character_dict['class_spells']['fighter_special']['first'],dnd_dict.character_dict['class_spells']['fighter_special']['second'])
            break

        elif choice == '0':
            break

        else:
            print("Error: Invalid Selection")
            continue

# Used to swap out the third level spells for Evocation and Abjuration, but only third level for all spells.
def fighter_spell_swap_third():
    while True:
        choice = input("""Do you want to replace one Fighter spell?
1) An Evocation or Abjuration Spell
2) Any School of Magic
0) No
Enter your selection: """)
        if choice == '1':
            dnd_skills.third_swap(dnd_magic.eldritch_knight_first,dnd_magic.eldritch_knight_second,dnd_magic.eldritch_knight_third,dnd_dict.character_dict['class_spells']['fighter']['first'],dnd_dict.character_dict['class_spells']['fighter']['second'],dnd_dict.character_dict['class_spells']['fighter']['third'])
            break

        elif choice == '2':
            dnd_skills.third_swap(dnd_magic.wizard_first,dnd_magic.wizard_second,dnd_magic.wizard_third,dnd_dict.character_dict['class_spells']['fighter_special']['first'],dnd_dict.character_dict['class_spells']['fighter_special']['second'],dnd_dict.character_dict['class_spells']['fighter_special']['third'])
            break

        elif choice == '0':
            break

        else:
            print("Error: Invalid Selection")
            continue



# Used to swap out the fourth level spells for Evocation and Abjuration, but only third level for all spells.
def fighter_spell_swap_fourth():
    while True:
        choice = input("""Do you want to replace one Fighter spell?
1) An Evocation or Abjuration Spell
2) Any School of Magic
0) No
Enter your selection: """)
        if choice == '1':
            dnd_skills.fourth_swap(dnd_magic.eldritch_knight_first,dnd_magic.eldritch_knight_second,dnd_magic.eldritch_knight_third,dnd_magic.eldritch_knight_fourth,dnd_dict.character_dict['class_spells']['fighter']['first'],dnd_dict.character_dict['class_spells']['fighter']['second'],dnd_dict.character_dict['class_spells']['fighter']['third'],dnd_dict.character_dict['class_spells']['fighter']['fourth'])
            break

        elif choice == '2':
            dnd_skills.third_swap(dnd_magic.wizard_first,dnd_magic.wizard_second,dnd_magic.wizard_third,dnd_dict.character_dict['class_spells']['fighter_special']['first'],dnd_dict.character_dict['class_spells']['fighter_special']['second'],dnd_dict.character_dict['class_spells']['fighter_special']['third'])
            break

        elif choice == '0':
            break

        else:
            print("Error: Invalid Selection")
            continue





def eldritch_knight3():
    feature1 = """Spellcasting

When you reach 3rd level, you augment your martial prowess with the ability to cast spells.
Cantrips

You learn two cantrips of your choice from the wizard spell list. You learn an additional wizard cantrip of your choice at 10th level.
Spell Slots

The Eldritch Knight Spellcasting table shows how many spell slots you have to cast your wizard spells of 1st level and higher. To cast one of these spells, you must expend a slot of the spell's level or higher. You regain all expended spell slots when you finish a long rest.

For example, if you know the 1st-level spell Shield and have a 1st-level and a 2nd-level spell slot available, you can cast Shield using either slot.
Spells Known of 1st Level and Higher

You know three 1st-level wizard spells of your choice, two of which you must choose from the abjuration and evocation spells on the wizard spell list.

The Spells Known column of the Eldritch Knight Spellcasting table shows when you learn more wizard spells of 1st level or higher. Each of these spells must be an abjuration or evocation spell of your choice, and must be of a level for which you have spell slots. For instance, when you reach 7th level in this class, you can learn one new spell of 1st or 2nd level.

The spells you learn at 8th, 14th, and 20th level can come from any school of magic.

Whenever you gain a level in this class, you can replace one of the wizard spells you know with another spell of your choice from the wizard spell list. The new spell must be of a level for which you have spell slots, and it must be an abjuration or evocation spell, unless you're replacing the spell you gained at 3rd, 8th, 14th, or 20th level from any school of magic.
Spellcasting Ability

Intelligence is your spellcasting ability for your wizard spells, since you learn your spells through study and memorization. You use your Intelligence whenever a spell refers to your spellcasting ability. In addition, you use your Intelligence modifier when setting the saving throw DC for a wizard spell you cast and when making an attack roll with one.

Spell save DC = 8 + your proficiency bonus + your Intelligence modifier

Spell attack modifier = your proficiency bonus + your Intelligence modifier"""

    feature2 = """Weapon Bond

At 3rd level, you learn a ritual that creates a magical bond between yourself and one weapon. You perform the ritual over the course of 1 hour, which can be done during a short rest. The weapon must be within your reach throughout the ritual, at the conclusion of which you touch the weapon and forge the bond.

Once you have bonded a weapon to yourself, you can't be disarmed of that weapon unless you are incapacitated. If it is on the same plane of existence, you can summon that weapon as a bonus action on your turn, causing it to teleport instantly to your hand.

You can have up to two bonded weapons, but can summon only one at a time with your bonus action. If you attempt to bond with a third weapon, you must break the bond with one of the other two."""

    print(feature1)
    dnd_magic.eldritch_knight_magic()
    print(feature2)
    dnd_dict.character_dict["features"]['weapon_bond_fighter'] = feature2
    dnd_dict.character_dict['semi_caster_level'] += 3
    dnd_skills.spell_slot_selection()
    spell_attack = ((dnd_dict.character_dict["Stats"]["intelligence"]['mod']) + dnd_dict.character_dict['prof_bonus'])
    dnd_dict.character_dict["spell_modifier"]['intelligence']['attack'] = spell_attack
    spell_save = ((dnd_dict.character_dict["Stats"]["intelligence"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
    dnd_dict.character_dict["spell_modifier"]['intelligence']['save'] = spell_save

def eldritch_knight7():
    feature = """War Magic

Beginning at 7th level, when you use your action to cast a cantrip, you can make one weapon attack as a bonus action."""
    print(feature)
    dnd_dict.character_dict["features"]['war_magic'] = feature

def eldritch_knight10():
    feature = """Eldritch Strike

At 10th level, you learn how to make your weapon strikes undercut a creature's resistance to your spells. When you hit a creature with a weapon attack, that creature has disadvantage on the next saving throw it makes against a spell you cast before the end of your next turn."""
    print(feature)
    dnd_dict.character_dict["features"]['eldritch_strike'] = feature

def eldritch_knight15():
    feature = """Arcane Charge

At 15th level, you gain the ability to teleport up to 30 feet to an unoccupied space you can see when you use your Action Surge. You can teleport before or after the additional action."""
    print(feature)
    dnd_dict.character_dict["features"]['arcane_charge'] = feature

def eldritch_knight18():
    feature = """Improved War Magic

Starting at 18th level, when you use your action to cast a spell, you can make one weapon attack as a bonus action."""
    print(feature)
    dnd_dict.character_dict["features"]['improved_war_magic'] = feature

def monk2():
    feature = """Ki

Starting at 2nd level, your training allows you to harness the mystic energy of ki. Your access to this energy is represented by a number of ki points. Your monk level determines the number of points you have, as shown in the Ki Points column of the Monk table.

You can spend these points to fuel various ki features. You start knowing three such features: Flurry of Blows, Patient Defense, and Step of the Wind. You learn more ki features as you gain levels in this class.

When you spend a ki point, it is unavailable until you finish a short or long rest, at the end of which you draw all of your expended ki back into yourself. You must spend at least 30 minutes of the rest meditating to regain your ki points.

Some of your ki features require your target to make a saving throw to resist the feature's effects. The saving throw DC is calculated as follows:

Ki save DC = 8 + your proficiency bonus + your Wisdom modifier

    Flurry of Blows. Immediately after you take the Attack action on your turn, you can spend 1 ki point to make two unarmed strikes as a bonus action.

    Patient Defense. You can spend 1 ki point to take the Dodge action as a bonus action on your turn.

    Step of the Wind. You can spend 1 ki point to take the Disengage or Dash action as a bonus action on your turn, and your jump distance is doubled for the turn.
"""
    feature2 = """Unarmored Movement

Starting at 2nd level, your speed increases by 10 feet while you are not wearing armor or wielding a shield. This bonus increases when you reach certain monk levels, as shown in the Monk table.

At 9th level, you gain the ability to move along vertical surfaces and across liquids on your turn without falling during the move."""

    feature3 = """Dedicated Weapon (Optional)

Also at 2nd level, you train yourself to use a variety of weapons as monk weapons, not just simple melee weapons and shortswords. Whenever you finish a short or long rest, you can touch one weapon, focus your ki on it, and then count that weapon as a monk weapon until you use this feature again.

The chosen weapon must meet these criteria:

    The weapon must be a simple or martial weapon.

    You must be proficient with it.

    It must lack the heavy and special properties.
"""

    print(feature)
    dnd_dict.character_dict["features"]['ki'] = feature

    print(feature2)
    dnd_dict.character_dict["features"]['unarmored_movement_monk'] = feature
    if dnd_dict.character_dict['unarmored_movement_barbarian'] > 0:
        new_speed = dnd_dict.character_dict['unarmored_movement_barbarian'] + 10
        dnd_dict.character_dict['unarmored_movement_monk']=new_speed
    else:
        new_speed = dnd_dict.character_dict['speed'] + 10
        dnd_dict.character_dict['unarmored_movement_monk']=new_speed


    print(feature3)
    dnd_dict.character_dict["features"]['dedicated_weapon'] = feature3

def monk3():
    feature = """Deflect Missiles

Starting at 3rd level, you can use your reaction to deflect or catch the missile when you are hit by a ranged weapon attack. When you do so, the damage you take from the attack is reduced by 1d10 + your Dexterity modifier + your monk level.

If you reduce the damage to 0, you can catch the missile if it is small enough for you to hold in one hand and you have at least one hand free. If you catch a missile in this way, you can spend 1 ki point to make a ranged attack with a range of 20/60 using the weapon or piece of ammunition you just caught, as part of the same reaction. You make this attack with proficiency, regardless of your weapon proficiencies, and the missile counts as a monk weapon for the attack."""
    print(feature)
    dnd_dict.character_dict["features"]['deflect_missiles'] = feature

    feature2 = """Ki-Fueled Attack (Optional)

Also at 3rd level, if you spend 1 ki point or more as part of your action on your turn, you can make one attack with an unarmed strike or a monk weapon as a bonus action before the end of the turn."""
    print(feature2)
    dnd_dict.character_dict["features"]['ki_fueled_attack'] = feature

def monk4():
    feature = """Slow Fall

Beginning at 4th level, you can use your reaction when you fall to reduce any falling damage you take by an amount equal to five times your monk level."""
    print(feature)
    dnd_dict.character_dict["features"]['slow_fall'] = feature

    feature2 = """Quickened Healing (Optional)

Also at 4th level, as an action, you can spend 2 ki points and roll a Martial Arts die. You regain a number of hit points equal to the number rolled plus your proficiency bonus."""
    print(feature2)
    dnd_dict.character_dict["features"]['quickened_healing'] = feature

def monk5():
    extra_attack()
    feature = """Stunning Strike

Starting at 5th level, you can interfere with the flow of ki in an opponent's body. When you hit another creature with a melee weapon attack, you can spend 1 ki point to attempt a stunning strike. The target must succeed on a Constitution saving throw or be stunned until the end of your next turn."""
    print(feature)
    dnd_dict.character_dict["features"]['stunning_strike'] = feature

    feature2 = """Focused Aim (Optional)

Also at 5th level, when you miss with an attack roll, you can spend 1 to 3 ki points to increase your attack roll by 2 for each of these ki points you spend, potentially turning the miss into a hit."""
    print(feature2)
    dnd_dict.character_dict["features"]['focused_aim'] = feature

def monk6():
    feature = """Ki-Empowered Strikes

Starting at 6th level, your unarmed strikes count as magical for the purpose of overcoming resistance and immunity to nonmagical attacks and damage."""
    print(feature)
    dnd_dict.character_dict["features"]['ki_empowered_strikes'] = feature
    if dnd_dict.character_dict['unarmored_movement_barbarian'] > 0:
        new_speed = dnd_dict.character_dict['unarmored_movement_barbarian'] + 15
        dnd_dict.character_dict['unarmored_movement_monk']=new_speed
    else:
        new_speed = dnd_dict.character_dict['speed'] + 15
        dnd_dict.character_dict['unarmored_movement_monk']+=5


# Evasion is used for multiple classes
def evasion():
    feature = """Evasion

At 7th level, your instinctive agility lets you dodge out of the way of certain area effects, such as a blue dragon's lightning breath or a fireball spell. When you are subjected to an effect that allows you to make a Dexterity saving throw to take only half damage, you instead take no damage if you succeed on the saving throw, and only half damage if you fail."""
    print(feature)
    dnd_dict.character_dict["features"]['evasion'] = feature
    

def monk7():
    evasion()
    feature = """Stillness of Mind

Starting at 7th level, you can use your action to end one effect on yourself that is causing you to be charmed or frightened."""
    print(feature)
    dnd_dict.character_dict["features"]['stillness_of_mind'] = feature

def monk10():
    feature = """Purity of Body

At 10th level, your mastery of the ki flowing through you makes you immune to disease and poison."""
    print(feature)
    dnd_dict.character_dict["features"]['purity_of_body'] = feature
    if dnd_dict.character_dict['unarmored_movement_barbarian'] > 0:
        new_speed = dnd_dict.character_dict['unarmored_movement_barbarian'] + 20
        dnd_dict.character_dict['unarmored_movement_monk']=new_speed
    else:
        new_speed = dnd_dict.character_dict['speed'] + 20
        dnd_dict.character_dict['unarmored_movement_monk']=new_speed

def monk13():
    feature = """Tongue of the Sun and Moon

Starting at 13th level, you learn to touch the ki of other minds so that you understand all spoken languages. Moreover, any creature that can understand a language can understand what you say."""
    print(feature)
    dnd_dict.character_dict["features"]['tongue_of_the_sun_and_moon'] = feature

def monk14():
    feature = """Diamond Soul

Beginning at 14th level, your mastery of ki grants you proficiency in all saving throws.

Additionally, whenever you make a saving throw and fail, you can spend 1 ki point to reroll it and take the second result."""
    print(feature)
    dnd_dict.character_dict["features"]['diamond_soul'] = feature
    dnd_dict.character_dict['saving_throws']['strength'] = 'Strength'
    dnd_dict.character_dict['saving_throws']['dexterity'] = 'Dexterity'
    dnd_dict.character_dict['saving_throws']['constitution'] = 'Constitution'
    dnd_dict.character_dict['saving_throws']['intelligence'] = 'Intelligence'
    dnd_dict.character_dict['saving_throws']['wisdom'] = 'Wisdom'
    dnd_dict.character_dict['saving_throws']['charisma'] = 'Charisma'
    dnd_skills.saving_throw_calc()
    if dnd_dict.character_dict['unarmored_movement_barbarian'] > 0:
        new_speed = dnd_dict.character_dict['unarmored_movement_barbarian'] + 25
        dnd_dict.character_dict['unarmored_movement_monk']=new_speed
    else:
        new_speed = dnd_dict.character_dict['speed'] + 25
        dnd_dict.character_dict['unarmored_movement_monk']=new_speed

def monk15():
    feature = """Timeless Body

At 15th level, your ki sustains you so that you suffer none of the frailty of old age, and you can't be aged magically. You can still die of old age, however. In addition, you no longer need food or water."""
    print(feature)
    dnd_dict.character_dict["features"]['timeless_body'] = feature

def monk18():
    feature = """Empty Body

Beginning at 18th level, you can use your action to spend 4 ki points to become invisible for 1 minute. During that time, you also have resistance to all damage but force damage.

Additionally, you can spend 8 ki points to cast the Astral Projection spell, without needing material components. When you do so, you can't take any other creatures with you."""
    print(feature)
    dnd_dict.character_dict["features"]['empty_body'] = feature
    if dnd_dict.character_dict['unarmored_movement_barbarian'] > 0:
        new_speed = dnd_dict.character_dict['unarmored_movement_barbarian'] + 30
        dnd_dict.character_dict['unarmored_movement_monk']=new_speed
    else:
        new_speed = dnd_dict.character_dict['speed'] + 30
        dnd_dict.character_dict['unarmored_movement_monk']=new_speed

def monk20():
    feature = """Perfect Self

At 20th level, when you roll for initiative and have no ki points remaining, you regain 4 ki points."""
    print(feature)
    dnd_dict.character_dict["features"]['perfect_self'] = feature

def four_elements_monk3():
    feature = """Disciple of the Elements

When you choose this tradition at 3rd level, you learn magical disciplines that harness the power of the four elements. A discipline requires you to spend ki points each time you use it.

You know the Elemental Attunement discipline and one other elemental discipline of your choice. You learn one additional elemental discipline of your choice at 6th, 11th, and 17th level.

Whenever you learn a new elemental discipline, you can also replace one elemental discipline that you already know with a different discipline.

Casting Elemental Spells. Some elemental disciplines allow you to cast spells. See chapter 10 for the general rules of spellcasting. To cast one of these spells, you use its casting time and other rules, but you don't need to provide material components for it.

Once you reach 5th level in this class, you can spend additional ki points to increase the level of an elemental discipline spell that you cast, provided that the spell has an enhanced effect at a higher level, as Burning Hands does. The spell's level increases by 1 for each additional ki point you spend. For example, if you are a 5th-level monk and use Sweeping Cinder Strike to cast Burning Hands, you can spend 3 ki points to cast it as a 2nd-level spell (the discipline's base cost of 2 ki points plus 1).

The maximum number of ki points you can spend to cast a spell in this way (including its base ki point cost and any additional ki points you spend to increase its level) is determined by your monk level, as shown in the Spells and Ki Points table.
Spells and Ki Points
Monk Levels 	Maximum Ki Points for a Spell
5th-8th 	3
9th-12th 	4
13th-16th 	5
17th-20th 	6"""
    print(feature)
    dnd_dict.character_dict["features"]['disciple_of_the_elements'] = feature
    dnd_four_elements.elemental_discipline()
    dnd_dict.character_dict['player_class']['monk']['subclass'] = 'Way of the Four Elements'

def four_elements_monk6():
    dnd_four_elements.elemental_discipline()
    dnd_four_elements.discipline_swap()

def four_elements_monk11():
    dnd_four_elements.elemental_discipline()
    dnd_four_elements.discipline_swap()

def four_elements_monk17():
    dnd_four_elements.elemental_discipline()
    dnd_four_elements.discipline_swap()

def open_hand_monk3():
    feature = """Open Hand Technique

Starting when you choose this tradition at 3rd level, you can manipulate your enemy's ki when you harness your own. Whenever you hit a creature with one of the attacks granted by your Flurry of Blows, you can impose one of the following effects on that target:

    It must succeed on a Dexterity saving throw or be knocked prone.

    It must make a Strength saving throw. If it fails, you can push it up to 15 feet away from you.

    It can't take reactions until the end of your next turn.
"""
    print(feature)
    dnd_dict.character_dict["features"]['open_hand_technique'] = feature
    dnd_dict.character_dict['player_class']['monk']['subclass'] = 'Way of the Open Hand'

def open_hand_monk6():
    feature = """Wholeness of Body

At 6th level, you gain the ability to heal yourself. As an action, you can regain hit points equal to three times your monk level. You must finish a long rest before you can use this feature again."""
    print(feature)
    dnd_dict.character_dict["features"]['wholeness_of_body'] = feature

def open_hand_monk11():
    feature = """Tranquility

Beginning at 11th level, you can enter a special meditation that surrounds you with an aura of peace. At the end of a long rest, you gain the effect of a Sanctuary spell that lasts until the start of your next long rest (the spell can end early as normal). The saving throw DC for the spell equals 8 + your Wisdom modifier + your proficiency bonus."""
    print(feature)
    dnd_dict.character_dict["features"]['tranquility_monk'] = feature

def open_hand_monk17():
    feature = """Quivering Palm

At 17th level, you gain the ability to set up lethal vibrations in someone's body. When you hit a creature with an unarmed strike, you can spend 3 ki points to start these imperceptible vibrations, which last for a number of days equal to your monk level. The vibrations are harmless unless you use your action to end them. To do so, you and the target must be on the same plane of existence. When you use this action, the creature must make a Constitution saving throw. If it fails, it is reduced to 0 hit points. If it succeeds, it takes 10d10 necrotic damage.

You can have only one creature under the effect of this feature at a time. You can choose to end the vibrations harmlessly without using an action."""
    print(feature)
    dnd_dict.character_dict["features"]['quivering_palm'] = feature

def shadow_monk3():
    feature = """Shadow Arts

Starting when you choose this tradition at 3rd level, you can use your ki to duplicate the effects of certain spells. As an action, you can spend 2 ki points to cast Darkness, Darkvision, Pass without Trace, or Silence, without providing material components. Additionally, you gain the Minor Illusion cantrip if you don't already know it."""
    print(feature)
    dnd_dict.character_dict["features"]['shadow_arts'] = feature
    dnd_dict.character_dict['player_class']['monk']['subclass'] = 'Way of the Shadow'

def shadow_monk6():
    feature = """Shadow Step

At 6th level, you gain the ability to step from one shadow into another. When you are in dim light or darkness, as a bonus action you can teleport up to 60 feet to an unoccupied space you can see that is also in dim light or darkness. You then have advantage on the first melee attack you make before the end of the turn."""
    print(feature)
    dnd_dict.character_dict["features"]['shadow_step'] = feature

def shadow_monk11():
    feature = """Cloak of Shadows

By 11th level, you have learned to become one with the shadows. When you are in an area of dim light or darkness, you can use your action to become invisible. You remain invisible until you make an attack, cast a spell, or are in an area of bright light."""
    print(feature)
    dnd_dict.character_dict["features"]['cloak_of_shadows'] = feature

def shadow_monk17():
    feature = """Opportunist

At 17th level, you can exploit a creature's momentary distraction when it is hit by an attack. Whenever a creature within 5 feet of you is hit by an attack made by a creature other than you, you can use your reaction to make a melee attack against that creature."""
    print(feature)
    dnd_dict.character_dict["features"]['opportunist_monk'] = feature

def breath_of_winter():
    feature = """Breath of Winter

Prerequisite: 17th Level
You can spend 6 ki points to cast Cone of Cold."""
    print(feature)
    dnd_dict.character_dict["features"]['breath_of_winter'] = feature
    dnd_dict.character_dict['elemental_disciplines']['breath_of_winter'] = 'Breath of Winter'

def clench_of_the_north_wind():
    feature = """Clench of the North Wind

Prerequisite: 6th Level
You can spend 3 ki points to cast Hold Person."""
    print(feature)
    dnd_dict.character_dict["features"]['clench_of_the_north_wind'] = feature
    dnd_dict.character_dict['elemental_disciplines']['clench_of_the_north_wind'] = 'Clench of the North Wind'

def elemental_attunement():
    feature = """Elemental Attunement

You can use your action to briefly control elemental forces within 30 feet of you, causing one of the following effects of your choice:

    Create a harmless, instantaneous sensory effect related to air, earth, fire, or water such as a shower of sparks, a puff of wind, a spray of light mist, or a gentle rumbling of stone.
    Instantaneously light or snuff out a candle, a torch, or a small campfire.
    Chill or warm up to 1 pound of nonliving material for up to 1 hour.
    Cause earth, fire, water, or mist that can fit within a 1-foot cube to shape itself into a crude form you designate for 1 minute.
"""
    print(feature)
    dnd_dict.character_dict["features"]['elemental_attunement'] = feature
    dnd_dict.character_dict['elemental_disciplines']['elemental_attunement'] = 'Elemental Attunement'

def eternal_mountain_defense():
    feature = """Eternal Mountain Defense

Prerequisite: 17th Level
You can spend 5 ki points to cast Stoneskin, targeting yourself."""
    print(feature)
    dnd_dict.character_dict["features"]['eternal_mountain_defense'] = feature
    dnd_dict.character_dict['elemental_disciplines']['eternal_mountain_defense'] = 'Eternal Mountain Defense'

def fangs_of_the_fire_snake():
    feature = """Fangs of the Fire Snake

When you use the Attack action on your turn, you can spend 1 ki point to cause tendrils of flame to stretch out from your fists and feet. Your reach with your unarmed strikes increases by 10 feet for that action, as well as the rest of the turn. A hit with such an attack deals fire damage instead of bludgeoning damage, and if you spend 1 ki point when the attack hits, it also deals an extra 1d10 fire damage."""
    print(feature)
    dnd_dict.character_dict["features"]['fangs_of_the_fire_snake'] = feature
    dnd_dict.character_dict['elemental_disciplines']['fangs_of_the_fire_snake'] = 'Fangs of the Fire Snake'

def fist_of_unbroken_air():
    feature = """Fist of Unbroken Air

You can create a blast of compressed air that strikes like a mighty fist. As an action, you can spend 2 ki points and choose a creature within 30 feet of you. That creature must make a Strength saving throw. On a failed save, the creature takes 3d10 bludgeoning damage, plus an extra 1d10 bludgeoning damage for each additional ki point you spend, and you can push the creature up to 20 feet away from you and knock it prone. On a successful save, the creature takes half as much damage, and you don't push it or knock it prone."""
    print(feature)
    dnd_dict.character_dict["features"]['fist_of_unbroken_air'] = feature
    dnd_dict.character_dict['elemental_disciplines']['fist_of_unbroken_air'] = 'Fist of Unbroken Air'

def flames_of_the_phoenix():
    feature = """Flames of the Phoenix

Prerequisite: 11th Level
You can spend 4 ki points to cast Fireball."""
    print(feature)
    dnd_dict.character_dict["features"]['flames_of_the_phoenix'] = feature
    dnd_dict.character_dict['elemental_disciplines']['flames_of_the_phoenix'] = 'Flames of the Phoenix'

def gong_of_the_summit():
    feature = """Gong of the Summit

Prerequisite: 6th Level
You can spend 3 ki points to cast Shatter."""
    print(feature)
    dnd_dict.character_dict["features"]['gong_of_the_summit'] = feature
    dnd_dict.character_dict['elemental_disciplines']['gong_of_the_summit'] = 'Gong of the Summit'

def mist_stance():
    feature = """Mist Stance

Prerequisite: 11th Level
You can spend 4 ki points to cast Gaseous Form, targeting yourself."""
    print(feature)
    dnd_dict.character_dict["features"]['mist_stance'] = feature
    dnd_dict.character_dict['elemental_disciplines']['mist_stance'] = 'Mist Stance'

def ride_the_wind():
    feature = """Ride the Wind

Prerequisite: 11th Level
You can spend 4 ki points to cast Fly, targeting yourself."""
    print(feature)
    dnd_dict.character_dict["features"]['ride_the_wind'] = feature
    dnd_dict.character_dict['elemental_disciplines']['ride_the_wind'] = 'Ride the Wind'

def river_of_hungry_flame():
    feature = """River of Hungry Flame

Prerequisite: 17th Level
You can spend 5 ki points to cast Wall of Fire."""
    print(feature)
    dnd_dict.character_dict["features"]['river_of_hungry_flame'] = feature
    dnd_dict.character_dict['elemental_disciplines']['river_of_hungry_flame'] = 'River of Hungry Flame'

def rush_of_the_gale_spirits():
    feature = """Rush of the Gale Spirits

You can spend 2 ki points to cast Gust of Wind."""
    print(feature)
    dnd_dict.character_dict["features"]['rush_of_the_gale_spirits'] = feature
    dnd_dict.character_dict['elemental_disciplines']['rush_of_the_gale_spirits'] = 'Rush of the Gale Spirits'

def shape_the_flowing_river():
    feature = """Shape the Flowing River

As an action, you can spend 1 ki point to choose an area of ice or water no larger than 30 feet on a side within 120 feet of you. You can change water to ice within the area and vice versa, and you can reshape ice in the area in any manner you choose. You can raise or lower the ice's elevation, create or fill in a trench, erect or flatten a wall, or form a pillar. The extent of any such changes can't exceed half the area's largest dimension. For example, if you affect a 30-foot square, you can create a pillar up to 15 feet high, raise or lower the square's elevation by up to 15 feet, dig a trench up to 15 feet deep, and so on. You can't shape the ice to trap or injure a creature in the area."""
    print(feature)
    dnd_dict.character_dict["features"]['shape_the_flowing_river'] = feature
    dnd_dict.character_dict['elemental_disciplines']['shape_the_flowing_river'] = 'Shape the Flowing River'

def sweeping_cinder_strike():
    feature = """Sweeping Cinder Strike

You can spend 2 ki points to cast Burning Hands."""
    print(feature)
    dnd_dict.character_dict["features"]['sweeping_cinder_strike'] = feature
    dnd_dict.character_dict['elemental_disciplines']['sweeping_cinder_strike'] = 'Sweeping Cinder Strike'

def water_whip():
    feature = """Water Whip

You can spend 2 ki points as an action to create a whip of water that shoves and pulls a creature to unbalance it. A creature that you can see that is within 30 feet of you must make a Dexterity saving throw. On a failed save, the creature takes 3d10 bludgeoning damage, plus an extra 1d10 bludgeoning damage for each additional ki point you spend, and you can either knock it prone or pull it up to 25 feet closer to you. On a successful save, the creature takes half as much damage, and you don't pull it or knock it prone.
"""
    print(feature)
    dnd_dict.character_dict["features"]['water_whip'] = feature
    dnd_dict.character_dict['elemental_disciplines']['water_whip'] = 'Water Whip'

def wave_of_rolling_earth():
    feature = """Wave of Rolling Earth

Prerequisite: 17th Level
You can spend 6 ki points to cast Wall of Stone."""
    print(feature)
    dnd_dict.character_dict["features"]['wave_of_rolling_earth'] = feature
    dnd_dict.character_dict['elemental_disciplines']['wave_of_rolling_earth'] = 'Wave of Rolling Earth'


def paladin2():
    dnd_fighting_styles.paladin_fighting_styles()
    feature = """Spellcasting

By 2nd level, you have learned to draw on divine magic through meditation and prayer to cast spells as a cleric does.
Preparing and Casting Spells

The Paladin table shows how many spell slots you have to cast your paladin spells. To cast one of your paladin spells of 1st level or higher, you must expend a slot of the spell's level or higher. You regain all expended spell slots when you finish a long rest.

You prepare the list of paladin spells that are available for you to cast, choosing from the paladin spell list. When you do so, choose a number of paladin spells equal to your Charisma modifier + half your paladin level, rounded down (minimum of one spell). The spells must be of a level for which you have spell slots.

For example, if you are a 5th-level paladin, you have four 1st-level and two 2nd-level spell slots. With a Charisma of 14, your list of prepared spells can include four spells of 1st or 2nd level, in any combination. If you prepare the 1st-level spell Cure Wounds, you can cast it using a 1st-level or a 2nd-level slot. Casting the spell doesn't remove it from your list of prepared spells.

You can change your list of prepared spells when you finish a long rest. Preparing a new list of paladin spells requires time spent in prayer and meditation: at least 1 minute per spell level for each spell on your list.
Spellcasting Ability

Charisma is your spellcasting ability for your paladin spells, since their power derives from the strength of your convictions. You use your Charisma whenever a spell refers to your spellcasting ability. In addition, you use your Charisma modifier when setting the saving throw DC for a paladin spell you cast and when making an attack roll with one.

Spell save DC = 8 + your proficiency bonus + your Charisma modifier

Spell attack modifier = your proficiency bonus + your Charisma modifier
Spellcasting Focus

You can use a holy symbol as a spellcasting focus for your paladin spells."""
    feature2 = """Divine Smite

Starting at 2nd level, when you hit a creature with a melee weapon attack, you can expend one spell slot to deal radiant damage to the target, in addition to the weapon's damage. The extra damage is 2d8 for a 1st-level spell slot, plus 1d8 for each spell level higher than 1st, to a maximum of 5d8. The damage increases by 1d8 if the target is an undead or a fiend, to a maximum of 6d8."""

    print(feature)
    print(feature2)
    dnd_dict.character_dict["features"]['divine_smite'] = feature2

def paladin3():
    feature = """Divine Health

By 3rd level, the divine magic flowing through you makes you immune to disease."""
    feature2 = """Harness Divine Power (Optional)

Also at 3rd level, you can expend a use of your Channel Divinity to fuel your spells. As a bonus action, you touch your holy symbol, utter a prayer, and regain one expended spell slot, the level of which can be no higher than half your proficiency bonus (rounded up). The number of times you can use this feature is based on the level you've reached in this class: 3rd level, once; 7th level, twice; and 15th level, thrice. You regain all expended uses when you finish a long rest."""

    feature3 = """Channel Divinity

Your oath allows you to channel divine energy to fuel magical effects. Each Channel Divinity option provided by your oath explains how to use it.

When you use your Channel Divinity, you choose which option to use. You must then finish a short or long rest to use your Channel Divinity again.

Some Channel Divinity effects require saving throws. When you use such an effect from this class, the DC equals your paladin spell save DC."""

    print(feature)
    dnd_dict.character_dict["features"]['divine_health'] = feature
    print(feature2)
    dnd_dict.character_dict["features"]['harness_divine_power'] = feature2
    print(feature3)
    dnd_dict.character_dict["features"]['channel_divinity_paladin'] = feature3


def paladin5():
    extra_attack()

def paladin6():
    feature = """Aura of Protection

Starting at 6th level, whenever you or a friendly creature within 10 feet of you must make a saving throw, the creature gains a bonus to the saving throw equal to your Charisma modifier (with a minimum bonus of +1). You must be conscious to grant this bonus.

At 18th level, the range of this aura increases to 30 feet."""
    print(feature)
    dnd_dict.character_dict["features"]['aura_of_protection'] = feature

def paladin10():
    feature = """Aura of Courage

Starting at 10th level, you and friendly creatures within 10 feet of you can't be frightened while you are conscious.

At 18th level, the range of this aura increases to 30 feet."""
    print(feature)
    dnd_dict.character_dict["features"]['aura_of_courage'] = feature

def paladin11():
    feature = """Improved Divine Smite

By 11th level, you are so suffused with righteous might that all your melee weapon strikes carry divine power with them. Whenever you hit a creature with a melee weapon, the creature takes an extra 1d8 radiant damage."""
    print(feature)
    dnd_dict.character_dict["features"]['improved_divine_smite'] = feature

def paladin14():
    feature = """Cleansing Touch

Beginning at 14th level, you can use your action to end one spell on yourself or on one willing creature that you touch.

You can use this feature a number of times equal to your Charisma modifier (a minimum of once). You regain expended uses when you finish a long rest."""
    print(feature)
    dnd_dict.character_dict["features"]['cleansing_touch'] = feature

def ancients_paladin3():
    feature = """Tenets of the Ancients

The tenets of the Oath of the Ancients have been preserved for uncounted centuries. This oath emphasizes the principles of good above any concerns of law or chaos. Its four central principles are simple.

Kindle the Light. Through your acts of mercy, kindness, and forgiveness, kindle the light of hope in the world, beating back despair.

Shelter the Light. Where there is good, beauty, love, and laughter in the world, stand against the wickedness that would swallow it. Where life flourishes, stand against the forces that would render it barren.

Preserve Your Own Light. Delight in song and laughter, in beauty and art. If you allow the light to die in your own heart, you can't preserve it in the world.

Be the Light. Be a glorious beacon for all who live in despair. Let the light of your joy and courage shine forth in all your deeds."""

    feature2 = """Oath Spells

You gain oath spells at the paladin levels listed.
Oath of the Ancients Spells
Paladin Level 	Spells
3rd 	Ensnaring Strike, Speak with Animals
5th 	Moonbeam, Misty Step
9th 	Plant Growth, Protection from Energy
13th 	Ice Storm, Stoneskin
17th 	Commune with Nature, Tree Stride"""

    feature3 = """Channel Divinity

When you take this oath at 3rd level, you gain the following two Channel Divinity options.

    Nature's Wrath. You can use your Channel Divinity to invoke primeval forces to ensnare a foe. As an action, you can cause spectral vines to spring up and reach for a creature within 10 feet of you that you can see. The creature must succeed on a Strength or Dexterity saving throw (its choice) or be restrained. While restrained by the vines, the creature repeats the saving throw at the end of each of its turns. On a success, it frees itself and the vines vanish.

    Turn the Faithless. You can use your Channel Divinity to utter ancient words that are painful for fey and fiends to hear. As an action, you present your holy symbol, and each fey or fiend within 30 feet of you that can hear you must make a Wisdom saving throw. On a failed save, the creature is turned for 1 minute or until it takes damage.

    A turned creature must spend its turns trying to move as far away from you as it can, and it can't willingly move to a space within 30 feet of you. It also can't take reactions. For its action, it can use only the Dash action or try to escape from an effect that prevents it from moving. If there's nowhere to move, the creature can use the Dodge action.

    If the creature's true form is concealed by an illusion, shapeshifting, or other effect, that form is revealed while it is turned.
"""

    print(feature)
    print(feature2)
    dnd_dict.character_dict["features"]['oath_spells'] = feature2
    print(feature3)
    dnd_dict.character_dict["features"]['channel_divinity_ancients'] = feature3

    added_spells = {'ensnaring_strike':'Ensnaring Strike','speak_with_animals':'Speak with Animals'}
    dnd_dict.character_dict['spells']['first'].update(added_spells)
    dnd_dict.character_dict['class_spells']['paladin']['first'].update(added_spells)
    dnd_dict.character_dict['special_spells']['first'].update(added_spells)
    dnd_dict.character_dict['player_class']['paladin']['subclass'] = 'Oath of the Ancients'

def ancients_paladin5():
    added_spells = {'moonbeam':'Moonbeam','misty_step':'Misty Step'}
    dnd_dict.character_dict['spells']['second'].update(added_spells)
    dnd_dict.character_dict['class_spells']['paladin']['second'].update(added_spells)
    dnd_dict.character_dict['special_spells']['second'].update(added_spells)

def ancients_paladin7():
    feature = """Aura of Warding

Beginning at 7th level, ancient magic lies so heavily upon you that it forms an eldritch ward. You and friendly creatures within 10 feet of you have resistance to damage from spells.

At 18th level, the range of this aura increases to 30 feet."""
    print(feature)
    dnd_dict.character_dict["features"]['aura_of_warding'] = feature

def ancients_paladin9():
    added_spells = {'plant_growth':'Plant Growth','protection_from_energy':'Protection from Energy'}
    dnd_dict.character_dict['spells']['third'].update(added_spells)
    dnd_dict.character_dict['class_spells']['paladin']['third'].update(added_spells)
    dnd_dict.character_dict['special_spells']['third'].update(added_spells)

def ancients_paladin13():
    added_spells = {'ice_storm':'Ice Storm','stoneskin':'Stoneskin'}
    dnd_dict.character_dict['spells']['fourth'].update(added_spells)
    dnd_dict.character_dict['class_spells']['paladin']['fourth'].update(added_spells)
    dnd_dict.character_dict['special_spells']['fourth'].update(added_spells)

def ancients_paladin15():
    feature = """Undying Sentinel

Starting at 15th level, when you are reduced to 0 hit points and are not killed outright, you can choose to drop to 1 hit point instead. Once you use this ability, you can't use it again until you finish a long rest.

Additionally, you suffer none of the drawbacks of old age, and you can't be aged magically."""
    print(feature)
    dnd_dict.character_dict["features"]['undying_sentinal'] = feature

def ancients_paladin17():
    added_spells = {'commune_with_nature':'Commune with Nature','tree_stride':'Tree Stride'}
    dnd_dict.character_dict['spells']['fifth'].update(added_spells)
    dnd_dict.character_dict['class_spells']['paladin']['fifth'].update(added_spells)
    dnd_dict.character_dict['special_spells']['fifth'].update(added_spells)

def ancients_paladin20():
    feature = """Elder Champion

At 20th level, you can assume the form of an ancient force of nature, taking on an appearance you choose. For example, your skin might turn green or take on a bark-like texture, your hair might become leafy or moss-like, or you might sprout antlers or a lion-like mane.

Using your action, you undergo a transformation. For 1 minute, you gain the following benefits:

    At the start of each of your turns, you regain 10 hit points.

    Whenever you cast a paladin spell that has a casting time of 1 action, you can cast it using a bonus action instead.

    Enemy creatures within 10 feet of you have disadvantage on saving throws against your paladin spells and Channel Divinity options.

Once you use this feature, you can't use it again until you finish a long rest."""
    print(feature)
    dnd_dict.character_dict["features"]['elder_champion'] = feature

def devotion_paladin3():
    feature = """Tenets of Devotion

Though the exact words and strictures of the Oath of Devotion vary, paladins of this oath share these tenets.

Honesty. Don't lie or cheat. Let your word be your promise.

Courage. Never fear to act, though caution is wise.

Compassion. Aid others, protect the weak, and punish those who threaten them. Show mercy to your foes, but temper it with wisdom.

Honor. Treat others with fairness, and let your honorable deeds be an example to them. Do as much good as possible while causing the least amount of harm.

Duty. Be responsible for your actions and their consequences, protect those entrusted to your care, and obey those who have just authority over you."""

    feature2 = """Oath Spells

You gain oath spells at the paladin levels listed.
Oath of Devotion Spells
Paladin Level 	Spells
3rd 	Protection from Evil and Good, Sanctuary
5th 	Lesser Restoration, Zone of Truth
9th 	Beacon of Hope, Dispel Magic
13th 	Freedom of Movement, Guardian of Faith
17th 	Commune, Flame Strike"""

    feature3 = """Channel Divinity

When you take this oath at 3rd level, you gain the following two Channel Divinity options.

    Sacred Weapon. As an action, you can imbue one weapon that you are holding with positive energy, using your Channel Divinity. For 1 minute, you add your Charisma modifier to attack rolls made with that weapon (with a minimum bonus of +1). The weapon also emits bright light in a 20-foot radius and dim light 20 feet beyond that. If the weapon is not already magical, it becomes magical for the duration.

    You can end this effect on your turn as part of any other action. If you are no longer holding or carrying this weapon, or if you fall unconscious, this effect ends.

    Turn the Unholy. As an action, you present your holy symbol and speak a prayer censuring fiends and undead, using your Channel Divinity. Each fiend or undead that can see or hear you within 30 feet of you must make a Wisdom saving throw. If the creature fails its saving throw, it is turned for 1 minute or until it takes damage.

    A turned creature must spend its turns trying to move as far away from you as it can, and it can't willingly move to a space within 30 feet of you. It also can't take reactions. For its action, it can use only the Dash action or try to escape from an effect that prevents it from moving. If there's nowhere to move, the creature can use the Dodge action.
"""

    print(feature)
    print(feature2)
    dnd_dict.character_dict["features"]['oath_spells'] = feature2
    print(feature3)
    dnd_dict.character_dict["features"]['channel_divinity_devotion'] = feature3

    added_spells = {'protection_from_evil_and_good':'Protection from Evil and Good','sanctuary':'Sanctuary'}
    dnd_dict.character_dict['spells']['first'].update(added_spells)
    dnd_dict.character_dict['class_spells']['paladin']['first'].update(added_spells)
    dnd_dict.character_dict['special_spells']['first'].update(added_spells)
    dnd_dict.character_dict['player_class']['paladin']['subclass'] = 'Oath of Devotion'

def devotion_paladin5():
    added_spells = {'lesser_restoration':'Lesser Restoration','zone_of_truth':'Zone of Truth'}
    dnd_dict.character_dict['spells']['second'].update(added_spells)
    dnd_dict.character_dict['class_spells']['paladin']['second'].update(added_spells)
    dnd_dict.character_dict['special_spells']['second'].update(added_spells)

def devotion_paladin7():
    feature = """Aura of Devotion

Starting at 7th level, you and friendly creatures within 10 feet of you can't be charmed while you are conscious.

At 18th level, the range of this aura increases to 30 feet."""
    print(feature)
    dnd_dict.character_dict["features"]['aura_of_devotion'] = feature

def devotion_paladin9():
    added_spells = {'beacon_of_hope':'Beacon of Hope','dispel_magic':'Dispel Magic'}
    dnd_dict.character_dict['spells']['third'].update(added_spells)
    dnd_dict.character_dict['class_spells']['paladin']['third'].update(added_spells)
    dnd_dict.character_dict['special_spells']['third'].update(added_spells)

def devotion_paladin13():
    added_spells = {'freedom_of_movement':'Freedom of Movement','guardian_of_faith':'Guardian of Faith'}
    dnd_dict.character_dict['spells']['fourth'].update(added_spells)
    dnd_dict.character_dict['class_spells']['paladin']['fourth'].update(added_spells)
    dnd_dict.character_dict['special_spells']['fourth'].update(added_spells)

def devotion_paladin15():
    feature = """Purity of Spirit

Beginning at 15th level, you are always under the effects of a Protection from Evil and Good spell."""
    print(feature)
    dnd_dict.character_dict["features"]['purity_of_spirit'] = feature

def devotion_paladin17():
    added_spells = {'commune':'Commune','flame_strike':'Flame Strike'}
    dnd_dict.character_dict['spells']['fifth'].update(added_spells)
    dnd_dict.character_dict['class_spells']['paladin']['fifth'].update(added_spells)
    dnd_dict.character_dict['special_spells']['fifth'].update(added_spells)

def devotion_paladin20():
    feature = """Holy Nimbus

At 20th level, as an action, you can emanate an aura of sunlight. For 1 minute, bright light shines from you in a 30-foot radius, and dim light shines 30 feet beyond that.

Whenever an enemy creature starts its turn in the bright light, the creature takes 10 radiant damage.

In addition, for the duration, you have advantage on saving throws against spells cast by fiends or undead.

Once you use this feature, you can't use it again until you finish a long rest."""
    print(feature)
    dnd_dict.character_dict["features"]['holy_nimbus'] = feature

def vengeance_paladin3():
    feature = """Tenets of Vengeance

The tenets of the Oath of Vengeance vary by paladin, but all the tenets revolve around punishing wrongdoers by any means necessary. Paladins who uphold these tenets are willing to sacrifice even their own righteousness to mete out justice upon those who do evil, so the paladins are often neutral or lawful neutral in alignment. The core principles of the tenets are brutally simple.

Fight the Greater Evil. Faced with a choice of fighting my sworn foes or combating a lesser evil, I choose the greater evil.

No Mercy for the Wicked. Ordinary foes might win my mercy, but my sworn enemies do not.

By Any Means Necessary. My qualms can't get in the way of exterminating my foes.

Restitution. If my foes wreak ruin on the world, it is because I failed to stop them. I must help those harmed by their misdeeds."""

    feature2 = """Oath Spells

You gain oath spells at the paladin levels listed.
Oath of Vengeance Spells
Paladin Level 	Spells
3rd 	Bane, Hunter's Mark
5th 	Hold Person, Misty Step
9th 	Haste, Protection from Energy
13th 	Banishment, Dimension Door
17th 	Hold Monster, Scrying"""

    feature3 = """Channel Divinity

When you take this oath at 3rd level, you gain the following two Channel Divinity options.

    Abjure Enemy. As an action, you present your holy symbol and speak a prayer of denunciation, using your Channel Divinity. Choose one creature within 60 feet of you that you can see. That creature must make a Wisdom saving throw, unless it is immune to being frightened. Fiends and undead have disadvantage on this saving throw.

    On a failed save, the creature is frightened for 1 minute or until it takes any damage. While frightened, the creature's speed is 0, and it can't benefit from any bonus to its speed.

    On a successful save, the creature's speed is halved for 1 minute or until the creature takes any damage.

    Vow of Enmity. As a bonus action, you can utter a vow of enmity against a creature you can see within 10 feet of you, using your Channel Divinity. You gain advantage on attack rolls against the creature for 1 minute or until it drops to 0 hit points or falls unconscious.
"""

    print(feature)
    print(feature2)
    dnd_dict.character_dict["features"]['oath_spells'] = feature2
    print(feature3)
    dnd_dict.character_dict["features"]['channel_divinity_vengeance'] = feature3

    added_spells = {'bane':'Bane','hunter\'s_mark':'Hunter\'s Mark'}
    dnd_dict.character_dict['spells']['first'].update(added_spells)
    dnd_dict.character_dict['class_spells']['paladin']['first'].update(added_spells)
    dnd_dict.character_dict['special_spells']['first'].update(added_spells)
    dnd_dict.character_dict['player_class']['paladin']['subclass'] = 'Oath of Vengeance'

def vengeance_paladin5():
    added_spells = {'hold_person':'Hold Person','misty_step':'Misty Step'}
    dnd_dict.character_dict['spells']['second'].update(added_spells)
    dnd_dict.character_dict['class_spells']['paladin']['second'].update(added_spells)
    dnd_dict.character_dict['special_spells']['second'].update(added_spells)

def vengeance_paladin7():
    feature = """Relentless Avenger

By 7th level, your supernatural focus helps you close off a foe's retreat. When you hit a creature with an opportunity attack, you can move up to half your speed immediately after the attack and as part of the same reaction. This movement doesn't provoke opportunity attacks."""
    print(feature)
    dnd_dict.character_dict["features"]['relentless_avenger'] = feature

def vengeance_paladin9():
    added_spells = {'haste':'Haste','protection_from_energy':'Protection from Energy'}
    dnd_dict.character_dict['spells']['third'].update(added_spells)
    dnd_dict.character_dict['class_spells']['paladin']['third'].update(added_spells)
    dnd_dict.character_dict['special_spells']['third'].update(added_spells)

def vengeance_paladin13():
    added_spells = {'banishment':'Banishment','dimension_door':'Dimension Door'}
    dnd_dict.character_dict['spells']['fourth'].update(added_spells)
    dnd_dict.character_dict['class_spells']['paladin']['fourth'].update(added_spells)
    dnd_dict.character_dict['special_spells']['fourth'].update(added_spells)

def vengeance_paladin15():
    feature = """Soul of Vengeance

Starting at 15th level, the authority with which you speak your Vow of Enmity gives you greater power over your foe. When a creature under the effect of your Vow of Enmity makes an attack, you can use your reaction to make a melee weapon attack against that creature if it is within range."""

    print(feature)
    dnd_dict.character_dict["features"]['soul_of_vengeance'] = feature

def vengeance_paladin17():
    added_spells = {'hold_monster':'Hold Monster','scrying':'Scrying'}
    dnd_dict.character_dict['spells']['fifth'].update(added_spells)
    dnd_dict.character_dict['class_spells']['paladin']['fifth'].update(added_spells)
    dnd_dict.character_dict['special_spells']['fifth'].update(added_spells)

def vengeance_paladin20():
    feature = """Avenging Angel

At 20th level, you can assume the form of an angelic avenger. Using your action, you undergo a transformation. For 1 hour, you gain the following benefits:

    Wings sprout from your back and grant you a flying speed of 60 feet.

    You emanate an aura of menace in a 30-foot radius. The first time any enemy creature enters the aura or starts its turn there during a battle, the creature must succeed on a Wisdom saving throw or become frightened of you for 1 minute or until it takes any damage. Attack rolls against the frightened creature have advantage.

Once you use this feature, you can't use it again until you finish a long rest."""

    print(feature)
    dnd_dict.character_dict["features"]['avenging_angel'] = feature

def uncanny_dodge():
    feature = """Uncanny Dodge

Starting at 5th level, when an attacker that you can see hits you with an attack, you can use your reaction to halve the attack's damage against you."""
    print(feature)
    dnd_dict.character_dict["features"]['uncanny_dodge'] = feature

def ranger2():
    dnd_fighting_styles.ranger_fighting_styles()
    x=1
    for x in range(x,3):
        if x < 3:
            print(f'{x}/2')
            dnd_skills.spell_add(dnd_magic.ranger_first,dnd_dict.character_dict['spells']['first'],dnd_dict.character_dict['class_spells']['ranger']['first'])
            x+=1
            continue
        elif x == 3:
            break
        

    feature = """Spellcasting

By the time you reach 2nd level, you have learned to use the magical essence of nature to cast spells, much as a druid does.
Spell Slots

The Ranger table shows how many spell slots you have to cast your ranger spells of 1st level and higher. To cast one of these spells, you must expend a slot of the spell's level or higher. You regain all expended spell slots when you finish a long rest.

For example, if you know the 1st-level spell Animal Friendship and have a 1st-level and a 2nd-level spell slot available, you can cast Animal Friendship using either slot.
Spells Known of 1st Level and Higher

You know two 1st-level spells of your choice from the ranger spell list.

The Spells Known column of the Ranger table shows when you learn more ranger spells of your choice. Each of these spells must be of a level for which you have spell slots. For instance, when you reach 5th level in this class, you can learn one new spell of 1st or 2nd level.

Additionally, when you gain a level in this class, you can choose one of the ranger spells you know and replace it with another spell from the ranger spell list, which also must be of a level for which you have spell slots.
Spellcasting Ability

Wisdom is your spellcasting ability for your ranger spells, since your magic draws on your attunement to nature. You use your Wisdom whenever a spell refers to your spellcasting ability. In addition, you use your Wisdom modifier when setting the saving throw DC for a ranger spell you cast and when making an attack roll with one.

Spell save DC = 8 + your proficiency bonus + your Wisdom modifier

Spell attack modifier = your proficiency bonus + your Wisdom modifier"""
    feature2 = """Spellcasting Focus (Optional)

At 2nd level, you can use a druidic focus as a spellcasting focus for your ranger spells. A druidic focus might be a sprig of mistletoe or holly, a wand or rod made of yew or another special wood, a staff drawn whole from a living tree, or an object incorporating feathers, fur, bones, and teeth from sacred animals."""
    print(feature)
    print(feature2)
    dnd_dict.character_dict["features"]['ranger_focus'] = feature2

def ranger3():
    feature = """Primeval Awareness

Beginning at 3rd level, you can use your action and expend one ranger spell slot to focus your awareness on the region around you. For 1 minute per level of the spell slot you expend, you can sense whether the following types of creatures are present within 1 mile of you (or within up to 6 miles if you are in your favored terrain): aberrations, celestials, dragons, elementals, fey, fiends, and undead. This feature doesn’t reveal the creatures’ location or number."""
    feature2 = """Primal Awareness (Optional)

This 3rd-level feature replaces the Primeval Awareness feature. You gain no benefit from the replaced feature and don't qualify for anything in the game that requires it.

You can focus your awareness through the interconnections of nature: you learn additional spells when you reach certain levels in this class if you don't already know them, as shown in the Primal Awareness Spells table. These spells don't count against the number of ranger spells you know.
Primal Awareness Spells 	
Ranger Level 	Spell
3rd 	Speak with Animals
5th 	Beast Sense
9th 	Speak with Plants
13th 	Locate Creature
17th 	Commune with Nature

You can cast each of these spells once without expending a spell slot. Once you cast a spell in this way, you can't do so again until you finish a long rest."""
    print(feature)
    print(feature2)

    while True:
        choice = input("""Do you want the Old or New Primeval Awareness Feature?
1) Old
2) New
 Enter your selection: """)
        if choice == '1':
            dnd_dict.character_dict["features"]['primeval_awareness_old'] = feature
            break

        elif choice == '2':
            dnd_dict.character_dict["features"]['primeval_awareness_new'] = feature2
            dnd_dict.character_dict['spells']['first']['speak_with_animals'] = 'Speak with Animals'
            dnd_dict.character_dict['special_spells']['first']['speak_with_animals'] = 'Speak with Animals'
            break

        else:
            print("Error: Invalid Input")
            continue


def ranger5():
    extra_attack()
    if 'primeval_awareness_new' in dnd_dict.character_dict['features']:
        dnd_dict.character_dict['spells']['second']['beast_sense'] = 'Beast Sense'
        dnd_dict.character_dict['special_spells']['second']['beast_sense'] = 'Beast Sense'

def ranger6():
    if 'deft_explorer' in dnd_dict.character_dict['features']:
        roving()
    if 'natural_explorer' in dnd_dict.character_dict['features']:
        natural_explorer()
    if 'favored_enemy' in dnd_dict.character_dict['features']:
        favored_enemy_after()

def ranger8():
    feature = """Land's Stride

Starting at 8th level, moving through nonmagical difficult terrain costs you no extra movement. You can also pass through nonmagical plants without being slowed by them and without taking damage from them if they have thorns, spines, or a similar hazard.

In addition, you have advantage on saving throws against plants that are magically created or manipulated to impede movement, such those created by the Entangle spell."""
    print(feature)
    dnd_dict.character_dict["features"]['land\'s_stride'] = feature

def ranger9():
    if 'primeval_awareness_new' in dnd_dict.character_dict['features']:
        dnd_dict.character_dict['spells']['third']['speak_with_plants'] = 'Speak with Plants'
        dnd_dict.character_dict['special_spells']['third']['speak_with_plants'] = 'Speak with Plants'

def ranger10():
    feature = """Hide in Plain Sight

Starting at 10th level, you can spend 1 minute creating camouflage for yourself. You must have access to fresh mud, dirt, plants, soot, and other naturally occurring materials with which to create your camouflage.

Once you are camouflaged in this way, you can try to hide by pressing yourself up against a solid surface, such as a tree or wall, that is at least as tall and wide as you are. You gain a +10 bonus to Dexterity (Stealth) checks as long as you remain there without moving or taking actions. Once you move or take an action or a reaction, you must camouflage yourself again to gain this benefit."""
    feature2 = """Nature's Veil (Optional)

This 10th-level feature replaces the Hide in Plain Sight feature. You gain no benefit from the replaced feature and don't qualify for anything in the game that requires it.

You draw on the powers of nature to hide yourself from view briefly. As a bonus action, you can magically become invisible, along with any equipment you are wearing or carrying, until the start of your next turn.

You can use this feature a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest."""

    print(feature)
    print(feature2)
    while True:
        choice = input("""Do you want the Hide in Plain Sight or Nature's Veil Feature?
1) Hide in Plain Sight
2) Nature's Veil
 Enter your selection: """)
        if choice == '1':
            dnd_dict.character_dict["features"]['hide_in_plain_sight'] = feature
            break

        elif choice == '2':
            dnd_dict.character_dict["features"]['nature\'s_veil'] = feature2
            break

        else:
            print("Error: Invalid Input")
            continue

    if 'deft_explorer' in dnd_dict.character_dict['features']:
        tireless()

    if 'natural_explorer' in dnd_dict.character_dict['features']:
        natural_explorer()



def ranger13():
    if 'primeval_awareness_new' in dnd_dict.character_dict['features']:
        dnd_dict.character_dict['spells']['fourth']['locate_creature'] = 'Locate Creature'
        dnd_dict.character_dict['special_spells']['fourth']['locate_creature'] = 'Locate Creature'

def ranger14():
    feature = """Vanish

Starting at 14th level, you can use the Hide action as a bonus action on your turn. Also, you can't be tracked by nonmagical means, unless you choose to leave a trail."""
    print(feature)
    dnd_dict.character_dict["features"]['vanish_ranger'] = feature
    if 'favored_enemy' in dnd_dict.character_dict['features']:
        favored_enemy_after()


def ranger17():
    if 'primeval_awareness_new' in dnd_dict.character_dict['features']:
        dnd_dict.character_dict['spells']['fifth']['commune_with_nature'] = 'Commune with Nature'
        dnd_dict.character_dict['special_spells']['fifth']['commune_with_nature'] = 'Commune with Nature'

def ranger18():
    feature = """Feral Senses

At 18th level, you gain preternatural senses that help you fight creatures you can't see. When you attack a creature you can't see, your inability to see it doesn't impose disadvantage on your attack rolls against it.

You are also aware of the location of any invisible creature within 30 feet of you, provided that the creature isn't hidden from you and you aren't blinded or deafened."""
    print(feature)
    dnd_dict.character_dict["features"]['feral_senses_ranger'] = feature

def ranger20():
    feature = """Foe Slayer

At 20th level, you become an unparalleled hunter of your enemies. Once on each of your turns, you can add your Wisdom modifier to the attack roll or the damage roll of an attack you make against one of your favored enemies. You can choose to use this feature before or after the roll, but before any effects of the roll are applied."""
    print(feature)
    dnd_dict.character_dict["features"]['foe_slayer'] = feature

def beast_master_ranger3():

    feature = """Ranger's Companion

At 3rd level, you gain a beast companion that accompanies you on your adventures and is trained to fight alongside you. Choose a beast that is no larger than Medium and that has a challenge rating of 1/4 or lower (appendix D presents statistics for the hawk, mastiff, and panther as examples). Add your proficiency bonus to the beast’s AC, attack rolls, and damage rolls, as well as to any saving throws and skills it is proficient in. Its hit point maximum equals its normal maximum or four times your ranger level, whichever is higher. Like any creature, the beast can spend Hit Dice during a short rest.

The beast obeys your commands as best as it can. It takes its turn on your initiative. On your turn, you can verbally command the beast where to move (no action required by you). You can use your action to verbally command it to take the Attack, Dash, Disengage, or Help action. If you don’t issue a command, the beast takes the Dodge action. Once you have the Extra Attack feature, you can make one weapon attack yourself when you command the beast to take the Attack action. While traveling through your favored terrain with only the beast, you can move stealthily at a normal pace.

If you are incapacitated or absent, the beast acts on its own, focusing on protecting you and itself. The beast never requires your command to use its reaction, such as when making an opportunity attack.

If the beast dies, you can obtain another one by spending 8 hours magically bonding with another beast that isn’t hostile to you, either the same type of beast as before or a different one."""

    feature2 = """Primal Companion (Optional)

This 3rd-level feature replaces the Ranger's Companion feature.

You magically summon a primal beast, which draws strength from your bond with nature. The beast is friendly to you and your companions and obeys your commands. Choose its stat block-Beast of the Land, Beast of the Sea, or Beast of the Sky-which uses your proficiency bonus (PB) in several places. You also determine the kind of animal the beast is, choosing a kind appropriate for the stat block. Whatever kind you choose, the beast bears primal markings, indicating its mystical origin.

In combat, the beast acts during your turn. It can move and use its reaction on its own, but the only action it takes is the Dodge action, unless you take a bonus action on your turn to command it to take another action. That action can be one in its stat block or some other action. You can also sacrifice one of your attacks when you take the Attack action to command the beast to take the Attack action. If
you are incapacitated, the beast can take any action of its choice, not just Dodge.

If the beast has died within the last hour, you can use your action to touch it and expend a spell slot of 1st level or higher. The beast returns to life after 1 minute with all its hit points restored. When you finish a long rest, you can summon a different primal beast. The new beast appears in an unoccupied space within 5 feet of you, and you choose its stat block and appearance. If you already have a beast from this feature, it vanishes when the new beast appears. The beast also vanishes if you die.
Beast of the Land
Medium beast
Armor Class: 13 + PB (natural armor)
Hit Points: 5 + five times your ranger level (the beast has a number of Hit Dice [d8s] equal to your ranger level)
Speed: 40 ft., climb 40ft.
STR 	DEX 	CON 	INT 	WIS 	CHA
14 (+2) 	14 (+2) 	15 (+2) 	8 (−1) 	14 (+2) 	11 (+0)
Senses: darkvision 60 ft., passive Perception 12
Languages: understands the languages you speak
Challenge: —
Proficiency Bonus (PB): equals your bonus
Charge: If the beast moves at least 20 feet straight toward a target and then hits it with a maul attack on the same turn, the target takes an extra ld6 slashing damage. If the target is a creature, it must succeed on a Strength saving throw against your spell save DC or be knocked prone.
Primal Bond: You can add your proficiency bonus to any ability check or saving throw that the beast makes.
Actions
Maul. Melee Weapon Attack: your spell attack modifier to hit, reach 5 ft., one target. Hit: 1d8 + 2 + PB slashing damage.
Beast of the Sea
Medium beast
Armor Class: 13 + PB (natural armor)
Hit Points: 5 + five times your ranger level (the beast has a number of Hit Dice [d8s] equal to your ranger level)
Speed: 5 ft., swim 60ft.
STR 	DEX 	CON 	INT 	WIS 	CHA
14 (+2) 	14 (+2) 	15 (+2) 	8 (−1) 	14 (+2) 	11 (+0)
Senses: darkvision 60 ft., passive Perception 12
Languages: understands the languages you speak
Challenge: —
Proficiency Bonus (PB): equals your bonus
Amphibious: The beast can breathe both air and water.
Primal Bond: You can add your proficiency bonus to any ability check or saving throw that the beast makes.
Actions
Binding Strike. Melee Weapon Attack: your spell attack modifier to hit, reach 5 ft., one target. Hit: 1d6 + 2 + PB piercing or bludgeoning damage (your choice), and the target is grappled (escape DC equals your spell save DC). Until this grapple ends, the beast can't use this attack on another target.
Beast of the Sky
Small beast
Armor Class: 13 + PB (natural armor)
Hit Points: 4 + four times your ranger level (the beast has a number of Hit Dice [d6s] equal to your ranger level)
Speed: 10 ft., fly 60ft.
STR 	DEX 	CON 	INT 	WIS 	CHA
6 (-2) 	16 (+3) 	13 (+1) 	8 (−1) 	14 (+2) 	11 (+0)
Senses: darkvision 60 ft., passive Perception 12
Languages: understands the languages you speak
Challenge: —
Proficiency Bonus (PB): equals your bonus
Flyby: The beast doesn't provoke opportunity attacks when it flies out of an enemy's reach.
Primal Bond: You can add your proficiency bonus to any ability check or saving throw that the beast makes.
Actions
Shred. Melee Weapon Attack: your spell attack modifier to hit, reach 5 ft., one target. Hit: 1d4 + 3 + PB slashing damage.
"""

    print(feature)
    print(feature2)
    while True:
        choice = input("""Do you want the Ranger's Companion or Primal Companion Feature?
1) Ranger's Companion
2) Primal Companion
 Enter your selection: """)
        if choice == '1':
            dnd_dict.character_dict["features"]['ranger\'s_companion'] = feature
            break

        elif choice == '2':
            dnd_dict.character_dict["features"]['primal_companion'] = feature2
            break

        else:
            print("Error: Invalid Input")
            continue

def beast_master_ranger7():
    feature = """Exceptional Training

Beginning at 7th level, on any of your turns when your beast companion doesn’t attack, you can use a bonus action to command the beast to take the Dash, Disengage, or Help action on its turn. In addition, the beast’s attacks now count as magical for the purpose of overcoming resistance and immunity to nonmagical attacks and damage."""
    print(feature)
    dnd_dict.character_dict["features"]['exceptional_training'] = feature

def beast_master_ranger11():
    feature = """Bestial Fury

Starting at 11th level, when you command your beast companion to take the Attack action, the beast can make two attacks, or it can take the Multiattack action if it has that action."""
    print(feature)
    dnd_dict.character_dict["features"]['beastial_fury_ranger'] = feature

def beast_master_ranger15():
    feature = """Share Spells

Beginning at 15th level, when you cast a spell targeting yourself, you can also affect your beast companion with the spell if the beast is within 30 feet of you."""
    print(feature)
    dnd_dict.character_dict["features"]['share_spells_ranger'] = feature

def hunter_ranger3():
    feature = """Hunter's Prey

At 3rd level, you gain one of the following features of your choice.

    Colossus Slayer. Your tenacity can wear down the most potent foes. When you hit a creature with a weapon attack, the creature takes an extra 1d8 damage if it’s below its hit point maximum. You can deal this extra damage only once per turn.

    Giant Killer. When a Large or larger creature within 5 feet of you hits or misses you with an attack, you can use your reaction to attack that creature immediately after its attack, provided that you can see the creature.

    Horde Breaker. Once on each of your turns when you make a weapon attack, you can make another attack with the same weapon against a different creature that is within 5 feet of the original target and within range of your weapon.
"""
    feature2 = """Colossus Slayer. Your tenacity can wear down the most potent foes. When you hit a creature with a weapon attack, the creature takes an extra 1d8 damage if it’s below its hit point maximum. You can deal this extra damage only once per turn."""

    feature3 = """Giant Killer. When a Large or larger creature within 5 feet of you hits or misses you with an attack, you can use your reaction to attack that creature immediately after its attack, provided that you can see the creature."""

    feature4 = """Horde Breaker. Once on each of your turns when you make a weapon attack, you can make another attack with the same weapon against a different creature that is within 5 feet of the original target and within range of your weapon."""

    print(feature)
    while True:
        choice = input("""Do you want the Collossus Slayer, Giant Killer, or Horde Breaker Feature?
1) Collossus Slayer
2) Giant Killer
3) Horde Breaker
 Enter your selection: """)
        if choice == '1':
            dnd_dict.character_dict["features"]['hunter\'s_prey_collossus_slayer'] = feature2
            break

        elif choice == '2':
            dnd_dict.character_dict["features"]['hunter\'s_prey_giant_killer'] = feature3
            break

        elif choice == '3':
            dnd_dict.character_dict["features"]['hunter\'s_prey_horde_breaker'] = feature4
            break

        else:
            print("Error: Invalid Input")
            continue


def hunter_ranger7():
    feature = """Defensive Tactics

At 7th level, you gain one of the following features of your choice.

    Escape the Horde. Opportunity attacks against you are made with disadvantage.

    Multiattack Defense. When a creature hits you with an attack, you gain a +4 bonus to AC against all subsequent attacks made by that creature for the rest of the turn.

    Steel Will. You have advantage on saving throws against being frightened.
"""

    feature2 = """Escape the Horde. Opportunity attacks against you are made with disadvantage."""

    feature3 = """Multiattack Defense. When a creature hits you with an attack, you gain a +4 bonus to AC against all subsequent attacks made by that creature for the rest of the turn."""

    feature4 = """Steel Will. You have advantage on saving throws against being frightened."""

    print(feature)
    while True:
        choice = input("""Do you want the Escape the Horde, Multiattack Defense, or the Steel Will Feature?
1) Escape the Horde
2) Multiattack Defense
3) Steel Will
 Enter your selection: """)
        if choice == '1':
            dnd_dict.character_dict["features"]['defensive_tactics_escape_the_horde'] = feature2
            break

        elif choice == '2':
            dnd_dict.character_dict["features"]['defensive_tactics_multiattack_defense'] = feature3
            break

        elif choice == '3':
            dnd_dict.character_dict["features"]['defensive_tactics_steel_will'] = feature4
            break

        else:
            print("Error: Invalid Input")
            continue


def hunter_ranger11():
    feature = """Multiattack

At 11th level, you gain one of the following features of your choice.

    Volley. You can use your action to make a ranged attack against any number of creatures within 10 feet of a point you can see within your weapon’s range. You must have ammunition for each target, as normal, and you make a separate attack roll for each target

    Whirlwind Attack. You can use your action to make melee attacks against any number of creatures within 5 feet of you, with a separate attack roll for each target.
"""
    feature2 = """Volley. You can use your action to make a ranged attack against any number of creatures within 10 feet of a point you can see within your weapon’s range. You must have ammunition for each target, as normal, and you make a separate attack roll for each target."""

    feature3 = """Whirlwind Attack. You can use your action to make melee attacks against any number of creatures within 5 feet of you, with a separate attack roll for each target."""

    print(feature)
    while True:
        choice = input("""Do you want the Volley or Whirlwind Attack Feature?
1) Volley
2) Whirlwind Attack
 Enter your selection: """)
        if choice == '1':
            dnd_dict.character_dict["features"]['multiattack_volley'] = feature2
            break

        elif choice == '2':
            dnd_dict.character_dict["features"]['multiattack_whirlwind_attack'] = feature2
            break


        else:
            print("Error: Invalid Input")
            continue

def hunter_ranger15():
    feature = """Superior Hunter's Defense

At 15th level, you gain one of the following features of your choice.

    Evasion. When you are subjected to an effect, such as a red dragon’s fiery breath or a lightning bolt spell, that allows you to make a Dexterity saving throw to take only half damage, you instead take no damage if you succeed on a saving throw, and only half damage if you fail

    Stand Against the Tide. When a hostile creature misses you with a melee attack, you can use your reaction to force that creature to repeat the same attack against another creature (other than itself) of your choice.

    Uncanny Dodge. When an attacker that you can see hits you with an attack, you can use your reaction to halve the attack’s damage against you.
"""

    feature2 = """Evasion. When you are subjected to an effect, such as a red dragon’s fiery breath or a lightning bolt spell, that allows you to make a Dexterity saving throw to take only half damage, you instead take no damage if you succeed on a saving throw, and only half damage if you fail"""

    feature3 = """Stand Against the Tide. When a hostile creature misses you with a melee attack, you can use your reaction to force that creature to repeat the same attack against another creature (other than itself) of your choice."""

    feature4 = """Uncanny Dodge. When an attacker that you can see hits you with an attack, you can use your reaction to halve the attack’s damage against you."""

    print(feature)
    while True:
        choice = input("""Do you want the Evasion, Stand Against the Tide or Uncanny Dodge Feature?
1) Evasion
2) Stand Against the Tide
3) Uncanny Dodge
 Enter your selection: """)
        if choice == '1':
            evasion()
            break

        elif choice == '2':
            dnd_dict.character_dict["features"]['hunter_defense_stand_against_the_tide'] = feature3
            break

        elif choice == '3':
            uncanny_dodge()
            break

        else:
            print("Error: Invalid Input")
            continue

def rogue2():
    feature = """Cunning Action

Starting at 2nd level, your quick thinking and agility allow you to move and act quickly. You can take a bonus action on each of your turns in combat. This action can be used only to take the Dash, Disengage, or Hide action."""

    print(feature)
    dnd_dict.character_dict["features"]['cunning_action'] = feature

def rogue3():
    feature = """Steady Aim (Optional)

At 3rd level, as a bonus action, you give yourself advantage on your next attack roll on the current turn. You can use this bonus action only if you haven't moved during this turn, and after you use the bonus action, your speed is 0 until the end of the current turn."""
    print(feature)
    dnd_dict.character_dict["features"]['steady_aim'] = feature

def rogue5():
    uncanny_dodge()

def rogue7():
    evasion()

def rogue11():
    feature = """Reliable Talent

By 11th level, you have refined your chosen skills until they approach perfection. Whenever you make an ability check that lets you add your proficiency bonus, you can treat a d20 roll of 9 or lower as a 10."""
    print(feature)
    dnd_dict.character_dict["features"]['reliable_talent'] = feature

def rogue14():
    feature = """Blindsense

Starting at 14th level, if you are able to hear, you are aware of the location of any hidden or invisible creature within 10 feet of you."""
    print(feature)
    dnd_dict.character_dict["features"]['blindsense_rogue'] = feature

def rogue15():
    feature = """Slippery Mind

By 15th level, you have acquired greater mental strength. You gain proficiency in Wisdom saving throws."""
    print(feature)
    dnd_dict.character_dict["features"]['slippery_mind'] = feature
    dnd_dict.character_dict['saving_throws']['wisdom'] = 'Wisdom'

def rogue18():
    feature = """Elusive

Beginning at 18th level, you are so evasive that attackers rarely gain the upper hand against you. No attack roll has advantage against you while you aren't incapacitated."""
    print(feature)
    dnd_dict.character_dict["features"]['elusive'] = feature

def rogue20():
    feature = """Stroke of Luck

At 20th level, you have an uncanny knack for succeeding when you need to. If your attack misses a target within range, you can turn the miss into a hit. Alternatively, if you fail an ability check, you can treat the d20 roll as a 20.

Once you use this feature, you can't use it again until you finish a short or long rest."""
    print(feature)
    dnd_dict.character_dict["features"]['stroke_of_luck'] = feature


# This function is for when the Rogue gets spells from any class. The Limited variables are used for Illusion and Enchantment schools, while the Full variables are used for any school of magic.

# Used to swap out the second level spells for Enchantment and Illusion, but only second level for all spells.
def rogue_spell_swap_second():
    while True:
        choice = input("""Do you want to replace one Rogue spell?
1) An Enchantment or Illusion Spell
2) Any School of Magic
0) No
Enter your selection: """)
        if choice == '1':
            dnd_skills.second_swap(dnd_magic.arcane_trickster_first,dnd_magic.arcane_trickster_second,dnd_dict.character_dict['class_spells']['rogue']['first'],dnd_dict.character_dict['class_spells']['rogue']['second'])
            break

        elif choice == '2':
            dnd_skills.second_swap(dnd_magic.wizard_first,dnd_magic.wizard_second,dnd_dict.character_dict['class_spells']['rogue_special']['first'],dnd_dict.character_dict['class_spells']['rogue_special']['second'])
            break

        elif choice == '0':
            break

        else:
            print("Error: Invalid Selection")
            continue

# Used to swap out the third level spells for Enchantment and Illusion, but only second level for all spells.
def rogue_spell_swap_third_early():
    while True:
        choice = input("""Do you want to replace one Rogue spell?
1) An Enchantment or Illusion Spell
2) Any School of Magic
0) No
Enter your selection: """)
        if choice == '1':
            dnd_skills.third_swap(dnd_magic.arcane_trickster_first,dnd_magic.arcane_trickster_second,dnd_magic.arcane_trickster_third,dnd_dict.character_dict['class_spells']['rogue']['first'],dnd_dict.character_dict['class_spells']['rogue']['second'],dnd_dict.character_dict['class_spells']['rogue']['third'])
            break

        elif choice == '2':
            dnd_skills.second_swap(dnd_magic.wizard_first,dnd_magic.wizard_second,dnd_dict.character_dict['class_spells']['rogue_special']['first'],dnd_dict.character_dict['class_spells']['rogue_special']['second'])
            break

        elif choice == '0':
            break

        else:
            print("Error: Invalid Selection")
            continue

# Used to swap out the third level spells for Enchantment and Illusion, but only third level for all spells.
def rogue_spell_swap_third():
    while True:
        choice = input("""Do you want to replace one Rogue spell?
1) An Enchantment or Illusion Spell
2) Any School of Magic
0) No
Enter your selection: """)
        if choice == '1':
            dnd_skills.third_swap(dnd_magic.arcane_trickster_first,dnd_magic.arcane_trickster_second,dnd_magic.arcane_trickster_third,dnd_dict.character_dict['class_spells']['rogue']['first'],dnd_dict.character_dict['class_spells']['rogue']['second'],dnd_dict.character_dict['class_spells']['rogue']['third'])
            break

        elif choice == '2':
            dnd_skills.third_swap(dnd_magic.wizard_first,dnd_magic.wizard_second,dnd_magic.wizard_third,dnd_dict.character_dict['class_spells']['rogue_special']['first'],dnd_dict.character_dict['class_spells']['rogue_special']['second'],dnd_dict.character_dict['class_spells']['rogue_special']['third'])
            break

        elif choice == '0':
            break

        else:
            print("Error: Invalid Selection")
            continue



# Used to swap out the fourth level spells for Enchantment and Illusion, but only third level for all spells.
def rogue_spell_swap_fourth():
    while True:
        choice = input("""Do you want to replace one Rogue spell?
1) An Enchantment or Illusion Spell
2) Any School of Magic
0) No
Enter your selection: """)
        if choice == '1':
            dnd_skills.fourth_swap(dnd_magic.arcane_trickster_first,dnd_magic.arcane_trickster_second,dnd_magic.arcane_trickster_third,dnd_magic.arcane_trickster_fourth,dnd_dict.character_dict['class_spells']['rogue']['first'],dnd_dict.character_dict['class_spells']['rogue']['second'],dnd_dict.character_dict['class_spells']['rogue']['third'],dnd_dict.character_dict['class_spells']['rogue']['fourth'])
            break

        elif choice == '2':
            dnd_skills.third_swap(dnd_magic.wizard_first,dnd_magic.wizard_second,dnd_magic.wizard_third,dnd_dict.character_dict['class_spells']['rogue_special']['first'],dnd_dict.character_dict['class_spells']['rogue_special']['second'],dnd_dict.character_dict['class_spells']['rogue_special']['third'])
            break

        elif choice == '0':
            break

        else:
            print("Error: Invalid Selection")
            continue








def rogue_spell_swap_late(limited_spell_list,full_spell_list,full_dict,special_dict,limited_class_dict,full_class_dict):
    while True:
        choice = input("""Do you want to replace one Rogue spell?
1) An Illusion or Enchantment Spell
2) Any School of Magic
3) No
Enter your selection: """)
        if choice == '1':
#            dnd_skills.spell_swap(class_dict,full_dict,class_dict)
            dnd_skills.spell_swap(limited_class_dict,special_dict,full_dict)
            dnd_skills.spell_add(limited_spell_list,full_dict,limited_class_dict)
            break

        elif choice == '2':
            dnd_skills.spell_swap(full_class_dict,special_dict,full_dict)
            dnd_skills.spell_add(full_spell_list,full_dict,full_class_dict)
            break

        elif choice == '3':
            break

        else:
            print("Error: Invalid Selection")
            continue

def arcane_trickster_rogue3():
    feature = """Spellcasting

When you reach 3rd level, you augment your martial prowess with the ability to cast spells.
Cantrips

You learn three cantrips: Mage Hand and two other cantrips of your choice from the wizard spell list. You learn another wizard cantrip of your choice at 10th level.
Spell Slots

The Arcane Trickster Spellcasting table shows how many spell slots you have to cast your wizard spells of 1st level and higher. To cast one of these spells, you must expend a slot of the spell's level or higher. You regain all expended spell slots when you finish a long rest.

For example, if you know the 1st-level spell Charm Person and have a 1st-level and a 2nd-level spell slot available, you can cast Charm Person using either slot.
Spells Known of 1st Level and Higher

You know three 1st-level wizard spells of your choice, two of which you must choose from the enchantment and illusion spells on the wizard spell list.

The Spells Known column of the Arcane Trickster Spellcasting table shows when you learn more wizard spells of 1st level or higher. Each of these spells must be an enchantment or illusion spell of your choice, and must be of a level for which you have spell slots. For instance, when you reach 7th level in this class, you can learn one new spell of 1st or 2nd level.

The spells you learn at 8th, 14th, and 20th level can come from any school of magic.

Whenever you gain a level in this class, you can replace one of the wizard spells you know with another spell of your choice from the wizard spell list. The new spell must be of a level for which you have spell slots, and it must be an enchantment or illusion spell, unless you're replacing the spell you gained at 3rd, 8th, 14th, or 20th level from any school of magic.
Spellcasting Ability

Intelligence is your spellcasting ability for your wizard spells, since you learn your spells through dedicated study and memorization. You use your Intelligence whenever a spell refers to your spellcasting ability. In addition, you use your Intelligence modifier when setting the saving throw DC for a wizard spell you cast and when making an attack roll with one.

Spell save DC = 8 + your proficiency bonus + your Intelligence modifier

Spell attack modifier = your proficiency bonus + your Intelligence modifier"""

    feature2 = """Mage Hand Legerdemain

Starting at 3rd level, when you cast Mage Hand, you can make the spectral hand invisible, and you can perform the following additional tasks with it:

    You can stow one object the hand is holding in a container worn or carried by another creature.

    You can retrieve an object in a container worn or carried by another creature.

    You can use thieves' tools to pick locks and disarm traps at range.

You can perform one of these tasks without being noticed by a creature if you succeed on a Dexterity (Sleight of Hand) check contested by the creature's Wisdom (Perception) check.

In addition, you can use the bonus action granted by your Cunning Action to control the hand.
"""
    print(feature)
    print(feature2)
    dnd_dict.character_dict["features"]['mage_hand_legerdemain'] = feature2
    dnd_dict.character_dict['class_spells']['rogue_cantrips']['mage_hand'] = 'Mage Hand'
    dnd_dict.character_dict['spells']['cantrips']['mage_hand'] = 'Mage Hand'
    dnd_magic.arcane_trickster_magic()
    dnd_dict.character_dict['semi_caster_level'] += 3
    spell_attack = ((dnd_dict.character_dict['Stats']['intelligence']['mod']) + dnd_dict.character_dict['prof_bonus'])
    spell_save = ((dnd_dict.character_dict['Stats']['intelligence']['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
    dnd_dict.character_dict['spell_modifier']['intelligence']['attack'] = spell_attack
    dnd_dict.character_dict['spell_modifier']['intelligence']['save'] = spell_save
    dnd_skills.spell_slot_selection()

def arcane_trickster_rogue9():
    feature = """Magical Ambush

Starting at 9th level, if you are hidden from a creature when you cast a spell on it, the creature has disadvantage on any saving throw it makes against the spell this turn."""
    print(feature)
    dnd_dict.character_dict["features"]['magical_ambush'] = feature

def arcane_trickster_rogue13():
    feature = """Versatile Trickster

At 13th level, you gain the ability to distract targets with your Mage Hand. As a bonus action on your turn, you can designate a creature within 5 feet of the spectral hand created by the spell. Doing so gives you advantage on attack rolls against that creature until the end of the turn."""
    print(feature)
    dnd_dict.character_dict["features"]['versatile_trickster'] = feature

def arcane_trickster_rogue17():
    feature = """Spell Thief

At 17th level, you gain the ability to magically steal the knowledge of how to cast a spell from another spellcaster.

Immediately after a creature casts a spell that targets you or includes you in its area of effect, you can use your reaction to force the creature to make a saving throw with its spellcasting ability modifier. The DC equals your spell save DC. On a failed save, you negate the spell's effect against you, and you steal the knowledge of the spell if it is at least 1st level and of a level you can cast (it doesn't need to be a wizard spell). For the next 8 hours, you know the spell and can cast it using your spell slots. The creature can't cast that spell until the 8 hours have passed.

Once you use this feature, you can't use it again until you finish a long rest."""
    print(feature)
    dnd_dict.character_dict["features"]['spell_thief'] = feature

def assassin_rogue3():
    feature = """Bonus Proficiencies

When you choose this archetype at 3rd level, you gain proficiency with the disguise kit and the poisoner's kit."""

    feature2 = """Assassinate

Starting at 3rd level, you are at your deadliest when you get the drop on your enemies. You have advantage on attack rolls against any creature that hasn't taken a turn in the combat yet. In addition, any hit you score against a creature that is surprised is a critical hit."""

    print(feature)
    dnd_dict.character_dict['Kits']['diguise_kit'] = 'Disguise Kit'
    dnd_dict.character_dict['Kits']['poisoner_kit'] = 'Poisoner\'s Kit'
    print(feature2)
    dnd_dict.character_dict["features"]['assassinate'] = feature2

def assassin_rogue9():
    feature = """Infiltration Expertise

Starting at 9th level, you can unfailingly create false identities for yourself. You must spend seven days and 25 gp to establish the history, profession, and affiliations for an identity. You can't establish an identity that belongs to someone else. For example, you might acquire appropriate clothing, letters of introduction, and official- looking certification to establish yourself as a member of a trading house from a remote city so you can insinuate yourself into the company of other wealthy merchants.

Thereafter, if you adopt the new identity as a disguise, other creatures believe you to be that person until given an obvious reason not to."""

    print(feature)
    dnd_dict.character_dict["features"]['infiltration_expertise'] = feature

def assassin_rogue13():
    feature = """Impostor

At 13th level, you gain the ability to unerringly mimic another person's speech, writing, and behavior. You must spend at least three hours studying these three components of the person's behavior, listening to speech, examining handwriting, and observing mannerisms.

Your ruse is indiscernible to the casual observer. If a wary creature suspects something is amiss, you have advantage on any Charisma (Deception) check you make to avoid detection."""

    print(feature)
    dnd_dict.character_dict["features"]['imposter_rogue'] = feature

def assassin_rogue17():
    feature = """Death Strike

Starting at 17th level, you become a master of instant death. When you attack and hit a creature that is surprised, it must make a Constitution saving throw (DC 8 + your Dexterity modifier + your proficiency bonus). On a failed save, double the damage of your attack against the creature."""
    print(feature)
    dnd_dict.character_dict["features"]['death_strike'] = feature

def thief_rogue3():
    feature = """Fast Hands

Starting at 3rd level, you can use the bonus action granted by your Cunning Action to make a Dexterity (Sleight of Hand) check, use your thieves' tools to disarm a trap or open a lock, or take the Use an Object action."""

    feature2 = """Second-Story Work

When you choose this archetype at 3rd level, you gain the ability to climb faster than normal; climbing no longer costs you extra movement.

In addition, when you make a running jump, the distance you cover increases by a number of feet equal to your Dexterity modifier."""

    print(feature)
    dnd_dict.character_dict["features"]['fast_hands'] = feature
    print(feature2)
    dnd_dict.character_dict["features"]['second_story_work'] = feature2

def thief_rogue9():
    feature = """Supreme Sneak

Starting at 9th level, you have advantage on a Dexterity (Stealth) check if you move no more than half your speed on the same turn."""
    print(feature)
    dnd_dict.character_dict["features"]['supreme_sneak'] = feature

def thief_rogue13():
    feature = """Use Magic Device

By 13th level, you have learned enough about the workings of magic that you can improvise the use of items even when they are not intended for you. You ignore all class, race, and level requirements on the use of magic items."""
    print(feature)
    dnd_dict.character_dict["features"]['use_magic_device'] = feature

def thief_rogue17():
    feature = """Thief's Reflexes

When you reach 17th level, you have become adept at laying ambushes and quickly escaping danger. You can take two turns during the first round of any combat. You take your first turn at your normal initiative and your second turn at your initiative minus 10. You can't use this feature when you are surprised."""
    print(feature)
    dnd_dict.character_dict["features"]['thief\'s_reflexes'] = feature


def careful_spell():
    feature = """Careful Spell. When you cast a spell that forces other creatures to make a saving throw, you can protect some of those creatures from the spell's full force. To do so, you spend 1 sorcery point and choose a number of those creatures up to your Charisma modifier (minimum of one creature). A chosen creature automatically succeeds on its saving throw against the spell."""
    print(feature)
    dnd_dict.character_dict["features"]['careful_spell'] = feature

def distant_spell():
    feature = """Distant Spell. When you cast a spell that has a range of 5 feet or greater, you can spend 1 sorcery point to double the range of the spell.
        When you cast a spell that has a range of touch, you can spend 1 sorcery point to make the range of the spell 30 feet."""
    print(feature)
    dnd_dict.character_dict["features"]['distant_spell'] = feature

def empowered_spell():
    feature = """Empowered Spell. When you roll damage for a spell, you can spend 1 sorcery point to reroll a number of the damage dice up to your Charisma modifier (minimum of one). You must use the new rolls.
        You can use Empowered Spell even if you have already used a different Metamagic option during the casting of the spell."""
    print(feature)
    dnd_dict.character_dict["features"]['empowered_spell'] = feature

def extended_spell():
    feature = """Extended Spell. When you cast a spell that has a duration of 1 minute or longer, you can spend 1 sorcery point to double its duration, to a maximum duration of 24 hours."""
    print(feature)
    dnd_dict.character_dict["features"]['extended_spell'] = feature

def heightened_spell():
    feature = """Heightened Spell. When you cast a spell that forces a creature to make a saving throw to resist its effects, you can spend 3 sorcery points to give one target of the spell disadvantage on its first saving throw made against the spell."""
    print(feature)
    dnd_dict.character_dict["features"]['heightened_spell'] = feature

def quickened_spell():
    feature = """Quickened Spell. When you cast a spell that has a casting time of 1 action, you can spend 2 sorcery points to change the casting time to 1 bonus action for this casting."""
    print(feature)
    dnd_dict.character_dict["features"]['quickened_spell'] = feature

def seeking_spell():
    feature = """Seeking Spell. If you make an attack roll for a spell and miss, you can spend 2 sorcerer points to reroll the d20, and you must use the new roll.
        You can use Seeking Spell even if you have already used a different Metamagic option during the casting of the spell."""
    print(feature)
    dnd_dict.character_dict["features"]['seeking_spell'] = feature

def subtle_spell():
    feature = """Subtle Spell. When you cast a spell, you can spend 1 sorcery point to cast it without any somatic or verbal components."""
    print(feature)
    dnd_dict.character_dict["features"]['subtle_spell'] = feature

def transmuted_spell():
    feature = """Transmuted Spell. When you cast a spell that deals a type of damage from the following list, you can spend 1 sorcery point to change that damage type to one of the other listed types: acid, cold, fire, lightning, poison, thunder."""
    print(feature)
    dnd_dict.character_dict["features"]['transmuted_spell'] = feature

def twinned_spell():
    feature = """Twinned Spell. When you cast a spell that targets only one creature and doesn't have a range of self, you can spend a number of sorcery points equal to the spell's level to target a second creature in range with the same spell (1 sorcery point if the spell is a cantrip). To be eligible, a spell must be incapable of targeting more than one creature at the spell's current level. For example, Magic Missile and Scorching Ray aren't eligible, but Ray of Frost and Chromatic Orb are."""
    print(feature)
    dnd_dict.character_dict["features"]['twinned_spell'] = feature

def sorcerer2():
    feature = """Font of Magic

At 2nd level, you tap into a deep wellspring of magic within yourself. This wellspring is represented by sorcery points, which allow you to create a variety of magical effects.

    Sorcery Points. You have 2 sorcery points, and you gain more as you reach higher levels, as shown in the Sorcery Points column of the Sorcerer table. You can never have more sorcery points than shown on the table for your level. You regain all spent sorcery points when you finish a long rest.

    Flexible Casting. You can use your sorcery points to gain additional spell slots, or sacrifice spell slots to gain additional sorcery points. You learn other ways to use your sorcery points as you reach higher levels.
        Creating Spell Slots. You can transform unexpended sorcery points into one spell slot as a bonus action on your turn. The Creating Spell Slots table shows the cost of creating a spell slot of a given level. You can create spell slots no higher in level than 5th. Any spell slot you create with this feature vanishes when you finish a long rest.
        Converting a Spell Slot to Sorcery Points. As a bonus action on your turn, you can expend one spell slot and gain a number of sorcery points equal to the slot's level.
"""
    print(feature)
    dnd_dict.character_dict["features"]['font_of_magic'] = feature


def sorcerous_versatility():
    while True:
        choice = input("""Select one option:
1) Replace one Metamagic Option
2) Replace one cantrip
3) Neither
Enter your selection: """)
        if choice == '1':
            dnd_skills.maneuver_swap(dnd_dict.character_dict['metamagic'],dnd_dict.character_dict['features'])
            dnd_metamagic.metamagic()
            break

        elif choice == '2':
            dnd_skills.cantrip_swap(dnd_magic.sorcerer_cantrip,dnd_dict.character_dict['class_spells']['sorcerer_cantrips'])
            break

        elif choice == '3':
            break

        else:
            print("Error: Invalid Input")
            continue

def sorcerer3():
    dnd_metamagic.first_metamagic()

def sorcerer5():
    feature = """Magical Guidance (Optional)

When you reach 5th level, you can tap into your inner wellspring of magic to try and conjure success from failure. When you make an ability check that fails, you can spend 1 sorcery point to reroll the d20, and you must use the new roll, potentially turning the failure into a success."""
    print(feature)
    dnd_dict.character_dict["features"]['magical_guidance_sorcerer'] = feature

def sorcerer10():
    dnd_metamagic.metamagic()

def sorcerer20():
    feature = """Sorcerous Restoration

At 20th level, you regain 4 expended sorcery points whenever you finish a short rest."""
    print(feature)
    dnd_dict.character_dict["features"]['sorcerous_restoration'] = feature

def draconic_sorcerer1():
    feature = """Dragon Ancestor

At 1st level, you choose one type of dragon as your ancestor. The damage type associated with each dragon is used by features you gain later.
Draconic Ancestry
Dragon Color 	Damage Type
Black 	Acid
Blue 	Lightning
Brass 	Fire
Bronze 	Lightning
Copper 	Acid
Gold 	Fire
Green 	Poison
Red 	Fire
Silver 	Cold
White 	Cold

You can speak, read, and write Draconic. Additionally, whenever you make a Charisma check when interacting with dragons, your proficiency bonus is doubled if it applies to the check.
Draconic Resilience

As magic flows through your body, it causes physical traits of your dragon ancestors to emerge. At 1st level, your hit point maximum increases by 1 and increases by 1 again whenever you gain a level in this class.

Additionally, parts of your skin are covered by a thin sheen of dragon-like scales. When you aren't wearing armor, your AC equals 13 + your Dexterity modifier."""
    dnd_dict.character_dict["player_class"]["sorcerer"]["subclass"] = "Draconic Bloodline"
    print(feature)
    dnd_dict.character_dict["features"]['draconic_resilience'] = feature
    ac = 13 + dnd_dict.character_dict['Stats']['dexterity']['mod']
    dnd_dict.character_dict['sorcerer_armor_class'] = ac

def draconic_sorcerer6():
    feature = """Elemental Affinity

Starting at 6th level, when you cast a spell that deals damage of the type associated with your draconic ancestry, add your Charisma modifier to one damage roll of that spell. At the same time, you can spend 1 sorcery point to gain resistance to that damage type for 1 hour."""
    print(feature)
    dnd_dict.character_dict["features"]['elemental_affinity_sorcerer'] = feature

def draconic_sorcerer14():
    feature = """Dragon Wings

At 14th level, you gain the ability to sprout a pair of dragon wings from your back, gaining a flying speed equal to your current speed. You can create these wings as a bonus action on your turn. They last until you dismiss them as a bonus action on your turn.

You can't manifest your wings while wearing armor unless the armor is made to accommodate them, and clothing not made to accommodate your wings might be destroyed when you manifest them."""
    print(feature)
    dnd_dict.character_dict["features"]['dragon_wings_sorcerer'] = feature

def draconic_sorcerer18():
    feature = """Draconic Presence

Beginning at 18th level, you can channel the dread presence of your dragon ancestor, causing those around you to become awestruck or frightened. As an action, you can spend 5 sorcery points to draw on this power and exude an aura of awe or fear (your choice) to a distance of 60 feet. For 1 minute or until you lose your concentration (as if you were casting a concentration spell), each hostile creature that starts its turn in this aura must succeed on a Wisdom saving throw or be charmed (if you chose awe) or frightened (if you chose fear) until the aura ends. A creature that succeeds on this saving throw is immune to your aura for 24 hours."""
    print(feature)
    dnd_dict.character_dict["features"]['draconic_presence_sorcerer'] = feature

def wild_magic_sorcerer1():
    feature = """Wild Magic Surge

Starting when you choose this origin at 1st level, your spellcasting can unleash surges of untamed magic. Immediately after you cast a sorcerer spell of 1st level or higher, the DM can have you roll a d20. If you roll a 1, roll on the Wild Magic Surge table to create a random magical effect.
Tides of Chaos

Starting at 1st level, you can manipulate the forces of chance and chaos to gain advantage on one attack roll, ability check, or saving throw. Once you do so, you must finish a long rest before you can use this feature again.

Any time before you regain the use of this feature, the DM can have you roll on the Wild Magic Surge table immediately after you cast a sorcerer spell of 1st level or higher. You then regain the use of this feature."""
    dnd_dict.character_dict["player_class"]["sorcerer"]["subclass"] = "Wild Magic"
    print(feature)
    dnd_dict.character_dict["features"]['wild_magic_surge'] = feature

def wild_magic_sorcerer6():
    feature = """Bend Luck

Starting at 6th level, you have the ability to twist fate using your wild magic. When another creature you can see makes an attack roll, an ability check, or a saving throw, you can use your reaction and spend 2 sorcery points to roll 1d4 and apply the number rolled as a bonus or penalty (your choice) to the creature's roll. You can do so after the creature rolls but before any effects of the roll occur."""
    print(feature)
    dnd_dict.character_dict["features"]['bend_luck_sorcerer'] = feature

def wild_magic_sorcerer14():
    feature = """Controlled Chaos

At 14th level, you gain a modicum of control over the surges of your wild magic. Whenever you roll on the Wild Magic Surge table, you can roll twice and use either number."""
    print(feature)
    dnd_dict.character_dict["features"]['controlled_chaos'] = feature

def wild_magic_sorcerer18():
    feature = """Spell Bombardment

Beginning at 18th level, the harmful energy of your spells intensifies. When you roll damage for a spell and roll the highest number possible on any of the dice, choose one of those dice, roll it again and add that roll to the damage. You can use the feature only once per turn."""
    print(feature)
    dnd_dict.character_dict["features"]['spell_bombardment_sorcerer'] = feature


def pact_of_the_blade():
    feature = """Pact of the Blade
        You can use your action to create a pact weapon in your empty hand. You can choose the form that this melee weapon takes each time you create it. You are proficient with it while you wield it. This weapon counts as magical for the purpose of overcoming resistance and immunity to nonmagical attacks and damage.
        Your pact weapon disappears if it is more than 5 feet away from you for 1 minute or more. It also disappears if you use this feature again, if you dismiss the weapon (no action required), or if you die.
        You can transform one magic weapon into your pact weapon by performing a special ritual while you hold the weapon. You perform the ritual over the course of 1 hour, which can be done during a short rest.
        You can then dismiss the weapon, shunting it into an extradimensional space, and it appears whenever you create your pact weapon thereafter. You can't affect an artifact or a sentient weapon in this way. The weapon ceases being your pact weapon if you die, if you perform the 1-hour ritual on a different weapon, or if you use a 1-hour ritual to break your bond to it. The weapon appears at your feet if it is in the extradimensional space when the bond breaks."""
    print(feature)
    dnd_dict.character_dict["features"]['pact_of_the_blade'] = feature
    dnd_dict.character_dict['player_class']['warlock']['pact'] = 'Blade'

def pact_of_the_chain():
    feature = """Pact of the Chain
        You learn the Find Familiar spell and can cast it as a ritual. The spell doesn't count against your number of spells known.
        When you cast the spell, you can choose one of the normal forms for your familiar or one of the following special forms: imp, pseudodragon, quasit, or sprite.
        Additionally, when you take the Attack action, you can forgo one of your own attacks to allow your familiar to use its reaction to make one attack with its reaction."""
    print(feature)
    dnd_dict.character_dict["features"]['pact_of_the_chain'] = feature
    dnd_dict.character_dict['player_class']['warlock']['pact'] = 'Chain'

def pact_of_the_tome():
    feature = """Pact of the Tome
        Your patron gives you a grimoire called a Book of Shadows. When you gain this feature, choose three cantrips from any class's spell list (the three needn't be from the same list). While the book is on your person, you can cast those cantrips at will. They don't count against your number of cantrips known. If they don't appear on the warlock spell list, they are nonetheless warlock spells for you.
        If you lose your Book of Shadows, you can perform a 1-hour ceremony to receive a replacement from your patron. This ceremony can be performed during a short or long rest, and it destroys the previous book. The book turns to ash when you die."""
    print(feature)
    dnd_dict.character_dict["features"]['pact_of_the_tome'] = feature
    dnd_dict.character_dict['player_class']['warlock']['pact'] = 'Tome'
# Make a list of all cantrips
    new_cantrip = dnd_magic.artificer_cantrip + dnd_magic.bard_cantrip + dnd_magic.cleric_cantrip + dnd_magic.druid_cantrip + dnd_magic.sorcerer_cantrip + dnd_magic.warlock_cantrip + dnd_magic.wizard_cantrip
    res = []
    [res.append(x) for x in new_cantrip if x not in res]
    res.sort() 
    x = 1
    for x in range(x,4):
        if x < 4:
            print(f'{x}/2')
            dnd_skills.spell_add(new_cantrip,dnd_dict.character_dict['spells']['cantrips'],dnd_dict.character_dict['special_spells']['tome_cantrips'])
            x+=1
            continue
        elif x == 4:
            break

def pact_of_the_talisman():
    feature = """Pact of the Talisman
        Your patron gives you an amulet, a talisman that can aid the wearer when the need is great. When the wearer fails an ability check, they can add a d4 to the roll, potentially turning the roll into a success. This benefit can be used a number of times equal to your proficiency bonus, and all expended uses are restored when you finish a long rest.
        If you lose the talisman, you can perform a 1-hour ceremony to receive a replacement from your patron. This ceremony can be performed during a short or long rest, and it destroys the previous amulet. The talisman turns to ash when you die."""
    print(feature)
    dnd_dict.character_dict["features"]['pact_of_the_talisman'] = feature
    dnd_dict.character_dict['player_class']['warlock']['pact'] = 'Talisman'

def warlock3():
    while True:
        choice = input("""Select the Pact you want to have:
1) Pact of the Blade
2) Pact of the Chain
3) Pact of the Tome
4) Pact of the Talisman
Enter your selection: """)
        if choice == '1':
            pact_of_the_blade()
            break

        elif choice == '2':
            pact_of_the_chain()
            break

        elif choice == '3':
            pact_of_the_tome()
            break

        elif choice == '4':
            pact_of_the_talisman()
            break

        else:
            print("Error: Invalid Input")
            continue


def eldritch_versatility():
    while True:
        choice = input("""Select one option:
1) Replace one spell
2) Replace your Pact Boon
3) Replace one Mystic Arcanum feature (if you are level 12 or higher)
4) None of the above
Enter your selection: """)
# Divide the choice based on subclass and class level
        if choice == '1':
            if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Archfey':
                if dnd_dict.character_dict['player_class']['warlock']['class_level'] == 4:
                    dnd_skills.second_swap(dnd_magic.archfey_warlock_first,dnd_magic.archfey_warlock_second,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'])

                    break

                elif dnd_dict.character_dict['player_class']['warlock']['class_level'] == 8:
                    dnd_skills.fourth_swap(dnd_magic.archfey_warlock_first,dnd_magic.archfey_warlock_second,dnd_magic.archfey_warlock_third,dnd_magic.archfey_warlock_fourth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'])
                    break

                else:
                    dnd_skills.fifth_swap(dnd_magic.archfey_warlock_first,dnd_magic.archfey_warlock_second,dnd_magic.archfey_warlock_third,dnd_magic.archfey_warlock_fourth,dnd_magic.archfey_warlock_fifth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'],dnd_dict.character_dict['class_spells']['warlock']['fifth'])
                    break


            if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Fiend':
                if dnd_dict.character_dict['player_class']['warlock']['class_level'] == 4:
                    dnd_skills.second_swap(dnd_magic.fiend_warlock_first,dnd_magic.fiend_warlock_second,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'])

                    break

                elif dnd_dict.character_dict['player_class']['warlock']['class_level'] == 8:
                    dnd_skills.fourth_swap(dnd_magic.fiend_warlock_first,dnd_magic.fiend_warlock_second,dnd_magic.fiend_warlock_third,dnd_magic.fiend_warlock_fourth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'])
                    break

                else:
                    dnd_skills.fifth_swap(dnd_magic.fiend_warlock_first,dnd_magic.fiend_warlock_second,dnd_magic.fiend_warlock_third,dnd_magic.fiend_warlock_fourth,dnd_magic.fiend_warlock_fifth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'],dnd_dict.character_dict['class_spells']['warlock']['fifth'])
                    break


            if dnd_dict.character_dict['player_class']['warlock']['subclass'] == 'Great Old One':
                if dnd_dict.character_dict['player_class']['warlock']['class_level'] == 4:
                    dnd_skills.second_swap(dnd_magic.goo_warlock_first,dnd_magic.goo_warlock_second,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'])

                    break

                elif dnd_dict.character_dict['player_class']['warlock']['class_level'] == 8:
                    dnd_skills.fourth_swap(dnd_magic.goo_warlock_first,dnd_magic.goo_warlock_second,dnd_magic.goo_warlock_third,dnd_magic.goo_warlock_fourth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'])
                    break

                else:
                    dnd_skills.fifth_swap(dnd_magic.goo_warlock_first,dnd_magic.goo_warlock_second,dnd_magic.goo_warlock_third,dnd_magic.goo_warlock_fourth,dnd_magic.goo_warlock_fifth,dnd_dict.character_dict['class_spells']['warlock']['first'],dnd_dict.character_dict['class_spells']['warlock']['second'],dnd_dict.character_dict['class_spells']['warlock']['third'],dnd_dict.character_dict['class_spells']['warlock']['fourth'],dnd_dict.character_dict['class_spells']['warlock']['fifth'])
                    break


        elif choice == '2':
            dnd_skills.pact_swap(dnd_dict.character_dict['pact_invocations'],dnd_dict.character_dict['invocations'],dnd_dict.character_dict['features'])
            warlock3()
            break

        elif choice == '3':
            if dnd_dict.character_dict['player_class']['warlock']['class_level'] >= 12:
                if dnd_dict.character_dict['player_class']['warlock']['class_level'] == 12:
                    dnd_skills.maneuver_swap(dnd_dict.character_dict['class_spells']['warlock']['sixth_level_arcanum'],dnd_dict.character_dict['spells']['sixth'])
                    dnd_skills.spell_add(dnd_magic.warlock_sixth,dnd_dict.character_dict['spells']['sixth'],dnd_dict.character_dict['class_spells']['warlock']['sixth_level_arcanum'])
                    break
    
                elif dnd_dict.character_dict['player_class']['warlock']['class_level'] == 16:
                    while True:
                        choice = input("""Select the level you want to change your arcanum spell:
1) Sixth
2) Seventh
3) Eighth
Enter your selection: """)
                        if choice == '1':
                            dnd_skills.maneuver_swap(dnd_dict.character_dict['class_spells']['warlock']['sixth_level_arcanum'],dnd_dict.character_dict['spells']['sixth'])
                            dnd_skills.spell_add(dnd_magic.warlock_sixth,dnd_dict.character_dict['spells']['sixth'],dnd_dict.character_dict['class_spells']['warlock']['sixth_level_arcanum'])
                            break
    
                        elif choice == '2':
                            dnd_skills.maneuver_swap(dnd_dict.character_dict['class_spells']['warlock']['seventh_level_arcanum'],dnd_dict.character_dict['spells']['seventh'])
                            dnd_skills.spell_add(dnd_magic.warlock_seventh,dnd_dict.character_dict['spells']['seventh'],dnd_dict.character_dict['class_spells']['warlock']['seventh_level_arcanum'])
                            break
    
                        elif choice == '3':
                            dnd_skills.maneuver_swap(dnd_dict.character_dict['class_spells']['warlock']['eighth_level_arcanum'],dnd_dict.character_dict['spells']['eighth'])
                            dnd_skills.spell_add(dnd_magic.warlock_eighth,dnd_dict.character_dict['spells']['eighth'],dnd_dict.character_dict['class_spells']['warlock']['eighth_level_arcanum'])
                            break
    
                        else:
                            print("Error: Invalid Input")
                            continue   

                elif dnd_dict.character_dict['player_class']['warlock']['class_level'] == 19:
                    while True:
                        choice = input("""Select the level you want to change your arcanum spell:
1) Sixth
2) Seventh
3) Eighth
4) Ninth
Enter your selection: """)
                        if choice == '1':
                            dnd_skills.maneuver_swap(dnd_dict.character_dict['class_spells']['warlock']['sixth_level_arcanum'],dnd_dict.character_dict['spells']['sixth'])
                            dnd_skills.spell_add(dnd_magic.warlock_sixth,dnd_dict.character_dict['spells']['sixth'],dnd_dict.character_dict['class_spells']['warlock']['sixth_level_arcanum'])
                            break
    
                        elif choice == '2':
                            dnd_skills.maneuver_swap(dnd_dict.character_dict['class_spells']['warlock']['seventh_level_arcanum'],dnd_dict.character_dict['spells']['seventh'])
                            dnd_skills.spell_add(dnd_magic.warlock_seventh,dnd_dict.character_dict['spells']['seventh'],dnd_dict.character_dict['class_spells']['warlock']['seventh_level_arcanum'])
                            break
    
                        elif choice == '3':
                            dnd_skills.maneuver_swap(dnd_dict.character_dict['class_spells']['warlock']['eighth_level_arcanum'],dnd_dict.character_dict['spells']['eighth'])
                            dnd_skills.spell_add(dnd_magic.warlock_eighth,dnd_dict.character_dict['spells']['eighth'],dnd_dict.character_dict['class_spells']['warlock']['eighth_level_arcanum'])
                            break
    
                        elif choice == '4':
                            dnd_skills.maneuver_swap(dnd_dict.character_dict['class_spells']['warlock']['ninth_level_arcanum'],dnd_dict.character_dict['spells']['ninth'])
                            dnd_skills.spell_add(dnd_magic.warlock_ninth,dnd_dict.character_dict['spells']['ninth'],dnd_dict.character_dict['class_spells']['warlock']['ninth_level_arcanum'])
                            break
    
                        else:
                            print("Error: Invalid Input")
            else:
                print("Error: You must be at least level 12 to select this feature")
                continue

            break

        elif choice == '4':
            break

        else:
            print("Error: Invalid Input")
            continue

def warlock11():
    feature = """Mystic Arcanum

At 11th level, your patron bestows upon you a magical secret called an arcanum. Choose one 6th-level spell from the warlock spell list as this arcanum.

You can cast your arcanum spell once without expending a spell slot. You must finish a long rest before you can do so again.

At higher levels, you gain more warlock spells of your choice that can be cast in this way: one 7th-level spell at 13th level, one 8th-level spell at 15th level, and one 9th-level spell at 17th level. You regain all uses of your Mystic Arcanum when you finish a long rest."""
    print(feature)
    dnd_dict.character_dict["features"]['mystic_arcanum'] = feature

def warlock20():
    feature = """Eldritch Master

At 20th level, you can draw on your inner reserve of mystical power while entreating your patron to regain expended spell slots. You can spend 1 minute entreating your patron for aid to regain all your expended spell slots from your Pact Magic feature. Once you regain spell slots with this feature, you must finish a long rest before you can do so again."""
    print(feature)
    dnd_dict.character_dict["features"]['eldritch_master_warlock'] = feature


def archfey_warlock1():
    feature = """Fey Presence

Starting at 1st level, your patron bestows upon you the ability to project the beguiling and fearsome presence of the fey. As an action, you can cause each creature in a 10-foot cube originating from you to make a Wisdom saving throw against your warlock spell save DC. The creatures that fail their saving throws are all charmed or frightened by you (your choice) until the end of your next turn.

Once you use this feature, you can't use it again until you finish a short or long rest."""
    print(feature)
    dnd_dict.character_dict["features"]['fey_presence'] = feature
    dnd_dict.character_dict["player_class"]["warlock"]["subclass"] = "Archfey"

def archfey_warlock6():
    feature = """Misty Escape

Starting at 6th level, you can vanish in a puff of mist in response to harm. When you take damage, you can use your reaction to turn invisible and teleport up to 60 feet to an unoccupied space you can see. You remain invisible until the start of your next turn or until you attack or cast a spell.

Once you use this feature, you can't use it again until you finish a short or long rest."""
    print(feature)
    dnd_dict.character_dict["features"]['misty_escape'] = feature

def archfey_warlock10():
    feature = """Beguiling Defenses

Beginning at 10th level, your patron teaches you how to turn the mind-affecting magic of your enemies against them. You are immune to being charmed, and when another creature attempts to charm you, you can use your reaction to attempt to turn the charm back on that creature. The creature must succeed on a Wisdom saving throw against your warlock spell save DC or be charmed by you for 1 minute or until the creature takes any damage."""
    print(feature)
    dnd_dict.character_dict["features"]['beguiling_defenses'] = feature

def archfey_warlock14():
    feature = """Dark Delirium

Starting at 14th level, you can plunge a creature into an illusory realm. As an action, choose a creature that you can see within 60 feet of you. It must make a Wisdom saving throw against your warlock spell save DC. On a failed save, it is charmed or frightened by you (your choice) for 1 minute or until your concentration is broken (as if you are concentrating on a spell). This effect ends early if the creature takes any damage.

Until this illusion ends, the creature thinks it is lost in a misty realm, the appearance of which you choose. The creature can see and hear only itself, you, and the illusion.

You must finish a short or long rest before you can use this feature again."""
    print(feature)
    dnd_dict.character_dict["features"]['dark_delirium'] = feature


def fiend_warlock1():
    feature = """Dark One's Blessing

Starting at 1st level, when you reduce a hostile creature to 0 hit points, you gain temporary hit points equal to your Charisma modifier + your warlock level (minimum of 1)."""
    print(feature)
    dnd_dict.character_dict["features"]['dark_ones_blessing'] = feature
    dnd_dict.character_dict["player_class"]["warlock"]["subclass"] = "Fiend"

def fiend_warlock6():
    feature = """Dark One's Own Luck

Starting at 6th level, you can call on your patron to alter fate in your favor. When you make an ability check or a saving throw, you can use this feature to add a d10 to your roll. You can do so after seeing the initial roll but before any of the roll's effects occur.

Once you use this feature, you can't use it again until you finish a short or long rest."""
    print(feature)
    dnd_dict.character_dict["features"]['dark_ones_own_luck'] = feature

def fiend_warlock10():
    feature = """Fiendish Resilience

Starting at 10th level, you can choose one damage type when you finish a short or long rest. You gain resistance to that damage type until you choose a different one with this feature. Damage from magical weapons or silver weapons ignores this resistance."""
    print(feature)
    dnd_dict.character_dict["features"]['fiendish_resilience'] = feature

def fiend_warlock14():
    feature = """Hurl Through Hell

Starting at 14th level, when you hit a creature with an attack, you can use this feature to instantly transport the target through the lower planes. The creature disappears and hurtles through a nightmare landscape.

At the end of your next turn, the target returns to the space it previously occupied, or the nearest unoccupied space. If the target is not a fiend, it takes 10d10 psychic damage as it reels from its horrific experience.

Once you use this feature, you can't use it again until you finish a long rest."""
    print(feature)
    dnd_dict.character_dict["features"]['hurl_through_hell'] = feature



def goo_warlock1():
    feature = """Awakened Mind

Starting at 1st level, your alien knowledge gives you the ability to touch the minds of other creatures. You can telepathically speak to any creature you can see within 30 feet of you. You don't need to share a language with the creature for it to understand your telepathic utterances, but the creature must be able to understand at least one language."""
    print(feature)
    dnd_dict.character_dict["features"]['awakened_mind'] = feature
    dnd_dict.character_dict["player_class"]["warlock"]["subclass"] = "Great Old One"

def goo_warlock6():
    feature = """Entropic Ward

At 6th level, you learn to magically ward yourself against attack and to turn an enemy's failed strike into good luck for yourself. When a creature makes an attack roll against you, you can use your reaction to impose disadvantage on that roll. If the attack misses you, your next attack roll against the creature has advantage if you make it before the end of your next turn.

Once you use this feature, you can't use it again until you finish a short or long rest."""
    print(feature)
    dnd_dict.character_dict["features"]['entropic_ward'] = feature

def goo_warlock10():
    feature = """Thought Shield

Starting at 10th level, your thoughts can't be read by telepathy or other means unless you allow it. You also have resistance to psychic damage, and whenever a creature deals psychic damage to you, that creature takes the same amount of damage that you do."""
    print(feature)
    dnd_dict.character_dict["features"]['though_shield'] = feature

def goo_warlock14():
    feature = """Create Thrall

At 14th level, you gain the ability to infect a humanoid's mind with the alien magic of your patron. You can use your action to touch an incapacitated humanoid. That creature is then charmed by you until a Remove Curse spell is cast on it, the charmed condition is removed from it, or you use this feature again.

You can communicate telepathically with the charmed creature as long as the two of you are on the same plane of existence."""
    print(feature)
    dnd_dict.character_dict["features"]['create_thrall_goo'] = feature

def wizard1():
    feature = """Spellbook

At 1st level, you have a spellbook containing six 1st-level wizard spells of your choice. Your spellbook is the repository of the wizard spells you know, except your cantrips, which are fixed in your mind.

The spells that you add to your spellbook as you gain levels reflect the arcane research you conduct on your own, as well as intellectual breakthroughs you have had about the nature of the multiverse. You might find other spells during your adventures. You could discover a spell recorded on a scroll in an evil wizard's chest, for example, or in a dusty tome in an ancient library.

Copying a Spell into the Book. When you find a wizard spell of 1st level or higher, you can add it to your spellbook if it is of a spell level you can prepare and if you can spare the time to decipher and copy it.

Copying a spell into your spellbook involves reproducing the basic form of the spell, then deciphering the unique system of notation used by the wizard who wrote it. You must practice the spell until you understand the sounds or gestures required, then transcribe it into your spellbook using your own notation.

For each level of the spell, the process takes 2 hours and costs 50 gp. The cost represents material components you expend as you experiment with the spell to master it, as well as the fine inks you need to record it. Once you have spent this time and money, you can prepare the spell just like your other spells.

Replacing the Book. You can copy a spell from your own spellbook into another book-for example, if you want to make a backup copy of your spellbook. This is just like copying a new spell into your spellbook, but faster and easier, since you understand your own notation and already know how to cast the spell. You need spend only 1 hour and 10 gp for each level of the copied spell.

If you lose your spellbook, you can use the same procedure to transcribe the spells that you have prepared into a new spellbook. Filling out the remainder of your spellbook requires you to find new spells to do so, as normal. For this reason, many wizards keep backup spellbooks in a safe place.

The Book's Appearance. Your spellbook is a unique compilation of spells, with its own decorative flourishes and margin notes. It might be a plain, functional leather volume that you received as a gift from your master, a finely bound gilt-edged tome you found in an ancient library or even a loose collection of notes scrounged together after you lost your previous spellbook in a mishap.
Preparing and Casting Spells

The Wizard table shows how many spell slots you have to cast your wizard spells of 1st level and higher. To cast one of these spells, you must expend a slot of the spell's level or higher. You regain all expended spell slots when you finish a long rest.

You prepare the list of wizard spells that are available for you to cast. To do so, choose a number of wizard spells from your spellbook equal to your Intelligence modifier + your wizard level (minimum of one spell). The spells must be of a level for which you have spell slots.

For example, if you're a 3rd-level wizard, you have four 1st-level and two 2nd-level spell slots. With an Intelligence of 16, your list of prepared spells can include six spells of 1st or 2nd level, in any combination, chosen from your spellbook. If you prepare the 1st-level spell Magic Missile, you can cast it using a 1st-level or a 2nd-level slot. Casting the spell doesn't remove it from your list of prepared spells.

You can change your list of prepared spells when you finish a long rest. Preparing a new list of wizard spells requires time spent studying your spellbook and memorizing the incantations and gestures you must make to cast the spell: at least 1 minute per spell level for each spell on your list."""

    print(feature)

def wizard2():
    feature = """Arcane Recovery

You have learned to regain some of your magical energy by studying your spellbook. Once per day when you finish a short rest, you can choose expended spell slots to recover. The spell slots can have a combined level that is equal to or less than half your wizard level (rounded up), and none of the slots can be 6th level or higher.

For example, if you're a 4th-level wizard, you can recover up to two levels worth of spell slots. You can recover either a 2nd-level spell slot or two 1st-level spell slots."""

    print(feature)
    dnd_dict.character_dict["features"]['arcane_recovery'] = feature

def wizard3():
    feature = """Cantrip Formulas (Optional)

At 3rd level, you have scribed a set of arcane formulas in your spellbook that you can use to formulate a cantrip in your mind. Whenever you finish a long rest and consult those formulas in your spellbook, you can replace one wizard cantrip you know with another cantrip from the wizard spell list."""
    print(feature)
    dnd_dict.character_dict["features"]['cantrip_formulas_wizard'] = feature

def wizard18():
    feature = """Spell Mastery

At 18th level, you have achieved such mastery over certain spells that you can cast them at will. Choose a 1st-level wizard spell and a 2nd-level wizard spell that are in your spellbook. You can cast those spells at their lowest level without expending a spell slot when you have them prepared. If you want to cast either spell at a higher level, you must expend a spell slot as normal.

By spending 8 hours in study, you can exchange one or both of the spells you chose for different spells of the same levels."""
    print(feature)
    dnd_dict.character_dict["features"]['spell_mastery_wizard'] = feature

def wizard20():
    feature = """Signature Spells

When you reach 20th level, you gain mastery over two powerful spells and can cast them with little effort. Choose two 3rd-level wizard spells in your spellbook as your signature spells. You always have these spells prepared, they don't count against the number of spells you have prepared, and you can cast each of them once at 3rd level without expending a spell slot. When you do so, you can't do so again until you finish a short or long rest.

If you want to cast either spell at a higher level, you must expend a spell slot as normal."""
    print(feature)
    dnd_dict.character_dict["features"]['signature_spell'] = feature

def abjuration_wizard2():
    feature = """Abjuration Savant

Beginning when you select this school at 2nd level, the gold and time you must spend to copy a abjuration spell into your spellbook is halved."""

    feature2 = """Arcane Ward

Starting at 2nd level, you can weave magic around yourself for protection. When you cast an abjuration spell of 1st level or higher, you can simultaneously use a strand of the spell's magic to create a magical ward on yourself that lasts until you finish a long rest. The ward has hit points equal to twice your wizard level + your Intelligence modifier. Whenever you take damage, the ward takes the damage instead. If this damage reduces the ward to 0 hit points, you take any remaining damage.

While the ward has 0 hit points, it can't absorb damage, but its magic remains. Whenever you cast an abjuration spell of 1st level or higher, the ward regains a number of hit points equal to twice the level of the spell.

Once you create the ward, you can't create it again until you finish a long rest."""

    print(feature)
    dnd_dict.character_dict["features"]['abjuration_savant'] = feature
    print(feature2)
    dnd_dict.character_dict["features"]['arcane_ward_wizard'] = feature2

def abjuration_wizard6():
    feature = """Projected Ward

Starting at 6th level, when a creature that you can see within 30 feet of you takes damage, you can use your reaction to cause your Arcane Ward to absorb that damage. If this damage reduces the ward to 0 hit points, the warded creature takes any remaining damage."""
    print(feature)
    dnd_dict.character_dict["features"]['projected_ward'] = feature

def abjuration_wizard10():
    feature = """Improved Abjuration

Beginning at 10th level, when you cast an abjuration spell that requires you to make an ability check as a part of casting that spell (as in Counterspell and Dispel Magic), you add your proficiency bonus to that ability check."""
    print(feature)
    dnd_dict.character_dict["features"]['improved_abjuration'] = feature

def abjuration_wizard14():
    feature = """Spell Resistance

Starting at 14th level, you have advantage on saving throws against spells.

Furthermore, you have resistance against the damage of spells."""
    print(feature)
    dnd_dict.character_dict["features"]['spell_resistance_wizard'] = feature

def conjuration_wizard2():

    feature = """Conjuration Savant

Beginning when you select this school at 2nd level, the gold and time you must spend to copy a Conjuration spell into your spellbook is halved."""

    feature2 = """Minor Conjuration

Starting at 2nd level when you select this school, you can use your action to conjure up an inanimate object in your hand or on the ground in an unoccupied space that you can see within 10 feet of you. This object can be no larger than 3 feet on a side and weigh no more than 10 pounds, and its form must be that of a nonmagical object that you have seen. The object is visibly magical, radiating dim light out to 5 feet.

The object disappears after 1 hour, when you use this feature again, or if it takes or deals any damage."""

    print(feature)
    dnd_dict.character_dict["features"]['conjuration_savant'] = feature
    print(feature2)
    dnd_dict.character_dict["features"]['minor_conjuration'] = feature2

def conjuration_wizard6():
    feature = """Benign Transportation

Starting at 6th level, you can use your action to teleport up to 30 feet to an unoccupied space that you can see. Alternatively, you can choose a space within range that is occupied by a Small or Medium creature. If that creature is willing, you both teleport, swapping places.

Once you use this feature, you can't use it again until you finish a long rest or you cast a conjuration spell of 1st level or higher."""
    print(feature)
    dnd_dict.character_dict["features"]['benign_transportation'] = feature

def conjuration_wizard10():
    feature = """Focused Conjuration

Beginning at 10th level, while you are concentrating on a conjuration spell, your concentration can't be broken as a result of taking damage."""
    print(feature)
    dnd_dict.character_dict["features"]['focused_conjuration'] = feature

def conjuration_wizard14():
    feature = """Durable Summons

Starting at 14th level, any creature that you summon or create with a conjuration spell has 30 temporary hit points."""
    print(feature)
    dnd_dict.character_dict["features"]['durable_summons'] = feature

def divination_wizard2():
    feature = """Divination Savant

Beginning when you select this school at 2nd level, the gold and time you must spend to copy a Divination spell into your spellbook is halved."""

    feature2 = """Portent

Starting at 2nd level when you choose this school, glimpses of the future begin to press in on your awareness. When you finish a long rest, roll two d20s and record the numbers rolled. You can replace any attack roll, saving throw, or ability check made by you or a creature that you can see with one of these foretelling rolls. You must choose to do so before the roll, and you can replace a roll in this way only once per turn.

Each foretelling roll can be used only once. When you finish a long rest, you lose any unused foretelling rolls."""

    print(feature)
    dnd_dict.character_dict["features"]['divination_savant'] = feature
    print(feature2)
    dnd_dict.character_dict["features"]['portent'] = feature2

def divination_wizard6():
    feature = """Expert Divination

Beginning at 6th level, casting divination spells comes so easily to you that it expends only a fraction of your spellcasting efforts. When you cast a divination spell of 2nd level or higher using a spell slot, you regain one expended spell slot. The slot you regain must be of a level lower than the spell you cast and can't be higher than 5th level."""
    print(feature)
    dnd_dict.character_dict["features"]['expert_divination'] = feature

def divination_wizard10():
    feature = """The Third Eye

Starting at 10th level, you can use your action to increase your powers of perception. When you do so, choose one of the following benefits, which lasts until you are incapacitated or you take a short or long rest. You can't use the feature again until you finish a short or long rest.

Darkvision. You gain darkvision out to a range of 60 feet.

Ethereal Sight. You can see into the Ethereal Plane within 60 feet of you.

Greater Comprehension. You can read any language.

See Invisibility. You can see invisible creatures and objects within 10 feet of you that are within line of sight."""
    print(feature)
    dnd_dict.character_dict["features"]['the_third_eye_wizard'] = feature

def divination_wizard14():
    feature = """Greater Portent

Starting at 14th level, the visions in your dreams intensify and paint a more accurate picture in your mind of what is to come. You roll three d20s for your Portent feature, rather than two."""
    print(feature)
    dnd_dict.character_dict["features"]['greater_portent'] = feature

def enchantment_wizard2():
    feature = """Enchantment Savant

Beginning when you select this school at 2nd level, the gold and time you must spend to copy a Enchantment spell into your spellbook is halved."""

    feature2 = """Hypnotic Gaze

Starting at 2nd level when you choose this school, your soft words and enchanting gaze can magically enthrall another creature. As an action, choose one creature that you can see within 5 feet of you. If the target can see or hear you, it must succeed on a Wisdom saving throw against your wizard spell save DC or be charmed by you until the end of your next turn. The charmed creature's speed drops to 0, and the creature is incapacitated and visibly dazed.

On subsequent turns, you can use your action to maintain this effect, extending its duration until the end of your next turn. However, the effect ends if you move more than 5 feet away from the creature, if the creature can neither see nor hear you, or if the creature takes damage.

Once the effect ends, or if the creature succeeds on its initial saving throw against this effect, you can't use this feature on that creature again until you finish a long rest."""

    print(feature)
    dnd_dict.character_dict["features"]['enchantment_savant'] = feature
    print(feature2)
    dnd_dict.character_dict["features"]['hypnotic_gaze_wizard'] = feature2

def enchantment_wizard6():
    feature = """Instinctive Charm

Beginning at 6th level, when a creature you can see within 30 feet of you makes an attack roll against you, you can use your reaction to divert the attack, provided that another creature is within the attack's range. The attacker must make a Wisdom saving throw against your wizard spell save DC. On a failed save, the attacker must target the creature that is closest to it, not including you or itself. If multiple creatures are closest, the attacker chooses which one to target.

On a successful save, you can't use this feature on the attacker again until you finish a long rest.

You must choose to use this feature before knowing whether the attack hits or misses. Creatures that can't be charmed are immune to this effect."""

    print(feature)
    dnd_dict.character_dict["features"]['instinctive_charm'] = feature

def enchantment_wizard10():
    feature = """Split Enchantment

Starting at 10th level, when you cast an enchantment spell of 1st level or higher that targets only one creature, you can have it target a second creature."""

    print(feature)
    dnd_dict.character_dict["features"]['split_enchantment'] = feature

def enchantment_wizard14():
    feature = """Alter Memories

At 14th level, you gain the ability to make a creature unaware of your magical influence on it. When you cast an enchantment spell to charm one or more creatures, you can alter one creature's understanding so that it remains unaware of being charmed.

Additionally, once before the spell expires, you can use your action to try to make the chosen creature forget some of the time it spent charmed. The creature must succeed on an Intelligence saving throw against your wizard spell save DC or lose a number of hours of its memories equal to 1 + your Charisma modifier (minimum 1). You can make the creature forget less time, and the amount of time can't exceed the duration of your enchantment spell."""

    print(feature)
    dnd_dict.character_dict["features"]['alter_memories_wizard'] = feature

def evocation_wizard2():
    feature = """Evocation Savant

Beginning when you select this school at 2nd level, the gold and time you must spend to copy a Evocation spell into your spellbook is halved."""

    feature2 = """Sculpt Spells

Beginning at 2nd level, you can create pockets of relative safety within the effects of your evocation spells. When you cast an evocation spell that affects other creatures that you can see, you can choose a number of them equal to 1 + the spell's level. The chosen creatures automatically succeed on their saving throws against the spell, and they take no damage if they would normally take half damage on a successful save."""

    print(feature)
    dnd_dict.character_dict["features"]['evocation_savant'] = feature
    print(feature2)
    dnd_dict.character_dict["features"]['sculpt_spells'] = feature2

def evocation_wizard6():
    feature = """Potent Cantrip

Starting at 6th level, your damaging cantrips affect even creatures that avoid the brunt of the effect. When a creature succeeds on a saving throw against your cantrip, the creature takes half the cantrip's damage (if any) but suffers no additional effect from the cantrip."""
    print(feature)
    dnd_dict.character_dict["features"]['potent_cantrip_wizard'] = feature

def evocation_wizard10():
    feature = """Empowered Evocation

Beginning at 10th level, you can add your Intelligence modifier (minimum of +1) to one damage roll of any wizard evocation spell that you cast."""
    print(feature)
    dnd_dict.character_dict["features"]['empowered_evocation'] = feature

def evocation_wizard14():
    feature = """Overchannel

Starting at 14th level, you can increase the power of your simpler spells. When you cast a wizard spell of 1st through 5th level that deals damage, you can deal maximum damage with that spell.

The first time you do so, you suffer no adverse effect. If you use this feature again before you finish a long rest, you take 2d12 necrotic damage for each level of the spell, immediately after you cast it. Each time you use this feature again before finishing a long rest, the necrotic damage per spell level increases by 1d12. This damage ignores resistance and immunity."""
    print(feature)
    dnd_dict.character_dict["features"]['overchannel'] = feature

def illusion_wizard2():
    feature = """Illusion Savant

Beginning when you select this school at 2nd level, the gold and time you must spend to copy a Illusion spell into your spellbook is halved."""

    feature2 = """Improved Minor Illusion

When you choose this school at 2nd level, you learn the Minor Illusion cantrip. If you already know this cantrip, you learn a different wizard cantrip of your choice. The cantrip doesn't count against your number of cantrips known.

When you cast Minor Illusion, you can create both a sound and an image with a single casting of the spell."""

    print(feature)
    dnd_dict.character_dict["features"]['illusion_savant'] = feature
    print(feature2)
    dnd_dict.character_dict["features"]['improved_minor_illusion'] = feature2
    dnd_dict.character_dict['spells']['minor_illusion'] = 'Minor Illusion'
    
def illusion_wizard6():
    feature = """Malleable Illusions

Starting at 6th level, when you cast an illusion spell that has a duration of 1 minute or longer, you can use your action to change the nature of that illusion (using the spell's normal parameters for the illusion), provided that you can see the illusion."""
    print(feature)
    dnd_dict.character_dict["features"]['malleable_illusions'] = feature

def illusion_wizard10():
    feature = """Illusory Self

Beginning at 10th level, you can create an illusory duplicate of yourself as an instant, almost instinctual reaction to danger. When a creature makes an attack roll against you, you can use your reaction to interpose the illusory duplicate between the attacker and yourself. The attack automatically misses you, then the illusion dissipates.

Once you use this feature, you can't use it again until you finish a short or long rest."""
    print(feature)
    dnd_dict.character_dict["features"]['illusory_self'] = feature

def illusion_wizard14():
    feature = """Illusory Reality

By 14th level, you have learned the secret of weaving shadow magic into your illusions to give them a semi-reality. When you cast an illusion spell of 1st level or higher, you can choose one inanimate, nonmagical object that is part of the illusion and make that object real. You can do this on your turn as a bonus action while the spell is ongoing. The object remains real for 1 minute. For example, you can create an illusion of a bridge over a chasm and then make it real long enough for your allies to cross.

The object can't deal damage or otherwise directly harm anyone."""
    print(feature)
    dnd_dict.character_dict["features"]['illusory_reality'] = feature

def necromancy_wizard2():
    feature = """Necromancy Savant

Beginning when you select this school at 2nd level, the gold and time you must spend to copy a Necromancy spell into your spellbook is halved."""

    feature2 = """Grim Harvest

At 2nd level, you gain the ability to reap life energy from creatures you kill with your spells. Once per turn when you kill one or more creatures with a spell of 1st level or higher, you regain hit points equal to twice the spell's level, or three times its level if the spell belongs to the School of Necromancy. You don't gain this benefit for killing constructs or undead."""

    print(feature)
    dnd_dict.character_dict["features"]['necromancy_savant'] = feature
    print(feature2)
    dnd_dict.character_dict["features"]['grim_harvest'] = feature2

def necromancy_wizard6():
    feature = """Undead Thralls

At 6th level, you add the Animate Dead spell to your spellbook if it is not there already. When you cast Animate Dead, you can target one additional corpse or pile of bones, creating another zombie or skeleton, as appropriate.

Whenever you create an undead using a necromancy spell, it has additional benefits:

    The creature's hit point maximum is increased by an amount equal to your wizard level.

    The creature adds your proficiency bonus to its weapon damage rolls."""

    print(feature)
    dnd_dict.character_dict["features"]['undead_thralls'] = feature
    dnd_dict.character_dict['spells']['third']['animate_dead'] = 'Animate Dead'

def necromancy_wizard10():
    feature = """Inured to Undeath

Beginning at 10th level, you have resistance to necrotic damage, and your hit point maximum can't be reduced. You have spent so much time dealing with undead and the forces that animate them that you have become inured to some of their worst effects."""
    print(feature)
    dnd_dict.character_dict["features"]['inured_to_undeath'] = feature

def necromancy_wizard14():
    feature = """Command Undead

Starting at 14th level, you can use magic to bring undead under your control, even those created by other wizards. As an action, you can choose one undead that you can see within 60 feet of you. That creature must make a Charisma saving throw against your wizard spell save DC. If it succeeds, you can't use this feature on it again. If it fails, it becomes friendly to you and obeys your commands until you use this feature again.

Intelligent undead are harder to control in this way. If the target has an Intelligence of 8 or higher, it has advantage on the saving throw. If it fails the saving throw and has an Intelligence of 12 or higher, it can repeat the saving throw at the end of every hour until it succeeds and breaks free."""
    print(feature)
    dnd_dict.character_dict["features"]['command_undead'] = feature

def transmutation_wizard2():
    feature = """Transmutation Savant

Beginning when you select this school at 2nd level, the gold and time you must spend to copy a Transmutation spell into your spellbook is halved."""

    feature2 = """Minor Alchemy

Starting at 2nd level when you select this school, you can temporarily alter the physical properties of one nonmagical object, changing it from one substance into another. You perform a special alchemical procedure on one object composed entirely of wood, stone (but not a gemstone), iron, copper, or silver, transforming it into a different one of those materials. For each 10 minutes you spend performing the procedure, you can transform up to 1 cubic foot of material. After 1 hour, or until you lose your concentration (as if you were concentrating on a spell), the material reverts to its original substance."""

    print(feature)
    dnd_dict.character_dict["features"]['transmutation_savant'] = feature
    print(feature2)
    dnd_dict.character_dict["features"]['minor_alchemy'] = feature2

def transmutation_wizard6():
    feature = """Transmuter's Stone

Starting at 6th level, you can spend 8 hours creating a transmuter's stone that stores transmutation magic. You can benefit from the stone yourself or give it to another creature. A creature gains a benefit of your choice as long as the stone is in the creature's possession. When you create the stone, choose the benefit from the following options:

    Darkvision out to a range of 60 feet

    An increase to speed of 10 feet while the creature is unencumbered

    Proficiency in Constitution saving throws

    Resistance to acid, cold, fire, lightning, or thunder damage (your choice whenever you choose this benefit)

Each time you cast a transmutation spell of 1st level or higher, you can change the effect of your stone if the stone is on your person.

If you create a new transmuter's stone, the previous one ceases to function."""

    print(feature)
    dnd_dict.character_dict["features"]['transmuters_stone'] = feature

def transmutation_wizard10():
    feature = """Shapechanger

At 10th level, you add the Polymorph spell to your spellbook, if it is not there already. You can cast Polymorph without expending a spell slot. When you do so, you can target only yourself and transform into a beast whose challenge rating is 1 or lower.

Once you cast Polymorph in this way, you can't do so again until you finish a short or long rest, though you can still cast it normally using an available spell slot."""

    print(feature)
    dnd_dict.character_dict["features"]['shapechanger_wizard'] = feature
    dnd_dict.character_dict['spells']['fourth']['polymorph'] = 'Polymorph'

def transmutation_wizard14():
    feature = """Master Transmuter

Starting at 14th level, you can use your action to consume the reserve of transmutation magic stored within your transmuter's stone in a single burst. When you do so, choose one of the following effects. Your transmuter's stone is destroyed and can't be remade until you finish a long rest.

Major Transformation. You can transmute one nonmagical object – no larger than a 5-foot cube – into another nonmagical object of similar size and mass and of equal or lesser value. You must spend 10 minutes handling the object to transform it.

Panacea. You remove all curses, diseases, and poisons affecting a creature that you touch with the transmuter's stone. The creature also regains all its hit points.

Restore Life. You cast the Raise Dead spell on a creature you touch with the transmuter's stone, without expending a spell slot or needing to have the spell in your spellbook.

Restore Youth. You touch the transmuter's stone to a willing creature, and that creature's apparent age is reduced by 3d10 years, to a minimum of 13 years. This effect doesn't extend the creature's lifespan."""

    print(feature)
    dnd_dict.character_dict["features"]['master_transmuter'] = feature

def abberant_dragonmark():
    feature = """
Aberrant Dragonmark
Prerequisite: No other dragonmark

You have manifested an aberrant dragonmark. Determine its appearance and the flaw associated with it. You gain the following benefits:

    Increase your Constitution score by 1, to a maximum of 20.
    You learn a cantrip of your choice from the sorcerer spell list. In addition, choose a 1st-level spell from the sorcerer spell list. You learn that spell and can cast it through your mark. Once you cast it, you must finish a short or long rest before you can cast it again through the mark. Constitution is your spellcasting ability for these spells.
    When you cast the 1st-level spell through your mark, you can expend one of your Hit Dice and roll it. If you roll an even number, you gain a number of temporary hit points equal to the number rolled. If you roll an odd number, one random creature within 30 feet of you (not including you) takes force damage equal to the number rolled. If no other creatures are in range, you take the damage.

You also develop a random flaw from the Aberrant Dragonmark Flaws table.
Aberrant Dragonmark Flawsd8	Flaw
1	Your mark is a source of constant physical pain.
2	Your mark whispers to you. Its meaning can be unclear.
3	When you're stressed, the mark hisses audibly.
4	The skin around the mark is burned, scaly, or withered.
5	Animals are uneasy around you.
6	You have a mood swing any time you use your mark.
7	Your looks change slightly whenever you use the mark.
8	You have horrific nightmares after you use your mark.
Option: Greater Aberrant Powers[–]

At the DM's option, a character who has the Aberrant Dragonmark feat has a chance of manifesting greater power. Upon reaching 10th level, such a character has a 10 percent chance of gaining an epic boon from among the options in chapter 7 of the Dungeon Master's Guide. If the character fails to gain a boon, they have a 10 percent chance the next time they gain a level.

If the character gains a boon, the DM chooses it or determines it randomly. The character also permanently loses one of their Hit Dice, and their hit point maximum is reduced by an amount equal to a roll of that die plus their Constitution modifier (minimum reduction of 1). This reduction can't be reversed by any means."""

    print(feature)
    dnd_dict.character_dict["features"]['aberrant_dragonmark'] = feature
    dnd_dict.character_dict["feats"]['abberant_dragonmark'] = 'Abberant Dragonmark'
    if dnd_dict.character_dict['Stats']['constitution']['base'] < 20:
        dnd_dict.character_dict['Stats']['constitution']['base'] += 1
# If the modifier is positive and increases, increase your hp by your total level
        mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['constitution']['base'])
        if mod > dnd_dict.character_dict['Stats']['constitution']['mod'] and mod > 0:
            new_hp = dnd_dict.character_dict['hp'] + dnd_dict.character_dict['total_level']
            dnd_dict.character_dict['hp'] = new_hp
            dnd_dict.character_dict['Stats']['constitution']['mod'] = mod
    dnd_skills.spell_add(dnd_magic.sorcerer_cantrip,dnd_dict.character_dict['spells']['cantrips'],dnd_dict.character_dict['special_spells']['cantrips'])
    dnd_skills.spell_add(dnd_magic.sorcerer_first,dnd_dict.character_dict['spells']['first'],dnd_dict.character_dict['special_spells']['first'])
    spell_attack = ((dnd_dict.character_dict["Stats"]["constitution"]['mod']) + dnd_dict.character_dict['prof_bonus'])
    dnd_dict.character_dict["spell_modifier"]['constitution']['attack'] = spell_attack
    spell_save = ((dnd_dict.character_dict["Stats"]["constitution"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
    dnd_dict.character_dict["spell_modifier"]['constitution']['save'] = spell_save


def actor():
    feature = """
Actor

Skilled at mimicry and dramatics, you gain the following benefits:

    Increase your Charisma score by 1, to a maximum of 20.
    You have advantage on Charisma (Deception) and Charisma (Performance) checks when trying to pass yourself off as a different person.
    You can mimic the speech of another person or the sounds made by other creatures. You must have heard the person speaking, or heard the creature make the sound, for at least 1 minute. A successful Wisdom (Insight) check contested by your Charisma (Deception) check allows a listener to determine that the effect is faked"""

    print(feature)
    dnd_dict.character_dict["features"]['actor'] = feature
    dnd_dict.character_dict["feats"]['actor'] = 'Actor'
    if dnd_dict.character_dict['Stats']['charisma']['base'] < 20:
        dnd_dict.character_dict['Stats']['charisma']['base'] += 1

def alert():
    feature = """
Alert

Always on the lookout for danger, you gain the following benefits:

    You gain a +5 bonus to initiative.
    You can't be surprised while you are conscious.
    Other creatures don't gain advantage on attack rolls against you as a result of being unseen by you."""
    print(feature)
    dnd_dict.character_dict["features"]['alert'] = feature
    dnd_dict.character_dict["feats"]['alert'] = 'Alert'
    dnd_dict.character_dict['passive_perception'] += 5

def artificer_initiate():
    feature = """
Artificer Initiate

You've learned some of an artificer's inventiveness:

    You learn one cantrip of your choice from the artificer spell list, and you learn one 1st-level spell of your choice from that list. Intelligence is your spellcasting ability for these spells.
    You can cast this feat's 1st-level spell without a spell slot, and you must finish a long rest before you can cast it in this way again. You can also cast the spell using any spell slots you have.
    You gain proficiency with one type of artisan's tools of your choice, and you can use that type of tool as a spellcasting focus for any spell you cast that uses Intelligence as its spellcasting ability"""
    print(feature)
    dnd_dict.character_dict["features"]['artificer_initiate'] = feature
    dnd_dict.character_dict["feats"]['artificer_initiate'] = 'Artificer Initiate'
    dnd_skills.spell_add(dnd_magic.artificer_cantrip,dnd_dict.character_dict['spells']['cantrips'],dnd_dict.character_dict['special_spells']['cantrips'])
    dnd_skills.spell_add(dnd_magic.artificer_first_classless,dnd_dict.character_dict['spells']['first'],dnd_dict.character_dict['special_spells']['first'])
    dnd_tools.artisan_tools()

def athlete():
    feature = """
Athlete

You have undergone extensive physical training to gain the following benefits:

    Increase your Strength or Dexterity by 1, to a maximum of 20.
    When you are prone, standing up uses only 5 feet of your movement.
    Climbing doesn't cost you extra movement.
    You can make a running long jump or a running high jump after moving only 5 feet on foot, rather than 10 feet."""
    print(feature)
    dnd_dict.character_dict["features"]['athlete'] = feature
    dnd_dict.character_dict["feats"]['athlete'] = 'Athlete'
    if dnd_dict.character_dict['Stats']['strength']['base'] < 20 or dnd_dict.character_dict['Stats']['dexterity']['base'] < 20:
        while True:
            choice = input("""Which stat would you like to increase by 1 to a maximum of 20?
1) Strength
2) Dexterity
Enter your selection: """)
            if choice == '1':
                if dnd_dict.character_dict['Stats']['strength']['base'] < 20:
                    dnd_dict.character_dict['Stats']['strength']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['strength']['base'])
                    dnd_dict.character_dict['Stats']['strength']['mod'] = mod
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            elif choice == '2':
                if dnd_dict.character_dict['Stats']['dexterity']['base'] < 20:
                    dnd_dict.character_dict['Stats']['dexterity']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['dexterity']['base'])
                    dnd_dict.character_dict['Stats']['dexterity']['mod'] = mod
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            else:
                print("Error: Invalid Input")
                continue
    if dnd_dict.character_dict['unarmored_movement_barbarian'] > 0:
        dnd_dict.character_dict['climb_speed'] == dnd_dict.character_dict['unarmored_movement_barbarian']
    if dnd_dict.character_dict['unarmored_movement_monk'] > 0:
        dnd_dict.character_dict['climb_speed'] == dnd_dict.character_dict['unarmored_movement_monk']
    else:
        dnd_dict.character_dict['climb_speed'] == dnd_dict.character_dict['speed']

def bountiful_luck():
    feature = """
Bountiful Luck
Prerequisite: Halfling

Your people have extraordinary luck, which you have learned to mystically lend to your companions when you see them falter. You're not sure how you do it; you just wish it, and it happens. Surely a sign of fortune's favor!

When an ally you can see within 30 feet of you rolls a 1 on the d20 for an attack roll, an ability check, or a saving throw, you can use your reaction to let the ally reroll the die. The ally must use the new roll.

When you use this ability, you can't use your Lucky racial trait before the end of your next turn."""
    print(feature)
    dnd_dict.character_dict["features"]['bountiful_luck'] = feature
    dnd_dict.character_dict["feats"]['bountiful_luck'] = 'Bountiful Luck'

def charger():
    feature = """
Charger

When you use your action to Dash, you can use a bonus action to make one melee weapon attack or to shove a creature.

If you move at least 10 feet in a straight line immediately before taking this bonus action, you either gain a +5 bonus to the attack's damage roll (if you chose to make a melee attack and hit) or push the target up to 10 feet away from you (if you chose to shove and you succeed)."""
    print(feature)
    dnd_dict.character_dict["features"]['charger'] = feature
    dnd_dict.character_dict["feats"]['charger'] = 'Charger'

def chef():
    feature = """
Chef

Time spent mastering the culinary arts has paid off, granting you the following benefits:

    Increase your Constitution or Wisdom by 1, to a maximum of 20.
    You gain proficiency with cook's utensils if you don't already have it.
    As part of a short rest, you can cook special food, provided you have ingredients and cook's utensils on hand. You can prepare enough of this food for a number of creatures equal to 4 + your proficiency bonus. At the end of the short rest, any creature who eats the food and spends one or more Hit Dice to regain hit points regains an extra 1d8 hit points.
    With one hour of work or when you finish a long rest, you can cook a number of treats equal to your proficiency bonus. These special treats last 8 hours after being made. A creature can use a bonus action to eat one of those treats to gain temporary hit points equal to your proficiency bonus."""
    print(feature)
    dnd_dict.character_dict["features"]['chef'] = feature
    dnd_dict.character_dict["feats"]['chef'] = 'Chef'
    dnd_dict.character_dict['Tools']['chef\'s_utensils'] = 'Chef\'s Utensils'
    if dnd_dict.character_dict['Stats']['wisdom']['base'] < 20 or dnd_dict.character_dict['Stats']['constitution']['base'] < 20:
        while True:
            choice = input("""Which stat would you like to increase by 1 to a maximum of 20?
1) Constitution
2) Wisdom
Enter your selection: """)
            if choice == '1':
                if dnd_dict.character_dict['Stats']['constitution']['base'] < 20:
                    dnd_dict.character_dict['Stats']['constitution']['base'] += 1
# If the modifier is positive and increases, increase your hp by your total level
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['constitution']['base'])
                    if mod > dnd_dict.character_dict['Stats']['constitution']['mod'] and mod > 0:
                        new_hp = dnd_dict.character_dict['hp'] + dnd_dict.character_dict['total_level']
                        dnd_dict.character_dict['hp'] = new_hp
                    dnd_dict.character_dict['Stats']['constitution']['mod'] = mod
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            elif choice == '2':
                if dnd_dict.character_dict['Stats']['wisdom']['base'] < 20:
                    dnd_dict.character_dict['Stats']['wisdom']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['wisdom']['base'])
                    dnd_dict.character_dict['Stats']['wisdom']['mod'] = mod
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            else:
                print("Error: Invalid Input")
                continue

def crossbow_expert():
    feature = """
Crossbow Expert

Thanks to extensive practice with the crossbow, you gain the following benefits:

    You ignore the loading quality of crossbows with which you are proficient.
    Being within 5 feet of a hostile creature doesn't impose disadvantage on your ranged attack rolls.
    When you use the Attack action and attack with a one-handed weapon, you can use a bonus action to attack with a hand crossbow you are holding"""
    print(feature)
    dnd_dict.character_dict["features"]['crossbow_expert'] = feature
    dnd_dict.character_dict["feats"]['crossbow_expert'] = 'Crossbow Expert'

def crusher():
    feature = """
Crusher

You are practiced in the art of crushing your enemies, granting you the following benefits:

    Increase your Strength or Constitution by 1, to a maximum of 20.
    Once per turn, when you hit a creature with an attack that deals bludgeoning damage, you can move it 5 feet to an unoccupied space, provided the target is no more than one size larger than you.
    When you score a critical hit that deals bludgeoning damage to a creature, attack rolls against that creature are made with advantage until the start of your next turn."""
    print(feature)
    dnd_dict.character_dict["features"]['crusher'] = feature
    dnd_dict.character_dict["feats"]['crusher'] = 'Crusher'

    if dnd_dict.character_dict['Stats']['strength']['base'] < 20 or dnd_dict.character_dict['Stats']['constitution']['base'] < 20:
        while True:
            choice = input("""Which stat would you like to increase by 1 to a maximum of 20?
1) Strength
2) Constitution
Enter your selection: """)

            if choice == '1':
                if dnd_dict.character_dict['Stats']['strength']['base'] < 20:
                    dnd_dict.character_dict['Stats']['strength']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['strength']['base'])
                    dnd_dict.character_dict['Stats']['strength']['mod'] = mod
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            elif choice == '2':
                if dnd_dict.character_dict['Stats']['constitution']['base'] < 20:
                    dnd_dict.character_dict['Stats']['constitution']['base'] += 1
# If the modifier is positive and increases, increase your hp by your total level
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['constitution']['base'])
                    if mod > dnd_dict.character_dict['Stats']['constitution']['mod'] and mod > 0:
                        new_hp = dnd_dict.character_dict['hp'] + dnd_dict.character_dict['total_level']
                        dnd_dict.character_dict['hp'] = new_hp
                    dnd_dict.character_dict['Stats']['constitution']['mod'] = mod
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue


            else:
                print("Error: Invalid Input")
                continue

def defensive_duelist():
    feature = """
Defensive Duelist
Prerequisite: Dexterity 13 or higher

When you are wielding a finesse weapon with which you are proficient and another creature hits you with a melee attack, you can use your reaction to add your proficiency bonus to your AC for that attack, potentially causing the attack to miss you."""
    print(feature)
    dnd_dict.character_dict["features"]['defensive_duelist'] = feature
    dnd_dict.character_dict["feats"]['defensive_duelist'] = 'Defensive Duelist'

def dragon_fear():
    feature = """
Dragon Fear
Prerequisite: Dragonborn

When angered, you radiate menace. You gain the following benefits:

    Increase your Strength, Constitution, or Charisma by 1, to a maximum of 20.
    Instead of exhaling destructive energy, you can expend a use of your Breath Weapon trait to roar, forcing each creature of your choice within 30 feet of you to make a Wisdom saving throw (DC 8 + your proficiency bonus + your Charisma modifier). A target automatically succeeds on the save if it can't hear or see you. On a failed save, a target becomes frightened of you for 1 minute. If the frightened target takes any damage, it can repeat the saving throw, ending the effect on itself on a success."""
    print(feature)
    dnd_dict.character_dict["features"]['dragon_fear'] = feature
    dnd_dict.character_dict["feats"]['dragon_fear'] = 'Dragon Fear'

    if dnd_dict.character_dict['Stats']['strength']['base'] < 20 or dnd_dict.character_dict['Stats']['constitution']['base'] < 20 or dnd_dict.character_dict['Stats']['charisma']['base'] < 20:
        while True:
            choice = input("""Which stat would you like to increase by 1 to a maximum of 20?
1) Strength
2) Constitution
3) Charisma
Enter your selection: """)

            if choice == '1':
                if dnd_dict.character_dict['Stats']['strength']['base'] < 20:
                    dnd_dict.character_dict['Stats']['strength']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['strength']['base'])
                    dnd_dict.character_dict['Stats']['strength']['mod'] = mod
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            elif choice == '2':
                if dnd_dict.character_dict['Stats']['constitution']['base'] < 20:
                    dnd_dict.character_dict['Stats']['constitution']['base'] += 1
# If the modifier is positive and increases, increase your hp by your total level
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['constitution']['base'])
                    if mod > dnd_dict.character_dict['Stats']['constitution']['mod'] and mod > 0:
                        new_hp = dnd_dict.character_dict['hp'] + dnd_dict.character_dict['total_level']
                        dnd_dict.character_dict['hp'] = new_hp
                    dnd_dict.character_dict['Stats']['constitution']['mod'] = mod
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            elif choice == '3':
                if dnd_dict.character_dict['Stats']['charisma']['base'] < 20:
                    dnd_dict.character_dict['Stats']['charisma']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['charisma']['base'])
                    dnd_dict.character_dict['Stats']['charisma']['mod'] = mod
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue


            else:
                print("Error: Invalid Input")
                continue

def dragon_hide():
    feature = """
Dragon Hide
Prerequisite: Dragonborn

You manifest scales and claws reminiscent of your draconic ancestors. You gain the following benefits:

    Increase your Strength, Constitution, or Charisma by 1, to a maximum of 20.
    Your scales harden. While you aren't wearing armor, you can calculate your AC as 13 + your Dexterity modifier. You can use a shield and still gain this benefit.
    You grow retractable claws from the tips of your fingers. Extending or retracting the claws requires no action. The claws are natural weapons, which you can use to make unarmed strikes. If you hit with them, you deal slashing damage equal to 1d4 + your Strength modifier, instead of the normal bludgeoning damage for an unarmed strike."""

    print(feature)
    dnd_dict.character_dict["features"]['dragon_hide'] = feature
    dnd_dict.character_dict["feats"]['dragon_hide'] = 'Dragon Hide'
    new_armor = dnd_dict.character_dict['Stats']['dexterity']['base'] + 13
    dnd_dict.character_dict['natural_armor_class'] = new_armor

    if dnd_dict.character_dict['Stats']['strength']['base'] < 20 or dnd_dict.character_dict['Stats']['constitution']['base'] < 20 or dnd_dict.character_dict['Stats']['charisma']['base'] < 20:
        while True:
            choice = input("""Which stat would you like to increase by 1 to a maximum of 20?
1) Strength
2) Constitution
3) Charisma
Enter your selection: """)

            if choice == '1':
                if dnd_dict.character_dict['Stats']['strength']['base'] < 20:
                    dnd_dict.character_dict['Stats']['strength']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['strength']['base'])
                    dnd_dict.character_dict['Stats']['strength']['mod'] = mod
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            elif choice == '2':
                if dnd_dict.character_dict['Stats']['constitution']['base'] < 20:
                    dnd_dict.character_dict['Stats']['constitution']['base'] += 1
# If the modifier is positive and increases, increase your hp by your total level
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['constitution']['base'])
                    if mod > dnd_dict.character_dict['Stats']['constitution']['mod'] and mod > 0:
                        new_hp = dnd_dict.character_dict['hp'] + dnd_dict.character_dict['total_level']
                        dnd_dict.character_dict['hp'] = new_hp
                    dnd_dict.character_dict['Stats']['constitution']['mod'] = mod
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            elif choice == '3':
                if dnd_dict.character_dict['Stats']['charisma']['base'] < 20:
                    dnd_dict.character_dict['Stats']['charisma']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['charisma']['base'])
                    dnd_dict.character_dict['Stats']['charisma']['mod'] = mod
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue


            else:
                print("Error: Invalid Input")
                continue

def drow_high_magic():
    feature = """
Drow High Magic
Prerequisite: Elf (drow)

You learn more of the magic typical of dark elves. You learn the detect magic spell and can cast it at will, without expending a spell slot. You also learn levitate and dispel magic, each of which you can cast once without expending a spell slot. You regain the ability to cast those two spells in this way when you finish a long rest. Charisma is your spellcasting ability for all three spells."""

    print(feature)
    dnd_dict.character_dict["features"]['drow_high_magic'] = feature
    dnd_dict.character_dict["feats"]['drow_high_magic'] = 'Drow High Magic'
    dnd_dict.character_dict['spells']['first']['detect_magic'] = 'Detect Magic'
    dnd_dict.character_dict['spells']['second']['levitate'] = 'Levitate'
    dnd_dict.character_dict['spells']['third']['dispel_magic'] = 'Dispel Magic'
    dnd_dict.character_dict['special_spells']['racial_spells']['detect_magic'] = 'Detect Magic'
    dnd_dict.character_dict['special_spells']['racial_spells']['levitate'] = 'Levitate'
    dnd_dict.character_dict['special_spells']['racial_spells']['dispel_magic'] = 'Dispel Magic'
    spell_attack = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'])
    dnd_dict.character_dict["spell_modifier"]['charisma']['attack'] = spell_attack
    spell_save = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
    dnd_dict.character_dict["spell_modifier"]['charisma']['save'] = spell_save

def dual_wielder():
    feature = """
Dual Wielder

You master fighting with two weapons, gaining the following benefits:

    You gain a +1 bonus to AC while you are wielding a separate melee weapon in each hand.
    You can use two-weapon fighting even when the one-handed melee weapons you are wielding aren't light.
    You can draw or stow two one-handed weapons when you would normally be able to draw or stow only one."""
    print(feature)
    dnd_dict.character_dict["features"]['dual_wielder'] = feature
    dnd_dict.character_dict["feats"]['dual_wielder'] = 'Dual Wielder'

def dungeon_delver():
    feature = """
Dungeon Delver

Alert to the hidden traps and secret doors found in many dungeons, you gain the following benefits:

    You have advantage on Wisdom (Perception) and Intelligence (Investigation) checks made to detect the presence of secret doors.
    You have advantage on saving throws made to avoid or resist traps.
    You have resistance to the damage dealt by traps.
    Traveling at a fast pace doesn't impose the normal -5 penalty on your passive Wisdom (Perception) score."""
    print(feature)
    dnd_dict.character_dict["features"]['dungeon_delver'] = feature
    dnd_dict.character_dict["feats"]['dungeoun_delver'] = 'Dungeon Delver'

def durable():
    feature = """
Durable

Hardy and resilient, you gain the following benefits:

    Increase your Constitution score by 1, to a maximum of 20.
    When you roll a Hit Die to regain hit points, the minimum number of hit points you regain from the roll equals twice your Constitution modifier (minimum of 2)"""
    print(feature)
    dnd_dict.character_dict["features"]['durable'] = feature
    dnd_dict.character_dict["feats"]['durable'] = 'Durable'
    if dnd_dict.character_dict['Stats']['constitution']['base'] < 20:
        dnd_dict.character_dict['Stats']['constitution']['base'] += 1
# If the modifier is positive and increases, increase your hp by your total level
        mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['constitution']['base'])
        if mod > dnd_dict.character_dict['Stats']['constitution']['mod'] and mod > 0:
            new_hp = dnd_dict.character_dict['hp'] + dnd_dict.character_dict['total_level']
            dnd_dict.character_dict['hp'] = new_hp
            dnd_dict.character_dict['Stats']['constitution']['mod'] = mod

def dwarven_fortitude():
    feature = """
Dwarven Fortitude
Prerequisite: Dwarf

You have the blood of dwarf heroes flowing through your veins. You gain the following benefits:

    Increase your Constitution score by 1, to a maximum of 20.
    Whenever you take the Dodge action in combat, you can spend one Hit Die to heal yourself. Roll the die, add your Constitution modifier, and regain a number of hit points equal to the total (minimum of 1)."""
    print(feature)
    dnd_dict.character_dict["features"]['dwarven_fortitude'] = feature
    dnd_dict.character_dict["feats"]['dwarven_fortitude'] = 'Dwarven Fortitude'
    if dnd_dict.character_dict['Stats']['constitution']['base'] < 20:
        dnd_dict.character_dict['Stats']['constitution']['base'] += 1
# If the modifier is positive and increases, increase your hp by your total level
        mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['constitution']['base'])
        if mod > dnd_dict.character_dict['Stats']['constitution']['mod'] and mod > 0:
            new_hp = dnd_dict.character_dict['hp'] + dnd_dict.character_dict['total_level']
            dnd_dict.character_dict['hp'] = new_hp
            dnd_dict.character_dict['Stats']['constitution']['mod'] = mod


def eldritch_adept():
    feature = """
Eldritch Adept
Prerequisite: Spellcasting or Pact Magic feature

Studying occult lore, you learn one Eldritch Invocation option of your choice from the warlock class. Your spellcasting ability for the invocation is Intelligence, Wisdom, or Charisma (choose when you select this feat). If the invocation has a prerequisite of any kind, you can choose that invocation only if you're a warlock who meets the prerequisite.

Whenever you gain a level, you can replace the invocation with another one from the warlock class."""
    print(feature)
    dnd_dict.character_dict["features"]['eldritch_adept'] = feature
    dnd_dict.character_dict["feats"]['eldritch_adept'] = 'Eldritch Adept'
    dnd_invocations.eldritch_adept_invocations()
    while True:
        choice = input("""What would you like your spellcasting modifier to be?
1) Intelligence
2) Wisdom
3) Charisma
Enter your selection: """)
        if choice == '1':
            spell_attack = ((dnd_dict.character_dict["Stats"]["intelligence"]['mod']) + dnd_dict.character_dict['prof_bonus'])
            dnd_dict.character_dict["spell_modifier"]['intelligence']['attack'] = spell_attack
            spell_save = ((dnd_dict.character_dict["Stats"]["intelligence"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
            dnd_dict.character_dict["spell_modifier"]['intelligence']['save'] = spell_save
            break
        elif choice == '2':
            spell_attack = ((dnd_dict.character_dict["Stats"]["wisdom"]['mod']) + dnd_dict.character_dict['prof_bonus'])
            dnd_dict.character_dict["spell_modifier"]['wisdom']['attack'] = spell_attack
            spell_save = ((dnd_dict.character_dict["Stats"]["wisdom"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
            dnd_dict.character_dict["spell_modifier"]['wisdom']['save'] = spell_save
            break
        elif choice == '3':
            spell_attack = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'])
            dnd_dict.character_dict["spell_modifier"]['charisma']['attack'] = spell_attack
            spell_save = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
            dnd_dict.character_dict["spell_modifier"]['charisma']['save'] = spell_save
            break
        else:
            print("Error: Invalid Input")
            continue

def elemental_adept():
    feature = """
Elemental Adept
Prerequisite: The ability to cast at least one spell

When you gain this feat, choose one of the following damage types: acid, cold, fire, lightning, or thunder.

Spells you cast ignore resistance to damage of the chosen type. In addition, when you roll damage for a spell you cast that deals damage of that type, you can treat any 1 on a damage die as a 2.

You can select this feat multiple times. Each time you do so, you must choose a different damage type."""
    print(feature)
    while True:
        choice = input("""Select the type of damage you want
1) Acid
2) Cold
3) Fire
4) Lightning
5) Thunder
Enter your selection: """)
        if choice == '1':
            if 'elemental_adept_acid' in dnd_dict.character_dict['feats']:
                print("Error: damage type already selected")
                continue
            else:
                dnd_dict.character_dict["features"]['elemental_adept_acid'] = feature
                dnd_dict.character_dict["feats"]['elemental_adept_acid'] = 'Elemental Adept (Acid)'
                break
        elif choice == '2':
            if 'elemental_adept_cold' in dnd_dict.character_dict['feats']:
                print("Error: damage type already selected")
                continue
            else:
                dnd_dict.character_dict["features"]['elemental_adept_cold'] = feature
                dnd_dict.character_dict["feats"]['elemental_adept_cold'] = 'Elemental Adept (Cold)'
                break
        elif choice == '3':
            if 'elemental_adept_fire' in dnd_dict.character_dict['feats']:
                print("Error: damage type already selected")
                continue
            else:
                dnd_dict.character_dict["features"]['elemental_adept_fire'] = feature
                dnd_dict.character_dict["feats"]['elemental_adept_fire'] = 'Elemental Adept (Fire)'
                break
        elif choice == '4':
            if 'elemental_adept_lightning' in dnd_dict.character_dict['feats']:
                print("Error: damage type already selected")
                continue
            else:
                dnd_dict.character_dict["features"]['elemental_adept_lightning'] = feature
                dnd_dict.character_dict["feats"]['elemental_adept_lightning'] = 'Elemental Adept (Lightning)'
                break
        elif choice == '5':
            if 'elemental_adept_thunder' in dnd_dict.character_dict['feats']:
                print("Error: damage type already selected")
                continue
            else:
                dnd_dict.character_dict["features"]['elemental_adept_thunder'] = feature
                dnd_dict.character_dict["feats"]['elemental_adept_thunder'] = 'Elemental Adept (Thunder)'
                break
        else:
            print("Error: Invalid Input")
            continue

def elven_accuracy():
    feature = """
Elven Accuracy
Prerequisite: Elf or half-elf

The accuracy of elves is legendary, especially that of elf archers and spellcasters. You have uncanny aim with attacks that rely on precision rather than brute force. You gain the following benefits:

    Increase your Dexterity, Intelligence, Wisdom, or Charisma by 1, to a maximum of 20.
    Whenever you have advantage on an attack roll using Dexterity, Intelligence, Wisdom, or Charisma, you can reroll one of the dice once."""
    print(feature)
    dnd_dict.character_dict["features"]['elven_accuracy'] = feature
    dnd_dict.character_dict["feats"]['elven_accuracy'] = 'Elven Accuracy'

    while True:
        choice = input("""Which stat would you like to increase by 1 to a maximum of 20?
1) Dexterity
2) Intelligence
3) Wisdom
4) Charisma
Enter your selection: """)

        if choice == '1':
            if dnd_dict.character_dict['Stats']['dexterity']['base'] < 20:
                dnd_dict.character_dict['Stats']['dexterity']['base'] += 1
                mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['dexterity']['base'])
                dnd_dict.character_dict['Stats']['dexterity']['mod'] = mod
                break
            else:
                print("You already have the maximum score in this stat")
                continue

        elif choice == '2':
            if dnd_dict.character_dict['Stats']['intelligence']['base'] < 20:
                dnd_dict.character_dict['Stats']['intelligence']['base'] += 1
                mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['intelligence']['base'])
                dnd_dict.character_dict['Stats']['intelligence']['mod'] = mod
                break
            else:
                print("You already have the maximum score in this stat")
                continue

        elif choice == '3':
            if dnd_dict.character_dict['Stats']['wisdom']['base'] < 20:
                dnd_dict.character_dict['Stats']['wisdom']['base'] += 1
                mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['wisdom']['base'])
                dnd_dict.character_dict['Stats']['wisdom']['mod'] = mod
                break
            else:
                print("You already have the maximum score in this stat")
                continue

        elif choice == '4':
            if dnd_dict.character_dict['Stats']['charisma']['base'] < 20:
                dnd_dict.character_dict['Stats']['charisma']['base'] += 1
                mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['charisma']['base'])
                dnd_dict.character_dict['Stats']['charisma']['mod'] = mod
                break
            else:
                print("You already have the maximum score in this stat")
                continue

        else:
            print("Error: Invalid Input")
            continue

def fade_away():
    feature = """
Fade Away
Prerequisite: Gnome

Your people are clever, with a knack for illusion magic. You have learned a magical trick for fading away when you suffer harm. You gain the following benefits:

    Increase your Dexterity or Intelligence by 1, to a maximum of 20.
    Immediately after you take damage, you can use a reaction to magically become invisible until the end of your next turn or until you attack, deal damage, or force someone to make a saving throw. Once you use this ability, you can't do so again until you finish a short or long rest."""

    print(feature)
    dnd_dict.character_dict["features"]['fade_away'] = feature
    dnd_dict.character_dict["feats"]['fade_away'] = 'Fade Away'

    if dnd_dict.character_dict['Stats']['dexterity']['base'] < 20 or dnd_dict.character_dict['Stats']['intelligence']['base'] < 20:
        while True:
            choice = input("""Which stat would you like to increase by 1 to a maximum of 20?
1) Dexterity
2) Intelligence
Enter your selection: """)

            if choice == '1':
                if dnd_dict.character_dict['Stats']['dexterity']['base'] < 20:
                    dnd_dict.character_dict['Stats']['dexterity']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['dexterity']['base'])
                    dnd_dict.character_dict['Stats']['dexterity']['mod'] = mod
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            elif choice == '2':
                if dnd_dict.character_dict['Stats']['intelligence']['base'] < 20:
                    dnd_dict.character_dict['Stats']['intelligence']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['intelligence']['base'])
                    dnd_dict.character_dict['Stats']['intelligence']['mod'] = mod
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue
            else:
                print("Error: invalid input")
                continue

def fey_teleportation():
    feature = """
Fey Teleportation
Prerequisite: Elf (high)

Your study of high elven lore has unlocked fey power that few other elves possess, except your eladrin cousins. Drawing on your fey ancestry, you can momentarily stride through the Feywild to shorten your path from one place to another. You gain the following benefits:

    Increase your Intelligence or Charisma by 1, to a maximum of 20.
    You learn to speak, read, and write Sylvan.
    You learn the misty step spell and can cast it once without expending a spell slot. You regain the ability to cast it in this way when you finish a short or long rest. Intelligence is your spellcasting ability for this spell."""
    print(feature)
    dnd_dict.character_dict["features"]['fey_teleportation'] = feature
    dnd_dict.character_dict["feats"]['fey_teleportation'] = 'Fey Teleportation'
    dnd_dict.character_dict['Languages']['sylvan'] = 'Sylvan'
    dnd_dict.character_dict['spells']['second']['misty_step'] = 'Misty Step'
    dnd_dict.character_dict['special_spells']['racial_spells']['misty_step'] = 'Misty Step'
    spell_attack = ((dnd_dict.character_dict["Stats"]["intelligence"]['mod']) + dnd_dict.character_dict['prof_bonus'])
    dnd_dict.character_dict["spell_modifier"]['intelligence']['attack'] = spell_attack
    spell_save = ((dnd_dict.character_dict["Stats"]["intelligence"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
    dnd_dict.character_dict["spell_modifier"]['intelligence']['save'] = spell_save

def fey_touched():
    feature = """
Fey Touched

Your exposure to the Feywild's magic has changed you, granting you the following benefits:

    Increase your Intelligence, Wisdom, or Charisma by 1, to a maximum of 20.
    You learn the misty step spell and one 1st-level spell of your choice. The 1st-level spell must be from the divination or enchantment school of magic. You can cast each of these spells without expending a spell slot. Once you cast either of these spells in this way, you can't cast that spell in this way again until you finish a long rest. You can also cast these spells using spell slots you have of the appropriate level. The spells' spellcasting ability is the ability increased by this feat."""
    print(feature)
    dnd_dict.character_dict["features"]['fey_touched'] = feature
    dnd_dict.character_dict["feats"]['fey_touched'] = 'Fey Touched'
    dnd_dict.character_dict['spells']['second']['misty_step'] = 'Misty Step'
    dnd_dict.character_dict['special_spells']['racial_spells']['misty_step'] = 'Misty Step'
    spell_list = ['Animal Friendship','Bane','Beast Bond','Bless','Charm Person','Command','Compelled Duel','Comprehend Languages','Detect Evil and Good','Detect Magic','Detect Poison and Disease','Dissonant Whispers','Heroism','Hex','Hunter\'s Mark','Identify','Sleep','Speak with Animals','Tasha\'s Hideous Laughter']
    dnd_skills.spell_add(spell_list,dnd_dict.character_dict['spells']['first'],dnd_dict.character_dict['special_spells']['racial_spells'])

    if dnd_dict.character_dict['Stats']['intelligence']['base'] < 20 or dnd_dict.character_dict['Stats']['wisdom']['base'] < 20 or dnd_dict.character_dict['Stats']['charisma']['base'] < 20:
        while True:
            choice = input("""Which stat would you like to increase by 1 to a maximum of 20?
1) Intelligence
2) Wisdom
3) Charisma
Enter your selection: """)

            if choice == '1':
                if dnd_dict.character_dict['Stats']['intelligence']['base'] < 20:
                    dnd_dict.character_dict['Stats']['intelligence']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['intelligence']['base'])
                    dnd_dict.character_dict['Stats']['intelligence']['mod'] = mod
                    spell_attack = ((dnd_dict.character_dict["Stats"]["intelligence"]['mod']) + dnd_dict.character_dict['prof_bonus'])
                    dnd_dict.character_dict["spell_modifier"]['intelligence']['attack'] = spell_attack
                    spell_save = ((dnd_dict.character_dict["Stats"]["intelligence"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
                    dnd_dict.character_dict["spell_modifier"]['intelligence']['save'] = spell_save
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            elif choice == '2':
                if dnd_dict.character_dict['Stats']['wisdom']['base'] < 20:
                    dnd_dict.character_dict['Stats']['wisdom']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['wisdom']['base'])
                    dnd_dict.character_dict['Stats']['wisdom']['mod'] = mod
                    spell_attack = ((dnd_dict.character_dict["Stats"]["wisdom"]['mod']) + dnd_dict.character_dict['prof_bonus'])
                    dnd_dict.character_dict["spell_modifier"]['wisdom']['attack'] = spell_attack
                    spell_save = ((dnd_dict.character_dict["Stats"]["wisdom"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
                    dnd_dict.character_dict["spell_modifier"]['wisdom']['save'] = spell_save
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            elif choice == '3':
                if dnd_dict.character_dict['Stats']['charisma']['base'] < 20:
                    dnd_dict.character_dict['Stats']['charisma']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['charisma']['base'])
                    dnd_dict.character_dict['Stats']['charisma']['mod'] = mod
                    spell_attack = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'])
                    dnd_dict.character_dict["spell_modifier"]['charisma']['attack'] = spell_attack
                    spell_save = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
                    dnd_dict.character_dict["spell_modifier"]['charisma']['save'] = spell_save
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            else:
                print("Error: Invalid Input")
                continue

def fighting_initiate():
    feature = """
Fighting Initiate
Prerequisite: Proficiency with a martial weapon

Your martial training has helped you develop a particular style of fighting. As a result, you learn one Fighting Style option of your choice from the fighter class. If you already have a style, the one you choose must be different.

Whenever you reach a level that grants the Ability Score Improvement feature, you can replace this feat's fighting style with another one from the fighter class that you don't have."""

    print(feature)
    dnd_dict.character_dict["features"]['fighting_initiate'] = feature
    dnd_dict.character_dict["feats"]['fighting_initiate'] = 'Fighting Initiate'
    dnd_fighting_styles.fighting_initiate_fighting_styles()

def flames_of_phlegethos():
    feature = """
Flames of Phlegethos
Prerequisite: Tiefling

You learn to call on hellfire to serve your commands. You gain the following benefits:

    Increase your Intelligence or Charisma by 1, to a maximum of 20.
    When you roll fire damage for a spell you cast, you can reroll any roll of 1 on the fire damage dice, but you must use the new roll, even if it is another 1.
    Whenever you cast a spell that deals fire damage, you can cause flames to wreathe you until the end of your next turn. The flames don't harm you or your possessions, and they shed bright light out to 30 feet and dim light for an additional 30 feet. While the flames are present, any creature within 5 feet of you that hits you with a melee attack takes 1d4 fire damage."""
    print(feature)
    dnd_dict.character_dict["features"]['flames_of_phlegethos'] = feature
    dnd_dict.character_dict["feats"]['flames_of_phlegthos'] = 'Flames of Phlegthos'
    if dnd_dict.character_dict['Stats']['intelligence']['base'] < 20 or dnd_dict.character_dict['Stats']['charisma']['base'] < 20:
        while True:
            choice = input("""Which stat would you like to increase by 1 to a maximum of 20?
1) Intelligence
2) Charisma
Enter your selection: """)

            if choice == '1':
                if dnd_dict.character_dict['Stats']['intelligence']['base'] < 20:
                    dnd_dict.character_dict['Stats']['intelligence']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['intelligence']['base'])
                    dnd_dict.character_dict['Stats']['intelligence']['mod'] = mod
                    spell_attack = ((dnd_dict.character_dict["Stats"]["intelligence"]['mod']) + dnd_dict.character_dict['prof_bonus'])
                    dnd_dict.character_dict["spell_modifier"]['intelligence']['attack'] = spell_attack
                    spell_save = ((dnd_dict.character_dict["Stats"]["intelligence"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
                    dnd_dict.character_dict["spell_modifier"]['intelligence']['save'] = spell_save
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue


            elif choice == '2':
                if dnd_dict.character_dict['Stats']['charisma']['base'] < 20:
                    dnd_dict.character_dict['Stats']['charisma']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['charisma']['base'])
                    dnd_dict.character_dict['Stats']['charisma']['mod'] = mod
                    spell_attack = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'])
                    dnd_dict.character_dict["spell_modifier"]['charisma']['attack'] = spell_attack
                    spell_save = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
                    dnd_dict.character_dict["spell_modifier"]['charisma']['save'] = spell_save
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            else:
                print("Error: Invalid Input")
                continue

def gift_of_the_chromatic_dragon():
    feature = """
Gift of the Chromatic Dragon

You've manifested some of the power of chromatic dragons, granting you the following benefits:

    Chromatic Infusion. As a bonus action, you can touch a simple or martial weapon and infuse it with one of the following damage types: acid, cold, fire, lightning, or poison. For the next minute, the weapon deals an extra 1d4 damage of the chosen type when it hits. After you use this bonus action, you can't do so again until you finish a long rest.

    Reactive Resistance. When you take acid, cold, fire, lightning, or poison damage, you can use your reaction to give yourself resistance to that instance of damage. You can use this reaction a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest."""
    print(feature)
    dnd_dict.character_dict["features"]['gift_of_the_chromatic_dragon'] = feature
    dnd_dict.character_dict["feats"]['gift_of_the_chromatic_dragon'] = 'Gift of the Chromatic Dragon'

def gift_of_the_gem_dragon():
    feature = """
Gift of the Gem Dragon

You've manifested some of the power of gem dragons, granting you the following benefits:

    Ability Score Increase. Increase your Intelligence, Wisdom, or Charisma by 1, to a maximum of 20.

    Telekinetic Reprisal. When you take damage from a creature that is within 10 feet of you, you can use your reaction to emanate telekinetic energy. The creature that dealt damage to you must make a Strength saving throw (DC equals 8 + your proficiency bonus + the ability modifier of the score increased by this feat). On a failed save, the creature takes 2d8 force damage and is pushed up to 10 feet away from you. On a successful save, the creature takes half as much damage and isn't pushed. You can use this reaction a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest."""
    print(feature)
    dnd_dict.character_dict["features"]['gift_of_the_gem_dragon'] = feature
    dnd_dict.character_dict["feats"]['gift_of_the_gem_dragon'] = 'Gift of the Gem Dragon'

    if dnd_dict.character_dict['Stats']['intelligence']['base'] < 20 or dnd_dict.character_dict['Stats']['wisdom']['base'] < 20 or dnd_dict.character_dict['Stats']['charisma']['base'] < 20:
        while True:
            choice = input("""Which stat would you like to increase by 1 to a maximum of 20?
1) Intelligence
2) Wisdom
3) Charisma
Enter your selection: """)

            if choice == '1':
                if dnd_dict.character_dict['Stats']['intelligence']['base'] < 20:
                    dnd_dict.character_dict['Stats']['intelligence']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['intelligence']['base'])
                    dnd_dict.character_dict['Stats']['intelligence']['mod'] = mod
                    spell_attack = ((dnd_dict.character_dict["Stats"]["intelligence"]['mod']) + dnd_dict.character_dict['prof_bonus'])
                    dnd_dict.character_dict["spell_modifier"]['intelligence']['attack'] = spell_attack
                    spell_save = ((dnd_dict.character_dict["Stats"]["intelligence"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
                    dnd_dict.character_dict["spell_modifier"]['intelligence']['save'] = spell_save
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            elif choice == '2':
                if dnd_dict.character_dict['Stats']['wisdom']['base'] < 20:
                    dnd_dict.character_dict['Stats']['wisdom']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['wisdom']['base'])
                    dnd_dict.character_dict['Stats']['wisdom']['mod'] = mod
                    spell_attack = ((dnd_dict.character_dict["Stats"]["wisdom"]['mod']) + dnd_dict.character_dict['prof_bonus'])
                    dnd_dict.character_dict["spell_modifier"]['wisdom']['attack'] = spell_attack
                    spell_save = ((dnd_dict.character_dict["Stats"]["wisdom"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
                    dnd_dict.character_dict["spell_modifier"]['wisdom']['save'] = spell_save
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            elif choice == '3':
                if dnd_dict.character_dict['Stats']['charisma']['base'] < 20:
                    dnd_dict.character_dict['Stats']['charisma']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['charisma']['base'])
                    dnd_dict.character_dict['Stats']['charisma']['mod'] = mod
                    spell_attack = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'])
                    dnd_dict.character_dict["spell_modifier"]['charisma']['attack'] = spell_attack
                    spell_save = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
                    dnd_dict.character_dict["spell_modifier"]['charisma']['save'] = spell_save
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            else:
                print("Error: Invalid Input")
                continue

def gift_of_the_metallic_dragon():
    feature = """
Gift of the Metallic Dragon

You've manifested some of the power of metallic dragons, granting you the following benefits:

    Draconic Healing. You learn the cure wounds spell. You can cast this spell without expending a spell slot. Once you cast this spell in this way, you can't do so again until you finish a long rest. You can also cast this spell using spell slots you have. The spell's spellcasting ability is Intelligence, Wisdom, or Charisma when you cast it with this feat (choose when you gain the feat).

    Protective Wings. You can manifest protective wings that can shield you or others. When you or another creature you can see within 5 feet of you is hit by an attack roll, you can use your reaction to manifest spectral wings from your back for a moment. You grant a bonus to the target's AC equal to your proficiency bonus against that attack roll, potentially causing it to miss. You can use this reaction a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest."""
    print(feature)
    dnd_dict.character_dict["features"]['gift_of_the_metallic_dragon'] = feature
    dnd_dict.character_dict["feats"]['gift_of_the_metallic_dragon'] = 'Gift of the Metallic Dragon'
    dnd_dict.character_dict['spells']['first']['cure_wounds'] = 'Cure Wounds'
    dnd_dict.character_dict['special_spells']['racial_spells']['cure_wounds'] = 'Cure Wounds'
    while True:
        choice = input("""What would you like your spellcasting modifier to be?
1) Intelligence
2) Wisdom
3) Charisma
Enter your selection: """)
        if choice == '1':
            spell_attack = ((dnd_dict.character_dict["Stats"]["intelligence"]['mod']) + dnd_dict.character_dict['prof_bonus'])
            dnd_dict.character_dict["spell_modifier"]['intelligence']['attack'] = spell_attack
            spell_save = ((dnd_dict.character_dict["Stats"]["intelligence"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
            dnd_dict.character_dict["spell_modifier"]['intelligence']['save'] = spell_save
            break
        elif choice == '2':
            spell_attack = ((dnd_dict.character_dict["Stats"]["wisdom"]['mod']) + dnd_dict.character_dict['prof_bonus'])
            dnd_dict.character_dict["spell_modifier"]['wisdom']['attack'] = spell_attack
            spell_save = ((dnd_dict.character_dict["Stats"]["wisdom"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
            dnd_dict.character_dict["spell_modifier"]['wisdom']['save'] = spell_save
            break
        elif choice == '3':
            spell_attack = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'])
            dnd_dict.character_dict["spell_modifier"]['charisma']['attack'] = spell_attack
            spell_save = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
            dnd_dict.character_dict["spell_modifier"]['charisma']['save'] = spell_save
            break
        else:
            print("Error: Invalid Input")
            continue

def grappler():
    feature = """
Grappler
Prerequisite: Strength 13 or higher

You've developed the skills necessary to hold your own in close-quarters grappling. You gain the following benefits:

    You have advantage on attack rolls against a creature you are grappling.
    You can use your action to try to pin a creature grappled by you. To do so, make another grapple check. If you succeed, you and the creature are both restrained until the grapple ends."""
    print(feature)
    dnd_dict.character_dict["features"]['grappler'] = feature
    dnd_dict.character_dict["feats"]['grappler'] = 'Grappler'

def great_weapon_master():
    feature = """
Great Weapon Master

You've learned to put the weight of a weapon to your advantage, letting its momentum empower your strikes. You gain the following benefits:

    On your turn, when you score a critical hit with a melee weapon or reduce a creature to 0 hit points with one, you can make one melee weapon attack as a bonus action.
    Before you make a melee attack with a heavy weapon that you are proficient with, you can choose to take a -5 penalty to the attack roll. If the attack hits, you add +10 to the attack's damage."""
    print(feature)
    dnd_dict.character_dict["features"]['great_weapon_master'] = feature
    dnd_dict.character_dict["feats"]['great_weapon_master'] = 'Great Weapon Master'

def gunner():
    feature = """
Gunner

You have a quick hand and keen eye when employing firearms, granting you the following benefits:

    Increase your Dexterity score by 1, to a maximum of 20.
    You gain proficiency with firearms (see "Firearms" in the Dungeon Master's Guide).
    You ignore the loading property of firearms.
    Being within 5 feet of a hostile creature doesn't impose disadvantage on your ranged attack rolls."""
    print(feature)
    dnd_dict.character_dict["features"]['gunner'] = feature
    dnd_dict.character_dict["feats"]['gunner'] = 'Gunner'
    if dnd_dict.character_dict['Stats']['dexterity']['base'] < 20:
        dnd_dict.character_dict['Stats']['dexterity']['base'] += 1

def healer():
    feature = """
Healer

You are an able physician, allowing you to mend wounds quickly and get your allies back in the fight. You gain the following benefits:

    When you use a healer's kit to stabilize a dying creature, that creature also regains 1 hit point.
    As an action, you can spend one use of a healer's kit to tend to a creature and restore 1d6 + 4 hit points to it, plus additional hit points equal to the creature's maximum number of Hit Dice. The creature can't regain hit points from this feat again until it finishes a short or long rest."""
    print(feature)
    dnd_dict.character_dict["features"]['healer'] = feature
    dnd_dict.character_dict["feats"]['healer'] = 'Healer'

def heavily_armored():
    feature = """
Heavily Armored
Prerequisite: Proficiency with medium armor

You have trained to master the use of heavy armor, gaining the following benefits:

    Increase your Strength score by 1, to a maximum of 20.
    You gain proficiency with heavy armor."""
    print(feature)
    dnd_dict.character_dict["features"]['heavily_armored'] = feature
    dnd_dict.character_dict["feats"]['heavily_armored'] = 'Heavily Armored'
    dnd_dict.character_dict['Armor_Prof']['heavy_armor'] = 'Heavy Armor'
    if dnd_dict.character_dict['Stats']['strength']['base'] < 20:
        dnd_dict.character_dict['Stats']['strength']['base'] += 1

def heavy_armor_master():
    feature = """
Heavy Armor Master
Prerequisite: Proficiency with heavy armor

You can use your armor to deflect strikes that would kill others. You gain the following benefits:

    Increase your Strength score by 1, to a maximum of 20.
    While you are wearing heavy armor, bludgeoning, piercing, and slashing damage that you take from nonmagical attacks is reduced by 3."""
    print(feature)
    dnd_dict.character_dict["features"]['heavy_armor_master'] = feature
    dnd_dict.character_dict["feats"]['heavy_armor_master'] = 'Heavy Armor Master'
    if dnd_dict.character_dict['Stats']['strength']['base'] < 20:
        dnd_dict.character_dict['Stats']['strength']['base'] += 1

def infernal_constitution():
    feature = """
Infernal Constitution
Prerequisite: Tiefling

Fiendish blood runs strong in you, unlocking a resilience akin to that possessed by some fiends. You gain the following benefits:

    Increase your Constitution score by 1, to a maximum of 20.
    You have resistance to cold and poison damage.
    You have advantage on saving throws against being poisoned."""
    print(feature)
    dnd_dict.character_dict["features"]['infernal_constitution'] = feature
    dnd_dict.character_dict["feats"]['infernal_constitution'] = 'Infernal Constitution'
    if dnd_dict.character_dict['Stats']['constitution']['base'] < 20:
        dnd_dict.character_dict['Stats']['constitution']['base'] += 1

def inspiring_leader():
    feature = """
Inspiring Leader
Prerequisite: Charisma 13 or higher

You can spend 10 minutes inspiring your companions, shoring up their resolve to fight. When you do so, choose up to six friendly creatures (which can include yourself) within 30 feet of you who can see or hear you and who can understand you. Each creature can gain temporary hit points equal to your level + your Charisma modifier. A creature can't gain temporary hit points from this feat again until it has finished a short or long rest."""
    print(feature)
    dnd_dict.character_dict["features"]['inspiring_leader'] = feature
    dnd_dict.character_dict["feats"]['inspiring_leader'] = 'Inspiring Leader'

def keen_mind():
    feature = """
Keen Mind

You have a mind that can track time, direction, and detail with uncanny precision. You gain the following benefits:

    Increase your Intelligence score by 1, to a maximum of 20.
    You always know which way is north.
    You always know the number of hours left before the next sunrise or sunset.
    You can accurately recall anything you have seen or heard within the past month."""
    print(feature)
    dnd_dict.character_dict["features"]['keen_mind'] = feature
    dnd_dict.character_dict["feats"]['keen_mind'] = 'Keen Mind'
    if dnd_dict.character_dict['Stats']['intelligence']['base'] < 20:
        dnd_dict.character_dict['Stats']['intelligence']['base'] += 1

def lightly_armored():
    feature = """
Lightly Armored

You have trained to master the use of light armor, gaining the following benefits:

    Increase your Strength or Dexterity by 1, to a maximum of 20.
    You gain proficiency with light armor."""
    print(feature)
    dnd_dict.character_dict["features"]['lightly_armored'] = feature
    dnd_dict.character_dict["feats"]['lightly_armored'] = 'Lightly Armored'
    dnd_dict.character_dict['Armor_Prof']['light_armor'] = 'Light Armor'
    if dnd_dict.character_dict['Stats']['strength']['base'] < 20 or dnd_dict.character_dict['Stats']['dexterity']['base'] < 20:
        while True:
            choice = input("""Which stat would you like to increase by 1 to a maximum of 20?
1) Strength
2) Dexterity
Enter your selection: """)

            if choice == '1':
                if dnd_dict.character_dict['Stats']['strength']['base'] < 20:
                    dnd_dict.character_dict['Stats']['strength']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['strength']['base'])
                    dnd_dict.character_dict['Stats']['strength']['mod'] = mod
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            elif choice == '2':
                if dnd_dict.character_dict['Stats']['dexterity']['base'] < 20:
                    dnd_dict.character_dict['Stats']['dexterity']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['dexterity']['base'])
                    dnd_dict.character_dict['Stats']['dexterity']['mod'] = mod
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            else:
                print("Error: Invalid Input")
                continue

def linguist():
    feature = """
Linguist

You have studied languages and codes, gaining the following benefits:

    Increase your Intelligence score by 1, to a maximum of 20.
    You learn three languages of your choice.
    You can ably create written ciphers. Others can't decipher a code you create unless you teach them, they succeed on an Intelligence check (DC equal to your Intelligence score + your proficiency bonus), or they use magic to decipher it."""
    print(feature)
    dnd_dict.character_dict["features"]['linguist'] = feature
    dnd_dict.character_dict["feats"]['linguist'] = 'Linguist'
    if dnd_dict.character_dict['Stats']['intelligence']['base'] < 20:
        dnd_dict.character_dict['Stats']['intelligence']['base'] += 1
    x = 1
    for x in range (x, 4):
        if x < 4:
            print(f'{x}/3')
            dnd_language.language()
            x+=1
            continue
        elif x == 4:
            break

def lucky():
    feature = """
Lucky

You have inexplicable luck that seems to kick in at just the right moment.

You have 3 luck points. Whenever you make an attack roll, an ability check, or a saving throw, you can spend one luck point to roll an additional d20. You can choose to spend one of your luck points after you roll the die, but before the outcome is determined. You choose which of the d20s is used for the attack roll, ability check, or saving throw.

You can also spend one luck point when an attack roll is made against you. Roll a d20, and then choose whether the attack uses the attacker's roll or yours. If more than one creature spends a luck point to influence the outcome of a roll, the points cancel each other out; no additional dice are rolled.

You regain your expended luck points when you finish a long rest."""
    print(feature)
    dnd_dict.character_dict["features"]['lucky'] = feature
    dnd_dict.character_dict["feats"]['lucky'] = 'Lucky'

def mage_slayer():
    feature = """
Mage Slayer

You have practiced techniques useful in melee combat against spellcasters, gaining the following benefits:

    When a creature within 5 feet of you casts a spell, you can use your reaction to make a melee weapon attack against that creature.
    When you damage a creature that is concentrating on a spell, that creature has disadvantage on the saving throw it makes to maintain its concentration.
    You have advantage on saving throws against spells cast by creatures within 5 feet of you."""
    print(feature)
    dnd_dict.character_dict["features"]['mage_slayer'] = feature
    dnd_dict.character_dict["feats"]['mage_slayer'] = 'Mage Slayer'

def magic_initiate():
    feature = """
Magic Initiate

Choose a class: bard, cleric, druid, sorcerer, warlock, or wizard. You learn two cantrips of your choice from that class's spell list.

In addition, choose one 1st-level spell to learn from that same list. Using this feat, you can cast the spell once at its lowest level, and you must finish a long rest before you can cast it in this way again.

Your spellcasting ability for these spells depends on the class you chose: Charisma for bard, sorcerer, or warlock; Wisdom for cleric or druid; or Intelligence for wizard."""
    print(feature)
    dnd_dict.character_dict["features"]['magic_initiate'] = feature
    dnd_dict.character_dict["feats"]['magic_initiate'] = 'Magic Initiate'
    while True:
        choice = input("""Select the class you want to learn a spell from
1) Bard
2) Cleric
3) Druid
4) Sorcerer
5) Warlock
6) Wizard
Enter your selection: """)
        if choice == '1':
            x = 1
            while x < 4:
                if x < 3:
                    print(f'{x}/2')
                    dnd_skills.spell_add(dnd_magic.bard_cantrip,dnd_dict.character_dict['spells']['cantrips'],dnd_dict.character_dict['special_spells']['cantrips'])
                    x+=1
                elif x == 3:
                    dnd_skills.spell_add(dnd_magic.bard_first,dnd_dict.character_dict['spells']['first'],dnd_dict.character_dict['special_spells']['first'])
                    spell_attack = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'])
                    dnd_dict.character_dict["spell_modifier"]['charisma']['attack'] = spell_attack
                    spell_save = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
                    dnd_dict.character_dict["spell_modifier"]['charisma']['save'] = spell_save
                    x+=1
                    break

        elif choice == '2':
            if dnd_dict.character_dict['player_class']['cleric']['class_level'] > 0:
                print("Error: You Already Know All Of These Spells")
                continue
            else:
                x = 1
                while x < 4:
                    if x < 3:
                        print(f'{x}/2')
                        dnd_skills.spell_add(dnd_magic.cleric_cantrip,dnd_dict.character_dict['spells']['cantrips'],dnd_dict.character_dict['special_spells']['cantrips'])
                        x+=1
                        continue
                    elif x == 3:
                        dnd_skills.spell_add(dnd_magic.cleric_first_classless,dnd_dict.character_dict['spells']['first'],dnd_dict.character_dict['special_spells']['first'])
                        spell_attack = ((dnd_dict.character_dict["Stats"]["wisdom"]['mod']) + dnd_dict.character_dict['prof_bonus'])
                        dnd_dict.character_dict["spell_modifier"]['wisdom']['attack'] = spell_attack
                        spell_save = ((dnd_dict.character_dict["Stats"]["wisdom"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
                        dnd_dict.character_dict["spell_modifier"]['wisdom']['save'] = spell_save
                        x+=1
                        break

        elif choice == '3':
            if dnd_dict.character_dict['player_class']['druid']['class_level'] > 0:
                print("Error: You Already Know All Of These Spells")
                continue
            else:
                x = 1
                while x < 4:
                    if x < 3:
                        print(f'{x}/2')
                        dnd_skills.spell_add(dnd_magic.druid_cantrip,dnd_dict.character_dict['spells']['cantrips'],dnd_dict.character_dict['special_spells']['cantrips'])
                        x+=1
                        continue
                    elif x == 3:
                        dnd_skills.spell_add(dnd_magic.druid_first_classless,dnd_dict.character_dict['spells']['first'],dnd_dict.character_dict['special_spells']['first'])
                        spell_attack = ((dnd_dict.character_dict["Stats"]["wisdom"]['mod']) + dnd_dict.character_dict['prof_bonus'])
                        dnd_dict.character_dict["spell_modifier"]['wisdom']['attack'] = spell_attack
                        spell_save = ((dnd_dict.character_dict["Stats"]["wisdom"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
                        dnd_dict.character_dict["spell_modifier"]['wisdom']['save'] = spell_save
                        x+=1
                        break
                
        elif choice == '4':
            x = 1
            while x < 4:
                if x < 3:
                    print(f'{x}/2')
                    dnd_skills.spell_add(dnd_magic.sorcerer_cantrip,dnd_dict.character_dict['spells']['cantrips'],dnd_dict.character_dict['special_spells']['cantrips'])
                    x+=1
                    continue
                elif x == 3:
                    dnd_skills.spell_add(dnd_magic.sorcerer_first,dnd_dict.character_dict['spells']['first'],dnd_dict.character_dict['special_spells']['first'])
                    spell_attack = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'])
                    dnd_dict.character_dict["spell_modifier"]['charisma']['attack'] = spell_attack
                    spell_save = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
                    dnd_dict.character_dict["spell_modifier"]['charisma']['save'] = spell_save
                    x+=1
                    break

        elif choice == '5':
            x = 1
            while x < 4:
                if x < 3:
                    print(f'{x}/2')
                    dnd_skills.spell_add(dnd_magic.warlock_cantrip,dnd_dict.character_dict['spells']['cantrips'],dnd_dict.character_dict['special_spells']['cantrips'])
                    x+=1
                    continue
                elif x == 3:
                    dnd_skills.spell_add(dnd_magic.warlock_first,dnd_dict.character_dict['spells']['first'],dnd_dict.character_dict['special_spells']['first'])
                    spell_attack = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'])
                    dnd_dict.character_dict["spell_modifier"]['charisma']['attack'] = spell_attack
                    spell_save = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
                    dnd_dict.character_dict["spell_modifier"]['charisma']['save'] = spell_save
                    x+=1
                    break

        elif choice == '6':
            x = 1
            while x < 4:
                if x < 3:
                    print(f'{x}/2')
                    dnd_skills.spell_add(dnd_magic.wizard_cantrip,dnd_dict.character_dict['spells']['cantrips'],dnd_dict.character_dict['special_spells']['cantrips'])
                    x+=1
                    continue
                elif x == 3:
                    dnd_skills.spell_add(dnd_magic.wizard_first,dnd_dict.character_dict['spells']['first'],dnd_dict.character_dict['special_spells']['first'])
                    spell_attack = ((dnd_dict.character_dict["Stats"]["intelligence"]['mod']) + dnd_dict.character_dict['prof_bonus'])
                    dnd_dict.character_dict["spell_modifier"]['intelligence']['attack'] = spell_attack
                    spell_save = ((dnd_dict.character_dict["Stats"]["intelligence"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
                    dnd_dict.character_dict["spell_modifier"]['intelligence']['save'] = spell_save
                    x+=1
                    break

        else:
            print("Error: invalid input")
            continue

        break
def martial_adept():
    feature = """
Martial Adept

You have martial training that allows you to perform special combat maneuvers. You gain the following benefits:

    You learn two maneuvers of your choice from among those available to the Battle Master archetype in the fighter class. If a maneuver you use requires your target to make a saving throw to resist the maneuver's effects, the saving throw DC equals 8 + your proficiency bonus + your Strength or Dexterity modifier (your choice).
    You gain one superiority die, which is a d6 (this die is added to any superiority dice you have from another source). This die is used to fuel your maneuvers. A superiority die is expended when you use it. You regain your expended superiority dice when you finish a short or long rest."""
    print(feature)
    dnd_dict.character_dict["features"]['martial_adept'] = feature
    dnd_dict.character_dict["feats"]['martial_adept'] = 'Martial Adept'
    x = 1
    for x in range (x, 3):
        if x < 3:
            print(f'{x}/2')
            dnd_maneuvers.maneuvers()
            x+=1
            continue
        elif x == 3:
            dnd_dict.character_dict['maneuvers']['d6'] += 1
            break

def medium_armor_master():
    feature = """
Medium Armor Master
Prerequisite: Proficiency with medium armor

You have practiced moving in medium armor to gain the following benefits:

    Wearing medium armor doesn't impose disadvantage on your Dexterity (Stealth) checks.
    When you wear medium armor, you can add 3, rather than 2, to your AC if you have a Dexterity of 16 or higher."""
    print(feature)
    dnd_dict.character_dict["features"]['medium_armor_master'] = feature
    dnd_dict.character_dict["feats"]['medium_armor_master'] = 'Medium Armor Master'

def metamagic_adept():
    feature = """
Metamagic Adept
Prerequisite: Spellcasting or Pact Magic feature

You've learned how to exert your will on your spells to alter how they function:

    You learn two Metamagic options of your choice from the sorcerer class. You can use only one Metamagic option on a spell when you cast it, unless the option says otherwise. Whenever you reach a level that grants the Ability Score Improvement feature, you can replace one of these Metamagic options with another one from the sorcerer class.
    You gain 2 sorcery points to spend on Metamagic (these points are added to any sorcery points you have from another source but can be used only on Metamagic). You regain all spent sorcery points when you finish a long rest."""
    print(feature)
    dnd_dict.character_dict["features"]['metamagic_adept'] = feature
    dnd_dict.character_dict["feats"]['metamagic_adept'] = 'Metamagic Adept'
    dnd_metamagic.metamagic_adept_choice()

def mobile():
    feature = """
Mobile

You are exceptionally speedy and agile. You gain the following benefits:

    Your speed increases by 10 feet.
    When you use the Dash action, difficult terrain doesn't cost you extra movement on that turn.
    When you make a melee attack against a creature, you don't provoke opportunity attacks from that creature for the rest of the turn, whether you hit or not."""
    print(feature)
    dnd_dict.character_dict["features"]['mobile'] = feature
    dnd_dict.character_dict["feats"]['mobile'] = 'Mobile'
    dnd_dict.character_dict['speed'] += 10
    if dnd_dict.character_dict['unarmored_movement_barbarian'] > 0:
        dnd_dict.character_dict['unarmored_movement_barbarian'] +=10
    if dnd_dict.character_dict['unarmored_movement_monk'] > 0:
        dnd_dict.character_dict['unarmored_movement_monk'] +=10
    if 'roving' in dnd_dict.character_dict['features']:
        dnd_dict.character_dict['swim_speed'] == dnd_dict.character_dict['speed']
        dnd_dict.character_dict['climb_speed'] == dnd_dict.character_dict['speed']

def moderately_armored():
    feature = """
Moderately Armored
Prerequisite: Proficiency with light armor

You have trained to master the use of medium armor and shields, gaining the following benefits:

    Increase your Strength or Dexterity by 1, to a maximum of 20.
    You gain proficiency with medium armor and shields."""
    print(feature)
    dnd_dict.character_dict["features"]['moderately_armored'] = feature
    dnd_dict.character_dict["feats"]['moderately_armored'] = 'Moderately Armored'
    dnd_dict.character_dict['Armor_Prof']['shields'] = 'Shields'
    dnd_dict.character_dict['Armor_Prof']['medium_armor'] = 'Medium Armor'
    if dnd_dict.character_dict['Stats']['strength']['base'] < 20 or dnd_dict.character_dict['Stats']['dexterity']['base'] < 20:
        while True:
            choice = input("""Which stat would you like to increase by 1 to a maximum of 20?
1) Strength
2) Dexterity
Enter your selection: """)

            if choice == '1':
                if dnd_dict.character_dict['Stats']['strength']['base'] < 20:
                    dnd_dict.character_dict['Stats']['strength']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['strength']['base'])
                    dnd_dict.character_dict['Stats']['strength']['mod'] = mod
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            elif choice == '2':
                if dnd_dict.character_dict['Stats']['dexterity']['base'] < 20:
                    dnd_dict.character_dict['Stats']['dexterity']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['dexterity']['base'])
                    dnd_dict.character_dict['Stats']['dexterity']['mod'] = mod
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            else:
                print("Error: Invalid Input")
                continue

def mounted_combatant():
    feature = """
Mounted Combatant

You are a dangerous foe to face while mounted. While you are mounted and aren't incapacitated, you gain the following benefits:

    You have advantage on melee attack rolls against any unmounted creature that is smaller than your mount.
    You can force an attack targeted at your mount to target you instead.
    If your mount is subjected to an effect that allows it to make a Dexterity saving throw to take only half damage, it instead takes no damage if it succeeds on the saving throw, and only half damage if it fails."""
    print(feature)
    dnd_dict.character_dict["features"]['mounted_combatant'] = feature
    dnd_dict.character_dict["feats"]['mounted_combatant'] = 'Mounted Combatant'

def observant():
    feature = """
Observant

Quick to notice details of your environment, you gain the following benefits:

    Increase your Intelligence or Wisdom by 1, to a maximum of 20.
    If you can see a creature's mouth while it is speaking a language you understand, you can interpret what it's saying by reading its lips.
    You have a +5 bonus to your passive Wisdom (Perception) and passive Intelligence (Investigation) scores."""
    print(feature)
    dnd_dict.character_dict["features"]['observant'] = feature
    dnd_dict.character_dict["feats"]['observant'] = 'Observant'
    if dnd_dict.character_dict['Stats']['intelligence']['base'] < 20 or dnd_dict.character_dict['Stats']['wisdom']['base'] < 20:
        while True:
            choice = input("""Which stat would you like to increase by 1 to a maximum of 20?
1) Intelligence
2) Wisdom
Enter your selection: """)

            if choice == '1':
                if dnd_dict.character_dict['Stats']['intelligence']['base'] < 20:
                    dnd_dict.character_dict['Stats']['intelligence']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['intelligence']['base'])
                    dnd_dict.character_dict['Stats']['intelligence']['mod'] = mod
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            elif choice == '2':
                if dnd_dict.character_dict['Stats']['wisdom']['base'] < 20:
                    dnd_dict.character_dict['Stats']['wisdom']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['wisdom']['base'])
                    dnd_dict.character_dict['Stats']['wisdom']['mod'] = mod
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue


            else:
                print("Error: Invalid Input")
                continue

    dnd_dict.character_dict['passive_perception'] += 5

def orcish_fury():
    feature = """
Orcish Fury
Prerequisite: Half-Orc

Your fury burns tirelessly. You gain the following benefits:

    Increase your Strength or Constitution by 1, to a maximum of 20.
    When you hit with an attack using a simple or martial weapon, you can roll one of the weapon's damage dice an additional time and add it as extra damage of the weapon's damage type. Once you use this ability, you can't use it again until you finish a short or long rest.
    Immediately after you use your Relentless Endurance trait, you can use your reaction to make one weapon attack."""
    print(feature)
    dnd_dict.character_dict["features"]['orcish_fury'] = feature
    dnd_dict.character_dict["feats"]['orcish_fury'] = 'Orcish Fury'
    if dnd_dict.character_dict['Stats']['strength']['base'] < 20 or dnd_dict.character_dict['Stats']['constitution']['base'] < 20:
        while True:
            choice = input("""Which stat would you like to increase by 1 to a maximum of 20?
1) Strength
2) Constitution
Enter your selection: """)

            if choice == '1':
                if dnd_dict.character_dict['Stats']['strength']['base'] < 20:
                    dnd_dict.character_dict['Stats']['strength']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['strength']['base'])
                    dnd_dict.character_dict['Stats']['strength']['mod'] = mod
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            elif choice == '2':
                if dnd_dict.character_dict['Stats']['constitution']['base'] < 20:
                    dnd_dict.character_dict['Stats']['constitution']['base'] += 1
# If the modifier is positive and increases, increase your hp by your total level
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['constitution']['base'])
                    if mod > dnd_dict.character_dict['Stats']['constitution']['mod'] and mod > 0:
                        new_hp = dnd_dict.character_dict['hp'] + dnd_dict.character_dict['total_level']
                        dnd_dict.character_dict['hp'] = new_hp
                    dnd_dict.character_dict['Stats']['constitution']['mod'] = mod
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue


            else:
                print("Error: Invalid Input")
                continue

def piercer():
    feature = """
Piercer

You have achieved a penetrating precision in combat, granting you the following benefits:

    Increase your Strength or Dexterity by 1, to a maximum of 20.
    Once per turn, when you hit a creature with an attack that deals piercing damage, you can reroll one of the attack's damage dice, and you must use the new roll.
    When you score a critical hit that deals piercing damage to a creature, you can roll one additional damage die when determining the extra piercing damage the target takes."""
    print(feature)
    dnd_dict.character_dict["features"]['piercer'] = feature
    dnd_dict.character_dict["feats"]['piercer'] = 'Piercer'
    if dnd_dict.character_dict['Stats']['strength']['base'] < 20 or dnd_dict.character_dict['Stats']['dexterity']['base'] < 20:
        while True:
            choice = input("""Which stat would you like to increase by 1 to a maximum of 20?
1) Strength
2) Dexterity
Enter your selection: """)

            if choice == '1':
                if dnd_dict.character_dict['Stats']['strength']['base'] < 20:
                    dnd_dict.character_dict['Stats']['strength']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['strength']['base'])
                    dnd_dict.character_dict['Stats']['strength']['mod'] = mod
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            elif choice == '2':
                if dnd_dict.character_dict['Stats']['dexterity']['base'] < 20:
                    dnd_dict.character_dict['Stats']['dexterity']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['dexterity']['base'])
                    dnd_dict.character_dict['Stats']['dexterity']['mod'] = mod
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            else:
                print("Error: Invalid Input")
                continue

def poisoner():
    feature = """
Poisoner

You can prepare and deliver deadly poisons, granting you the following benefits:

    When you make a damage roll that deals poison damage, it ignores resistance to poison damage.
    You can apply poison to a weapon or piece of ammunition as a bonus action, instead of an action.
    You gain proficiency with the poisoner's kit if you don't already have it. With one hour of work using a poisoner's kit and expending 50 gp worth of materials, you can create a number of doses of potent poison equal to your proficiency bonus. Once applied to a weapon or piece of ammunition, the poison retains its potency for 1 minute or until you hit with the weapon or ammunition. When a creature takes damage from the coated weapon or ammunition, that creature must succeed on a DC 14 Constitution saving throw or take 2d8 poison damage and become poisoned until the end of your next turn."""
    print(feature)
    dnd_dict.character_dict["features"]['poisoner'] = feature
    dnd_dict.character_dict["feats"]['poisoner'] = 'Poisoner'
    dnd_dict.character_dict['Kits']['poisoner_kit'] = 'Poisoner\'s Kit'

def polearm_master():
    feature = """
Polearm Master

You can keep your enemies at bay with reach weapons. You gain the following benefits:

    When you take the Attack action and attack with only a glaive, halberd, quarterstaff, or spear, you can use a bonus action to make a melee attack with the opposite end of the weapon; this attack uses the same ability modifier as the primary attack. The weapon's damage die for this attack is a d4, and the attack deals bludgeoning damage.
    While you are wielding a glaive, halberd, pike, quarterstaff, or spear, other creatures provoke an opportunity attack from you when they enter the reach you have with that weapon."""
    print(feature)
    dnd_dict.character_dict["features"]['polearm_master'] = feature
    dnd_dict.character_dict["feats"]['polearm_master'] = 'Polearm Master'

def prodigy():
    feature = """
Prodigy
Prerequisite: Half-Elf, half-orc, or human

You have a knack for learning new things. You gain the following benefits:

    You gain one skill proficiency of your choice, one tool proficiency of your choice, and fluency in one language of your choice.
    Choose one skill in which you have proficiency. You gain expertise with that skill, which means your proficiency bonus is doubled for any ability check you make with it. The skill you choose must be one that isn't already benefiting from a feature, such as Expertise, that doubles your proficiency bonus."""
    print(feature)
    dnd_dict.character_dict["features"]['prodigy'] = feature
    dnd_dict.character_dict["feats"]['prodigy'] = 'Prodigy'
    dnd_skills.skill_choice()
    dnd_language.language()
    dnd_tools.artisan_tools()

def resilient():
    feature = """
Resilient

Choose one ability score. You gain the following benefits:

    Increase the chosen ability score by 1, to a maximum of 20.
    You gain proficiency in saving throws using the chosen ability."""

    print(feature)
    dnd_dict.character_dict["features"]['resilient'] = feature
    dnd_dict.character_dict["feats"]['resilient'] = 'Resilient'

    if dnd_dict.character_dict['Stats']['strength']['base'] < 20 or dnd_dict.character_dict['Stats']['dexterity']['base'] < 20 or dnd_dict.character_dict['Stats']['constitution']['base'] < 20 or dnd_dict.character_dict['Stats']['intelligence']['base'] < 20 or dnd_dict.character_dict['Stats']['wisdom']['base'] < 20 or dnd_dict.character_dict['Stats']['charisma']['base'] < 20:
        while True:
            choice = input("""Which stat would you like to increase by 1 to a maximum of 20?
1) Strength
2) Dexterity
3) Constitution
4) Intelligence
5) Wisdom
6) Charisma
Enter your selection: """)

            if choice == '1':
                if dnd_dict.character_dict['Stats']['strength']['base'] < 20:
                    dnd_dict.character_dict['Stats']['strength']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['strength']['base'])
                    dnd_dict.character_dict['Stats']['strength']['mod'] = mod
                    dnd_dict.character_dict['saving_throws']['strength'] = 'Strength'
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            elif choice == '2':
                if dnd_dict.character_dict['Stats']['dexterity']['base'] < 20:
                    dnd_dict.character_dict['Stats']['dexterity']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['dexterity']['base'])
                    dnd_dict.character_dict['Stats']['dexterity']['mod'] = mod
                    dnd_dict.character_dict['saving_throws']['dexterity'] = 'Dexterity'
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            elif choice == '3':
                if dnd_dict.character_dict['Stats']['constitution']['base'] < 20:
                    dnd_dict.character_dict['Stats']['constitution']['base'] += 1
# If the modifier is positive and increases, increase your hp by your total level
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['constitution']['base'])
                    if mod > dnd_dict.character_dict['Stats']['constitution']['mod'] and mod > 0:
                        new_hp = dnd_dict.character_dict['hp'] + dnd_dict.character_dict['total_level']
                        dnd_dict.character_dict['hp'] = new_hp
                    dnd_dict.character_dict['Stats']['constitution']['mod'] = mod
                    dnd_dict.character_dict['saving_throws']['constitution'] = 'Constitution'
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            elif choice == '4':
                if dnd_dict.character_dict['Stats']['intelligence']['base'] < 20:
                    dnd_dict.character_dict['Stats']['intelligence']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['intelligence']['base'])
                    dnd_dict.character_dict['Stats']['intelligence']['mod'] = mod
                    dnd_dict.character_dict['saving_throws']['intelligence'] = 'Intelligence'
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            elif choice == '5':
                if dnd_dict.character_dict['Stats']['wisdom']['base'] < 20:
                    dnd_dict.character_dict['Stats']['wisdom']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['wisdom']['base'])
                    dnd_dict.character_dict['Stats']['wisdom']['mod'] = mod
                    dnd_dict.character_dict['saving_throws']['wisdom'] = 'Wisdom'
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            elif choice == '6':
                if dnd_dict.character_dict['Stats']['charisma']['base'] < 20:
                    dnd_dict.character_dict['Stats']['charisma']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['charisma']['base'])
                    dnd_dict.character_dict['Stats']['charisma']['mod'] = mod
                    dnd_dict.character_dict['saving_throws']['charisma'] = 'Charisma'
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue


            else:
                print("Error: Invalid Input")
                continue

def revenant_blade():
    feature = """
Revenant Blade
Prerequisite: Elf

You are descended from a master of the double-bladed scimitar, and some of that mastery has passed on to you. You gain the following benefits:

    Increase your Strength or Dexterity by 1, to a maximum of 20.
    While you are holding a double-bladed scimitar with two hands, you gain a +1 bonus to Armor Class.
    A double-bladed scimitar has the finesse property when you wield it."""

    print(feature)
    dnd_dict.character_dict["features"]['revenant_blade'] = feature
    dnd_dict.character_dict["feats"]['revenant_blade'] = 'Revenant Blade'
    if dnd_dict.character_dict['Stats']['strength']['base'] < 20 or dnd_dict.character_dict['Stats']['dexterity']['base'] < 20:
        while True:
            choice = input("""Which stat would you like to increase by 1 to a maximum of 20?
1) Strength
2) Dexterity
Enter your selection: """)

            if choice == '1':
                if dnd_dict.character_dict['Stats']['strength']['base'] < 20:
                    dnd_dict.character_dict['Stats']['strength']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['strength']['base'])
                    dnd_dict.character_dict['Stats']['strength']['mod'] = mod
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            elif choice == '2':
                if dnd_dict.character_dict['Stats']['dexterity']['base'] < 20:
                    dnd_dict.character_dict['Stats']['dexterity']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['dexterity']['base'])
                    dnd_dict.character_dict['Stats']['dexterity']['mod'] = mod
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            else:
                print("Error: Invalid Input")
                continue

def ritual_caster():
    feature = """
Ritual Caster
Prerequisite: Intelligence or Wisdom 13 or higher

You have learned a number of spells that you can cast as rituals. These spells are written in a ritual book, which you must have in hand while casting one of them.

When you choose this feat, you acquire a ritual book holding two 1st-level spells of your choice. Choose one of the following classes: bard, cleric, druid, sorcerer, warlock, or wizard. You must choose your spells from that class's spell list, and the spells you choose must have the ritual tag. The class you choose also determines your spellcasting ability for these spells: Charisma for bard, sorcerer, or warlock; Wisdom for cleric or druid; or Intelligence for wizard.

If you come across a spell in written form, such as a magical spell scroll or a wizard's spellbook, you might be able to add it to your ritual book. The spell must be on the spell list for the class you chose, the spell's level can be no higher than half your level (rounded up), and it must have the ritual tag. The process of copying the spell into your ritual book takes 2 hours per level of the spell, and costs 50 gp per level. The cost represents material components you expend as you experiment with the spell to master it, as well as the fine inks you need to record it."""

    print(feature)
    dnd_dict.character_dict["features"]['ritual_caster'] = feature
    dnd_dict.character_dict["feats"]['ritual_caster'] = 'Ritual Caster'

    while True:
        choice = input("""Select the class you want to learn a spell from
1) Bard
2) Cleric
3) Druid
4) Sorcerer
5) Warlock
6) Wizard
Enter your selection: """)
        if choice == '1':
            if 'detect_magic' in dnd_dict.character_dict['spells']['first'] and 'comprehend_languages' in dnd_dict.character_dict['spells']['first'] and 'identify' in dnd_dict.character_dict['spells']['first'] and 'illusory_script' in dnd_dict.character_dict['spells']['first'] and 'speak_with_animals' in dnd_dict.character_dict['spells']['first'] and 'unseen_servant' in dnd_dict.character_dict['spells']['first']:
                print("Error: You already know all of these spells")
                continue
            else:
                x = 1
                for x in range (x,3):
                    if x < 3:
                        print(f'{x}/2')
                        dnd_skills.spell_add(dnd_magic.bard_ritual_first,dnd_dict.character_dict['spells']['first'],dnd_dict.character_dict['special_spells']['first'])
                        spell_attack = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'])
                        dnd_dict.character_dict["spell_modifier"]['charisma']['attack'] = spell_attack
                        spell_save = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
                        dnd_dict.character_dict["spell_modifier"]['charisma']['save'] = spell_save
                        x+=1
                        continue

                    elif x == 3:
                        break

        elif choice == '2':
            if 'detect_magic' in dnd_dict.character_dict['spells']['first'] and 'ceremony' in dnd_dict.character_dict['spells']['first'] and 'detect_poison_and_disease' in dnd_dict.character_dict['spells']['first'] and 'purify_food_and_drink' in dnd_dict.character_dict['spells']['first']:
                print("Error: You already know all of these spells")
                continue
            else:
                x = 1
                for x in range (x, 3):
                    if x < 3:
                        print(f'{x}/2')
                        dnd_skills.spell_add(dnd_magic.cleric_ritual_first,dnd_dict.character_dict['spells']['first'],dnd_dict.character_dict['special_spells']['first'])
                        spell_attack = ((dnd_dict.character_dict["Stats"]["wisdom"]['mod']) + dnd_dict.character_dict['prof_bonus'])
                        dnd_dict.character_dict["spell_modifier"]['wisdom']['attack'] = spell_attack
                        spell_save = ((dnd_dict.character_dict["Stats"]["wisdom"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
                        dnd_dict.character_dict["spell_modifier"]['wisdom']['save'] = spell_save
                        x+=1
                        continue
                    elif x == 3:
                        break

        elif choice == '3':
            if 'detect_magic' in dnd_dict.character_dict['spells']['first'] and 'speak_with_animals' in dnd_dict.character_dict['spells']['first'] and 'detect_poison_and_disease' in dnd_dict.character_dict['spells']['first'] and 'purify_food_and_drink' in dnd_dict.character_dict['spells']['first']:
                print("Error: You already know all of these spells")
                continue
            else:
                x = 1
                for x in range (x, 3):
                    if x < 3:
                        print(f'{x}/2')
                        dnd_skills.spell_add(dnd_magic.druid_ritual_first,dnd_dict.character_dict['spells']['first'],dnd_dict.character_dict['special_spells']['first'])
                        spell_attack = ((dnd_dict.character_dict["Stats"]["wisdom"]['mod']) + dnd_dict.character_dict['prof_bonus'])
                        dnd_dict.character_dict["spell_modifier"]['wisdom']['attack'] = spell_attack
                        spell_save = ((dnd_dict.character_dict["Stats"]["wisdom"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
                        dnd_dict.character_dict["spell_modifier"]['wisdom']['save'] = spell_save
                        x+=1
                        continue
                    elif x == 3:
                        break
                
        elif choice == '4':
            if 'detect_magic' in dnd_dict.character_dict['spells']['first'] and 'comprehend_languages' in dnd_dict.character_dict['spells']['first']:
                print("Error: You already know all of these spells")
                continue
            else:
                x = 1
                for x in range (x, 3):
                    if x < 3:
                        print(f'{x}/2')
                        dnd_skills.spell_add(dnd_magic.sorcerer_ritual_first,dnd_dict.character_dict['spells']['first'],dnd_dict.character_dict['special_spells']['first'])
                        spell_attack = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'])
                        dnd_dict.character_dict["spell_modifier"]['charisma']['attack'] = spell_attack
                        spell_save = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
                        dnd_dict.character_dict["spell_modifier"]['charisma']['save'] = spell_save
                        x+=1
                        continue
                    elif x == 3:
                        break

        elif choice == '5':
            if 'alarm' in dnd_dict.character_dict['spells']['first'] and 'comprehend_languages' in dnd_dict.character_dict['spells']['first'] and 'detect_poison_and_disease' in dnd_dict.character_dict['spells']['first'] and 'find_familiar' in dnd_dict.character_dict['spells']['first'] and 'floating_disk' in dnd_dict.character_dict['spells']['first']  and 'identify' in dnd_dict.character_dict['spells']['first']  and 'illusory_script' in dnd_dict.character_dict['spells']['first']  and 'purify_food_and_drink' in dnd_dict.character_dict['spells']['first']  and 'speak_with_animals' in dnd_dict.character_dict['spells']['first'] and 'unseen_servant' in dnd_dict.character_dict['spells']['first']:
                print("Error: You already know all of these spells")
                continue
            else:
                x = 1
                for x in range (x, 3):
                    if x < 3:
                        print(f'{x}/2')
                        dnd_skills.spell_add(dnd_magic.warlock_ritual_first,dnd_dict.character_dict['spells']['first'],dnd_dict.character_dict['special_spells']['first'])
                        spell_attack = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'])
                        dnd_dict.character_dict["spell_modifier"]['charisma']['attack'] = spell_attack
                        spell_save = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
                        dnd_dict.character_dict["spell_modifier"]['charisma']['save'] = spell_save
                        x+=1
                        continue
                    elif x == 3:
                        break

        elif choice == '6':
            if 'alarm' in dnd_dict.character_dict['spells']['first'] and 'comprehend_languages' in dnd_dict.character_dict['spells']['first'] and 'detect_magic' in dnd_dict.character_dict['spells']['first'] and 'find_familiar' in dnd_dict.character_dict['spells']['first'] and 'tenser\'s_floating_disk' in dnd_dict.character_dict['spells']['first']  and 'identify' in dnd_dict.character_dict['spells']['first']  and 'illusory_script' in dnd_dict.character_dict['spells']['first']  and 'unseen_servant' in dnd_dict.character_dict['spells']['first']:
                print("Error: You already know all of these spells")
                continue
            else:
                x = 1
                for x in range (x, 3):
                    if x < 3:
                        print(f'{x}/2')
                        dnd_skills.spell_add(dnd_magic.wizard_ritual_first,dnd_dict.character_dict['spells']['first'],dnd_dict.character_dict['special_spells']['first'])
                        dnd_skills.spell_add(dnd_magic.wizard_first,dnd_dict.character_dict['spells']['first'],dnd_dict.character_dict['special_spells']['first'])
                        spell_attack = ((dnd_dict.character_dict["Stats"]["intelligence"]['mod']) + dnd_dict.character_dict['prof_bonus'])
                        dnd_dict.character_dict["spell_modifier"]['intelligence']['attack'] = spell_attack
                        spell_save = ((dnd_dict.character_dict["Stats"]["intelligence"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
                        dnd_dict.character_dict["spell_modifier"]['intelligence']['save'] = spell_save
                        x+=1
                        continue
                    elif x == 3:
                        break

        else:
            print("Error: invalid input")
            continue

        break

def savage_attacker():
    feature = """
Savage Attacker

Once per turn when you roll damage for a melee weapon attack, you can reroll the weapon's damage dice and use either total."""
    print(feature)
    dnd_dict.character_dict["features"]['savage_attacker'] = feature
    dnd_dict.character_dict["feats"]['savage_attacker'] = 'Savage Attacker'

def second_chance():
    feature = """
Second Chance
Prerequisite: Halfling

Fortune favors you when someone tries to strike you. You gain the following benefits:

    Increase your Dexterity, Constitution, or Charisma by 1, to a maximum of 20.
    When a creature you can see hits you with an attack roll, you can use your reaction to force that creature to reroll. Once you use this ability, you can't use it again until you roll initiative at the start of combat or until you finish a short or long rest."""
    print(feature)
    dnd_dict.character_dict["features"]['second_chance'] = feature
    dnd_dict.character_dict["feats"]['second_chance'] = 'Second Chance'

    if dnd_dict.character_dict['Stats']['dexterity']['base'] < 20 or dnd_dict.character_dict['Stats']['constitution']['base'] < 20 or dnd_dict.character_dict['Stats']['charisma']['base'] < 20:
        while True:
            choice = input("""Which stat would you like to increase by 1 to a maximum of 20?
1) Dexterity
2) Constitution
3) Charisma
Enter your selection: """)

            if choice == '1':
                if dnd_dict.character_dict['Stats']['dexterity']['base'] < 20:
                    dnd_dict.character_dict['Stats']['dexterity']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['dexterity']['base'])
                    dnd_dict.character_dict['Stats']['dexterity']['mod'] = mod
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            elif choice == '2':
                if dnd_dict.character_dict['Stats']['constitution']['base'] < 20:
                    dnd_dict.character_dict['Stats']['constitution']['base'] += 1
# If the modifier is positive and increases, increase your hp by your total level
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['constitution']['base'])
                    if mod > dnd_dict.character_dict['Stats']['constitution']['mod'] and mod > 0:
                        new_hp = dnd_dict.character_dict['hp'] + dnd_dict.character_dict['total_level']
                        dnd_dict.character_dict['hp'] = new_hp
                    dnd_dict.character_dict['Stats']['constitution']['mod'] = mod
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            elif choice == '3':
                if dnd_dict.character_dict['Stats']['charisma']['base'] < 20:
                    dnd_dict.character_dict['Stats']['charisma']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['charisma']['base'])
                    dnd_dict.character_dict['Stats']['charisma']['mod'] = mod
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            else:
                print("Error: Invalid Input")
                continue

def sentinel():
    feature = """
Sentinel

You have mastered techniques to take advantage of every drop in any enemy's guard, gaining the following benefits:

    When you hit a creature with an opportunity attack, the creature's speed becomes 0 for the rest of the turn.
    Creatures provoke opportunity attacks from you even if they take the Disengage action before leaving your reach.
    When a creature within 5 feet of you makes an attack against a target other than you (and that target doesn't have this feat), you can use your reaction to make a melee weapon attack against the attacking creature."""
    print(feature)
    dnd_dict.character_dict["features"]['sentinel'] = feature
    dnd_dict.character_dict["feats"]['sentinel'] = 'Sentinel'

def shadow_touched():
    feature = """
Shadow Touched

Your exposure to the Shadowfell's magic has changed you, granting you the following benefits:

    Increase your Intelligence, Wisdom, or Charisma by 1, to a maximum of 20.
    You learn the invisibility spell and one 1st-level spell of your choice. The 1st-level spell must be from the illusion or necromancy school of magic. You can cast each of these spells without expending a spell slot. Once you cast either of these spells in this way, you can't cast that spell in this way again until you finish a long rest. You can also cast these spells using spell slots you have of the appropriate level. The spells' spellcasting ability is the ability increased by this feat."""
    print(feature)
    dnd_dict.character_dict["features"]['shadow_touched'] = feature
    dnd_dict.character_dict["feats"]['shadow_touched'] = 'Shadow Touched'
    dnd_dict.character_dict['spells']['second']['invisibility'] = 'Invisibility'
    dnd_dict.character_dict['special_spells']['racial_spells']['invisibility'] = 'Invisibility'
    spell_list = ['Cause Fear','Color Spray','Disguise Self','Distort Value','False Life','Illusory Script','Inflict Wounds','Ray of Sickness','Silent Image']
    dnd_skills.spell_add(spell_list,dnd_dict.character_dict['spells']['first'],dnd_dict.character_dict['special_spells']['racial_spells'])

    if dnd_dict.character_dict['Stats']['intelligence']['base'] < 20 or dnd_dict.character_dict['Stats']['wisdom']['base'] < 20 or dnd_dict.character_dict['Stats']['charisma']['base'] < 20:
        while True:
            choice = input("""Which stat would you like to increase by 1 to a maximum of 20?
1) Intelligence
2) Wisdom
3) Charisma
Enter your selection: """)

            if choice == '1':
                if dnd_dict.character_dict['Stats']['intelligence']['base'] < 20:
                    dnd_dict.character_dict['Stats']['intelligence']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['intelligence']['base'])
                    dnd_dict.character_dict['Stats']['intelligence']['mod'] = mod
                    spell_attack = ((dnd_dict.character_dict["Stats"]["intelligence"]['mod']) + dnd_dict.character_dict['prof_bonus'])
                    dnd_dict.character_dict["spell_modifier"]['intelligence']['attack'] = spell_attack
                    spell_save = ((dnd_dict.character_dict["Stats"]["intelligence"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
                    dnd_dict.character_dict["spell_modifier"]['intelligence']['save'] = spell_save
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            elif choice == '2':
                if dnd_dict.character_dict['Stats']['wisdom']['base'] < 20:
                    dnd_dict.character_dict['Stats']['wisdom']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['wisdom']['base'])
                    dnd_dict.character_dict['Stats']['wisdom']['mod'] = mod
                    spell_attack = ((dnd_dict.character_dict["Stats"]["wisdom"]['mod']) + dnd_dict.character_dict['prof_bonus'])
                    dnd_dict.character_dict["spell_modifier"]['wisdom']['attack'] = spell_attack
                    spell_save = ((dnd_dict.character_dict["Stats"]["wisdom"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
                    dnd_dict.character_dict["spell_modifier"]['wisdom']['save'] = spell_save
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            elif choice == '3':
                if dnd_dict.character_dict['Stats']['charisma']['base'] < 20:
                    dnd_dict.character_dict['Stats']['charisma']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['charisma']['base'])
                    dnd_dict.character_dict['Stats']['charisma']['mod'] = mod
                    spell_attack = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'])
                    dnd_dict.character_dict["spell_modifier"]['charisma']['attack'] = spell_attack
                    spell_save = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
                    dnd_dict.character_dict["spell_modifier"]['charisma']['save'] = spell_save
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            else:
                print("Error: Invalid Input")
                continue

def sharpshooter():
    feature = """
Sharpshooter

You have mastered ranged weapons and can make shots that others find impossible. You gain the following benefits:

    Attacking at long range doesn't impose disadvantage on your ranged weapon attack rolls.
    Your ranged weapon attacks ignore half cover and three-quarters cover.
    Before you make an attack with a ranged weapon that you are proficient with, you can choose to take a -5 penalty to the attack roll. If the attack hits, you add +10 to the attack's damage."""
    print(feature)
    dnd_dict.character_dict["features"]['sharpshooter'] = feature
    dnd_dict.character_dict["feats"]['sharpshooter'] = 'Sharpshooter'

def shield_master():
    feature = """
Shield Master

You use shields not just for protection but also for offense. You gain the following benefits while you are wielding a shield:

    If you take the Attack action on your turn, you can use a bonus action to try to shove a creature within 5 feet of you with your shield.
    If you aren't incapacitated, you can add your shield's AC bonus to any Dexterity saving throw you make against a spell or other harmful effect that targets only you.
    If you are subjected to an effect that allows you to make a Dexterity saving throw to take only half damage, you can use your reaction to take no damage if you succeed on the saving throw, interposing your shield between yourself and the source of the effect."""
    print(feature)
    dnd_dict.character_dict["features"]['shield_master'] = feature
    dnd_dict.character_dict["feats"]['shield_master'] = 'Shield Master'

def skill_expert():
    feature = """
Skill Expert

You have honed your proficiency with particular skills, granting you the following benefits:

    Increase one ability score of your choice by 1, to a maximum of 20.
    You gain proficiency in one skill of your choice.
    Choose one skill in which you have proficiency. You gain expertise with that skill, which means your proficiency bonus is doubled for any ability check you make with it. The skill you choose must be one that isn't already benefiting from a feature, such as Expertise, that doubles your proficiency bonus."""
    print(feature)
    dnd_dict.character_dict["features"]['skill_expert'] = feature
    dnd_dict.character_dict["feats"]['skill_expert'] = 'Skill Expert'

    if dnd_dict.character_dict['Stats']['strength']['base'] < 20 or dnd_dict.character_dict['Stats']['dexterity']['base'] < 20 or dnd_dict.character_dict['Stats']['constitution']['base'] < 20 or dnd_dict.character_dict['Stats']['intelligence']['base'] < 20 or dnd_dict.character_dict['Stats']['wisdom']['base'] < 20 or dnd_dict.character_dict['Stats']['charisma']['base'] < 20:
        while True:
            choice = input("""Which stat would you like to increase by 1 to a maximum of 20?
1) Strength
2) Dexterity
3) Constitution
4) Intelligence
5) Wisdom
6) Charisma
Enter your selection: """)

            if choice == '1':
                if dnd_dict.character_dict['Stats']['strength']['base'] < 20:
                    dnd_dict.character_dict['Stats']['strength']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['strength']['base'])
                    dnd_dict.character_dict['Stats']['strength']['mod'] = mod
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            elif choice == '2':
                if dnd_dict.character_dict['Stats']['dexterity']['base'] < 20:
                    dnd_dict.character_dict['Stats']['dexterity']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['dexterity']['base'])
                    dnd_dict.character_dict['Stats']['dexterity']['mod'] = mod
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            elif choice == '3':
                if dnd_dict.character_dict['Stats']['constitution']['base'] < 20:
                    dnd_dict.character_dict['Stats']['constitution']['base'] += 1
# If the modifier is positive and increases, increase your hp by your total level
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['constitution']['base'])
                    if mod > dnd_dict.character_dict['Stats']['constitution']['mod'] and mod > 0:
                        new_hp = dnd_dict.character_dict['hp'] + dnd_dict.character_dict['total_level']
                        dnd_dict.character_dict['hp'] = new_hp
                    dnd_dict.character_dict['Stats']['constitution']['mod'] = mod
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            elif choice == '4':
                if dnd_dict.character_dict['Stats']['intelligence']['base'] < 20:
                    dnd_dict.character_dict['Stats']['intelligence']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['intelligence']['base'])
                    dnd_dict.character_dict['Stats']['intelligence']['mod'] = mod
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            elif choice == '5':
                if dnd_dict.character_dict['Stats']['wisdom']['base'] < 20:
                    dnd_dict.character_dict['Stats']['wisdom']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['wisdom']['base'])
                    dnd_dict.character_dict['Stats']['wisdom']['mod'] = mod
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            elif choice == '6':
                if dnd_dict.character_dict['Stats']['charisma']['base'] < 20:
                    dnd_dict.character_dict['Stats']['charisma']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['charisma']['base'])
                    dnd_dict.character_dict['Stats']['charisma']['mod'] = mod
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue


            else:
                print("Error: Invalid Input")
                continue

    dnd_skills.skill_choice()
    dnd_skills.expertise()

def skilled():
    feature = """
Skilled

You gain proficiency in any combination of three skills or tools of your choice."""
    print(feature)
    dnd_dict.character_dict["features"]['skilled'] = feature
    dnd_dict.character_dict["feats"]['skilled'] = 'Skilled'
    x = 1
    while True:
        while x < 5:
            if x < 4:
                print(f'{x}/3')
                choice = input("""Select what you want to increase
1) Skill
2) Tool
Enter your selection: """)
                if choice == '1':
                    if 'acrobatics' in dnd_dict.character_dict['skill_prof'] and 'animal_handling' in dnd_dict.character_dict['skill_prof'] and 'arcana' in dnd_dict.character_dict['skill_prof'] and 'athletics' in dnd_dict.character_dict['skill_prof'] and 'deception' in dnd_dict.character_dict['skill_prof'] and 'history' in dnd_dict.character_dict['skill_prof'] and 'insight' in dnd_dict.character_dict['skill_prof'] and 'intimidation' in dnd_dict.character_dict['skill_prof'] and 'investigation' in dnd_dict.character_dict['skill_prof'] and 'medicine' in dnd_dict.character_dict['skill_prof'] and 'nature' in dnd_dict.character_dict['skill_prof'] and 'perception' in dnd_dict.character_dict['skill_prof'] and 'performance' in dnd_dict.character_dict['skill_prof'] and 'persuasion' in dnd_dict.character_dict['skill_prof'] and 'religion' in dnd_dict.character_dict['skill_prof'] and 'sleight_of_hand' in dnd_dict.character_dict['skill_prof'] and 'stealth' in dnd_dict.character_dict['skill_prof'] and 'survival' in dnd_dict.character_dict['skill_prof']:
                        print("Error: You are already proficient with every skill")
                        continue
                    else:
                        dnd_skills.skill_choice()
                        x+=1
#                        continue

                elif choice == '2':
                    dnd_tools.artisan_tools()
                    x+=1
#                    continue

                else:
                    print("Error: Invalid Input")
                    continue

            elif x == 4:
                x+=1
                break
        break

def skulker():
    feature = """
Skulker
Prerequisite: Dexterity 13 or higher

You are expert at slinking through shadows. You gain the following benefits:

    You can try to hide when you are lightly obscured from the creature from which you are hiding.
    When you are hidden from a creature and miss it with a ranged weapon attack, making the attack doesn't reveal your position.
    Dim light doesn't impose disadvantage on your Wisdom (Perception) checks relying on sight."""
    print(feature)
    dnd_dict.character_dict["features"]['skulker'] = feature
    dnd_dict.character_dict["feats"]['skulker'] = 'Skulker'

def slasher():
    feature = """
Slasher

You've learned where to cut to have the greatest results, granting you the following benefits:

    Increase your Strength or Dexterity by 1, to a maximum of 20.
    Once per turn when you hit a creature with an attack that deals slashing damage, you can reduce the speed of the target by 10 feet until the start of your next turn.
    When you score a critical hit that deals slashing damage to a creature, you grievously wound it. Until the start of your next turn, the target has disadvantage on all attack rolls."""
    print(feature)
    dnd_dict.character_dict["features"]['slasher'] = feature
    dnd_dict.character_dict["feats"]['slasher'] = 'Slasher'
    if dnd_dict.character_dict['Stats']['strength']['base'] < 20 or dnd_dict.character_dict['Stats']['dexterity']['base'] < 20:
        while True:
            choice = input("""Which stat would you like to increase by 1 to a maximum of 20?
1) Strength
2) Dexterity
Enter your selection: """)

            if choice == '1':
                if dnd_dict.character_dict['Stats']['strength']['base'] < 20:
                    dnd_dict.character_dict['Stats']['strength']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['strength']['base'])
                    dnd_dict.character_dict['Stats']['strength']['mod'] = mod
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            elif choice == '2':
                if dnd_dict.character_dict['Stats']['dexterity']['base'] < 20:
                    dnd_dict.character_dict['Stats']['dexterity']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['dexterity']['base'])
                    dnd_dict.character_dict['Stats']['dexterity']['mod'] = mod
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            else:
                print("Error: Invalid Input")
                continue

def spell_sniper():
    feature = """
Spell Sniper
Prerequisite: The ability to cast at least one spell

You have learned techniques to enhance your attacks with certain kinds of spells, gaining the following benefits:

    When you cast a spell that requires you to make an attack roll, the spell's range is doubled.
    Your ranged spell attacks ignore half cover and three-quarters cover.
    You learn one cantrip that requires an attack roll. Choose the cantrip from the bard, cleric, druid, sorcerer, warlock, or wizard spell list. Your spellcasting ability for this cantrip depends on the spell list you chose from: Charisma for bard, sorcerer, or warlock; Wisdom for cleric or druid; or Intelligence for wizard."""
    print(feature)
    dnd_dict.character_dict["features"]['spell_sniper'] = feature
    dnd_dict.character_dict["feats"]['spell_sniper'] = 'Spell Sniper'

    while True:
        choice = input("""Select the class you want to learn a spell from
1) Bard
2) Cleric
3) Druid
4) Sorcerer
5) Warlock
6) Wizard
Enter your selection: """)
        if choice == '1':
            dnd_skills.spell_add(dnd_magic.bard_cantrip,dnd_dict.character_dict['spells']['cantrips'],dnd_dict.character_dict['special_spells']['cantrips'])
            spell_attack = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'])
            dnd_dict.character_dict["spell_modifier"]['charisma']['attack'] = spell_attack
            spell_save = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
            dnd_dict.character_dict["spell_modifier"]['charisma']['save'] = spell_save
            break

        elif choice == '2':
            dnd_skills.spell_add(dnd_magic.cleric_cantrip,dnd_dict.character_dict['spells']['cantrips'],dnd_dict.character_dict['special_spells']['cantrips'])
            spell_attack = ((dnd_dict.character_dict["Stats"]["wisdom"]['mod']) + dnd_dict.character_dict['prof_bonus'])
            dnd_dict.character_dict["spell_modifier"]['wisdom']['attack'] = spell_attack
            spell_save = ((dnd_dict.character_dict["Stats"]["wisdom"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
            dnd_dict.character_dict["spell_modifier"]['wisdom']['save'] = spell_save
            break

        elif choice == '3':
            dnd_skills.spell_add(dnd_magic.druid_cantrip,dnd_dict.character_dict['spells']['cantrips'],dnd_dict.character_dict['special_spells']['cantrips'])
            spell_attack = ((dnd_dict.character_dict["Stats"]["wisdom"]['mod']) + dnd_dict.character_dict['prof_bonus'])
            dnd_dict.character_dict["spell_modifier"]['wisdom']['attack'] = spell_attack
            spell_save = ((dnd_dict.character_dict["Stats"]["wisdom"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
            dnd_dict.character_dict["spell_modifier"]['wisdom']['save'] = spell_save
            break
                
        elif choice == '4':
            dnd_skills.spell_add(dnd_magic.sorcerer_cantrip,dnd_dict.character_dict['spells']['cantrips'],dnd_dict.character_dict['special_spells']['cantrips'])
            spell_attack = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'])
            dnd_dict.character_dict["spell_modifier"]['charisma']['attack'] = spell_attack
            spell_save = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
            dnd_dict.character_dict["spell_modifier"]['charisma']['save'] = spell_save
            break

        elif choice == '5':
            dnd_skills.spell_add(dnd_magic.warlock_cantrip,dnd_dict.character_dict['spells']['cantrips'],dnd_dict.character_dict['special_spells']['cantrips'])
            spell_attack = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'])
            dnd_dict.character_dict["spell_modifier"]['charisma']['attack'] = spell_attack
            spell_save = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
            dnd_dict.character_dict["spell_modifier"]['charisma']['save'] = spell_save
            break

        elif choice == '6':
            dnd_skills.spell_add(dnd_magic.wizard_cantrip,dnd_dict.character_dict['spells']['cantrips'],dnd_dict.character_dict['special_spells']['cantrips'])
            spell_attack = ((dnd_dict.character_dict["Stats"]["intelligence"]['mod']) + dnd_dict.character_dict['prof_bonus'])
            dnd_dict.character_dict["spell_modifier"]['intelligence']['attack'] = spell_attack
            spell_save = ((dnd_dict.character_dict["Stats"]["intelligence"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
            dnd_dict.character_dict["spell_modifier"]['intelligence']['save'] = spell_save
            break

        else:
            print("Error: invalid input")
            continue

def squat_nimbleness():
    feature = """
Squat Nimbleness
Prerequisite: Dwarf or a Small race

You are uncommonly nimble for your race. You gain the following benefits:

    Increase your Strength or Dexterity by 1, to a maximum of 20.
    Increase your walking speed by 5 feet.
    You gain proficiency in the Acrobatics or Athletics skill (your choice).
    You have advantage on any Strength (Athletics) or Dexterity (Acrobatics) check you make to escape from being grappled."""
    print(feature)
    dnd_dict.character_dict["features"]['squat_nimbleness'] = feature
    dnd_dict.character_dict["feats"]['squat_nimbleness'] = 'Squat Nimbleness'
    if dnd_dict.character_dict['Stats']['strength']['base'] < 20 or dnd_dict.character_dict['Stats']['dexterity']['base'] < 20:
        while True:
            choice = input("""Which stat would you like to increase by 1 to a maximum of 20?
1) Strength
2) Dexterity
Enter your selection: """)

            if choice == '1':
                if dnd_dict.character_dict['Stats']['strength']['base'] < 20:
                    dnd_dict.character_dict['Stats']['strength']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['strength']['base'])
                    dnd_dict.character_dict['Stats']['strength']['mod'] = mod
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            elif choice == '2':
                if dnd_dict.character_dict['Stats']['dexterity']['base'] < 20:
                    dnd_dict.character_dict['Stats']['dexterity']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['dexterity']['base'])
                    dnd_dict.character_dict['Stats']['dexterity']['mod'] = mod
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            else:
                print("Error: Invalid Input")
                continue


    dnd_dict.character_dict['speed'] += 5
    if 'roving' in dnd_dict.character_dict['features']:
        dnd_dict.character_dict['climb_speed'] == dnd_dict.character_dict['speed']
        dnd_dict.character_dict['swim_speed'] == dnd_dict.character_dict['speed']
    if dnd_dict.character_dict['unarmored_movement_barbarian'] > 0:
        dnd_dict.character_dict['unarmored_movement_barbarian'] +=5
    if dnd_dict.character_dict['unarmored_movement_monk'] > 0:
        dnd_dict.character_dict['unarmored_movement_monk'] +=5

    if 'acrobatics' not in dnd_dict.character_dict['skill_prof'] or 'athletics' not in dnd_dict.character_dict['skill_prof']:
        while True:
            choice = input("""Select one skill to gain proficiency in:
1) Acrobatics
2) Athletics
Enter your selection: """)
            if choice == '1':
                if 'acrobatics' in dnd_dict.character_dict['skill_prof']:
                    print("Error: You are already proficient with this skill")
                    continue
                else:
                    dnd_dict.character_dict['skill_prof']['acrobatics'] = 'Acrobatics'
                    break

            elif choice == '2':
                if 'athletics' in dnd_dict.character_dict['skill_prof']:
                    print("Error: You are already proficient with this skill")
                    continue
                else:
                    dnd_dict.character_dict['skill_prof']['athletics'] = 'Athletics'
                    break

            else:
                print("Error: Invalid Selection")
                continue

def strixhaven_initiate():
    print("""
Strixhaven Initiate

You have studied some magical theory and have learned a few spells associated with Strixhaven University.

Choose one of Strixhaven's colleges: Lorehold, Prismari, Quandrix, Silverquill, or Witherbloom. You learn two cantrips and one 1st-level spell based on the college you choose, as specified in the Strixhaven Spells table.

You can cast the chosen 1st-level spell without a spell slot, and you must finish a long rest before you can cast it in this way again. You can also cast the spell using any spell slots you have.

Your spellcasting ability for this feat's spells is Intelligence, Wisdom, or Charisma (choose when you select this feat).
Strixhaven SpellsCollege	Cantrips	1st-Level Spell
Lorehold	Choose two from light, sacred flame, and thaumaturgy.	Choose one 1st-level cleric or wizard spell.
Prismari	Choose two from fire bolt, prestidigitation, and ray of frost.	Choose one 1st-level bard or sorcerer spell.
Quandrix	Choose two from druidcraft, guidance, and mage hand.	Choose one 1st-level druid or wizard spell.
Silverquill	Choose two from sacred flame, thaumaturgy, and vicious mockery.	Choose one 1st-level bard or cleric spell.
Witherbloom	Choose two from chill touch, druidcraft, and spare the dying.	Choose one 1st-level druid or wizard spell.""")
    feature = """Strixhaven Initiate

You have studied some magical theory and have learned a few spells associated with Strixhaven University.

Choose one of Strixhaven's colleges: Lorehold, Prismari, Quandrix, Silverquill, or Witherbloom. You learn two cantrips and one 1st-level spell based on the college you choose, as specified in the Strixhaven Spells table.

You can cast the chosen 1st-level spell without a spell slot, and you must finish a long rest before you can cast it in this way again. You can also cast the spell using any spell slots you have."""

    dnd_dict.character_dict["feats"]['strixhaven_initiate'] = 'Strixhaven Initiate'
    dnd_dict.character_dict["features"]['strixhaven_initiate'] = 'Strixhaven Initiate'

    while True:
        choice1 = input("""Select the college you want to attend
1) Lorehold
2) Prismari
3) Quandrix
4) Silverquill
5) Witherbloon
Enter your selection: """)
        if choice1 == '1':
            dnd_dict.character_dict["feats"]['strixhaven_initiate_lorehold'] = 'Strixhaven Initiate (Lorehold)'
            spell_list = ['Light','Sacred Flame','Thaumaturgy']
            counter = 1

            while True:
# Puts the unknown spells in a list.
# Breaks if you learn two spells or have no other spells to learn
                lorehold_spells = []
                for i in spell_list:
                     if i not in dnd_dict.character_dict['spells']['cantrips'].values():
                         lorehold_spells.append(i)
                if len(lorehold_spells) == 0:
                    break
                elif counter < 3:
                    dnd_skills.strixhaven_spells(lorehold_spells)
                    counter += 1
                else:
                    break

            while True:
                choice3 = input("""Select the spell list you want to learn from
1) Cleric
2) Wizard
Enter your selection: """)
                if choice3 == '1':
                    #Present an error message if you already have the cleric spells
                    if dnd_dict.character_dict['player_class']['cleric']['class_level'] > 0:
                        print("You already know all of these spells")
                        continue
                    else:
                        dnd_skills.spell_add(dnd_magic.cleric_first_classless,dnd_dict.character_dict['spells']['first'],dnd_dict.character_dict['special_spells']['first'])
                        spell_attack = ((dnd_dict.character_dict["Stats"]["wisdom"]['mod']) + dnd_dict.character_dict['prof_bonus'])
                        dnd_dict.character_dict["spell_modifier"]['wisdom']['attack'] = spell_attack
                        spell_save = ((dnd_dict.character_dict["Stats"]["wisdom"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
                        dnd_dict.character_dict["spell_modifier"]['wisdom']['save'] = spell_save
                        break

                elif choice3 == '2':
                    dnd_skills.spell_add(dnd_magic.wizard_first,dnd_dict.character_dict['spells']['first'],dnd_dict.character_dict['special_spells']['first'])
                    spell_attack = ((dnd_dict.character_dict["Stats"]["intelligence"]['mod']) + dnd_dict.character_dict['prof_bonus'])
                    dnd_dict.character_dict["spell_modifier"]['intelligence']['attack'] = spell_attack
                    spell_save = ((dnd_dict.character_dict["Stats"]["intelligence"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
                    dnd_dict.character_dict["spell_modifier"]['intelligence']['save'] = spell_save
                    break

                else:
                    print("Error: Invalid Input")
                    continue


        elif choice1 == '2':
            dnd_dict.character_dict["feats"]['strixhaven_initiate_prismari'] = 'Strixhaven Initiate (Prismari)'

            spell_list = ['Fire Bolt','Prestidigitation','Ray of Frost']
            counter = 1
            while True:
                prismari_spells = []
                for i in spell_list:
                     if i not in dnd_dict.character_dict['spells']['cantrips'].values():
                         prismari_spells.append(i)
                if len(prismari_spells) == 0:
                    break
                elif counter < 3:
                    dnd_skills.strixhaven_spells(prismari_spells)
                    counter += 1
                else:
                    break

            while True:
                choice3 = input("""Select the spell list you want to learn from
1) Bard
2) Sorcerer
Enter your selection: """)
                if choice3 == '1':
                    dnd_skills.spell_add(dnd_magic.bard_first,dnd_dict.character_dict['spells']['first'],dnd_dict.character_dict['special_spells']['first'])
                    spell_attack = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'])
                    dnd_dict.character_dict["spell_modifier"]['charisma']['attack'] = spell_attack
                    spell_save = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
                    dnd_dict.character_dict["spell_modifier"]['charisma']['save'] = spell_save
                    break

                elif choice3 == '2':
                    dnd_skills.spell_add(dnd_magic.sorcerer_first,dnd_dict.character_dict['spells']['first'],dnd_dict.character_dict['special_spells']['first'])
                    spell_attack = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'])
                    dnd_dict.character_dict["spell_modifier"]['charisma']['attack'] = spell_attack
                    spell_save = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
                    dnd_dict.character_dict["spell_modifier"]['charisma']['save'] = spell_save
                    break

                else:
                    print("Error: Invalid Input")
                    continue

        elif choice1 == '3':
            dnd_dict.character_dict["feats"]['strixhaven_initiate_quandrix'] = 'Strixhaven Initiate (Quandrix)'

            spell_list = ['Druidcraft','Guidance','Mage Hand']
            counter = 1
            while True:
                quandrix_spells = []
                for i in spell_list:
                     if i not in dnd_dict.character_dict['spells']['cantrips'].values():
                         quandrix_spells.append(i)
                if len(quandrix_spells) == 0:
                    break
                elif counter < 3:
                    dnd_skills.strixhaven_spells(quandrix_spells)
                    counter += 1
                else:
                    break


            while True:
                choice3 = input("""Select the spell list you want to learn from
1) Druid
2) Wizard
Enter your selection: """)
                if choice3 == '1':
# Present an error message if you already have the cleric spells
                    if dnd_dict.character_dict['player_class']['druid']['class_level'] > 0:
                        print("You already know all of these spells")
                        continue
                    else:
                        dnd_skills.spell_add(dnd_magic.druid_first_classless,dnd_dict.character_dict['spells']['first'],dnd_dict.character_dict['special_spells']['first'])
                        spell_attack = ((dnd_dict.character_dict["Stats"]["wisdom"]['mod']) + dnd_dict.character_dict['prof_bonus'])
                        dnd_dict.character_dict["spell_modifier"]['wisdom']['attack'] = spell_attack
                        spell_save = ((dnd_dict.character_dict["Stats"]["wisdom"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
                        dnd_dict.character_dict["spell_modifier"]['wisdom']['save'] = spell_save
                        break

                elif choice3 == '2':
                    dnd_skills.spell_add(dnd_magic.wizard_first,dnd_dict.character_dict['spells']['first'],dnd_dict.character_dict['special_spells']['first'])
                    spell_attack = ((dnd_dict.character_dict["Stats"]["intelligence"]['mod']) + dnd_dict.character_dict['prof_bonus'])
                    dnd_dict.character_dict["spell_modifier"]['intelligence']['attack'] = spell_attack
                    spell_save = ((dnd_dict.character_dict["Stats"]["intelligence"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
                    dnd_dict.character_dict["spell_modifier"]['intelligence']['save'] = spell_save
                    break

                else:
                    print("Error: Invalid Input")
                    continue

        elif choice1 == '4':
            dnd_dict.character_dict["feats"]['strixhaven_initiate_silverquill'] = 'Strixhaven Initiate (Silverquill)'
            spell_list = ['Vicious Mockery','Sacred Flame','Thaumaturgy']
            counter = 1
            while True:
                silverquill_spells = []
                for i in spell_list:
                     if i not in dnd_dict.character_dict['spells']['cantrips'].values():
                         silverquill_spells.append(i)
                if len(silverquill_spells) == 0:
                    break
                elif counter < 3:
                    dnd_skills.strixhaven_spells(silverquill_spells)
                    counter += 1
                else:
                    break
            while True:
                choice3 = input("""Select the spell list you want to learn from
1) Bard
2) Cleric
Enter your selection: """)
                if choice3 == '1':
                    dnd_skills.spell_add(dnd_magic.bard_first,dnd_dict.character_dict['spells']['first'],dnd_dict.character_dict['special_spells']['first'])
                    spell_attack = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'])
                    dnd_dict.character_dict["spell_modifier"]['charisma']['attack'] = spell_attack
                    spell_save = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
                    dnd_dict.character_dict["spell_modifier"]['charisma']['save'] = spell_save
                    break

                elif choice3 == '2':
# Present an error message if you already have the cleric spells
                    if dnd_dict.character_dict['player_class']['cleric']['class_level'] > 0:
                        print("You already know all of these spells")
                        continue
                    else:
                        dnd_skills.spell_add(dnd_magic.cleric_first_classless,dnd_dict.character_dict['spells']['first'],dnd_dict.character_dict['special_spells']['first'])
                        spell_attack = ((dnd_dict.character_dict["Stats"]["wisdom"]['mod']) + dnd_dict.character_dict['prof_bonus'])
                        dnd_dict.character_dict["spell_modifier"]['wisdom']['attack'] = spell_attack
                        spell_save = ((dnd_dict.character_dict["Stats"]["wisdom"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
                        dnd_dict.character_dict["spell_modifier"]['wisdom']['save'] = spell_save
                        break

                else:
                    print("Error: Invalid Input")
                    continue

        elif choice1 == '5':
            dnd_dict.character_dict["feats"]['strixhaven_initiate_witherbloom'] = 'Strixhaven Initiate (Witherbloom)'
            spell_list = ['Druidcraft','Chill Touch','Spare the Dying']
            counter = 1
            while True:
                witherbloom_spells = []
                for i in spell_list:
                     if i not in dnd_dict.character_dict['spells']['cantrips'].values():
                         witherbloom_spells.append(i)
                if len(witherbloom_spells) == 0:
                    break
                elif counter < 3:
                    dnd_skills.strixhaven_spells(witherbloom_spells)
                    counter += 1
                else:
                    break
            while True:
                choice3 = input("""Select the spell list you want to learn from
1) Druid
2) Wizard
Enter your selection: """)
                if choice3 == '1':
# Present an error message if you already have the cleric spells
                    if dnd_dict.character_dict['player_class']['druid']['class_level'] > 0:
                        print("You already know all of these spells")
                        continue
                    else:
                        dnd_skills.spell_add(dnd_magic.druid_first_classless,dnd_dict.character_dict['spells']['first'],dnd_dict.character_dict['special_spells']['first'])
                        spell_attack = ((dnd_dict.character_dict["Stats"]["wisdom"]['mod']) + dnd_dict.character_dict['prof_bonus'])
                        dnd_dict.character_dict["spell_modifier"]['wisdom']['attack'] = spell_attack
                        spell_save = ((dnd_dict.character_dict["Stats"]["wisdom"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
                        dnd_dict.character_dict["spell_modifier"]['wisdom']['save'] = spell_save
                        break

                elif choice3 == '2':
                    dnd_skills.spell_add(dnd_magic.wizard_first,dnd_dict.character_dict['spells']['first'],dnd_dict.character_dict['special_spells']['first'])
                    spell_attack = ((dnd_dict.character_dict["Stats"]["intelligence"]['mod']) + dnd_dict.character_dict['prof_bonus'])
                    dnd_dict.character_dict["spell_modifier"]['intelligence']['attack'] = spell_attack
                    spell_save = ((dnd_dict.character_dict["Stats"]["intelligence"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
                    dnd_dict.character_dict["spell_modifier"]['intelligence']['save'] = spell_save
                    break

                else:
                    print("Error: Invalid Input")
                    continue

        else:
            print("Error: Invalid Input")
            continue

        break

def strixhaven_mascot():
    feature = """Prerequisite: 4th Level, Strixhaven Initiate Feat

You have learned how to summon a Strixhaven mascot to assist you, granting you these benefits:

    You can cast the Find Familiar spell as a ritual. Your familiar can take the form of the mascot associated with the college you chose for the Strixhaven Initiate feat: a spirit statue mascot (Lorehold), an art elemental mascot (Prismari), a fractal mascot (Quandrix), an inkling mascot (Silverquill), or a pest mascot (Witherbloom).

    When you take the Attack action on your turn, you can forgo one attack to allow your mascot familiar to make one attack of its own with its reaction.

    If your mascot familiar is within 60 feet of you, you can be teleported as an action, swapping places with the familiar. If your destination space is too small for you to occupy, the teleportation fails and is wasted. Once you teleport this way, you can't do so again until you finish a long rest, unless you expend a spell slot of 2nd level or higher to do it again."""
    print(feature)
    dnd_dict.character_dict["features"]['strixhaven_mascot'] = feature
    dnd_dict.character_dict["feats"]['strixhaven_mascot'] = 'Strixhaven Mascot'
    dnd_dict.character_dict['spells']['first']['find_familiar'] = 'Find Familiar'

    if 'strixhaven_initiate_lorehold' in dnd_dict.character_dict['feats']: 
        dnd_dict.character_dict['spells']['first']['find_familiar_lorehold'] = 'Find Familiar (Spirit Statue Mascot)'

    if 'strixhaven_initiate_prismari' in dnd_dict.character_dict['feats']: 
        dnd_dict.character_dict['spells']['first']['find_familiar_prismari'] = 'Find Familiar (Art Elemental Mascot)'

    if 'strixhaven_initiate_quandrix' in dnd_dict.character_dict['feats']: 
        dnd_dict.character_dict['spells']['first']['find_familiar_quandrix'] = 'Find Familiar (Fractal Mascot)'

    if 'strixhaven_initiate_silverquill' in dnd_dict.character_dict['feats']: 
        dnd_dict.character_dict['spells']['first']['find_familiar_silverquill'] = 'Find Familiar (Inkling Mascot)'

    if 'strixhaven_initiate_witherbloom' in dnd_dict.character_dict['feats']: 
        dnd_dict.character_dict['spells']['first']['find_familiar_witherbloom'] = 'Find Familiar (Pest Mascot)'

def svirfneblin_magic():
    feature = """
Svirfneblin Magic
Prerequisite: Gnome (deep)

You have inherited the innate spellcasting ability of your ancestors. This ability allows you to cast nondetection on yourself at will, without needing a material component. You can also cast each of the following spells once with this ability: blindness/deafness, blur, and disguise self. You regain the ability to cast these spells when you finish a long rest.

Intelligence is your spellcasting ability for these spells, and you cast them at their lowest possible levels."""
    print(feature)
    dnd_dict.character_dict["features"]['svirfneblin_magic'] = feature
    dnd_dict.character_dict["feats"]['svirfneblin_magic'] = 'Svirfneblin Magic'
    dnd_dict.character_dict['spells']['first']['nondetection'] = 'Nondetection'
    dnd_dict.character_dict['special_spells']['racial_spells']['nondetection'] = 'Nondetection'
    spell_attack = ((dnd_dict.character_dict["Stats"]["intelligence"]['mod']) + dnd_dict.character_dict['prof_bonus'])
    dnd_dict.character_dict["spell_modifier"]['intelligence']['attack'] = spell_attack
    spell_save = ((dnd_dict.character_dict["Stats"]["intelligence"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
    dnd_dict.character_dict["spell_modifier"]['intelligence']['save'] = spell_save

def tavern_brawler():
    feature = """
Tavern Brawler

Accustomed to rough-and-tumble fighting using whatever weapons happen to be at hand, you gain the following benefits:

    Increase your Strength or Constitution by 1, to a maximum of 20.
    You are proficient with improvised weapons.
    Your unarmed strike uses a d4 for damage.
    When you hit a creature with an unarmed strike or an improvised weapon on your turn, you can use a bonus action to attempt to grapple the target."""
    print(feature)
    dnd_dict.character_dict["features"]['tavern_brawler'] = feature
    dnd_dict.character_dict["feats"]['tavern_brawler'] = 'Tavern Brawler'

    if dnd_dict.character_dict['Stats']['strength']['base'] < 20 or dnd_dict.character_dict['Stats']['constitution']['base'] < 20:
        while True:
            choice = input("""Which stat would you like to increase by 1 to a maximum of 20?
1) Strength
2) Constitution
Enter your selection: """)

            if choice == '1':
                if dnd_dict.character_dict['Stats']['strength']['base'] < 20:
                    dnd_dict.character_dict['Stats']['strength']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['strength']['base'])
                    dnd_dict.character_dict['Stats']['strength']['mod'] = mod
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            elif choice == '2':
                if dnd_dict.character_dict['Stats']['constitution']['base'] < 20:
                    dnd_dict.character_dict['Stats']['constitution']['base'] += 1
# If the modifier is positive and increases, increase your hp by your total level
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['constitution']['base'])
                    if mod > dnd_dict.character_dict['Stats']['constitution']['mod'] and mod > 0:
                        new_hp = dnd_dict.character_dict['hp'] + dnd_dict.character_dict['total_level']
                        dnd_dict.character_dict['hp'] = new_hp
                    dnd_dict.character_dict['Stats']['constitution']['mod'] = mod
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue


            else:
                print("Error: Invalid Input")
                continue

    dnd_dict.character_dict['Weapon_Prof']['improvised_weapons'] = 'Improvised Weapons'

def telekinetic():
    feature = """
Telekinetic

You learn to move things with your mind, granting you the following benefits:

    Increase your Intelligence, Wisdom, or Charisma by 1, to a maximum of 20.
    You learn the mage hand cantrip. You can cast it without verbal or somatic components, and you can make the spectral hand invisible. If you already know this spell, its range increases by 30 feet when you cast it. Its spellcasting ability is the ability increased by this feat.
    As a bonus action, you can try to telekinetically shove one creature you can see within 30 feet of you. When you do so, the target must succeed on a Strength saving throw (DC 8 + your proficiency bonus + the ability modifier of the score increased by this feat) or be moved 5 feet toward you or away from you. A creature can willingly fail this save."""

    print(feature)
    dnd_dict.character_dict["features"]['telekinetic'] = feature
    dnd_dict.character_dict["feats"]['telekinetic'] = 'Telekinetic'
    dnd_dict.character_dict['spells']['cantrips']['mage_hand'] = 'Mage Hand'

    if dnd_dict.character_dict['Stats']['intelligence']['base'] < 20 or dnd_dict.character_dict['Stats']['wisdom']['base'] < 20 or dnd_dict.character_dict['Stats']['charisma']['base'] < 20:
        while True:
            choice = input("""Which stat would you like to increase by 1 to a maximum of 20?
1) Intelligence
2) Wisdom
3) Charisma
Enter your selection: """)

            if choice == '1':
                if dnd_dict.character_dict['Stats']['intelligence']['base'] < 20:
                    dnd_dict.character_dict['Stats']['intelligence']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['intelligence']['base'])
                    dnd_dict.character_dict['Stats']['intelligence']['mod'] = mod
                    spell_attack = ((dnd_dict.character_dict["Stats"]["intelligence"]['mod']) + dnd_dict.character_dict['prof_bonus'])
                    dnd_dict.character_dict["spell_modifier"]['intelligence']['attack'] = spell_attack
                    spell_save = ((dnd_dict.character_dict["Stats"]["intelligence"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
                    dnd_dict.character_dict["spell_modifier"]['intelligence']['save'] = spell_save
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            elif choice == '2':
                if dnd_dict.character_dict['Stats']['wisdom']['base'] < 20:
                    dnd_dict.character_dict['Stats']['wisdom']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['wisdom']['base'])
                    dnd_dict.character_dict['Stats']['wisdom']['mod'] = mod
                    spell_attack = ((dnd_dict.character_dict["Stats"]["wisdom"]['mod']) + dnd_dict.character_dict['prof_bonus'])
                    dnd_dict.character_dict["spell_modifier"]['wisdom']['attack'] = spell_attack
                    spell_save = ((dnd_dict.character_dict["Stats"]["wisdom"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
                    dnd_dict.character_dict["spell_modifier"]['wisdom']['save'] = spell_save
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            elif choice == '3':
                if dnd_dict.character_dict['Stats']['charisma']['base'] < 20:
                    dnd_dict.character_dict['Stats']['charisma']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['charisma']['base'])
                    dnd_dict.character_dict['Stats']['charisma']['mod'] = mod
                    spell_attack = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'])
                    dnd_dict.character_dict["spell_modifier"]['charisma']['attack'] = spell_attack
                    spell_save = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
                    dnd_dict.character_dict["spell_modifier"]['charisma']['save'] = spell_save
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            else:
                print("Error: Invalid Input")
                continue

def telepathic():
    feature = """
Telepathic

You awaken the ability to mentally connect with others, granting you the following benefits:

    Increase your Intelligence, Wisdom, or Charisma by 1, to a maximum of 20.
    You can speak telepathically to any creature you can see within 60 feet of you. Your telepathic utterances are in a language you know, and the creature understands you only if it knows that language. Your communication doesn't give the creature the ability to respond to you telepathically.
    You can cast the detect thoughts spell, requiring no spell slot or components, and you must finish a long rest before you can cast it this way again. Your spellcasting ability for the spell is the ability increased by this feat. If you have spell slots of 2nd level or higher, you can cast this spell with them."""

    print(feature)
    dnd_dict.character_dict["features"]['telepathic'] = feature
    dnd_dict.character_dict["feats"]['telepathic'] = 'Telepathic'
    dnd_dict.character_dict['spells']['first']['detect_thoughts'] = 'Detect Thoughts'

    if dnd_dict.character_dict['Stats']['intelligence']['base'] < 20 or dnd_dict.character_dict['Stats']['wisdom']['base'] < 20 or dnd_dict.character_dict['Stats']['charisma']['base'] < 20:
        while True:
            choice = input("""Which stat would you like to increase by 1 to a maximum of 20?
1) Intelligence
2) Wisdom
3) Charisma
Enter your selection: """)

            if choice == '1':
                if dnd_dict.character_dict['Stats']['intelligence']['base'] < 20:
                    dnd_dict.character_dict['Stats']['intelligence']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['intelligence']['base'])
                    dnd_dict.character_dict['Stats']['intelligence']['mod'] = mod
                    spell_attack = ((dnd_dict.character_dict["Stats"]["intelligence"]['mod']) + dnd_dict.character_dict['prof_bonus'])
                    dnd_dict.character_dict["spell_modifier"]['intelligence']['attack'] = spell_attack
                    spell_save = ((dnd_dict.character_dict["Stats"]["intelligence"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
                    dnd_dict.character_dict["spell_modifier"]['intelligence']['save'] = spell_save
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            elif choice == '2':
                if dnd_dict.character_dict['Stats']['wisdom']['base'] < 20:
                    dnd_dict.character_dict['Stats']['wisdom']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['wisdom']['base'])
                    dnd_dict.character_dict['Stats']['wisdom']['mod'] = mod
                    spell_attack = ((dnd_dict.character_dict["Stats"]["wisdom"]['mod']) + dnd_dict.character_dict['prof_bonus'])
                    dnd_dict.character_dict["spell_modifier"]['wisdom']['attack'] = spell_attack
                    spell_save = ((dnd_dict.character_dict["Stats"]["wisdom"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
                    dnd_dict.character_dict["spell_modifier"]['wisdom']['save'] = spell_save
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            elif choice == '3':
                if dnd_dict.character_dict['Stats']['charisma']['base'] < 20:
                    dnd_dict.character_dict['Stats']['charisma']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['charisma']['base'])
                    dnd_dict.character_dict['Stats']['charisma']['mod'] = mod
                    spell_attack = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'])
                    dnd_dict.character_dict["spell_modifier"]['charisma']['attack'] = spell_attack
                    spell_save = ((dnd_dict.character_dict["Stats"]["charisma"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
                    dnd_dict.character_dict["spell_modifier"]['charisma']['save'] = spell_save
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            else:
                print("Error: Invalid Input")
                continue

def tough():
    feature = """
Tough

Your hit point maximum increases by an amount equal to twice your level when you gain this feat. Whenever you gain a level thereafter, your hit point maximum increases by an additional 2 hit points."""

    print(feature)
    dnd_dict.character_dict["features"]['tough'] = feature
    dnd_dict.character_dict["feats"]['tough'] = 'Tough'
    new_hp = dnd_dict.character_dict['total_level'] * 2
    dnd_dict.character_dict['hp'] += new_hp

def war_caster():
    feature = """
War Caster
Prerequisite: The ability to cast at least one spell

You have practiced casting spells in the midst of combat, learning techniques that grant you the following benefits:

    You have advantage on Constitution saving throws that you make to maintain your concentration on a spell when you take damage.
    You can perform the somatic components of spells even when you have weapons or a shield in one or both hands.
    When a hostile creature's movement provokes an opportunity attack from you, you can use your reaction to cast a spell at the creature, rather than making an opportunity attack. The spell must have a casting time of 1 action and must target only that creature."""
    print(feature)
    dnd_dict.character_dict["features"]['war_caster'] = feature
    dnd_dict.character_dict["feats"]['war_caster'] = 'War Caster'

def weapon_master():
    feature = """
Weapon Master

You have practiced extensively with a variety of weapons, gaining the following benefits:

    Increase your Strength or Dexterity by 1, to a maximum of 20.
    You gain proficiency with four weapons of your choice. Each one must be a simple or a martial weapon."""
    print(feature)
    dnd_dict.character_dict["features"]['weapon_master'] = feature
    dnd_dict.character_dict["feats"]['weapon_master'] = 'Weapon Master'

    if dnd_dict.character_dict['Stats']['strength']['base'] < 20 or dnd_dict.character_dict['Stats']['dexterity']['base'] < 20:
        while True:
            choice = input("""Which stat would you like to increase by 1 to a maximum of 20?
1) Strength
2) Dexterity
Enter your selection: """)

            if choice == '1':
                if dnd_dict.character_dict['Stats']['strength']['base'] < 20:
                    dnd_dict.character_dict['Stats']['strength']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['strength']['base'])
                    dnd_dict.character_dict['Stats']['strength']['mod'] = mod
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            elif choice == '2':
                if dnd_dict.character_dict['Stats']['dexterity']['base'] < 20:
                    dnd_dict.character_dict['Stats']['dexterity']['base'] += 1
                    mod = dnd_class.Character.mod(dnd_dict.character_dict['Stats']['dexterity']['base'])
                    dnd_dict.character_dict['Stats']['dexterity']['mod'] = mod
                    break
                else:
                    print("You already have the maximum score in this stat")
                    continue

            else:
                print("Error: Invalid Input")
                continue

    weapon_list = ['Club','Dagger','Greatclub','Handaxe','Javelin','Light Hammer','Mace','Quarterstaff','Sickle','Spear','Light Crossbow','Dart','Shortbow','Sling','Battleaxe','Flail','Glaive','Greataxe','Greatsword','Halberd','Lance','Longsword','Maul','Morningstar','Pike','Rapier','Scimitar','Shortsword','Trident','War Pick','Warhammer','Whip','Blowgun','Hand Crossbow','Heavy Crossbow','Longbow','Net']

    x = 1
    for x in range (x,5):
        if x < 5:
            dnd_skills.skill_addition(weapon_list,dnd_dict.character_dict['Weapon_Prof'])
            x+=5
            continue
        elif x == 5:
            break

def wood_elf_magic():
    feature = """
Wood Elf Magic
Prerequisite: Elf (wood)

You learn the magic of the primeval woods, which are revered and protected by your people. You learn one druid cantrip of your choice. You also learn the longstrider and pass without trace spells, each of which you can cast once without expending a spell slot. You regain the ability to cast these two spells in this way when you finish a long rest. Wisdom is your spellcasting ability for all three spells."""

    print(feature)
    dnd_dict.character_dict["features"]['wood_elf_magic'] = feature
    dnd_dict.character_dict["feats"]['wood_elf_magic'] = 'Wood Elf Magic'
    dnd_skills.spell_add(dnd_magic.druid_cantrip,dnd_dict.character_dict['spells']['cantrips'],dnd_dict.character_dict['special_spells']['racial_spells'])
    dnd_dict.character_dict['spells']['longstrider'] = 'Longstrider'
    dnd_dict.character_dict['special_spells']['racial_spells']['longstrider'] = 'Longstrider'
    dnd_dict.character_dict['spells']['second']['pass_without_trace'] = 'Pass Without Trace'
    dnd_dict.character_dict['special_spells']['racial_spells']['pass_without_trace'] = 'Pass Without Trace'
    spell_attack = ((dnd_dict.character_dict["Stats"]["wisdom"]['mod']) + dnd_dict.character_dict['prof_bonus'])
    dnd_dict.character_dict["spell_modifier"]['wisdom']['attack'] = spell_attack
    spell_save = ((dnd_dict.character_dict["Stats"]["wisdom"]['mod']) + dnd_dict.character_dict['prof_bonus'] + 8)
    dnd_dict.character_dict["spell_modifier"]['wisdom']['save'] = spell_save

def boon_of_combat_prowess():
    feature = """Boon of Combat Prowess

When you miss with a melee weapon attack, you can choose to hit instead. Once you use this boon, you can't use it again until you finish a short rest."""

    print(feature)
    dnd_dict.character_dict["features"]['boon_of_combat_prowess'] = feature
    dnd_dict.character_dict["boon"]['boon_of_combat_prowess'] = 'Boon of Combat Prowess'

def boon_of_dimensional_travel():
    feature = """Boon of Dimensional Travel

As an action, you can cast the Misty Step spell, without using a spell slot or any components. Once you do so, you can't use this boon again until you finish a short rest."""

    print(feature)
    dnd_dict.character_dict["features"]['boon_of_dimensional_travel'] = feature
    dnd_dict.character_dict["boon"]['boon_of_dimensional_travel'] = 'Boon of Dimensional Travel'

def boon_of_fate():
    feature = """Boon of Fate

When another creature that you can see within 60 feet of you makes an ability check, an attack roll, or a saving throw, you can roll a d10 and apply the result as a bonus or penalty to the roll. Once you use this boon, you can't use it again until you finish a short rest."""

    print(feature)
    dnd_dict.character_dict["features"]['boon_of_fate'] = feature
    dnd_dict.character_dict["boon"]['boon_of_fate'] = 'Boon of Fate'

def boon_of_fortitude():
    feature = """Boon of Fortitude

Your hit point maximum increases by 40."""

    print(feature)
    dnd_dict.character_dict["features"]['boon_of_fortitude'] = feature
    dnd_dict.character_dict["boon"]['boon_of_fortitude'] = 'Boon of Fortitude'
    dnd_dict.character_dict['hp'] += 40

def boon_of_high_magic():
    feature = """Boon of High Magic

You gain one 9th-level spell slot, provided that you already have one."""

    print(feature)
    dnd_dict.character_dict["features"]['boon_of_high_magic'] = feature
    dnd_dict.character_dict["boon"]['boon_of_high_magic'] = 'Boon of High Magic'
    dnd_dict.character_dict['spell_slots']['ninth'] += 1

def boon_of_immortality():
    feature = """Boon of Immortality

You stop aging. You are immune to any effect that would age you, and you can't die from old age."""

    print(feature)
    dnd_dict.character_dict["features"]['boon_of_immortality'] = feature
    dnd_dict.character_dict["boon"]['boon_of_immortality'] = 'Boon of Immortality'

def boon_of_invincibility():
    feature = """Boon of Invincibility

When you take damage from any source, you can reduce that damage to 0. Once you use this boon, you can't use it again until you finish a short rest."""

    print(feature)
    dnd_dict.character_dict["features"]['boon_of_invincibility'] = feature
    dnd_dict.character_dict["boon"]['boon_of_invincibility'] = 'Boon of Invincibility'

def boon_of_irresistible_offense():
    feature = """Boon of Irresistible Offense

You can bypass the damage resistances of any creature."""

    print(feature)
    dnd_dict.character_dict["features"]['boon_of_irresistible_offense'] = feature
    dnd_dict.character_dict["boon"]['boon_of_irresistible_offense'] = 'Boon of Irresistible Offense'

def boon_of_luck():
    feature = """Boon of Luck

You can add a d10 roll to any ability check, attack roll, or saving throw you make. Once you use this boon, you can't use it again until you finish a short rest."""

    print(feature)
    dnd_dict.character_dict["features"]['boon_of_luck'] = feature
    dnd_dict.character_dict["boon"]['boon_of_luck'] = 'Boon of Luck'

def boon_of_magic_resistance():
    feature = """Boon of Magic Resistance

You have advantage on saving throws against spells and other magical effects."""

    print(feature)
    dnd_dict.character_dict["features"]['boon_of_magic_resistance'] = feature
    dnd_dict.character_dict["boon"]['boon_of_magic_resistance'] = 'Boon of Magic Resistance'

def boon_of_peerless_aim():
    feature = """Boon of Peerless Aim

You can give yourself a +20 bonus to a ranged attack roll you make. Once you use this boon, you can't use it again until you finish a short rest."""

    print(feature)
    dnd_dict.character_dict["features"]['boon_of_peerless_aim'] = feature
    dnd_dict.character_dict["boon"]['boon_of_peerless_aim'] = 'Boon of Peerless Aim'

def boon_of_perfect_health():
    feature = """Boon of Perfect Health

You are immune to all diseases and poisons, and you have advantage on Constitution saving throws."""

    print(feature)
    dnd_dict.character_dict["features"]['boon_of_perfect_health'] = feature
    dnd_dict.character_dict["boon"]['boon_of_perfect_health'] = 'Boon of Perfect Health'

def boon_of_planar_travel():
    feature = """Boon of Planar Travel

When you gain this boon, choose a plane of existence other than the Material Plane. You can now use an action to cast the Plane Shift spell (no spell slot or components required), targeting yourself only, and travel to the chosen plane, or from that plane back to the Material Plane. Once you use this boon, you can't use it again until you finish a short rest."""

    print(feature)
    dnd_dict.character_dict["features"]['boon_of_planar_travel'] = feature
    dnd_dict.character_dict["boon"]['boon_of_planar_travel'] = 'Boon of Planar Travel'

def boon_of_quick_casting():
    feature = """Boon of Quick Casting

Choose one of your spells of 1st through 3rd level that has a casting time of 1 action. That spell's casting time is now 1 bonus action for you."""

    print(feature)
    dnd_dict.character_dict["features"]['boon_of_quick_casting'] = feature
    dnd_dict.character_dict["boon"]['boon_of_quick_casting'] = 'Boon of Quick Casting'

def boon_of_recovery():
    feature = """Boon of Recovery

You can use a bonus action to regain a number of hit points equal to half your hit point maximum. Once you use this boon, you can't use it again until you finish a long rest."""

    print(feature)
    dnd_dict.character_dict["features"]['boon_of_recovery'] = feature
    dnd_dict.character_dict["boon"]['boon_of_recovery'] = 'Boon of Recovery'

def boon_of_resilience():
    feature = """Boon of Resilience

You have resistance to bludgeoning, piercing, and slashing damage from nonmagical weapons."""

    print(feature)
    dnd_dict.character_dict["features"]['boon_of_resilience'] = feature
    dnd_dict.character_dict["boon"]['boon_of_resilience'] = 'Boon of Resilience'

def boon_of_skill_proficiency():
    feature = """Boon of Skill Proficiency

You gain proficiency in all skills."""

    print(feature)
    dnd_dict.character_dict["features"]['boon_of_skill_proficiency'] = feature
    dnd_dict.character_dict["boon"]['boon_of_skill_proficiency'] = 'Boon of Skill Proficiency'
    all_skills = {'acrobatics':'Acrobatics','animal_handling':'Animal Handling','arcana':'Arcana','athletics':'Athletics','deception':'Deception','history':'History','insight':'Insight','intimidation':'Intimidation','investigation':'Investigation','medicine':'Medicine','nature':'Nature','perception':'Perception','performance':'Performance','persuasion':'Persuasion','religion':'Religion','sleight_of_hand':'Sleight of Hand','stealth':'Stealth','survival':'Survival'}    
    dnd_dict.character_dict['skill_prof'].update(all_skills)
# Get rid of any skill proficiencies from Beguiling Influence
    if 'beguiling_influence' in dnd_dict.character_dict['features']:
        dnd_dict.character_dict['influence'] = {}


    if 'persuasion' not in dnd_dict.character_dict['skill_prof'] or dnd_dict.character_dict['expertise']:
        dnd_dict.character_dict['influence']['persuasion'] = 'Persuasion'

def boon_of_speed():
    feature = """Boon of Speed

Your walking speed increases by 30 feet. In addition, you can use a bonus action to take the Dash or Disengage action. Once you do so, you can't do so again until you finish a short rest."""

    print(feature)
    dnd_dict.character_dict["features"]['boon_of_speed'] = feature
    dnd_dict.character_dict["boon"]['boon_of_speed'] = 'Boon of Speed'

    dnd_dict.character_dict['speed'] += 30
    if 'roving' in dnd_dict.character_dict['features']:
        dnd_dict.character_dict['climb_speed'] == dnd_dict.character_dict['speed']
        dnd_dict.character_dict['swim_speed'] == dnd_dict.character_dict['speed']
    if dnd_dict.character_dict['unarmored_movement_barbarian'] > 0:
        dnd_dict.character_dict['unarmored_movement_barbarian'] += 30
    if dnd_dict.character_dict['unarmored_movement_monk'] > 0:
        dnd_dict.character_dict['unarmored_movement_monk'] += 30

def boon_of_spell_mastery():
    feature = """Boon of Spell Mastery

Choose one 1st-level sorcerer, warlock, or wizard spell that you can cast. You can now cast that spell at its lowest level without expending a spell slot."""

    print(feature)
    dnd_dict.character_dict["features"]['boon_of_spell_mastery'] = feature
    dnd_dict.character_dict["boon"]['boon_of_spell_mastery'] = 'Boon of Spell Mastery'

def boon_of_spell_recall():
    feature = """Boon of Spell Recall

You can cast any spell you know or have prepared without expending a spell slot. Once you do so, you can't use this boon again until you finish a long rest."""

    print(feature)
    dnd_dict.character_dict["features"]['boon_of_spell_recall'] = feature
    dnd_dict.character_dict["boon"]['boon_of_spell_recall'] = 'Boon of Spell Recall'

def boon_of_the_fire_soul():
    feature = """Boon of the Fire Soul

You have immunity to fire damage. You can also cast Burning Hands (save DC 15) at will, without using a spell slot or any components."""

    print(feature)
    dnd_dict.character_dict["features"]['boon_of_the_fire_soul'] = feature
    dnd_dict.character_dict["boon"]['boon_of_the_fire_soul'] = 'Boon of the Fire Soul'

def boon_of_the_night_spirit():
    feature = """Boon of the Night Spirit

While completely in an area of dim light or darkness, you can become invisible as an action. You remain invisible until you take an action or a reaction."""

    print(feature)
    dnd_dict.character_dict["features"]['boon_of_the_night_spirit'] = feature
    dnd_dict.character_dict["boon"]['boon_of_the_night_spirit'] = 'Boon of the Night Spirit'

def boon_of_the_stormborn():
    feature = """Boon of the Stormborn

You have immunity to lightning and thunder damage. You can also cast Thunderwave (save DC 15) at will, without using a spell slot or any components."""

    print(feature)
    dnd_dict.character_dict["features"]['boon_of_the_stormborn'] = feature
    dnd_dict.character_dict["boon"]['boon_of_the_stormborn'] = 'Boon of the Stormborn'

def boon_of_the_unfettered():
    feature = """Boon of the Unfettered

You have advantage on ability checks made to resist being grappled. In addition, you can use an action to automatically escape a grapple or free yourself of restraints of any kind."""

    print(feature)
    dnd_dict.character_dict["features"]['boon_of_the_unfettered'] = feature
    dnd_dict.character_dict["boon"]['boon_of_the_unfettered'] = 'Boon of the Unfettered'

def boon_of_truesight():
    feature = """Boon of Truesight

You have truesight out to a range of 60 feet."""

    print(feature)
    dnd_dict.character_dict["features"]['boon_of_truesight'] = feature
    dnd_dict.character_dict["boon"]['boon_of_truesight'] = 'Boon of Truesight'

def boon_of_undetectability():
    feature = """Boon of Undetectability

You gain a +10 bonus to Dexterity (Stealth) checks, and you can't be detected or targeted by divination magic, including scrying sensors."""

    print(feature)
    dnd_dict.character_dict["features"]['boon_of_undetectability'] = feature
    dnd_dict.character_dict["boon"]['boon_of_undetectability'] = 'Boon of Undetectability'






































































































