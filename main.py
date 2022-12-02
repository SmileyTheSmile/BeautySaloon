from ui import UI
from transactions import Transactions
from constants import EXAMPLE_CLIENT


def main():
    business_logic = Transactions()

    # result = business_logic.register_new_client(**EXAMPLE_CLIENT)

    result = business_logic.log_in(login="kdanil01",
                                   password="begemot")
    print(result)

    # ui = UI(business_logic)
    # ui.mainloop()


if __name__ == '__main__':
    main()
