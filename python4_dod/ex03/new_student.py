import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate random id of 15 chars

    Returns:
        str: id of 15 chars
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Student class"""
    name: str
    surname: str
    active: bool = True
    # define login and id attributes but don't init the values, init them in
    # __post_init__ function that is called right after __init__ function
    # which is responsible of the construction of the class
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        """Post __init__ function to specify the login and id of the student
        The login match to the first letter of the name
        followed by his surname
        The id is the result of the function generate_id()
        """
        self.login = self.name[0] + self.surname
        self.id = generate_id()
