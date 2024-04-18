from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class Character

    Methods:
        is_alive(self) -> bool
        die(self)
    """
    def __init__(self, name, isAlive=True):
        """Character class constructor

        Args:
            name (_type_): name of the character
            isAlive (bool, optional): define if character is alive or not.
                                      Defaults to True.
        """
        self.first_name = name
        self.is_alive = isAlive

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
