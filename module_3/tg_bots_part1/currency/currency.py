class Currency:
    def __init__(self, from_=None, to_=None,amount=None):
        self.from_ = from_
        self.to_ = to_
        self.amount=amount

    def get_attrs_as_dict(self):
        return {
            "from_": self.from_,
            "to_": self.to_,
            "amount":self.amount

        }
