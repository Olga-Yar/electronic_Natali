
from src.item import Item


class Phone(Item):
    """
        Класс для представления телефонов в магазине.
        """
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        """
                Создание экземпляра класса phone.

                :param name: Название товара.
                :param price: Цена за единицу товара.
                :param quantity: Количество товара в магазине.
                :param number_of_sim: Количество сим-карт.
                """
        super().__init__(name, price, quantity)
        if number_of_sim > 0:
            self.number_of_sim = number_of_sim
        else:
            ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"
