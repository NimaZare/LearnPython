peoples = []

with open("peoples.csv") as file:
    for line in file:
        name, job = line.rstrip().split(",")
        people = {"name": name, "job": job}
        peoples.append(people)

for people in sorted(peoples, key=lambda people: people["name"]):
    print(f"{people['name']} is a {people['job']}")
