class Account:
    def __init__(self, no_borrowed_books, no_reseved_books, no_returned_books, no_lost_books, fine_amount  ):
        self.__no_borrowed_books= no_borrowed_books
        self.__no_reseved_books = no_reseved_books
        self.__no_returned_books = no_returned_books
        self.__no_lost_books = no_lost_books
        self.__fine_amount = fine_amount
     
    def get_name(self):
         return self.__no_borrowed_books

    def set_name(self, no_borrowed_books):
        self.__no_borrowed_books = no_borrowed_books

    def get_name(self):
         return self.__no_reseved_books

    def set_name(self, no_reseved_books):
        self.__no_reseved_books = no_reseved_books

    def get_name(self):
         return self.__no_returned_books

    def set_name(self, no_returned_books):
        self.__no_returned_books = no_returned_books
    
    def get_name(self):
         return self.__no_lost_books

    def set_name(self, no_lost_books):
        self.__no_lost_books = no_lost_books

    def get_fine_amount(self):
         return self.__fine_amount

    def set_fine_amount(self, fine_amount):
        self.__fine_amount = fine_amount

 

    

       
        
