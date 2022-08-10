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

    # ideas: graphics lib

    """
    main window
    
        0: Add new expense
        1: Delete expense
        2: Update current expenses / earnings
        3: Show stats
    
    /add new expense
    
        input("New expense name")
        int(input("New expense amount"))
        
        dict_[new_expense_name] = new_expense_amount
    
    /delete expense
    
        input("Which expense to delete")
        
        try:
            dict_["expense"]
        except KeyError as e: print("This expense does not exist.")
    
    /update current expenses
    
        a = [x for x in range(0, len(list(dict_.keys())))]
        
        for each in a:
            f"{each}: {list(dict_.keys()))[each]}"
            
            0: Salary
            1: Rent
            2: Fuel
            3: Food
            4: Saving Target
            
        int(input("Choice")
        int(input("New amount")
        
        list(dict_.keys())[choice] = new_amount
    
    /show stats
    
        print relevant statistics, in user-defined ranges, for expenses, earnings and savings.
    
    """

    while True:
        ...


if __name__ == "__main__":
    main()
