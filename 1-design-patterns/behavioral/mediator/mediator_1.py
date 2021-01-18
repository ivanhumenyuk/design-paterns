from __future__ import annotations


# mediator class
class Realtor:
    def __init__(self):
        self.__client_list = []

    def book(self, client: Applicant, apartment_adress) -> str:
        name = client.name
        self.__client_list.append(client)
        print(f"\nClient {name} has booked apartment in {apartment_adress}.\n")

    def get_client_list(self) -> list:
        return self.__client_list

    def delete_clint(self, name):
        list = self.__client_list
        list.pop(list.index(name))
        return f'Client {name} has already deleted from list'


class Applicant:
    def __init__(self, name, realtor: Realtor):
        self.__name = name
        self.realtor = realtor

    @property
    def name(self) -> str:
        return self.__name

    def book_appartment(self, apartment_adress):
        self.realtor.book(self, apartment_adress)
        return f'I book apartment on {apartment_adress}'


if __name__ == '__main__':
    realtor = Realtor()
    client1 = Applicant('Boris Ivanov', realtor)
    client2 = Applicant('Timofey Yaskiv', realtor)
    client3 = Applicant('Bob Markaryan', realtor)
    client4 = Applicant('Andrey Grachev', realtor)

    print(client1.book_appartment('Lenina 23a'))