import ui.project_ui as ui
import datetime as dt


class BudgetTracker:
    expenses_data: dict

    monthly_income: int
    monthly_savings: int
    recurring_expenses_data: dict

    def __init__(self) -> None:
        self.expenses_data = dict()
        self.monthly_income = int()
        self.monthly_savings = int()
        self.recurring_expenses_data = dict()

    # todo: need to add a new parameter for loading (eg. load_date_from_csv=False)
    # todo: add a "to_data: dict" as parameter to this function to use it for both dicts ?
    def add_new_expense(self) -> None:

        new_expense_name = ui.get_new_expense_name()
        new_expense_amount = ui.get_new_expense_amount()

        now = str(dt.datetime.now())[0:21]

        if self.expenses_data.get(new_expense_name) is None:
            new_expense_name = new_expense_name.title()
            self.expenses_data[now] = {new_expense_name: new_expense_amount}
        else:
            self.expenses_data[now][new_expense_name] += new_expense_amount

    # todo: add graphs, for user-defined ranges (months, days, etc)
    def show_data(self, add_index=False) -> None:

        print()

        for index, (key, value) in enumerate(self.expenses_data.items()):

            for inner_key, inner_value in value.items():

                if add_index:
                    print(
                        f"[{index}] ({key}): [{inner_key} - {inner_value}]"
                    )
                else:
                    print(
                        f"({key}): [{inner_key} - {inner_value}]"
                    )

    # todo: fix incomprehensible looping in the future (self.data[list(self.data.keys()[-])])
    def update_expense(self, delete_instead=False) -> None:

        ui.display_update_expense_intro_message()
        self.show_data(add_index=True)

        choice = int(ui.get_user_input_as_string())

        if delete_instead:
            new_value = None
        else:
            new_value = ui.get_new_value()

        dict_keys = self.expenses_data.keys()
        list_of_keys = list(dict_keys)
        key_selected_by_user = list_of_keys[choice]

        if delete_instead:
            ui.display_deletion_key_warning(key_selected_by_user)
            self.expenses_data.pop(key_selected_by_user)
        else:
            inner_dict = self.expenses_data[key_selected_by_user]
            inner_dict_list_of_keys = list(inner_dict.keys())
            inner_dict_at_selection_zero = inner_dict_list_of_keys[0]

            inner_dict[inner_dict_at_selection_zero] = new_value

    def add_monthly_income(self):

        income = ui.get_income()
        self.monthly_income = income

    def set_monthly_savings_target(self):

        savings = ui.get_monthly_savings()
        self.monthly_savings = savings

    def calculate_maximum_spending_to_next_payment(self) -> float:

        next_payment = ui.get_next_payment()
        current_amount = ui.get_current_amount()

        if self.monthly_savings == 0:
            choice = ui.display_no_savings_warning_message()

            if "n" in choice.lower():

                while self.monthly_savings == 0:
                    self.set_monthly_savings_target()

                    if current_amount - self.monthly_savings <= 0:
                        ui.display_warning_high_savings()
                        self.monthly_savings = 0

        if next_payment == 0:
            next_payment = 1

        return round((current_amount - self.monthly_savings) / next_payment, 2)

