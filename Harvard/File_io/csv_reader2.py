import csv

peoples = []

with open("peoples2.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        peoples.append(row)
        #peoples.append({"name": row["name"], "job": row["job"]})

for people in sorted(peoples, key=lambda people: people["name"]):
    print(f"{people['name']} are a {people['job']}")
