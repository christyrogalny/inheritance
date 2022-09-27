import PersonClass as p

def main():
    name = 'John'
    address = '1234 Main St'
    phone = '123-456 - 7890'
    cust_number = 1234
    on_list = False

    person1 = p.Person(name, address, phone)


    customer1 = p.Customer(name, address, phone, cust_number, on_list)

    person1.print_person()


    print()
    print()
    print()


    customer1.print_person()



main()