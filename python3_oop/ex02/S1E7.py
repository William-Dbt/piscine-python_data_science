from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self,
                 name,
                 isAlive=True,
                 family_name="Baratheon",
                 eyes="brown",
                 hairs="dark"):
        """Baratheon class constructor

        Args:
            name (_type_): name of baratheon
            isAlive (bool, optional): define if character is alive or not.
                                      Defaults to True.
        """
        super().__init__(name, isAlive, family_name, eyes, hairs)

    def die(self):
        """Makes character dies
        """
        self.is_alive = False

    def __str__(self) -> str:
        """Bound __str__ method to return a string

        Returns:
            str: string to show
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        """Bound __repr__ method to return a string

        Returns:
            str: result of __str__ method
        """
        return self.__str__()


class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(self,
                 name,
                 isAlive=True,
                 family_name="Lannister",
                 eyes="blue",
                 hairs="light"):
        """Lannister class constructor

        Args:
            name (_type_): name of lannister
            isAlive (bool, optional): define if character is alive or not.
                                      Defaults to True.
        """
        super().__init__(name, isAlive, family_name, eyes, hairs)

    def die(self):
        """Makes character dies"""
        self.is_alive = False

    @classmethod
    def create_lannister(cls, name, isAlive=True):
        """Classmethod to create a lannister char

        Args:
            name (_type_): name of the character
            isAlive (bool, optional): define if character is alive or not.
                                      Defaults to True.

        Returns:
            _type_: instance of Lannister class
        """
        return (cls(name, isAlive))

    def __str__(self) -> str:
        """Bound __str__ method to return a string

        Returns:
            str: string to show
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        """Bound __repr__ method to return a string

        Returns:
            str: result of __str__ method
        """
        return self.__str__()
