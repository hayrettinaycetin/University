class Weapons:
    def __init__(self, name, bullets, speed, base_damage, price):
        self.name = name
        self.bullets = bullets
        self.speed = speed
        self.base_damage = base_damage
        self.price = price

    def calculate_damage(self, hit_location):
        if hit_location == "headshot":
            return self.base_damage * 2
        elif hit_location == "foot_shot":
            return self.base_damage * 0.5
        else:
            return self.base_damage

# Example usage:
Weapon_1 = Weapons("KELEŞ", 30, 0.5, 10, 300)
print(Weapon_1.calculate_damage("headshot"))  # Output: 20
print(Weapon_1.calculate_damage("foot_shot"))  # Output: 5
print(Weapon_1.calculate_damage("bodyshot"))  # Output: 10