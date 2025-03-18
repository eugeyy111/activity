class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def describe(self):
        """Displays the details of the book."""
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year Published: {self.year_published}")
        print("-" * 20)

# Create three Book objects
book1 = Book(title="The Notebook ", author="eugene the great ", year_published=1948)
book2 = Book(title="Me Before You", author="sika the servant", year_published=2003)
book3 = Book(title="The Alchemist", author=" Paulo donna ", year_published=1982)

# Display the details of each book
book1.describe()
book2.describe()
book3.describe()