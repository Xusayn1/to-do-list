from utils.menu import menu
import to_do.manager as manager
import logging
from core.models import create_tables

logger = logging.getLogger(__name__)


def to_do_menu():
    while True:
        print("Welcome to Do List")
        print(menu)
        option = input("Select an option: ")
        if option == "1":
             manager.add_task()
        elif option == "2":
            manager.do_list_tasks()
        elif option == "3":
            manager.done_list_tasks()
        elif option == "4":
            manager.do_tasks()
        elif option == "5":
            manager.remove_task()
        elif option == "6":
            print("Goodbye")
            logging.info('menu process is done')
            break
        else:
            print("Invalid option")
            logging.warning("Invalid option")
            break

if __name__ == "__main__":
    # create_tables()
    to_do_menu()