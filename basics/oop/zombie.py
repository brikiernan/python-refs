from enemy import Enemy
import random


class Zombie(Enemy):
    """A class representing a Zombie enemy, inheriting from Enemy."""

    def __init__(self):
        super().__init__("Zombie")

    def talk(self):
        print(f"{self.get_type_of_enemy()} groans menacingly!")

    def spread_infection(self):
        print(f"{self.get_type_of_enemy()} spreads a deadly infection!")

    def special_attack(self):
        print(
            f"{self.get_type_of_enemy()} lunges at you with its decaying claws!"
        )
        did_special_attack_work = random.random() < 0.5
        if did_special_attack_work:
            self.health_points += 2
            print(f"{self.get_type_of_enemy()} regains 2 health points!")
