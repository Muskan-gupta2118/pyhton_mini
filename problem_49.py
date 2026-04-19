# method overriding
class Avengers:
    def attack(self):
        print("Avenger attacks normally ⚔️")


class Ironman(Avengers):
    def attack(self):   # overriding parent method
        print("Ironman attacks with laser 🔥")


# objects
a = Avengers()
i = Ironman()

a.attack()   # parent method
i.attack()   # overridden method