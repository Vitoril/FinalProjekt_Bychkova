from tkinter import Entry

from Appartaments.Appataments import Appartament
from tkinter import *
if __name__ == '__main__':
    root = Tk()
    root.title("Реестр средств измерний")
    root.geometry("600x500")

    label_address = Label(text="Введите адресс")
    label_address.pack()
    entry_address = Entry()
    entry_address.pack()

    label_square = Label(text="Площадь квартиры")  # текстовая метка
    label_square.pack()  # размещение метки в окне
    entry_square = Entry()  # поле ввода
    entry_square.pack()  # размещение поля ввода в окне

    label_number_of_rooms = Label(text="Количество комнат")  # текстовая метка
    label_number_of_rooms.pack()  # размещение метки в окне
    entry_number_of_rooms = Entry()  # поле ввода
    entry_number_of_rooms.pack()  # размещение поля ввода в окне

    label_rent_price = Label(text="Стоимость аренды за сутку")  # текстовая метка
    label_rent_price.pack()  # размещение метки в окне
    # поле ввода для адреса
    entry_rent_price = Entry()  # поле ввода
    entry_rent_price.pack()  # размещение поля ввода в окне

    label_description = Label(text="Описание квартиры")  # текстовая метка
    label_description.pack()  # размещение метки в окне
    # поле ввода для адреса
    entry_description = Entry()  # поле ввода
    entry_description.pack()  # размещение поля ввода в окне

    def add_app():
        address = entry_address.get()
        square = entry_square.get()
        number_of_rooms = entry_number_of_rooms.get()
        rent_price = entry_rent_price.get()
        description = entry_description.get()
        appartaments = Appartament(address, square, number_of_rooms, rent_price, description)

        list_appart.append(appartaments)
        list_appart_var.set(list_appart)

    bth_add_Si = Button(text="Добавить квартиру", command=add_app)
    bth_add_Si.pack()

    list_appart = []
    list_appart_var = Variable(value=list_appart)
    appart_listbox = Listbox(width=50, listvariable=list_appart_var)
    appart_listbox.pack()


    def delete():
        index = appart_listbox.curselection()
        list_appart.remove(list_appart[index[0]])
        list_appart_var.set(list_appart)

    def sv():
        index = appart_listbox.curselection()
        list_appart[index[0]].svobodna()
        list_appart_var.set(list_appart)


    def sd():
        index = appart_listbox.curselection()
        list_appart[index[0]].sdana()
        list_appart_var.set(list_appart)

    bth_add_Si = Button(text="Удалить", command=delete)
    bth_add_Si.pack()

    bth_add_Si = Button(text="Свободна", command=sv)
    bth_add_Si.pack()

    bth_add_Si = Button(text="Сдана", command=sd)
    bth_add_Si.pack()

    root.mainloop()
