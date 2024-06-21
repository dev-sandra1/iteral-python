
def search_names(names, find_name):
    count = names.count(find_name)
    if find_name in names:
        print(f"el nombre {find_name} se encuentra con un total de recurrencias de {count}")
    else:
        print("no está")

names = ["sami", "luz", "sami", "name", "lila"]
find_name = "sami"

search_names(names, find_name)