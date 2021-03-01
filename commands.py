# Course: CS 30
# Period: 1
# Date Created: 21/02/28
# Date Last Modified: 21/02/28
# Name: Jack Anderson
# Description: Functions for dealing with commands


class Commands:
    def __init__(self):
        self.commands_list = {'up': 'move up',
                              'down': 'move down',
                              'right': 'move right',
                              'left': 'move left',
                              'pick up': 'pick up item',
                              'give': 'give item to nearby character',
                              'talk': 'talk to nearby character',
                              'follow': 'ask nearby character to follow',
                              'inventory': 'checks player inventory',
                              'quit': 'quit the game'
                              }

    def print_commands(self):
        """Prints available commands"""
        print("\nAvailable commands:")
        for command, command_desc in self.commands_list.items():
            print(f"{command} - {command_desc}")
