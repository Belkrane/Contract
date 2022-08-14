class contract:
    def __init__(self, name, phoneNumber, emailAddress, address):
        self.name = name
        self.phoneNumber = phoneNumber
        self.emailAddress  = emailAddress
        self.address = address
    
    def set_contract(self, name, phoneNumber, emailAdress, address):
        self.name = name
        self.phoneNumber = phoneNumber
        self.emailAddress = emailAdress
        self.address  = address

    def print_contract(self):
        print("Name: %s", self.name)
        print("Phone Number: %s", self.phoneNumber)
        print("Email Address: %s", self.emailAddress)
        print("Address: %s", self.address)



def contractMenu(self):
        print("1.연락처 입력")
        print("2.연락처 출력")
        print("3.연락처 삭제")
        print("4.종료")
        menu = input("메뉴 선택: ")
        
        return (int)menu


def run():
    print("running Contract...")

    while true:
        menuNumber = contractMenu()





if __name__ == "__main__":
    run()

