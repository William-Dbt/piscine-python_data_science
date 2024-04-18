from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class Character

    Methods:
        is_alive(self) -> bool
        die(self)
    """
    def __init__(self, name, isAlive=True):
        """Class constructor

        Args:
            name (_type_): name of the character
            isAlive (bool, optional): define if character is alive or not.
                                      Defaults to True.
        """
        self.first_name = name
        self.is_alive = isAlive

    @abstractmethod
    def is_alive(self) -> bool:
        """Check either character is alive or not

        Returns:
            bool: True for alive, False otherwise
        """
        pass

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
    def is_alive(self) -> bool:
        """Check if character is alive or not

        Returns:
            bool: _description_
        """
        return (True if self.is_alive else False)

    def die(self):
        """Method to kill Stark character
        """
        self.is_alive = False
