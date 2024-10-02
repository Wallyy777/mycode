#!/usr/bin/pythoin3
"""
Creator: Davonta W
Sponsor: TLG
This is a text adventure game that allows players to explore different rooms,
pick up items, encounter a monster, and engage in combat. It also has a teleport
feature, and the player must find a way to survive and win. The game incorporates 
inventory management, room descriptions, and traps.

1. Multiple Rooms with descriptions and items.
2. Combat system with monster encounter and health system.
3. Teleportation system for quick room navigation.
"""

import random
import time

class Player:
    """Player class for managing player stats, inventory, and movement"""
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.strength = 10
        self.inventory = []
        self.moves = 0

    def move(self, room):
        """Increment the move counter and move to a different room"""
        self.moves += 1
        return room

    def add_item(self, item):
        """Add item to player inventory"""
        self.inventory.append(item)

    def show_inventory(self):
        """Display player's inventory"""
        if not self.inventory:
            print("Your inventory is empty.")
        else:
            print(f"Inventory: {', '.join(self.inventory)}")

    def attack(self, monster):
        """Combat system where player attacks the monster"""
        damage = random.randint(5, self.strength)
        monster.health -= damage
        print(f"You attack the monster, dealing {damage} damage!")

    def use_item(self, inventory):
        item_selection = input("Which item do you want to use?")
        for item in self.inventory:
            if item == item_selection:
                print(f'Using {item}')
                j = self.inventory.remove(item)
        if j == "apple":
            self.health += random.randint(7,15)
class Monster:
    """Monster class for managing monster health and strength"""
    def __init__(self):
        self.health = 50
        self.strength = 8

    def attack(self, player):
        """Monster attacks the player"""
        damage = random.randint(3, self.strength)
        player.health -= damage
        print(f"The monster attacks you, dealing {damage} damage!")

# Define room descriptions and items
rooms = {
    "hall": {
        "description": "A grand hall with flickering torches.",
        "directions": {"north": "kitchen", "east": "living room"},
        "items": ["torch"]
    },
    "kitchen": {
        "description": "A kitchen with a strange smell coming from the oven.",
        "directions": {"south": "hall"},
        "items": ["knife", "apple"]
    },
    "living room": {
        "description": "A cozy room with old furniture.",
        "directions": {"west": "hall", "trapdoor": "dungeon"},
        "items": ["book", "teleport stone"]
    },
    "dungeon": {
        "description": "A dark, cold dungeon with no way out.",
        "directions": {},
        "items": []
    }
}

def describe_room(room_name):
    """Function to describe the current room and available directions/items"""
    room = rooms[room_name]
    print(f"\nYou are in the {room_name}. {room['description']}")
    print(f"You see: {', '.join(room['items']) if room['items'] else 'Nothing interesting.'}")
    print(f"Exits: {', '.join(room['directions'].keys())}")

def teleport(player):
    """Teleport the player to any room"""
    room_name = input("Which room would you like to teleport to? ").lower()
    if room_name in rooms:
        print(f"Teleporting to {room_name}...")
        return player.move(room_name)
    else:
        print("That room doesn't exist!")
        return None

def encounter_monster(player):
    """Encounter the monster and engage in combat"""
    print("\nYou have encountered a monster!")
    monster = Monster()

    while player.health > 0 and monster.health > 0:
        print(f"\nPlayer Health: {player.health}, Monster Health: {monster.health}")
        action = input("Do you want to attack (a) or run (r)? ").lower()

        if action == 'a':
            player.attack(monster)
            if monster.health > 0:
                monster.attack(player)
        elif action == 'r':
            print("You ran away!")
            return False
        else:
            print("Invalid action!")
    
    if player.health <= 0:
        print("You were defeated by the monster...")
        return True  # Game over
    else:
        print("You have defeated the monster!")
        return False

def main():
    """Main game loop"""
    print("Welcome to the Adventure Game!")
    name = input("Enter your name, hero: ")
    player = Player(name)
    current_room = "hall"
    
    while player.health > 0:
        describe_room(current_room)
        action = input("What would you like to do? (go, get, teleport, inventory, quit): ").lower()
        
        if action == "go":
            direction = input("Which direction? ").lower()
            if direction in rooms[current_room]['directions']:
                next_room = rooms[current_room]['directions'][direction]
                if next_room == "dungeon":
                    print("You fall into a trapdoor and can't return!")
                    current_room = player.move(next_room)
                else:
                    current_room = player.move(next_room)
            else:
                print("You can't go that way.")
        
        elif action == "get":
            item = input("What item do you want to pick up? ").lower()
            if item in rooms[current_room]["items"]:
                player.add_item(item)
                rooms[current_room]["items"].remove(item)
                print(f"You picked up {item}!")
            else:
                print("That item is not here.")
        
        elif action == "teleport":
            room = teleport(player)
            if room:
                current_room = room
        
        elif action == "inventory":
            player.show_inventory()

        elif action == "quit":
            print("Thank you for playing!")
            break
        
        # Random monster encounter
        if random.randint(1, 5) == 1:
            game_over = encounter_monster(player)
            if game_over:
                break

    if player.health <= 0:
        print("You have died. Game over!")

if __name__ == "__main__":
    main()

