# Course: CS 30
# Period: 1
# Date Created: 21/02/28
# Date Last Modified: 21/02/28
# Name: Jack Anderson
# Description: Classes for dealing with characters


# Character Class
class Character:
    """Making a normal character"""
    def __init__(self, name, description, how_to_save, conversations):
        self.name = name
        self.description = description
        self.how_to_save = how_to_save
        self.conversations = conversations

    def talk(self):
        print("hello")


class MovableCharacter(Character):
    """Making a character that can move with the player"""
    def __init__(self, name, description, how_to_save, conversations):
        super().__init__(name, description, how_to_save, conversations)
        self.following = False

    def follow(self):
        self.following = True

