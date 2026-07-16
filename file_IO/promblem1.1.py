with open("notes.txt","w") as file:
    content = "learning python is fun"
    file.write(content)

with open("notes.txt","r") as file:
    file_content = file.read()
    print(file_content)