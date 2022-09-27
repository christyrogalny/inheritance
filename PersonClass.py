class Person:

    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone


    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone

    def print_person(self):
        print('Name: ', self.__name)


    
class Customer(Person):

    def __init__(self,name, address, phone, cust_number, on_list):
        Person.__init__(self, name, address, phone)
        self.__cust_number = cust_number
        self.__on_list = on_list

    
    def print_person(self):
        print("METHOD #1")
        print('Name: ', Person.get_name(self))
        print('Addr: ', Person.get_address(self))
        print('Phone: ', Person.get_phone(self))


        print()
        print()

        print('METHOD #2')
        Person.print_person(self)


        print('Customer Number: ', self.__cust_number)
        if self.__on_list:
            print('On Mailing list: Yes')
        else:
            print('On Mailing List: No')



