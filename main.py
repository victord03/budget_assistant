import project_classes

NEW_LINE = "\n"
INPUT_DECO = "> "


def get_user_input() -> int:
    return int(input(INPUT_DECO))


def display_question(category: str) -> None:

    match category:
        case "salary":
            f"{NEW_LINE}Enter your current salary (monthly):"
        case "rent":
            f"{NEW_LINE}Enter your current rent expenses (monthly): "
        case "fuel":
            f"{NEW_LINE}Enter your current fuel expenses (monthly):"
        case "food":
            f"{NEW_LINE}Enter your current food expenses (monthly):"
        case "savings":
            f"{NEW_LINE}Enter your current saving target goal (monthly):"


def display_options():

    print(
        "\nUpdate "
    )

def main():

    categories = (
        "salary",
        "rent",
        "fuel",
        "food",
        "saving_target",
    )

    user_data = {
        "salary": 0,
        "rent": 0,
        "fuel": 0,
        "food": 0,
        "saving_target": 0,
    }

    usr_data = project_classes.Salary(*user_data.values())

    while True:
        ...


if __name__ == "__main__":
    main()
