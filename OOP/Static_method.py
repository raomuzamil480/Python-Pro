# A method that performs some task related to the class, but doesn’t need (  object ) data.

# Uses for validations like bank , etc

class Bank:
    @staticmethod
    def valid(pin):
        if len(pin)==4:
            return True
        return False
print(Bank.valid("124"))

