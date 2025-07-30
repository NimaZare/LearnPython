def main():
    # name, house = get_student()
    student = get_student()
    # print(f"{name} from {house}")
    # print(f"{student[0]} from {student[1]}")
    print(f"{student['name']} from {student['house']}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    # return name, house  # ==> return a Tuple Value
    # return (name, house)  # ==> return a Tuple Value
    # return [name, house]  # ==> return a List Value and we can assignment items
    return {"name": name, "house": house}  # ==> return a Dictionary Value


if __name__ == "__main__":
    main()
