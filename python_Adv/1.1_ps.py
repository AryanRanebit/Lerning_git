from tomlkit import string


def change(self):
    return self.replace(" ", "-")
p=change("Hello World")
print(p)
    

#create a class with a method that takes a string and returns the string with all vowels removed.
