class calculator:
    """Calculator class"""
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Do scalar product on two list and print result"""
        result = 0

        for item1, item2 in zip(V1, V2):
            result += item1 * item2

        print(result)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Do addition on two list and print result in one list"""
        print([float(item1 + item2) for item1, item2 in zip(V1, V2)])

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Do subtraction on two list and print result in one list"""
        print([float(item1 - item2) for item1, item2 in zip(V1, V2)])
