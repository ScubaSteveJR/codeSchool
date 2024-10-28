from item import Item


class Phone(Item):
    all = []

    def __init__(self, name: str, price: float, quantity, broken_phones=0):
        super().__init__(name, price, quantity)
        # Run validations to the received arguments
        assert broken_phones >= 0, f"Broken Phones {
            broken_phones} is not greater than or equal to zero!"

        # Assign to self object
        self.broken_phones = broken_phones

        # Actions to exucute
        Phone.all.append(self)
