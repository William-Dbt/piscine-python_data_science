class calculator:
    def __init__(self, vector):
        self.vector = vector

    def __add__(self, object) -> None:
        self.vector = [item + object for item in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        self.vector = [item * object for item in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        self.vector = [item - object for item in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        try:
            self.vector = [item / object for item in self.vector]
        except ZeroDivisionError:
            print("Error: You cannot divide by 0")
            return

        print(self.vector)
