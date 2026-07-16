with open("tasks.txt", "w") as file:
    content = '''Complete the project by Friday.
    I need to review the code and write documentation.
    Also, prepare a presentation for the team meeting.'''
    file.write(content)

with open("tasks.txt", "a") as file:
    additional_content = "\nDon't forget to submit the timesheet."
    file.write(additional_content)

with open("tasks.txt", "r") as f:
    for lines in f.readlines():
        print(lines.strip())