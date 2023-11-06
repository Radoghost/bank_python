from bank import Bank
from client import Client
from colors import Color
import os


color = Color()
RED = color.RED
GREEN = color.GREEN
END = color.ENDC

clients = [
    Client(1, "Andrzej", "Andrzejewski", "001", 1500.00),
    Client(2, "Robert", "Robertowy", "002", 473.20),
]

bank = Bank()
bank.clients.extend(clients)


class Manager:
    IS_RUNING = True


    def show_menu(self):
        print('''
    WYBIERZ OPCJĘ:

    1 => LISTA WSZYSTKICH KLIENTÓW BANKU

    2 => LOGOWANIE

    3 => ZAKOŃCZ PROGRAM

    WYBIERZ 1, 2 LUB 3:
    ''')
        
    def get_choice(self):
        choice = int(input())
        if choice == 1:
            os.system("cls")
            bank.show_clients()
        
        elif choice == 2:
            os.system("cls")
            logged_client = bank.log_in()
            os.system("cls")
            logged_client.show_client_info()

            if isinstance(logged_client, Client):
                transfer_to_account = input("WPISZ NUMER KONTA NA KTÓRY CHCESZ WYKONAĆ PRZELEW: ")
                os.system("cls")
                if transfer_to_account == logged_client.account_number:
                    print(f"{RED}NIE MOŻESZ ZROBIĆ PRZELEWU NA WŁASNE KONTO{END}")
                    self.IS_RUNING = False
                transfer_to_account = bank.get_client_by_account_number(transfer_to_account)
                if isinstance(transfer_to_account, Client):
                    bank_transfer = bank.make_money_transfer(logged_client ,transfer_to_account)
                    if bank_transfer:
                        os.system("cls")
                        print(f"{GREEN}PRZELEW ZOSTAŁ WYKONANY{END}")
                        bank.show_clients()
                        self.IS_RUNING = False
                    else:
                        print(f"{RED}NIEWYSTARCZAJĄCE ŚRODKI NA RACHUNKU{END}")
                        self.IS_RUNING = False
                else:
                    print(f"{RED}NIEPRAWIDŁOWY NUMER KONTA{END}")
                    self.IS_RUNING = False
            else:
                self.IS_RUNING = False
        
        elif choice == 3:
            self.IS_RUNING = False
        else:
            pass