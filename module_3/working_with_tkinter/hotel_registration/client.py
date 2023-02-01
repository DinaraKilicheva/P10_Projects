class Client:
    def __init__(self, name, age, address, length_stay, payment):
        self.name = name
        self.age = age
        self.address = address
        self.length_stay = length_stay
        self.payment = payment

    def get_info(self, flag=False):
        if flag:
            return {
                "Name": self.name,
                "Age": self.age,
                "Address": self.address,
                "Length stay": self.length_stay,
                "Payment": self.payment,
            }
        return [
            self.name,
            self.age,
            self.address,
            self.length_stay,
            self.payment,
        ]
