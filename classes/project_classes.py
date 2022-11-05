from ui.project_ui import get_user_input_as_integer, get_user_input_as_string


class BudgetTracker:
    data: dict

    # todo: instead of monthly, just log any new expense + the date

    def __init__(self) -> None:

        self.data = {}

        print("\nEnter your salary (monthly):")
        amount = get_user_input_as_integer()

        print("\nEnter your rent expense (monthly):")
        rent = get_user_input_as_integer()

        self.data["salary"] = amount
        self.data["rent"] = rent

    def add_new_expense(self) -> None:

        new_expense_name = get_user_input_as_string(display_text="\nEnter new expense name:")

        print("\nEnter new expense amount:")
        new_expense_amount = get_user_input_as_integer()

        self.data[new_expense_name] = new_expense_amount

    def delete_expense(self) -> None:

        to_delete = get_user_input_as_string(display_text="\nEnter expense name to delete:")

        try:
            self.data.pop(to_delete)
        except KeyError as e:
            print("Expense name does not exist in the data.")

    def update_current_expenses(self) -> None:

        number_of_keys = [x for x in range(0, len(list(self.data.keys())))]

        print()
        for each in number_of_keys:
            print(f"{each}: {list(self.data.keys())[each].title()}")

        print("\nEnter category number:")
        choice = get_user_input_as_integer()

        print("\nEnter new value:")
        new_amount = get_user_input_as_integer()

        self.data[list(self.data.keys())[choice]] = new_amount

    def show_data(self) -> None:

        print()

        for key, value in self.data.items():
            print(
                f"{key.title()}: {value:,}"
            )

