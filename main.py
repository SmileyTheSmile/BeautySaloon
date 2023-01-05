from ui import UI
from transactions import Transactions
from constants import DebugData


def main():
    business_logic = Transactions()

    #result_code, data = business_logic.add_cosmetologist(DebugData.example_cosmetologist)

    ui = UI(business_logic)
    ui.mainloop()


if __name__ == '__main__':
    main()
