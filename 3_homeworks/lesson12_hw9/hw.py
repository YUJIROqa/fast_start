class Book():
    page_material = 'paper'
    have_text = True
    book_name = 'bookname'
    author = 'authorname'
    quantity_pages = 100
    ISBN = '1234567890'
    registration = True

    def is_reg_true(self):
        if self.registration == True:
            print(f'Название {self.book_name}, Автор: {self.author}, Количество страниц: {self.quantity_pages}, Материал {self.page_material}, Зарегистрирована')
        else:
            print(f'Название {self.book_name}, Автор: {self.author}, Количество страниц: {self.quantity_pages}, Материал {self.page_material}')

    def __init__(self, book_name, author, quantity_pages, ISBN, registration):
        self.book_name = book_name
        self.author = author
        self.quantity_pages = quantity_pages
        self.ISBN = ISBN
        self.registration = registration


class SchoolBooks(Book):
    subject = 'school subject'
    grade = 19
    tasks = True
        
    def __init__(self, book_name, author, quantity_pages, ISBN, registration, subject, grade, tasks):
        super().__init__(book_name, author, quantity_pages, ISBN, registration)
        self.subject = subject
        self.grade = grade
        self.tasks = tasks

    def is_reg_true(self):
        if self.registration == True:
            print(f'Название {self.book_name}, Автор: {self.author}, Количество страниц: {self.quantity_pages}, Предмет {self.subject}, Класс {self.grade}, Зарегистрирована')
        else:
            print(f'Название {self.book_name}, Автор: {self.author}, Количество страниц: {self.quantity_pages}, Предмет {self.subject}, Класс {self.grade}')
    
GOT = Book('Game of Thrones', 'George R.R. Martin', 1000, '978-5-04-092586-0', True)

rich_father = Book('Rich Father Poor Father', 'Robert Kiyosaki', 200, '978-1-5011-2472-7', False)

ilon_mask = Book('Ilon Mask', 'Ilon Mask', 100, '978-1-5011-2472-7', False)

how_to_make_money = Book('How to make money', 'Ilon Mask', 100, '978-1-5011-2472-7', False)

power_of_subconsious = Book('The Power of Subconsious Mind', 'Joseph Murphy', 100, '978-1-5011-2472-7', False)

books = [GOT, rich_father, ilon_mask, how_to_make_money, power_of_subconsious]
for book in books:
    book.is_reg_true()


match_9class = SchoolBooks('Math 9 class', 'Elena Golovina', 150, '978-5-04-092586-0', False, 'Math', 9, True)

english_6class = SchoolBooks('English 6 class', 'Igor Meshrug', 124, '295-5-04-31254213-0', False, 'English', 6, True)

literature_11class = SchoolBooks('Literature 11 class', 'Oksana Zabuzhko', 176, '295-5-04-31254213-0', False, 'Literature', 11, True)

physics_10class = SchoolBooks('Physics 10 class', 'Dmitriy Belyaev', 265, '295-5-04-31254213-0', True, 'Physics', 10, True)

chemistry_11class = SchoolBooks('Chemistry 11 class', 'Dmitriy Belyaev', 215, '295-5-04-31254213-0', False, 'Chemistry', 11, True)

school_books = [match_9class, english_6class, literature_11class, physics_10class, chemistry_11class]

for book in school_books:
    book.is_reg_true()