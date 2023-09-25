import datetime


class Book:
    def __init__(self, title):
        self.title = title
        self.contracts_list = []

    def contracts(self):
         return [contract for contract in Contract.all_contracts if contract.book == self]

    def authors(self):
        return [contract.author for contract in self.contracts()]

class Author:
    def __init__(self, name):
        self.name = name
        self.contracts_list = []

    def contracts(self):
         return [contract for contract in Contract.all_contracts if contract.author == self]

    def books(self):
          return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        self.contracts_list.append(contract)
        book.contracts_list.append(contract)
        return contract

    def total_royalties(self):
         return sum(contract.royalties for contract in self.contracts())

class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author should be an instance of the Author class")
        if not isinstance(book, Book):
            raise Exception("Book should be an instance of the Book class")
        if not isinstance(date, str):
            raise Exception("Date should be a string")
        if not isinstance(royalties, int):
            raise Exception("Royalties should be an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        self.all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls):
        return sorted(cls.all_contracts, key=lambda contract: contract.date)



