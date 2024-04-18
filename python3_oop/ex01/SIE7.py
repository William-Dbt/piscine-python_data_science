from SIE9 import Character


class Baratheon(Character):
    def __init__(self, name, isAlive=True):
        super().__init__(name, isAlive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        self.is_alive = False

# class Lannister(Character):
#     def __init__(self, name, isAlive=True):
#         super().__init()


Robert = Baratheon("Robert")
print(Robert.__dict__)
print(Robert.__str__)