class Appartament:
    #конструктор;
    def __init__(self, address, square, number_of_rooms, rent_price, description):
        self.status = "Свободна"
        self.address = address
        self.square = square
        self.number_of_rooms = number_of_rooms
        self.rent_price = rent_price
        self.description = description

    def svobodna(self):
        self.status = "Свободна"

    def sdana(self):
        self.status = "Сдана"

    def __str__(self):
        return self.status + "-- Адресс: " + str(self.address) + "; " + "Площадь: " + str(self.square) + "; " + "Количество комнат: " + str(self.number_of_rooms) + "; " + "Стоимость за сутки: " + str(self.rent_price) + "; " + "Описание: " + str(self.description)

