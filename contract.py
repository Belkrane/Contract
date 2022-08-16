class contract:
    def __init__(self):
        self.name = input("Name? ")
        self.phoneNumber = input("Phone Number? ")
        self.emailAddress = input("Email Address? ")
        self.address = input("Address? ")
        
    def __init__(self):
        return

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
            
    return contract_list

def saveContractFile(contract_list):
    contractFile = open("./contract_db.txt", "w")
    
    for contract in contract_list:
        contractFile.write(contract.name + '\n')
        contractFile.write(contract.phoneNumber + '\n')
        contractFile.write(contract.emailAddress + '\n')
        contractFile.write(contract.address + '\n')
    
    contractFile.close()

def loadContractFile():
    contractFile = open("./contract_db.txt", "r")

    contractInfo = contractFile.readlines()
    contract_list = []
    itemCount = int(len(contractInfo) / 4)

    for i in range(itemCount):
        name = contractInfo[i * 4].rstrip('\n')
        phoneNumber = contractInfo[i * 4 + 1].rstrip('\n')
        emailAddress = contractInfo[i * 4 + 2].rstrip('\n')
        address = contractInfo[i * 4 + 3].rstrip('\n')
        contract_item = contract()
        contract_item.set_contract(name, phoneNumber, emailAddress, address)

        contract_list.append(contract_item)

    return contract_list


def run():
    print("running Contract...")
    contract_list = []
    contract_list = loadContractFile()

    while 1:
        menuNumber = contractMenu()

        if menuNumber == 1:
            newContract = contract()
            contract_list.append(newContract)
        elif menuNumber == 2:
            for Outcontract in contract_list :
                Outcontract.print_contract()
        elif menuNumber == 3:
            contract_list = delete_contract(contract_list)
        elif menuNumber == 4:
            saveContractFile(contract_list)
            break





if __name__ == "__main__":
    run()

