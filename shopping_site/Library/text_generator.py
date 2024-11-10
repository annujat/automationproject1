def text_data(part):
    data = open(".\\Assets\\subject_message.txt", "r")
    if part == "subject":
        data.seek(9)
        subject = data.readline()
        return subject
    else:
        data.seek(47)
        return data.read()
