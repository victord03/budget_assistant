import os
import ui.project_ui as ui


def check_if_file_exists(path: str) -> str:
    """Checks if the path chosen already exists.

    If it does, it informs the user. The user can choose to overwrite or choose a new name.

    In both cases, returns the final path that will be used."""

    while os.path.exists(path):

        ui.display_warning_file_overwrite(path)

        choice = ui.get_user_input_as_string()

        if "y" in choice.lower():
            break
        elif "n" in choice.lower():
            choice = ui.get_abort_or_save_confirmation_for_path()

            if "a" in choice.lower():
                path = ""
                break
            elif "p" in choice.lower():
                new_path = ui.get_new_path()
                path = new_path
            else:
                ui.display_unknown_choice()
                path = ""
                break

    return path


def format_data_to_string(data: dict) -> str:
    """Formats each dict value from BudgetTracker.expenses_dict as a string in csv format to be exported in a text
    file."""

    string = ""

    for key, value in data.items():
        for inner_key, inner_value in value.items():
            string += f"\n{key},{inner_key},{inner_value}"

    return string


def save_to_file(path: str, data: dict) -> bool:
    """Attempts to save the data to the path given.

    If the path exists and the user chooses to abort the operation, nothing happens.

    Otherwise, the BudgetTracker.expenses_dict data is formatted in a csv format, and saved as a text file,
    at the specified path.

    Returns True or False depending on whether the operation succeeded or failed."""

    path = check_if_file_exists(path)

    if path == "":
        return False
    else:
        data_as_string = format_data_to_string(data)
        header = "date,expense,amount"

        with open(path, "w") as f:
            f.write(header + data_as_string)

        return True
