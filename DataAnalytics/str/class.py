class BaseSalary:
    def __init__(self, base_salary, bonus_rate=0.1, symbol="$") -> None:
        self.base_salary = base_salary
        self.bonus_rate = bonus_rate
        self.symbol = symbol
        self.total_salary = base_salary * (1 + bonus_rate)
        self.bonus = self.total_salary - self.base_salary

    def __repr__(self) -> str:
        return f'{self.symbol}{self.base_salary:,.0f}'

    def calculate_salary(self):
        return f'{self.symbol}{self.total_salary:,.0f}'

    def calculate_bonus(self):
        return f'{self.symbol}{self.bonus:,.0f}'


salary = BaseSalary(100000)
