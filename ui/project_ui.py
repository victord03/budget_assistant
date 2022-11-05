from utils.project_constants import NEW_LINE, INPUT_DECO


def get_user_input_as_integer() -> int:
    return int(input(INPUT_DECO))


def get_user_input_as_string(display_text="") -> str:
    return input(display_text + INPUT_DECO)


def display_options():

    a = f"{NEW_LINE}0: Add new expense"
    b = f"{NEW_LINE}1: Delete expense"
    c = f"{NEW_LINE}2: Update current expenses / earnings"
    d = f"{NEW_LINE}3: Show current stats"

    return a + b + c + d

