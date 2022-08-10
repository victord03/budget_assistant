
class Salary:
    amount: int
    rent: int
    fuel: int
    food: int
    saving_target: int

    # todo: implement
    extra_expenses: int
    extra_earnings: int

    def __init__(self, amount: int, rent: int, fuel: int, food: int, saving_target: int) -> None:
        self.amount = amount
        self.rent = rent
        self.fuel = fuel
        self.food = food
        self.saving_target = saving_target

    def infer_net_profit(self) -> int:
        return self.amount - (self.rent + self.fuel + self.food + self.saving_target)

    def display_yearly_net_profit(self) -> int:
        return self.infer_net_profit() * 14
