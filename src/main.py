from classes.project_classes import BudgetTracker
from ui.project_ui import display_options, get_user_input_as_integer


def main():

    my_budget_tracker = BudgetTracker()

    while True:
        display_options()
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


if __name__ == "__main__":
    main()
