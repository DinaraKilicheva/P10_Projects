def read_from_txt(file_path):
    try:
        with open(file_path, "r") as file:
            data = file.read()
    except FileNotFoundError as e:
        print(e)
    else:
        data = list(data)
        for letter in data:
            if letter.isalpha():
                yield letter


read_txt = read_from_txt("test.txt")
for text in read_txt:
    print(text)
