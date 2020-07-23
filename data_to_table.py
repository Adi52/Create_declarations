from openpyxl import load_workbook


class DataToTable:
    def __init__(self):
        self.main_file = 'deklaracje/rezydenci.xlsx'

    def load_data_to_table(self, commissioning_body, fee, yacht, parking_peroid, parking_place):
        wb = load_workbook(self.main_file)
        ws = wb.active
        data = [commissioning_body['nip'], commissioning_body['name'], commissioning_body['e-mail'],
                commissioning_body['tel'], fee['quarter_fee'], yacht['name'], parking_peroid['from'],
                parking_peroid['to'], parking_place, yacht['length'], yacht['width']]
        ws.append(data)
        wb.save('deklaracje/rezydenci.xlsx')


"""
TEST

yacht = {'name': 'Fordzik', 'registration_number': 'GD-102', 'home_port': 'Gdańsk', 'length': 12.00, 'width': 3.00,
         'ytype': 'Motorowy'}
fee = {'parking_fee': 8000, 'quarter_fee': 2000}
owner_details = {'name': 'Adrian Bieliński', 'address': 'Anny Jagiellonki 23/14, Gdańsk'}
parking_peroid = {'from': '01.05.2020', 'to': '31.10.2020'}
commissioning_body = {'name': 'jw', 'address': 'jw',
                      'tel': '510494063', 'e-mail': 'adimr52@gmail.com',
                      'nip': 'BRAK'}

x = DataToTable()
x.load_data_to_table(commissioning_body, fee, yacht, parking_peroid, 'D-121')
"""
