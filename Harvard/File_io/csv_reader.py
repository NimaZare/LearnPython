import csv

peoples = []

with open("peoples.csv") as file:
    reader = csv.reader(file)
    for name, job in reader:
        peoples.append({"name": name, "job": job})

for people in sorted(peoples, key=lambda people: people["name"]):
    print(f"{people['name']} are a {people['job']}")
