from utils.project_constants import NEW_LINE, INPUT_DECO


def get_user_input_as_integer() -> int:
    return int(input(INPUT_DECO))


def get_user_input_as_string() -> str:
    return input(INPUT_DECO)


def display_options():

    print(
        f"{NEW_LINE}0: Add new expense"
        + f"{NEW_LINE}1: Delete expense"
        + f"{NEW_LINE}2: Update current expenses / earnings"
        + f"{NEW_LINE}3: Show current stats"
    )


