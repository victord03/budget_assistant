from classes.project_classes import BudgetTracker
from ui.project_ui import display_options, get_user_input_as_string
from utils import save_to_hd


def main():

    my_budget_tracker = BudgetTracker()
    path = r"C:\Users\3tr0001\Desktop\expenses.txt"

    test_data = True
    if test_data:
        my_budget_tracker.data.update(
            {
                "2022-11-05 09:42:09.0": {"Food": 6.00},
                "2022-11-06 04:55:56.9": {"Batteries (AA)": 3.30},
                "2022-11-07 23:25:17.5": {"Cookies": 2.49},
                "2022-11-07 21:21:09.2": {"Toothbrush": 1.00}
            }
        )

    loop = True
    if loop:

        while True:
            print(display_options())
            choice = get_user_input_as_string()

            try:
                choice_int = int(choice)
            except ValueError:
                break

            match choice_int:
                case 0:
                    my_budget_tracker.add_new_expense()
                case 1:
                    my_budget_tracker.update_expense(delete_instead=True)
                case 2:
                    my_budget_tracker.update_expense()
                case 3:
                    my_budget_tracker.show_data()
                case 4:
                    # todo: needs reworking
                    return_code = save_to_hd.save_to_file(path, my_budget_tracker)
                    if not return_code:
                        print("Loop return code 0 (save operation not completed).")
                        break
                    elif return_code:
                        print("Loop return code 1 (save operation was completed).")
                        break


if __name__ == "__main__":
    main()
