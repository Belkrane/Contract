class contract:
    def __init__(self):
        self.name = input("Name? ")
        self.phoneNumber = input("Phone Number? ")
        self.emailAddress = input("Email Address? ")
        self.address = input("Address? ")
        
    
    def set_contract(self, name, phoneNumber, emailAdress, address):
        self.name = name
        self.phoneNumber = phoneNumber
        self.emailAddress = emailAdress
        self.address  = address

    def print_contract(self):
        print("-----------------------------------------------")
        print("Name: ", self.name)
        print("Phone Number: ", self.phoneNumber)
        print("Email Address: ", self.emailAddress)
        print("Address: ", self.address)
        print("-----------------------------------------------")


def contractMenu():
    print("1.Input Contract")
    print("2.Print Contract")
    print("3.Delete Contract")
    print("4.EXIT")
    menu = input("Choose Menu: ")
        
    return int(menu)

def delete_contract(contract_list):
    name = input("Name? ")

    for contract in contract_list:
        if contract.name == name:
            contract_list.remove(contract)
            


def run():
    print("running Contract...")
    contract_list = []

    while 1:
        menuNumber = contractMenu()

        if menuNumber == 1:
            newContract = contract()
            contract_list.append(newContract)
        elif menuNumber == 2:
            for Outcontract in contract_list :
                Outcontract.print_contract()
        elif menuNumber == 3:
            delete_contract(contract_list)
        elif menuNumber == 4:
            break





if __name__ == "__main__":
    run()

