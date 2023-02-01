def read_names(file_path):
    try:
        with open(file_path, "r") as file:
            data = file.readlines()
    except FileNotFoundError as e:
        print(e)
    else:
        for elem in data:
            if elem.split("=")[0].strip() == "name":
                yield elem.split("=")[1].strip()


planet_names = read_names("planets.txt")

for planet in planet_names:
    print(planet)

