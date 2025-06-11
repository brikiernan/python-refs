from enemy import Enemy
from zombie import Zombie

from ogre import Ogre
from hero import Hero
from weapon import Weapon


def battle(e1: Enemy, e2: Enemy):
    """Polymorphic battle function that takes two enemies."""
    print(
        f"A battle begins between {e1.get_type_of_enemy()} and {e2.get_type_of_enemy()}!"
    )
    e1.talk()
    e2.talk()

    while e1.health_points > 0 and e2.health_points > 0:
        print("--- New Round ---")
        e1.walk_forward()
        e2.walk_forward()
        print("-------------")
        e1.special_attack()
        e2.special_attack()
        print(
            f"{e1.get_type_of_enemy()} has {e1.health_points} health points left."
        )
        print(
            f"{e2.get_type_of_enemy()} has {e2.health_points} health points left."
        )
        print("-------------")
        e2.attack()
        e1.health_points -= e2.attack_damage
        e1.attack()
        e2.health_points -= e1.attack_damage

    print("------ Battle Over -------")
    print(
        f"{e1.get_type_of_enemy()} has {e1.health_points} health points left."
    )
    print(
        f"{e2.get_type_of_enemy()} has {e2.health_points} health points left."
    )

    if e1.health_points > 0:
        print(f"{e1.get_type_of_enemy()} wins the battle!")
    else:
        print(f"{e2.get_type_of_enemy()} wins the battle!")


def hero_battle(hero: Hero, enemy: Enemy):

    print(f"A battle begins between a hero and {enemy.get_type_of_enemy()}!")
    hero.talk()
    enemy.talk()

    while hero.health_points > 0 and enemy.health_points > 0:

        print("--- New Round ---")
        hero.walk_forward()
        enemy.walk_forward()
        # enemy.special_attack()
        print("-------------")
        hero.attack()
        hero.health_points -= enemy.attack_damage
        print(f"Hero has {hero.health_points} health points left.")
        enemy.attack()
        enemy.health_points -= hero.attack_damage
        print(
            f"{enemy.get_type_of_enemy()} has {enemy.health_points} health points left."
        )

    print("------ Battle Over -------")
    print(f"Hero has {hero.health_points} health points left.")
    print(
        f"{enemy.get_type_of_enemy()} has {enemy.health_points} health points left."
    )

    if hero.health_points > 0:
        print("Hero wins the battle!")
    else:
        print(f"{enemy.get_type_of_enemy()} wins the battle!")


battle(Zombie(), Ogre())

zombie = Zombie()
hero = Hero()
weapon = Weapon("Sword", 5)
hero.weapon = weapon
hero.equip_weapon()

hero_battle(hero, zombie)

hero_battle(hero, Ogre())
