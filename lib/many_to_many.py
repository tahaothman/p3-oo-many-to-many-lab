class Book:
    def __init__(self, title):
        self.title = title
        self.contracts_list = []

    def contracts(self):
        return self.contracts_list

    def authors(self):
        authors = []
        for contract in self.contracts_list:
            authors.append(contract.author)
        return authors

class Author:
    def __init__(self, name):
        self.name = name
        self.contracts_list = []

    def contracts(self):
        return self.contracts_list

    def books(self):
        books = []
        for contract in self.contracts_list:
            books.append(contract.book)
        return books

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        self.contracts_list.append(contract)
        book.contracts_list.append(contract)
        return contract

    def total_royalties(self):
        total = 0
        for contract in self.contracts_list:
            total += contract.royalties
        return total

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

