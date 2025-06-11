from weapon import Weapon


class Hero:
    def __init__(
        self,
        health_points: int = 10,
        attack_damage: int = 1,
    ):
        self.health_points = health_points
        self.attack_damage = attack_damage
        self.is_weapon_equipped = False
        self.weapon: Weapon | None = None

    def equip_weapon(self):
        """Equip a weapon to the hero."""
        if self.weapon is not None and not self.is_weapon_equipped:
            self.attack_damage += self.weapon.attack_increase
            self.is_weapon_equipped = True
            print(
                f"Equipped {self.weapon.weapon_type}, attack damage increased to {self.attack_damage}."
            )

    def attack(self):
        """Perform an attack."""
        print(f"Hero attacks for {self.attack_damage} damage!")

    def talk(self):
        """Hero talks."""
        print("I am the hero, ready to fight for justice!")

    def walk_forward(self):
        """Hero walks forward."""
        print("The hero strides forward with confidence.")
