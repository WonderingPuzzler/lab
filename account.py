class Account:
    def __init__(self, name: str) -> None:
        """

        Constructor function to set up object
        :param name: The name of the account holder
        """
        self.__account_name = name
        self.__balance = 0

    def deposit(self, amount) -> bool:
        """
        Method to increase account balance
        :param amount: Decides how much should be added to account balance
        :return: Returns True if account balance was changed, False if amount was 0 or lower/not changed
        """
        if amount > 0:
            self.__balance += amount
            return True
        else:
            return False

    def withdraw(self, amount) -> bool:
        """

        Method to decrease account balance
        :param amount: decides how much should be added to account balance
        :return: Returns True if account balance was changed, False if amount was not changed/if amount was 0 or less, or greater than the account balance
        """
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            return True
        else:
            return False

    def get_balance(self) -> int:
        """

        Method to access the account balance
        :return: Account balance
        """
        return self.__balance

    def get_name(self) -> str:
        """

        Method to access the account holder's name
        :return: Account name
        """
        return self.__account_name
