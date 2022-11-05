import os
from datetime import datetime
from classes.project_classes import BudgetTracker
from ui.project_ui import get_user_input_as_string


def check_if_file_exists(path: str) -> str:

    while os.path.exists(path):

        with open(path) as f:
            content = f.readlines()
            last_date = content[0]  # first line has to be the date

        print(f"File already exists. File date: {last_date}. Overwrite ?")

        choice = get_user_input_as_string()

        if "y" in choice:
            break
        elif "n" in choice:
            new_path = get_user_input_as_string(display_text="\nEnter new path:")
            path = new_path

    return path


def format_data_to_string(data: BudgetTracker) -> str:

    string = ""

    for key, value in data.data.items():
        string += f"\n{key.title()}: {value:,}"

    return string


def save_to_file(path: str, data: BudgetTracker):

    path = check_if_file_exists(path)
    data_as_string = format_data_to_string(data)
    date_today = str(datetime.now().date())

    with open(path, "w") as f:
        f.write(date_today + data_as_string)