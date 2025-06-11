class Enemy:

    def __init__(
        self,
        type_of_enemy: str = "Generic Enemy",
        health_points: int = 10,
        attack_damage: int = 1,
    ):
        self.__type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage
        print(f"A new enemy of type '{self.__type_of_enemy}' has appeared!")

    def get_type_of_enemy(self):
        return self.__type_of_enemy

    def talk(self):
        print(f"I am a {self.__type_of_enemy}. Be prepared to fight!")

    def walk_forward(self):
        print(f"{self.__type_of_enemy} moves closer to you.")

    def attack(self):
        print(
            f"{self.__type_of_enemy} attacks you for {self.attack_damage} damage!"
        )

    def special_attack(self):
        print(f"{self.get_type_of_enemy()} has no special attack defined.")
