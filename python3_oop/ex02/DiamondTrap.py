from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Represent the king"""
    def __init__(self, name, isAlive=True):
        """King class constructor

        Args:
            name (str): name of the king
            isAlive (bool, optional): define if king is alive.
                                      Defaults to True.
        """
        super().__init__(name, isAlive)

    def set_eyes(self, eyesColor):
        """Set eyes colors

        Args:
            eyesColor (str): eyes color
        """
        self.eyes = eyesColor

    def set_hairs(self, hairsColor):
        """Set hairs colors

        Args:
            hairsColor (str): hairs color
        """
        self.hairs = hairsColor

    def get_eyes(self) -> str:
        """Get eyes colors

        Returns:
            str: eyes color
        """
        return self.eyes

    def get_hairs(self) -> str:
        """Get hairs colors

        Returns:
            str: hairs color
        """
        return self.hairs
