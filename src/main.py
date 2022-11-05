from classes.project_classes import BudgetTracker
from ui.project_ui import display_options, get_user_input_as_integer
from utils import save_to_hd


def main():

    my_budget_tracker = BudgetTracker()

    loop = False
    if loop:
        while True:
            print(display_options())
            choice_int = get_user_input_as_integer()

            match choice_int:
                case 0:
                    my_budget_tracker.add_new_expense()
                case 1:
                    my_budget_tracker.delete_expense()
                case 2:
                    my_budget_tracker.update_current_expenses()
                case 3:
                    my_budget_tracker.show_data()

            # todo: add graphs, for user-defined ranges (in months)

    my_budget_tracker.add_new_expense()

    path = r"C:\Users\3tr0001\Desktop\expenses.txt"
    save_to_hd.save_to_file(path, my_budget_tracker)


if __name__ == "__main__":
    main()
