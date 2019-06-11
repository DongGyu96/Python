STATE = 0
CITY = 1

class Theater:
    def __init__(self, name, date, address, tel, type, code):
        self.name = name
        self.date = date
        self.address = address
        self.addresslist = self.address.split()
        self.tel = tel
        self.type = type
        self.code = code
        self.Print()

    def Print(self):
        print(self.addresslist)