import doctest


class Bed:
    def __init__(self, size: str, material: str, weight_capacity: float):
        """
        Кровать

        :param size: Размер кровати (односпальная, двуспальная, двухъярусная)
        :param material: Материал кровати (дуб, красное дерево, ясень)
        :param weight_capacity: Максимальная нагрузка на кровать в килограммах

        Примеры:
        >>> bed = Bed("двуспальная", "дуб", 200.0)
        """
        if size not in ["односпальная", "двуспальная", "двухъярусная"]:
            raise ValueError("Размер кровати должен быть: 'односпальная', 'двуспальная' или 'двухъярусная'.")
        if material not in ["дуб", "красное дерево", "ясень"]:
            raise ValueError("Материал должен быть: 'дуб', 'красное дерево' или 'ясень'.")
        if not isinstance(weight_capacity, (int, float)) or weight_capacity <= 0:
            raise ValueError("Максимальная нагрузка должна быть положительным числом.")

        self.size = size
        self.material = material
        self.weight_capacity = weight_capacity

    def fold(self) -> str:
        """
        Сложить кровать, если она складная

        :return: Строка с сообщением о результате

        Примеры:
        >>> bed = Bed("двухъярусная", "ясень", 150.0)
        >>> bed.fold()
        'Кровать сложена.'
        """
        return "Кровать сложена."

    def clean(self) -> str:
        """
        Почистить кровать

        :return: Строка с сообщением о результате

        Примеры:
        >>> bed = Bed("двуспальная", "красное дерево", 200.0)
        >>> bed.clean()
        'Кровать почищена и убрана.'
        """
        return "Кровать почищена и убрана."

    def check_stability(self) -> bool:
        """
        Проверить устойчивость кровати

        :return: True, если кровать устойчива, иначе False

        Примеры:
        >>> bed = Bed("двуспальная", "дуб", 300.0)
        >>> bed.check_stability()
        True
        """
        return True


if __name__ == "__main__":
    doctest.testmod()
