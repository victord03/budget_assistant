from utils.project_constants import NEW_LINE, INPUT_DECO


def get_user_input_as_float(display_text="") -> float:
    return round(float(input(display_text + INPUT_DECO)), 2)


def get_user_input_as_string(display_text="") -> str:
    return input(display_text + INPUT_DECO)


def display_options():

    a = f"{NEW_LINE}0: Add a new expense"
    b = f"{NEW_LINE}1: Delete an expense"
    c = f"{NEW_LINE}2: Update an expense"
    d = f"{NEW_LINE}3: Show current stats"

    return a + b + c + d

