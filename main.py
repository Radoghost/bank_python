from manager import Manager

manager = Manager()

if __name__ == "__main__":


    while manager.IS_RUNING:
        manager.show_menu()
        manager.get_choice()