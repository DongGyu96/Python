STATE = 0
CITY = 1

class Theater:
    def __init__(self, name, date, address, tel, type, code):
        if name != None:
            name = name.replace("제1관", "")
            name = name.replace("제2관", "")
            name = name.replace("제3관", "")
            name = name.replace("제4관", "")
            name = name.replace("제5관", "")
            name = name.replace("제6관", "")
            name = name.replace("제7관", "")
            name = name.replace("제8관", "")
            name = name.replace("제9관", "")
            name = name.replace("제10관", "")
            name = name.replace("제11관", "")
            name = name.replace("1관", "")
            name = name.replace("2관", "")
            name = name.replace("3관", "")
            name = name.replace("4관", "")
            name = name.replace("5관", "")
            name = name.replace("6관", "")
            name = name.replace("7관", "")
            name = name.replace("8관", "")
            name = name.replace("9관", "")
            name = name.replace("10관", "")
            name = name.replace("11관", "")
            name = name.replace("()", "")
            name = name.replace("<>", "")

        self.name = name
        self.date = date
        self.address = address
        try:
            self.addresslist = self.address.split()
        except:
            self.addresslist = self.address
        self.tel = tel
        self.type = type
        self.code = code

    def Print(self):
        print(self.addresslist)