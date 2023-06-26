class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    # override read as string method
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    # Getter
    @property
    def name(self):
        return self._name
    
    # Setter
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    # Getter
    @property
    def house(self):
        return self._house
    
    # Setter
    @house.setter
    def name(self, house):
        if house not in ["Amol", "Tehran", "Sari"]:
            raise ValueError("Invalid house")
        self._house = house
    
    # Static method for this class
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)
    


def main():
    student = Student.get()
    print(student)

if __name__ == "__main__":
    main()
