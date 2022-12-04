NL = "\n"
INPUT_DECO = f"{NL}> "


# INPUTS
def get_user_input_as_float(display_text="") -> float:
    return round(float(input(display_text + INPUT_DECO)), 2)


def get_user_input_as_string(display_text="") -> str:
    return input(display_text + INPUT_DECO)


def get_new_expense_name() -> str:
    return get_user_input_as_string(display_text=f"{NL}Enter new expense name:")


def get_new_expense_amount() -> float:
    return get_user_input_as_float(display_text=f"{NL}Enter new expense amount:")


def get_new_value() -> float:
    return get_user_input_as_float(display_text=f"{NL}Enter new value:")


def get_income() -> int:
    return int(get_user_input_as_string(display_text=f"{NL}Enter monthly income (net):"))


def get_monthly_savings() -> int:
    return int(get_user_input_as_string(display_text=f"{NL}Enter monthly savings target:"))


def get_next_payment() -> int:
    return int(get_user_input_as_string(display_text=f"{NL}In how many days is the next payment ?"))


def get_current_amount() -> float:
    return get_user_input_as_float(display_text=f"{NL}What is your current available amount ?")


def get_abort_or_save_confirmation_for_path() -> str:
    return get_user_input_as_string("\nAbort saving or update path ? (type 'a' or 'p' to select)")


def get_new_path() -> str:
    return get_user_input_as_string(display_text="\nEnter new path:")


# DISPLAYS
def display_options() -> None:

    a = f"{NL}0: Add a new expense"
    b = f"{NL}1: Delete an expense"
    c = f"{NL}2: Update an expense"
    d = f"{NL}3: Show current stats"
    e = f"{NL}4: Save current to file"

    print(a + b + c + d + e)


def display_class_dict(expenses_data: dict, add_index=False) -> None:
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
    print(f"{NL}The maximum amount possible to be spending every day until the next payment is: {result:,} EUR.")


def display_update_expense_intro_message() -> None:
    print(f"{NL}Select which value to modify using its corresponding index.")


def display_deletion_key_warning(key) -> None:
    input(f"{NL}Confirm deletion of key '{key}' by pressing enter.")


def display_no_savings_warning_message() -> str:
    return get_user_input_as_string(display_text=f"{NL}Will calculate without any savings target. Proceed? (y or n)")


def display_warning_file_overwrite(path: str) -> None:
    print(f"Attempting to save as {path}, but the file already exists. Overwrite ? (y or n)")


def display_warning_high_savings() -> None:
    a = f"{NL}Cannot choose this high amount of savings because it is either higher or equal "
    b = "to the current amount specified. Please choose new amount."
    print(a + b)


def display_unknown_choice() -> None:
    print("Unknown choice. Exiting.")


def display_loop_return_code_0() -> None:
    print("Loop return code 0 (save operation not completed).")


def display_loop_return_code_1() -> None:
    print("Loop return code 1 (save operation was completed).")

