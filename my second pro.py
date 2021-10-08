class Mobile_phones:
    def __init__(self, phones):
        self.phones = phones

    def list_phones(self):
        print("Available phones ")
        for phone in self.phones:
            print(phone)

    def Buy_phone(self, Buy_phone):
        if Buy_phone in self.phones:
            print("Buy Your Phone")
            self.phones.remove(Buy_phone)
        else:
            print("The Phone is Not Available")

    def Repair_phone(self, Repair_phone):
        print("We will Repair Your Phone ")
        self.phones.append(Repair_phone)


phones = ["Samsung", "Redmi", "Poco", "Apple"]
o = Mobile_phones(phones)
msg = """ 
    1.Available Phone
    2.Buy Phone
    3.Repair Phone
"""
while True:
    print(msg)
    ch = int(input("Enter Your Choice : "))
    if ch == 1:
        o.list_phones()
    elif ch == 2:
        phone = (int(input("Enter Your phone Name : ")))
        o.Buy_phone()
    elif ch == 3:
        phone = (int(input("Enter Your phone Name : ")))
        o.Repair_phone()
    else:
        print("Thank You and Come Again ")
        quit()
