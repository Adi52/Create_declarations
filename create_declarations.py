from tkinter import *
from tkinter import messagebox
from CreateDeclaration import CreateDeclaration

root = Tk()
root.title('  Generowanie deklaracji postoju jachtu - NCŻ')


windowWidth = 420
windowHeight = 570

# Gets both half the screen width/height and window width/height
positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2 - 50)

# Positions the window in the center of the page.
root.geometry("+{}+{}".format(positionRight, positionDown))

# Display icon
root.tk.call('wm', 'iconphoto', root.w, PhotoImage(file='icon.ico'))


def clear_text_boxes():
    options = [parking_place, date, registration_number, name_yacht, home_port, yacht_length, yacht_width,
               owner_details_name, owner_details_address, commissioning_body_name, commissioning_body_address,
               commissioning_body_tel, commissioning_body_email, commissioning_body_nip, chip_card]

    for option in options:
        option.delete(0, END)
    yacht_type_var.set('')
    parking_peroid_from_var.set('')
    parking_peroid_to_var.set('')


def submit():
    owner_details = {'name': owner_details_name.get(), 'address': owner_details_address.get()}
    parking_peroid = {'from': parking_peroid_from_var.get(), 'to': parking_peroid_to_var.get()}
    commissioning_body = {'name': commissioning_body_name.get(), 'address': commissioning_body_address.get(),
                          'tel': commissioning_body_tel.get(), 'e-mail': commissioning_body_email.get(),
                          'nip': commissioning_body_nip.get()}

    try:
        test = CreateDeclaration(parking_place.get(), date.get(), name_yacht.get(), registration_number.get(),
                                 home_port.get(), float(yacht_length.get()), float(yacht_width.get()),
                                 yacht_type_var.get(), owner_details, commissioning_body, parking_peroid,
                                 chip_card.get())

        test.create_document()
        messagebox.showinfo("", 'Stworzono deklaracje oraz dodano klienta do bazy!')
        clear_text_boxes()
    except ValueError:
        message = "Wprowadzono nieprawidłowe dane!\n Długość oraz szerokość jachtu musi być wpisana bez dodatkowych znaków!"
        messagebox.showerror("Błąd", message)


def correct_my(value_if_allowed):
    # Entry just float numbers to length and width
    if value_if_allowed == "":
        return True

    try:
        float(value_if_allowed)
        return True

    except ValueError:
        return False


parking_peroid_from_var = StringVar(root)
parking_peroid_to_var = StringVar(root)
yacht_type_var = StringVar(root)

yacht_data_label = Label(root, text='Dane jachtu')
yacht_data_label.grid(row=0, column=0, columnspan=2, padx=20, pady=(5, 0))

parking_place_label = Label(root, text='Miejsce postoju')
parking_place_label.grid(row=1, column=0, padx=20)
parking_place = Entry(root, width=30)
parking_place.grid(row=1, column=1)

date_label = Label(root, text='Data')
date_label.grid(row=2, column=0, padx=20)
date = Entry(root, width=30)
date.grid(row=2, column=1, padx=20)

name_yacht_label = Label(root, text='Nazwa jachtu')
name_yacht_label.grid(row=3, column=0, padx=20)
name_yacht = Entry(root, width=30)
name_yacht.grid(row=3, column=1, padx=20)

registration_number_label = Label(root, text='Numer rejestracyjny')
registration_number_label.grid(row=4, column=0, padx=20)
registration_number = Entry(root, width=30)
registration_number.grid(row=4, column=1, padx=20)

home_port_label = Label(root, text='Port macierzysty')
home_port_label.grid(row=5, column=0, padx=20)
home_port = Entry(root, width=30)
home_port.grid(row=5, column=1, padx=20)

yacht_length_label = Label(root, text='Długość jachtu')
yacht_length_label.grid(row=6, column=0, padx=20)
yacht_length = Entry(root, width=30)
yacht_length.grid(row=6, column=1, padx=20)
# Limit entry to numbers
reg = root.register(correct_my)
yacht_length.config(validate='key', validatecommand=(reg, '%P'))

yacht_width_label = Label(root, text='Szerokość')
yacht_width_label.grid(row=7, column=0, padx=20)
yacht_width = Entry(root, width=30)
yacht_width.grid(row=7, column=1, padx=20)
yacht_width.config(validate='key', validatecommand=(reg, '%P'))

yacht_type_label = Label(root, text='Typ jachtu')
yacht_type_label.grid(row=8, column=0, padx=20)
yacht_type = OptionMenu(root, yacht_type_var, 'motorowy', 'żaglowy')
yacht_type.grid(row=8, column=1, padx=20)

owner_details_label0 = Label(root, text='Dane właściciela')
owner_details_label0.grid(row=9, column=0, columnspan=2, padx=20)

owner_details_name_label = Label(root, text='Imię i nazwisko')
owner_details_name_label.grid(row=10, column=0, padx=20)
owner_details_name = Entry(root, width=30)
owner_details_name.grid(row=10, column=1, padx=20)

owner_details_address_label = Label(root, text='Adres')
owner_details_address_label.grid(row=11, column=0, padx=20)
owner_details_address = Entry(root, width=30)
owner_details_address.grid(row=11, column=1, padx=20)

commissioning_body0_label = Label(root, text='Podmiot zlecający')
commissioning_body0_label.grid(row=12, column=0, columnspan=2, padx=20)

commissioning_body_name_label = Label(root, text='Nazwa firmy')
commissioning_body_name_label.grid(row=13, column=0, padx=20)
commissioning_body_name = Entry(root, width=30)
commissioning_body_name.grid(row=13, column=1, padx=20)

commissioning_body_address_label = Label(root, text='Adres')
commissioning_body_address_label.grid(row=14, column=0, padx=20)
commissioning_body_address = Entry(root, width=30)
commissioning_body_address.grid(row=14, column=1, padx=20)

commissioning_body_tel_label = Label(root, text='Nr telefonu')
commissioning_body_tel_label.grid(row=15, column=0, padx=20)
commissioning_body_tel = Entry(root, width=30)
commissioning_body_tel.grid(row=15, column=1, padx=20)

commissioning_body_email_label = Label(root, text='Adres e-mail')
commissioning_body_email_label.grid(row=16, column=0, padx=20)
commissioning_body_email = Entry(root, width=30)
commissioning_body_email.grid(row=16, column=1, padx=20)

commissioning_body_nip_label = Label(root, text='NIP klubu/stowarzyszenia')
commissioning_body_nip_label.grid(row=17, column=0, padx=20)
commissioning_body_nip = Entry(root, width=30)
commissioning_body_nip.grid(row=17, column=1, padx=20)

parking_peroid0_label = Label(root, text='Okres postoju')
parking_peroid0_label.grid(row=18, column=0, columnspan=2, padx=20)

parking_peroid_from_label = Label(root, text='Od')
parking_peroid_from_label.grid(row=19, column=0, padx=20)
parking_peroid_from = OptionMenu(root, parking_peroid_from_var, '01.05.2020', '01.11.2020')
parking_peroid_from.grid(row=19, column=1, padx=20)

parking_peroid_to_label = Label(root, text='Do')
parking_peroid_to_label.grid(row=20, column=0, padx=20)
parking_peroid_to = OptionMenu(root, parking_peroid_to_var, '31.10.2020', '30.04.2021')
parking_peroid_to.grid(row=20, column=1, padx=20)

chip_card_label = Label(root, text='Karta chipowa (szt.)')
chip_card_label.grid(row=21, column=0, padx=20)
chip_card = Entry(root, width=30)
chip_card.grid(row=21, column=1, padx=20)

create_button = Button(root, text='Generuj', width=53, height=3, command=submit)
create_button.grid(row=22, column=0, columnspan=2, padx=20, pady=10)

root.mainloop()


# Dodaj zapis najpotrzebniejszych danych w tabeli