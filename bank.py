class Bank:

    def __init__(self):
        self.clients = []

    def log_in(self):
        user_account = input("ZALOGUJ SIĘ WYBIERAJĄC ID KLIENTA: ")
        for client in self.clients:
            try:
                if int(user_account) == client.id:
                    return client
            except:
                print("LOGOWANIE NIEUDANE")
        return False
            
    def make_money_transfer(self, client, account_to_transfer):
        amount_to_transfer = float(input("PODAJ KWOTĘ PRZELEWU: "))
        if amount_to_transfer > 0 and amount_to_transfer <= client.account_balance:
            client.account_balance -= amount_to_transfer
            account_to_transfer.account_balance += amount_to_transfer
            return True
        else:
            return False

    def get_client_by_account_number(self, acc_number):
        for client in self.clients:
            if client.account_number == acc_number:
                return client
        return False
                        
    def show_clients(self):
        print("ID | IMIĘ I NAZWISKO | NR KONTA | SALDO")
        for client in self.clients:
            print(f"{client.id} | {client.name} {client.last_name} | {client.account_number} | {round(client.account_balance, 2)}")
    
