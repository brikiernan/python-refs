from enemy import Enemy
import random


class Ogre(Enemy):
    """A class representing an Ogre enemy, inheriting from Enemy."""

    def __init__(self):
        super().__init__("Ogre", 20, 5)

    def talk(self):
        print(f"{self.get_type_of_enemy()} bellows loudly, Me smash you!")

    def special_attack(self):
        print(f"{self.get_type_of_enemy()} swings its club with great force!")
        did_special_attack_work = random.random() < 0.2
        if did_special_attack_work:
            self.health_points += 4
            print(f"{self.get_type_of_enemy()} regains 4 health points!")
