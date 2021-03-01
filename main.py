# Course: CS 30
# Period: 1
# Date Created: 21/02/28
# Date Last Modified: 21/02/28
# Name: Jack Anderson
# Description: Making a RPG game with classes


# Importing functions
from character import Character, MovableCharacter
from commands import Commands
from items import GameItem
from g_map import GMap, Location

# Set up game
# Load Commands
game_commands = Commands()

# Creating Locations
loc_list = []
loc_list.append(Location('library', 'all the bookshelves had been push to ' +
                                    'the walls to make room for a small ' +
                                    'pentagram in the middle', 'no item',
                                    'celine', ["down", "right"]))
loc_list.append(Location('science lab', 'an old lab with rotting tables and ' +
                                        'shelves full of broken empty bottles',
                                        'dented camera', 'no character',
                                        ["down", "left", "right"]))
loc_list.append(Location('music room', 'a room with a couple of chairs and ' +
                                       'filled with multiple different ' +
                                       'kinds of instruments', 'no item',
                                       'the crying spirit', ["down", "left"]))
loc_list.append(Location('cafeteria', 'a broken-down cafeteria with rotting ' +
                                      'tables and chairs', 'pretty cane',
                                      'no character', ["up", "down", "right"]))
loc_list.append(Location('security office', 'a dark office with a desk, 9 ' +
                                            'computer monitors sat on the ' +
                                            'desk in a 3x3 stack showing ' +
                                            'static', 'no item', 'the hacker',
                                            ["up", "down", "left", "right"]))
loc_list.append(Location('office', 'an office with a nice desk and a couple ' +
                                   'of bookshelves and filing cabinets',
                                   'no item', 'the business man',
                                   ["up", "down", "Left"]))
loc_list.append(Location('empty room', 'an empty room with nothing in it ' +
                                       'but dust and two doors', 'no item',
                                       'player', ["up", "right"]))
loc_list.append(Location('gym', 'a large gym with multiple dust-covered ' +
                                'bleachers', 'pretty music box',
                                'no character', ["up", "left", "right"]))
loc_list.append(Location('classroom', 'a room with one large desk and ' +
                                      'multiple smaller desks facing a ' +
                                      'chalk board and covered in dust',
                                      'no item', 'damien', ["up", "left"]))

# Creating Characters
game_chara = {"celine": MovableCharacter('celine', 'the sister of damien',
                                                   'bring her to damien', ''),
              "damien": Character('damien', 'the brother of celine',
                                            'bring celine to him',
                                            ''),
              "the hacker": Character('the hacker', 'a rude hacker who is ' +
                                                    'good with computers',
                                                    'give him the dented ' +
                                                    'camera',
                                                    ''),
              "the business man": Character('the business man',
                                            'a well-dressed business man',
                                            'give him the pretty cane',
                                            ''),
              "the_crying_spirit": Character('the crying spirit',
                                             'a spirit with permanent ' +
                                             'tear streaks and a' +
                                             'knack for music',
                                             'give him the pretty ' +
                                             'music box', '')}

# Loading Items
game_items = {"dented camera": GameItem('dented camera',
                                        'a dented video camera, looks like ' +
                                        'it has been through a lot of use'),
              "pretty cane": GameItem('pretty cane',
                                      'an ornate pretty cane with a claw ' +
                                      'holding a glass ball on the top'),
              "music box": GameItem('pretty music box',
                                    'a small white box with a red stripe ' +
                                    'going up each side and small metal ' +
                                    'crank on the one side')}

# Set up map
game_map = GMap(loc_list)

# Set up player
player_inventory = []
player_location = game_map.player_start
player_location.print_loc()

# Main game input loop
message = ''
while message != 'quit':
    message = input('Enter a command (type ? for help): ')
    if message == '?':
        game_commands.print_commands()
    elif message == 'up':
        game_map.move_direction(player_location, message)
    elif message == 'down':
        game_map.move_direction(player_location, message)
    elif message == 'right':
        game_map.move_direction(player_location, message)
    elif message == 'left':
        game_map.move_direction(player_location, message)
    elif message == 'pick up':
        print("You pick up item")
    elif message == 'give':
        print("You give item to nearby character")
    elif message == 'talk':
        print("You talk to nearby character")
    elif message == 'follow':
        print("You ask nearby character to follow you")
    elif message == 'inventory':
        player_inventory.print_inv()
    elif message == 'quit':
        print("Quitting game")
    else:
        print("Invalid Command")

