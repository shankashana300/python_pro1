class Expense:
    """
    Represents an Expense with a name, category, and amount.
    """

    def __init__(self, name, category, amount):
        self.name = name  # Name of the expense
        self.category = category  # Category of the expense
        self.amount = amount  # Amount of the expense

    def __repr__(self):
        """
        Provides a readable string representation of the Expense instance.
        """
        return f"<Expense: {self.name}, {self.category}, LKR {self.amount:.2f}>"
