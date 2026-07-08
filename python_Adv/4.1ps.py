#Create a class book with attributes title and author.

#Implement __str__() so that printing the object displays "Title by Author".
#Implement __len__() so that len(book) returns the length of the title.
#Create two Book objects and test these methods.

class book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def __str__(self):
        return f"Title of the book is {self.title} and the author is {self.author}"
    def len(self):
        return len(self.title)
b1=book("The Great Gatsby","F. Scott Fitzgerald")
b2=book("To Kill a Mockingbird","Harper Lee")
print(b1)
print(b1.len())
print(b2)
print(b2.len())