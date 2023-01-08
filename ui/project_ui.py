NL = "\n"
INPUT_DECO = f"{NL}> "


# INPUTS
def get_user_input_as_float(display_text="") -> float:
    """Returns the user input as a float. A display_text can be shown to the user."""
    return round(float(input(display_text + INPUT_DECO)), 2)


def get_user_input_as_string(display_text="") -> str:
    """Returns the user input as a string. A display_text can be shown to the user."""
    return input(display_text + INPUT_DECO)


def get_new_expense_name() -> str:
    """Captures a new expense name given by user. Calls get_user_input_as_string."""
    return get_user_input_as_string(display_text=f"{NL}Enter new expense name:")


def get_new_expense_amount() -> float:
    """Captures a new expense amount given by user. Calls get_user_input_as_float."""
    return get_user_input_as_float(display_text=f"{NL}Enter new expense amount:")


def get_new_value() -> float:
    """Captures a new value given by user for updating an expense. Calls get_user_input_as_float."""
    return get_user_input_as_float(display_text=f"{NL}Enter new value:")


def get_income() -> int:
    """Captures a new income amount given by user. Calls get_user_input_as_float, cast into an integer."""
    return int(get_user_input_as_string(display_text=f"{NL}Enter monthly income (net):"))


def get_monthly_savings() -> int:
    """Captures a new monthly savings amount given by user. Calls get_user_input_as_float, cast into an integer."""
    return int(get_user_input_as_string(display_text=f"{NL}Enter monthly savings target:"))


def get_next_payment() -> int:
    """Captures the days until the next payment given by user. Calls get_user_input_as_float, cast into an integer."""
    return int(get_user_input_as_string(display_text=f"{NL}In how many days is the next payment ?"))


def get_current_amount() -> float:
    """Captures the current balance account given by user. Calls get_user_input_as_float."""
    return get_user_input_as_float(display_text=f"{NL}What is your current available amount ?")


def get_abort_or_save_confirmation_for_path() -> str:
    """Captures a confirmation given by user. Calls get_user_input_as_string."""
    return get_user_input_as_string("\nAbort saving or update path ? (type 'a' or 'p' to select)")


def get_new_path() -> str:
    """Captures a new path given by user. Calls get_user_input_as_string."""
    return get_user_input_as_string(display_text="\nEnter new path:")


# DISPLAYS
def display_options() -> None:
    """Displays the main tool options (main menu)."""

    a = f"{NL}0: Add a new expense"
    b = f"{NL}1: Delete an expense"
    c = f"{NL}2: Update an expense"
    d = f"{NL}3: Show current stats"
    e = f"{NL}4: Save current to file"

    print(a + b + c + d + e)


def display_class_dict(expenses_data: dict, add_index=False) -> None:
    """Displays BudgetTracker.expenses_data dict.

    It loops through all keys (which are str dates), and then through
    all values (which are expense_name: expense_amount dict pairs) and
    displays each one.

    Using enumerate, it is able to display a small incrementing number
    next to the dates to improve readability. By default, this option
    is off because it will be only used when the user will select a
    key for some other action (update, delete, etc)."""

    print()

    for index, (key, value) in enumerate(expenses_data.items()):

        for inner_key, inner_value in value.items():

            if add_index:
                print(
                    f"[{index}] ({key}): [{inner_key} - {inner_value}]"
                )
            else:
                print(
                    f"({key}): [{inner_key} - {inner_value}]"
                )


def display_calculated_spending_to_next_payment(result: float) -> None:
    """Displays a message along with the result of the function calculate_maximum_spending_to_next_payment under
    project_classes.BudgetTracker."""
    print(f"{NL}The maximum amount possible to be spending every day until the next payment is: {result:,} EUR.")


def display_update_expense_intro_message() -> None:
    """Displays an explanatory message to the user, concerning what action is expected next."""
    print(f"{NL}Select which value to modify or delete using its corresponding index.")


def display_no_savings_warning_message() -> str:
    """Displays a message to the user. Requires specific user input ('y' or 'n') to continue."""
    return get_user_input_as_string(display_text=f"{NL}Will calculate without any savings target. Proceed? (y or n)")


def display_unknown_choice() -> None:
    """Displays an unknown choice message."""
    print("Unknown choice. Exiting.")


def display_loop_return_code_0() -> None:
    """Displays an unsuccessful loop return code message (0)."""
    print("Loop return code 0 (save operation not completed).")


def display_loop_return_code_1() -> None:
    """Displays a successful loop return code message (1)."""
    print("Loop return code 1 (save operation was completed).")


# WARNINGS
def display_deletion_key_warning(key) -> None:
    """Displays a warning message to the user. Requires user input to continue."""
    input(f"{NL}Confirm deletion of key '{key}' by pressing enter.")


def display_warning_file_overwrite(path: str) -> None:
    """Displays a warning message to the user. Requires specific user input ('y' or 'n') to continue."""
    print(f"Attempting to save as {path}, but the file already exists. Overwrite ? (y or n)")


def display_warning_high_savings() -> None:
    """Displays a warning message to the user concerning higher savings value than income chosen."""
    a = f"{NL}Cannot choose this high amount of savings because it is either higher or equal "
    b = "to the current amount specified. Please choose new amount."
    print(a + b)
