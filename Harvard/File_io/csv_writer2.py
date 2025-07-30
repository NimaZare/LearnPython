import csv

name = input("What's your name? ")
job = input("What's your job? ")

with open("peoples2.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "job"])
    writer.writerow({"name": name, "job": job})
