
class Character:
    def __init__(self, name, origin):
        self.name = name
        self.origin = origin

    def describe(self):
        return f"{self.name} comes from {self.origin}."

#
class Superhero(Character):
    def __init__(self, name, origin, power, alias):
        super().__init__(name, origin)
        self.power = power
        self.alias = alias

    def use_power(self):
        return f"{self.alias} uses {self.power} to save the day!"

    def describe(self):
        return f"{self.alias} ({self.name}) from {self.origin} has the power of {self.power}."

#Example usage
hero1 = Superhero("Clark Kent", "Krypton", "Super Strength", "Superman")
hero2 = Superhero("Diana Prince", "Themyscira", "Combat Mastery", "Wonder Woman")

print(hero1.describe())
print(hero1.use_power())
print(hero2.describe())
print(hero2.use_power())
