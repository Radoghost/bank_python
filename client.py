class Client:
    
    def __init__(self, id, name, last_name, account_number, account_balance):
        self.id = id
        self.name = name
        self.last_name = last_name
        self.account_number = account_number
        self.account_balance = account_balance


    def show_client_info(self):
        print(f'''
ZALOGOWANY KLIENT

ID: {self.id}

IMIĘ I NAZWISKO: {self.name} {self.last_name}

NR KONTA: {self.account_number}

SALDO: {self.account_balance} zł

''')