import json
from files import JSON_FILE_PATH, CSV_FILE_PATH
from csv import DictReader

# Читаем .json
with open(JSON_FILE_PATH, "r") as f:
    users = json.load(f)

# Читаем .csv
with open(CSV_FILE_PATH, "r") as f2:
    csv_reader = DictReader(f2)

    # Итерируемся
    iteration_user = iter(users)
    for row in csv_reader:
        try:
            some_user = next(iteration_user)
        except StopIteration:
            iteration_user = iter(users)
            some_user = next(iteration_user)

        if "books" not in some_user:
            some_user["books"] = []

        some_user["books"].append({"title": row["Title"],
                                   "author": row["Author"],
                                   "pages": row["Pages"],
                                   "genre": row["Genre"]
                                   })

data = []
for user in users:
    data.append({
        "name": user["name"],
        "gender": user["gender"],
        "address": user["address"],
        "age": user["age"],
        "books": user["books"]
    })

# Записываем в результирующий .json файл
with open("result.json", "w") as f3:
    f3.write(json.dumps(data, indent=4))
