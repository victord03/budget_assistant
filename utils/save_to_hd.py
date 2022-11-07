import os
from classes.project_classes import BudgetTracker
from ui.project_ui import get_user_input_as_string


def check_if_file_exists(path: str) -> str:

    while os.path.exists(path):

        print(f"Attempting to save as {path}, but the file already exists. Overwrite ?")

        choice = get_user_input_as_string()

        if "y" in choice.lower():
            break
        elif "n" in choice.lower():
            choice = get_user_input_as_string("\nAbort saving or update path ? (type 'a' or 'p' to select)")

            if "a" in choice.lower():
                path = ""
                break
            elif "p" in choice.lower():
                new_path = get_user_input_as_string(display_text="\nEnter new path:")
                path = new_path
            else:
                print("Unknown choice. Exiting.")
                path = ""
                break

    return path


def format_data_to_string(data: BudgetTracker) -> str:

    string = ""

    for key, value in data.data.items():
        for inner_key, inner_value in value.items():
            string += f"\n{key},{inner_key},{inner_value}"

    return string


def save_to_file(path: str, data: BudgetTracker) -> bool:

    path = check_if_file_exists(path)

    if path == "":
        return False
    else:
        data_as_string = format_data_to_string(data)
        header = "date,expense,amount"

        with open(path, "w") as f:
            f.write(header + data_as_string)

        return True
