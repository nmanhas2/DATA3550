import random
import tkinter as tk 
from tkinter import messagebox #https://www.tutorialspoint.com/python/python_gui_programming.htm
import time 

# Warrior Classes
class Warrior: 
    def __init__(self, health=50, attack=5):
        self.starting_health = health
        self.health = health
        self.attack = attack
    
    def is_alive(self):       
        return self.health > 0
    
    def take_hit(self, hit_damage):
        self.health -= max(hit_damage, 0)
    
    def hit(self, defense = 0):
        return self.attack - defense

#Knight class, same as warrior but with 7 attack
class Knight(Warrior):
    def __init__(self):
        super().__init__(attack=7)

#Defender class, has defense
class Defender(Warrior):
    def __init__(self):
        super().__init__()
        self.defense = 2

#Lancer class, can pierce through opponent and hit adjacent one
class Lancer(Warrior):
    def __init__(self):
        super().__init__()

    def attack_with_piercing(self, opponent, next_opponent=None):
        # Lancer pierces and hits adjacent opponent
        if next_opponent and next_opponent.health > ((self.attack * 0.5)):
            next_opponent.take_hit(self.attack * 0.5)  # 50% damage to adjacent opponent

#Vampire class, can heal based on vampirism
class Vampire(Warrior):
    def __init__(self):
        super().__init__()
        self.vampirism = 0.5

    def hit(self, defense = 0):
        damage = self.attack - defense
        #Vampire heals damge * vampirism ratio
        self.health = min(self.health + damage * self.vampirism, self.starting_health)
        return damage

#Healer class, can heal ally based on heal attribute. Can't go beyond starting health
#of ally class type
class Healer(Warrior):
    def __init__(self):
        super().__init__(attack=0)
        self.heal = 2

    def heal_ally(self, ally):
        #Healer can heal ally
        ally.health = min(ally.health + self.heal, ally.starting_health)

#Fight simulation function
def fight(party, opponent, selected, canvas):
    round_count = 0
    class_1 = type(selected).__name__
    opp = opponent[0]
    class_2 = type(opp).__name__

    #Begin fight simulation
    while selected.is_alive() and opp.is_alive():

        ############### GUI UPDATES ########################

        round_count += 1
        print(f"Round: {round_count}")
        
        ############### PLAYER'S TURN ########################

        if isinstance(selected, Healer):
            healer_action(party, selected)
        elif isinstance(opp, Defender):
            opp.take_hit(selected.hit(opp.defense))
        else:
            opp.take_hit(selected.hit())

        #Lancer's piercing attack
        if isinstance(selected, Lancer):
            if len(opponent) > 1:
                next_opp = opponent[1]  #Attack next opponent 
                selected.attack_with_piercing(opp, next_opp)
            else:
                selected.attack_with_piercing(opp)
            

        # Check if opponent is dead
        if not opp.is_alive():
            update_canvas(canvas, selected, opp)
            messagebox.showinfo("",f"{class_2} has been defeated!")
            return True

        ############## OPPONENT's TURN #######################

        # Opponent's turn to attack
        if isinstance(opp, Healer):
            healer_action(opponent, opp)
        else:
            selected.take_hit(opp.hit())

        #Lancer's piercing attack
        if isinstance(opp, Lancer):
            if (len(party) > 1):
                next_party_member = party[party.index(selected) + 1]  #Attack next party member
                opp.attack_with_piercing(selected, next_party_member)
            else:
                opp.attack_with_piercing(selected)

        update_canvas(canvas, selected, opp)
        time.sleep(1) 

        # Check if player is dead
        if not selected.is_alive():
            update_canvas(canvas, selected, opp)
            messagebox.showinfo("", f"{class_1} has been defeated!")
            return False

    return False

# Healing action
def healer_action(party, healer):
    pos = party.index(healer)
    if pos < len(party) - 1:
        ally = party[pos + 1]
        healer.heal_ally(ally)

# Update canvas for health bars
def update_canvas(canvas, selected, opp):
    canvas.delete("all")
    # Draw health bars for player and opponent
    canvas.create_text(100, 50, text=f"{type(selected).__name__}: {selected.health}", fill="black")
    canvas.create_text(300, 50, text=f"{type(opp).__name__}: {opp.health}", fill="black")

    player_health_bar = canvas.create_rectangle(100, 70, 100 + selected.health, 90, fill="green")
    opponent_health_bar = canvas.create_rectangle(300, 70, 300 + opp.health, 90, fill="red")
    canvas.update()

# Generate party and opponent
def generate_party(party_size):
    classes = [Healer(), Warrior(), Lancer(), Defender(), Knight(), Vampire()]
    party = []
    for i in range(party_size):
        warrior = random.choice(classes)
        party.append(warrior)
        classes.remove(warrior)
    return party

# Select a warrior for battle
def select_warrior(party, canvas):
    selected_index = None
    while selected_index is None:
        try:
            selected_index = int(input(f"Select a warrior (0-{len(party) - 1}): "))
            if 0 <= selected_index < len(party):
                warrior = party[selected_index]
                return warrior
            else:
                print("Invalid selection, try again.")
                selected_index = None
        except ValueError as e:
            print(f"Error: {e}. Please type in a number.")

def main():
    again = True
    root = tk.Tk()
    root.title("Battle Simulator")
    root.geometry("500x500")

    # Set up canvas for drawing
    canvas = tk.Canvas(root, width=500, height=500)
    canvas.pack()

    # Setup a fight between two parties
    while again:
        party = [Vampire(), Lancer(), Healer()]
        opponent = [Defender(), Healer(), Defender(), Healer()]
        while len(party) > 0 and len(opponent) > 0:
            print(f"Your opponent is: {type(opponent[0]).__name__}")
            selected = select_warrior(party, canvas)
            while isinstance(selected, Healer) and isinstance(opponent[0], Healer):
                print("Can't select healer against healer.")
                selected = select_warrior(party, canvas)

            if fight(party, opponent, selected, canvas):
                print(f"Your {type(selected).__name__} won!")
                opponent.pop(0)
            else:
                print(f"Your {type(selected).__name__} lost...")
                party.pop(party.index(selected))

            if not party:
                messagebox.showinfo("Game Over", "Your party has been defeated!")
                break
            if not opponent:
                messagebox.showinfo("Game Over", "You defeated the opponents!")
                break
        if(input("Play again?(y\\n): ").upper() == "Y"):
            again = True
            canvas.delete("all")
        else:
            again = False

if __name__ == "__main__":
    main()
