from ui.project_ui import get_user_input_as_float, get_user_input_as_string
import datetime as dt


class BudgetTracker:
    data: dict

    def __init__(self) -> None:
        self.data = dict()

    # todo: need to add a new parameter for loading (eg. load_date_from_csv=False)
    def add_new_expense(self) -> None:

        new_expense_name = get_user_input_as_string(display_text="\nEnter new expense name:")

        print("\nEnter new expense amount:")
        new_expense_amount = get_user_input_as_float()

        now = str(dt.datetime.now())[0:21]

        if self.data.get(new_expense_name) is None:
            new_expense_name = new_expense_name.title()
            self.data[now] = {new_expense_name: new_expense_amount}
        else:
            self.data[now][new_expense_name] += new_expense_amount

    def show_data(self, add_index=False) -> None:

        print()

        for index, (key, value) in enumerate(self.data.items()):

            for inner_key, inner_value in value.items():

                if add_index:
                    print(
                        f"[{index}] ({key}): [{inner_key} - {inner_value}]"
                    )
                else:
                    print(
                        f"({key}): [{inner_key} - {inner_value}]"
                    )

    # todo: fix incomprehensible looping in the future (self.data[list(self.data.keys()[-])])
    def update_expense(self, delete_instead=False) -> None:

        print("\nSelect which value to modify using its corresponding index.")
        self.show_data(add_index=True)

        choice = int(get_user_input_as_string())

        if delete_instead:
            new_value = None
        else:
            new_value = get_user_input_as_float(display_text="\nEnter new value:")

        dict_keys = self.data.keys()
        list_of_keys = list(dict_keys)
        key_selected_by_user = list_of_keys[choice]

        if delete_instead:
            input(f"\nConfirm deletion of key '{key_selected_by_user}' by pressing enter.")
            self.data.pop(key_selected_by_user)
        else:
            inner_dict = self.data[key_selected_by_user]
            inner_dict_list_of_keys = list(inner_dict.keys())
            inner_dict_at_selection_zero = inner_dict_list_of_keys[0]

            inner_dict[inner_dict_at_selection_zero] = new_value

