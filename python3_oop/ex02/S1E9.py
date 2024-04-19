from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class Character

    Methods:
        die(self): Makes character die
    """
    def __init__(self,
                 name,
                 isAlive=True,
                 family_name="Duclou",
                 eyes="Rainbow",
                 hairs="bald"):
        """Character class constructor

        Args:
            name (_type_): name of the character
            isAlive (bool, optional): define if character is alive or not.
                                      Defaults to True.
            family_name (str, optional): set family name. Defaults to "Duclou".
            eyes (str, optional): set eyes color. Defaults to "Rainbow".
            hairs (str, optional): set hairs color. Defaults to "bald".
        """
        self.first_name = name
        self.is_alive = isAlive
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    @abstractmethod
    def die(self):
        """Makes character dies
        """
        pass


class Stark(Character):
    """Stark class character

    Args:
        Character (_type_): abstract class to use for methods is_alive and die
    """
    def die(self):
        """Method to kill Stark character
        """
        self.is_alive = False
