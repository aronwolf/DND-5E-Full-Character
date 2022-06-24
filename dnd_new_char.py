#!/usr/bin/python3
import os, stat_roller, dnd_features, dnd_language, dnd_tools, dnd_dict, dnd_skills, dnd_race, dnd_class_select, dnd_class, dnd_background, dnd_display, dnd_save_load, json

def initial_char():


#    dnd_save_load.load_choice()


# Set initial stats
    stat_roller.stat_selection()

# Choose Race
    dnd_race.player_race()

# Choose Background
    dnd_background.player_background()

# Choose Class
    dnd_class_select.player_class()

# Save the data
    dnd_save_load.save_display()

# Display the results
    dnd_display.char_display()

if __name__ == '__main__':
    initial_char()
