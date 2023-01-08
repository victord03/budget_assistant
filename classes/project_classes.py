import ui.project_ui as ui
from utils import date_and_time as dt


class BudgetTracker:
    """Main project class.

    Tracks financial data input by the user, or calculated by functions."""

    expenses_data: dict

    monthly_income: int
    monthly_savings: int
    recurring_expenses_data: dict

    def __init__(self) -> None:
        """Init function. Simply initializes attributes to either 0 or empty dicts."""
        self.expenses_data = dict()
        self.monthly_income = int()
        self.monthly_savings = int()
        self.recurring_expenses_data = dict()

    # todo: need to add a new parameter for loading (eg. load_date_from_csv=False)
    # todo: add a "to_data: dict" as parameter to this function to use it for both dicts ?
    def add_new_expense(self) -> None:
        """Creates a new expense to be tracked in the main class, specifically
        under the BudgetTracker.expenses_data dict.

        Fist asks the following input from the user:
        1) New expense name
        2) New expense amount

        Calls the utils.date_and_time.format_time_now to format the current moment as a string to be used as a key.

        It then creates a new dict entry with the datetime.datetime.now()
        as a key and the pair new expense name and amount as a dict value."""

        new_expense_name = ui.get_new_expense_name()
        new_expense_amount = ui.get_new_expense_amount()

        now = dt.format_time_now()

        new_expense_name = new_expense_name.title()
        self.expenses_data[now] = {new_expense_name: new_expense_amount}

    # todo: add graphs, for user-defined ranges (months, days, etc)
    def show_data(self, add_index=False) -> None:
        """Displays BudgetTracker.expenses_data dict.

        Calls the ui.display_class_dict function."""

        print()

        ui.display_class_dict(self.expenses_data, add_index=add_index)

    # todo: fix incomprehensible looping in the future (self.data[list(self.data.keys()[-])])
    def update_expense(self, delete_instead=False) -> None:
        """Updates an existing expense already tracked under the
        BudgetTracker.expenses_data dict.

        Calls a function from the UI element which displays a message
        informing about the impending action.

        Displays all the BudgetTracker.expenses_data dict content.

        The user selects a number used as index for simplicity.

        Gets the new value for the expense from the user.

        Replaces the value stored with the new provided by the user.

        There is the option to delete the key entirely instead. This is because
        the exact same function is called for the self.delete_expense method.
        Displays a final warning in that case, by calling the corresponding
        function from the UI element."""

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

    def delete_expense(self):
        """Deletes an expense from the BudgetTracker.expenses_data dict.

        Runs the self.update_expense function with the 'delete_instead'
        parameter set to True which does just that."""
        self.update_expense(delete_instead=True)

    def add_monthly_income(self):
        """Adds a monthly income as provided by the user,
        and stores it as an attribute in the BudgetTracker class."""

        income = ui.get_income()
        self.monthly_income = income

    def set_monthly_savings_target(self):
        """Sets a monthly savings target as provided by the user,
        and stores it as an attribute in the BudgetTracker class."""

        savings = ui.get_monthly_savings()
        self.monthly_savings = savings

    def calculate_maximum_spending_to_next_payment(self) -> float:
        """Calculates the maximum amount of spending possible per day,
        given the remaining account balance and the number of days
        until the next payment, and assuming equal distribution over
        the days.

        Gets the user input on:
        1) Current account / savings balance
        2) Days until next payment

        If self.monthly_savings is set to 0, it attempts to warn the
        user in case it was forgotten to be set prior. The user can
        skip this step, or set a target right then. Otherwise, the monthly
        savings attribute is set to 0.

        Since the calculation uses a division over the total number of days
        to next payment, if next payment is set to 0, it is modified to 1. In
        practical terms, it doesn't make sense for the user to input 0 here
        because this means that the next payment will be occurring today,
        therefore the remaining account balance can all be spent today.

        Returns the result as a float, down to two decimal places."""

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

