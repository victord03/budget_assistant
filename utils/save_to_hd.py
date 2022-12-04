import os
import ui.project_ui as ui


def check_if_file_exists(path: str) -> str:

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

    string = ""

    for key, value in data.items():
        for inner_key, inner_value in value.items():
            string += f"\n{key},{inner_key},{inner_value}"

    return string


def save_to_file(path: str, data: dict) -> bool:

    path = check_if_file_exists(path)

    if path == "":
        return False
    else:
        data_as_string = format_data_to_string(data)
        header = "date,expense,amount"

        with open(path, "w") as f:
            f.write(header + data_as_string)

        return True
