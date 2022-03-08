from importlib.resources import contents


with open("input.txt", "r") as ext_file:
    for line in ext_file:
        data = line.split('\n')
        print(data)
