import csv

name = input("What's your name? ")
job = input("What's your job? ")

with open("peoples2.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, job])
