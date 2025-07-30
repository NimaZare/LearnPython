name = input("What's your name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")

names = []

with open("names.txt") as file:
    for line in file:
        # .rstrip()  method for remove '\n' in the end of every lines
        names.append(line.rstrip())

for name in sorted(names):
    print(f"Hello, {name}")

# Decending Sort
# for name in sorted(names, reverse=True):
#     print(f"Hello, {name}")


# --- Other Idea ---
# with open("names.txt") as file:
#     for line in sorted(file):
#         print(f"Hello,", line.rstrip())
